#!/bin/bash
#jupyter nbconvert --to notebook --execute datasense.ipynb

# strat the frontend
streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0 &

# start the backend

#exec gunicorn backend:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
# in modern gunicron is not necessary, fast apis univcorn itself have workers for handling multiple requests
exec fastapi run --workers 2 --host 0.0.0.0 --port 8000 backend.py 