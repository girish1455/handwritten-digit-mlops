
# Handwritten Digit Detection - MLOps Project

This project demonstrates a complete MLOps workflow including:
- Model training
- Model testing
- FastAPI deployment
- Docker containerization
- GitHub Actions CI/CD pipeline

## Run Locally

Train model:
python src/train.py

Run API:
uvicorn src.main:app --reload

Open browser:
http://127.0.0.1:8000/docs

## Docker

docker build -t digit-api .
docker run -p 8000:8000 digit-api
