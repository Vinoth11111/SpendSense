import joblib
from fastapi import FastAPI
from pydantic import BaseModel, validator
import pandas as pd
import time
import re
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    handlers=[logging.FileHandler('logs.log'),
                              logging.StreamHandler()])
log = logging.getLogger(__name__)

class dataformat(BaseModel):
    sms_text : str | list[str]
    @validator('sms_text')
    def check_sms_text(cls,v): #cls - class method itself(dataformat),v- value passed to the validator
        if len(v) == 0:
            log.error('sms_text cannot be empty')
            raise ValueError('sms_text cannot be empty')
        elif len(v) > 4000:
            log.error('sms_text cannot have more than 1000 entries')
            raise ValueError('sms_text cannot have more than 1000 entries')
        return v
        
app = FastAPI()
loaded_model =  None
# load the model
@app.on_event('startup')
def startup_event():
    global loaded_model
    log.info('loading model....')
    loaded_model = joblib.load('./full_classification_pipeline.joblib')
    log.info('model loaded successfully')

def data_process(text):
    # Rs Rs. or INR space optional 1-2 digit,2-3digit,1-3digit dot 1-2 digit
    #?: is used for caturing and continueing the catpure if it not used it will immedidatly return the initally captured txt(Rs)
    log.info('Processing data to mask sensitive information and extract amount')
    pattern = r'(?:Rs\.?|INR)\s?\d{1,4}(?:,\d{2})*(?:,\d{3})*(?:\.\d+)?'
    masked_sms = re.sub(r'\d{9,18}','Masked_Number',text)
    log.info('Masked sensitive information in the text and extracted amount')
    amt = re.search(pattern,text)
    if amt:
        str_amt = amt.group()
        pro_str = re.sub(r',','',str_amt)
        int_amt = pro_str[3:].strip()

        return float(int_amt),masked_sms
    
    

async def data_preparation(data: dataformat) -> pd.DataFrame: 
    log.info('data received for prediction')
    log.info('converting the text into vector form....')
    try:
        if isinstance(data.sms_text,list):
            new_data = pd.DataFrame({'sms_text': data.sms_text})
            log.info('Got string input for sms_text')
            new_data['masked_sms_text'] = new_data['sms_text'].apply(lambda s: data_process(s)[1] if data_process(s)[1] else s)
            new_data['amount'] = new_data['masked_sms_text'].apply(lambda x: data_process(x)[0] if data_process(x)[0] else 0)
            log.info('Data Successfully  processed for prediction')

            return new_data[['masked_sms_text','amount']]
        """else:
            log.info('Got list of string or file as a input for sms_text')
            new_data = pd.DataFrame({'sms_text': data.sms_text})
            new_data['masked_sms_text'] = new_data['sms_text'].apply(lambda s: data_process(s)[1] if data_process(s)[1] else s)
            new_data['amount'] = new_data['masked_sms_text'].apply(lambda x: data_process(x)[0] if data_process(x)[0] else 0)
            log.info('Data Successfully  processed for prediction')
            return new_data[['masked_sms_text','amount']]"""
    except Exception as e:
        log.error(f'Error in data preparation: {e}')
@app.post('/predict')
async def predict(data: dataformat) -> dict:
    start_time = time.time()
    log.info('loading model....')
    model = loaded_model
    log.info('model loaded')
    new_data = await data_preparation(data)
    prediction = model.predict(new_data[['masked_sms_text']])
    prob = model.predict_proba(new_data[['masked_sms_text']]).max(axis=1)
    end_time = time.time() - start_time
    log.info(f'Prediction time taken: {end_time} seconds')
    log.info(f'Prediction successful,prediction: {prediction},probabilities: {prob}')
    return {'Prediction':prediction.tolist(),'Probabilities': prob.tolist(), 'amounts': new_data['amount'].tolist(), 'Masked_SMS_Text': new_data['masked_sms_text'].tolist()}


