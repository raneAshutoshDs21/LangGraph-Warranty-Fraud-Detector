# 🧠 AI-Powered Warranty & Insurance Claim Adjudication System

An end-to-end agentic AI system that automates warranty and insurance claim approval, fraud detection, and human escalation using LangGraph multi-agent workflows, Azure OpenAI, and cloud-native deployment on Azure.

---

## 📌 Project Overview

This application processes claim data uploaded as a CSV file and automatically decides whether a claim should be:

✅ Approved

❌ Rejected (fraudulent or policy violation)

🧑‍⚖️ Escalated to a human reviewer when confidence is low

The system uses multiple collaborating agents to analyze claim attributes, detect fraud signals, validate policy rules, and determine decision confidence. Clear cases are automated, while ambiguous cases follow a human-in-the-loop workflow to ensure safe and reliable decisions.

The solution supports batch claim processing, significantly reducing manual effort and accelerating claim resolution time.

---
## 🏗️ System Architecture
<img width="865" height="2553" alt="Untitled diagram-2025-12-26-114500" src="https://github.com/user-attachments/assets/3dd4d207-b5fb-4b5c-a8b2-f579cf682c4f" />

---

## 🧩 Key Features
- Multi-agent claim analysis using LangGraph

- Fraud detection with LLM-driven reasoning

- Human-in-the-loop escalation for uncertain cases

- Batch processing of claims via CSV upload

- Optimized Azure OpenAI token usage

- Dockerized and cloud-ready deployment

- Scalable architecture suitable for enterprise workflows

---
## 🛠️ Tech Stack

| Category | Technology |
|---------|------------|
| Agent Orchestration | LangGraph |
| LLM | Azure OpenAI |
| Backend | Python |
| UI | Streamlit |
| Containerization | Docker |
| Cloud Platform | Microsoft Azure |

---
## 📊 Quantifiable Impact

- ~65–75% of claims auto-approved or auto-rejected without human intervention

- ~50–60% reduction in manual claim review effort

- Claim decision time reduced from minutes to seconds
---
🖼️ Screenshots
📂 Resource Creation (Azure)

📤 CSV Upload Interface

🧠 Agent Decision Flow

📊 Claim Decision Output

📁 Place screenshots inside a /screenshots folder in the repository.

---
🎥 Application Demo (Screen Recording)

▶️ Watch the demo here:


---
## 🚀 Deployment Docker+Azure CLI

The application is packaged using Docker and deployed on Microsoft Azure, ensuring portability and environment consistency.

### Step 1: Build the image
```cmd
docker build -t <your-app-name> .
docker run -p 8501:8501 claim-ai-app
```
### Step 2: Azure CLI Login
```cmd
az login
```
### Step 3:Login to Azure Container Registery
```cmd
az acr login --name <your acr name>
```
### Step 4: Tag the docker image
```cmd
docker tag <your tag name>.azurecr.io/<your-image-name>:latest
```
### Step 5: Push the Image
```cmd
docker push <your tag name>.azurecr.io/<your-image-name>:latest
```
### Step 6: Create new web app resource and add all the necessary info and click on create.
---

## 🔐 Environment Variables

Create a .env file with the following:
```
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
```
---
## 📁 Project Structure
```
WARRANTY_FRAUD_DETECTION/
│
├── .venv/ # Python virtual environment
├── data/ # Sample claim datasets (CSV files)
├── Screenshots & app demo/ # Application screenshots and demo recordings
│
├── .dockerignore # Docker ignore rules
├── .env # Environment variables (not committed)
├── agent.ipynb # Agent experimentation and prototyping notebook
├── app.py # Streamlit application entry point
├── Dockerfile # Docker configuration for deployment
├── main.py # LangGraph orchestration and core logic
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
---
## 🧪 Future Enhancements

Integration with real-time claim ingestion APIs

Advanced fraud scoring with historical data

Role-based access for reviewers

Monitoring and logging using Azure services
---
## 👤 Author

Ashutosh Santosh Rane

AI / ML Engineer | Azure AI






