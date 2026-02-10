# SentryAi Deployment Guide

This guide provides instructions for deploying the SentryAi Credit Fraud Detection system.

## 1. Local Deployment with Docker

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.

### Build the Image
```bash
docker build -t sentryai-fraud-detection .
```

### Run the Container
```bash
docker run -p 5000:5000 sentryai-fraud-detection
```
Access the dashboard at `http://localhost:5000`.

## 2. Cloud Deployment (Hugging Face Spaces)

Hugging Face Spaces is an excellent choice for deploying ML applications.

### Steps:
1. Create a new **Space** on Hugging Face.
2. Select **Docker** as the SDK.
3. Upload the following files:
    - `app.py`
    - `requirements.txt`
    - `Dockerfile`
    - `models/` (entire directory)
    - `static/` (entire directory)
    - `templates/` (entire directory)
4. Hugging Face will automatically build and deploy your container.

## 3. Deployment using Flask (Traditional)

If not using Docker, ensure you have Python 3.11 installed.

```bash
pip install -r requirements.txt
python app.py
```

> [!IMPORTANT]
> The `creditcard.csv` dataset is NOT required for deployment once the model is trained and saved in the `models/` directory. This significantly reduces image size and deployment complexity.
