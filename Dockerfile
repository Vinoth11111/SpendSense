FROM python:3.11-slim

# Set working directory
WORKDIR /app

#create a root user

RUN useradd -m -u 1000 user

# Set environment variables
# Setting HOME to the user's home directory and updating PATH
# setting the path so the system before looking into default paths also looks into /home/user/bin
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Copy requirements file
COPY --chown=user:user requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY --chown=user:user start.sh .
# Copy the rest of the application code

COPY --chown=user:user . .

#give execute permission to start.sh
RUN chmod +x ./start.sh
# Expose the port FastAPI runs on
EXPOSE 8000
#expose streamlit port
EXPOSE 8501
USER user

# Command to run the FastAPI app with Uvicorn
#CMD ["Uvicorn","backend:app", "--host", "0.0.0.0", "--port", "8000","streamlit","run","frontend.py","--server.port","8501","--server.address","0.0.0.0","--server.websocket.enableCORS","false"]
CMD ["bash","./start.sh"]