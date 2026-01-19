# SpendSense: Cloud-Native Personal Finance API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-ECS%20%7C%20Fargate-232F3E?style=flat&logo=amazon-aws)
![Status](https://img.shields.io/badge/Status-Deployed-success)

> **Quick Summary:** SpendSense is a production-ready personal finance tracking API designed to centralize and structure financial data. Built with a focus on **high performance** and **cloud-native scalability**, it utilizes a containerized architecture deployed on AWS to ensure data persistence and reliability.

---

## 🚀 Project Overview

Managing personal finances often involves messy spreadsheets or fragmented apps. **SpendSense** solves this by providing a robust, schema-governed backend that allows users to programmatically track transactions, categorize expenses, and monitor budgets.

From a Machine Learning perspective, this project serves as the **Data Engineering Foundation**: providing the clean, structured, and historical data necessary for future predictive features like spending forecasts or anomaly detection.

**Key Objectives:**
* **Scalable Infrastructure:** Moving beyond "local scripts" to a fully containerized cloud environment.
* **Data Integrity:** Implementing a relational PostgreSQL schema to ensure financial records remain consistent and ACID-compliant.
* **Production Standards:** Using FastAPI for asynchronous request handling and Docker for environment parity between development and production.

---

## 🏗️ Architecture

The system follows a "Serverless-First" architecture, reducing operational overhead while maintaining high performance.

1.  **API Layer:** FastAPI serves as the gateway, handling asynchronous CRUD operations for transactions and user budgets.
2.  **Database Layer:** A PostgreSQL instance stores relational data, ensuring complex queries (like monthly spending aggregations) are efficient.
3.  **Containerization:** The entire application is containerized using **Docker**, ensuring the app runs identically on local machines and the cloud.
4.  **Cloud Deployment:** Hosted on **AWS ECS (Elastic Container Service)** using **AWS Fargate**, providing a serverless execution environment that scales without managing EC2 instances.

---

## 🛠️ Technical Stack & Decisions

I chose this stack to demonstrate a "Full-Cycle" engineering mindset—owning the code from the first line of Python to the final AWS deployment.

| Component | Tool Used | Why this choice? |
| :--- | :--- | :--- |
| **Backend Framework** | `FastAPI` | High performance (Starlette-based) and automatic Pydantic validation for sensitive financial data. |
| **Database** | `PostgreSQL` | Required for relational integrity. Financial data needs strict schemas to prevent data loss or type errors. |
| **Containerization** | `Docker` | Eliminates "it works on my machine" issues and allows for seamless cloud integration. |
| **Cloud Provider** | `AWS (ECS/Fargate)` | Chosen to demonstrate proficiency in modern DevOps/MLOps workflows and serverless container orchestration. |

---

## 📈 Future ML Roadmap (The "Engineer" Vision)

To bridge this project into a Machine Learning context, the following modules are planned:

* **Expense Categorization (NLP):** Using a lightweight transformer model to automatically categorize transactions based on raw merchant descriptions.
* **Spending Forecasting:** Implementing a Time-Series model (like Prophet or LSTM) to predict next month's expenses based on historical patterns.
* **Anomaly Detection:** An Isolation Forest model to alert users of unusual or fraudulent spending spikes.

---

## 🛠️ How to Run Locally

### 1. Prerequisites
* Docker & Docker Compose installed.
* Python 3.10+ (if running without Docker).

### 2. Setup & Installation
```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)[YourUsername]/SpendSense.git
cd SpendSense

# Create environment variables
touch .env
### 3. Launch with Docker
'''bash
docker-compose up --build
The API will be available at http://localhost:8000 and the interactive Swagger documentation at http://localhost:8000/docs.
