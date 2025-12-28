🧠 AI-Powered Warranty & Insurance Claim Adjudication System

An end-to-end agentic AI system that automates warranty and insurance claim approval, fraud detection, and human escalation using LangGraph multi-agent workflows, Azure OpenAI, and cloud-native deployment on Azure.

📌 Project Overview

This application processes claim data uploaded as a CSV file and automatically decides whether a claim should be:

✅ Approved

❌ Rejected (fraudulent or policy violation)

🧑‍⚖️ Escalated to a human reviewer when confidence is low

The system uses multiple collaborating agents to analyze claim attributes, detect fraud signals, validate policy rules, and determine decision confidence. Clear cases are automated, while ambiguous cases follow a human-in-the-loop workflow to ensure safe and reliable decisions.

The solution supports batch claim processing, significantly reducing manual effort and accelerating claim resolution time.
