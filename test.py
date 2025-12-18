from fastapi.testclient import TestClient
from backend import app
# server_url = 'http://127.0.0.1:8000/predict'

with TestClient(app) as client:
    response = client.post('/predict',json={'sms_text':"SBI UPI transaction of INR 125.50 to Swiggy (Order ID SWG789) completed on 12/09/2023. Ref No: SBI0912XYZ."})
    print(response.status_code)
    assert response.status_code == 200
    print('contented to the server successfully',response.status_code)
    predicted_data = response.json()
    assert predicted_data['Prediction'] == [0]
    print('Prediction test passed successfully',predicted_data['Prediction'])