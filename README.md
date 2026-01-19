# SpendSense: Cloud-Native Personal Finance API

![Python](https://img.shields.io/badge/Python-3.11.5%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-ECS%20%7C%20Fargate-232F3E?style=flat&logo=amazon-aws)
![Status](https://img.shields.io/badge/Status-Deployed-success)


## Quick Summary
**SpendSense** is a production-ready API designed to centralize and structure financial data for machine learning workflows.  
Built with a strong emphasis on **data integrity, privacy, and scalability**, it transforms raw SMS transaction alerts into clean, categorized financial intelligence using a containerized, cloud-native architecture.

---

## The Problem: Challenges in Financial Data Engineering

Building a reliable expense tracking system is difficult because raw financial data is often:

- **Unstructured & Fragmented**  
  Transaction alerts arrive as noisy SMS strings, making them incompatible with standard analytical pipelines.

- **Security-Sensitive**  
  Raw logs frequently contain PII (Personally Identifiable Information) such as account numbers, creating significant privacy and compliance risks if processed naively.

- **Prone to Data Drift**  
  Without strict validation, inconsistent inputs lead to *“Garbage In, Garbage Out”*, degrading model reliability and downstream ML performance.

---

## The Solution: SpendSense

SpendSense acts as a **secure, schema-governed gateway** between raw financial text and actionable intelligence.

The system enforces **data quality, privacy, and validation** before any information reaches the machine learning inference layer.

---

## Key Engineering Highlights

### PII Anonymization Engine
A custom **Regex-based masking layer** identifies and replaces sensitive account identifiers with generic tokens, ensuring downstream ML models never process private user data.

---

### Schema-Governed API (Contract-Based)
Utilizes **Pydantic models** to enforce strict data constraints at the API boundary.  
Malformed requests are rejected immediately, preserving compute resources and guaranteeing data integrity.

---

### Async & Scalable Architecture
Built on **FastAPI’s asynchronous request handling**, enabling high-throughput batch processing without blocking.  
The entire stack is **fully Dockerized**, ensuring environment parity from local development to AWS Fargate.

---

### Integrated ML Inference
Serves a serialized **Scikit-learn classification pipeline** that performs:
- Real-time feature extraction  
- Expense categorization  
- Confidence probability scoring  

This enables automated auditing and ML-driven financial insights.

---

## Architecture

(./SpendSense_Arch_Diagram.png)
The system follows a **stateless, serverless-first design** to minimize operational overhead while maintaining high performance.

- **Frontend (Streamlit)**  
  User-facing interface for uploading CSV/TXT files or entering transaction text manually.

- **API Gateway (FastAPI)**  
  Validates incoming payloads and asynchronously routes requests to processing logic.

- **Data Processing Layer**  
  Custom pipeline handling Regex-based PII masking and feature engineering (e.g., amount extraction).

- **Inference Engine**  
  Loads a pre-trained full classification pipeline via **Joblib** to predict spending categories (Food, Travel, Bills, etc.).

- **Deployment**  
  Containerized with **Docker** and hosted on **AWS ECS/Fargate** for scalable, serverless execution.

---

## Technical Stack & Design Decisions

| Component | Tool Used | Rationale |
|---------|----------|-----------|
| Backend Framework | FastAPI | High performance (Starlette-based) with native Pydantic support for schema validation |
| Frontend UI | Streamlit | Rapid prototyping and real-time visualization of predictions |
| ML Inference | Scikit-learn | Predictable latency, robustness, and production-friendly pipelines |
| Containerization | Docker | Eliminates environment inconsistencies and enables cloud portability |
| Cloud Infrastructure | AWS ECS/Fargate | Demonstrates MLOps proficiency with serverless container orchestration |

---

## Future ML Roadmap

Planned enhancements to evolve SpendSense into a full financial intelligence platform:

- **Advanced NLP Categorization**  
  Transition to Transformer-based models (BERT / DistilBERT) for richer merchant text understanding.

- **Spending Forecasting**  
  Implement time-series models (Prophet, LSTM) to predict monthly budget variance.

- **Persistence Layer**  
  Integrate **PostgreSQL** to enable historical trend analysis and long-term behavioral insights.

---

## How to Run Locally

### 1. Prerequisites
- Docker & Docker Compose  
- Python 3.10+ (if running without Docker)

---

### 2. Setup & Installation

```bash
# Clone the repository
git clone https://github.com/Vinoth11111/SpendSense.git
cd SpendSense

# Give execution permission to the start script
chmod +x start.sh

```
### 3. Launch with Docker
Option A: Using Docker (Recommended)

```bash
docker-compose up --build
```
Option B: Manual Execution
```bash
./start.sh
```
The SpendSense will be available at http://localhost:8501 and the interactive Swagger documentation at http://localhost:8000/docs
