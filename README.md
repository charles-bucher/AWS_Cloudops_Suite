# AWS Cloud Support Simulator 🚀

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Overview

**AWS Cloud Support Simulator** is an interactive learning tool that simulates **real-world AWS support scenarios**.  
Practice troubleshooting EC2, S3, IAM, Lambda, CloudWatch, and more, **safely and hands-on** — no production systems required.  

Perfect for self-learners, career pivoters, and anyone looking to build practical cloud support experience.

---

## Features 🌟

- Simulated AWS services: EC2, S3, IAM, Lambda, CloudWatch, GuardDuty  
- AI-assisted scenario guidance for troubleshooting  
- Hands-on exercises for incident response  
- Reusable Python scripts and notebooks  
- Screenshots and visual walkthroughs for guidance  

---

## Screenshots 📸

<div align="center">

| ![Confirm](screenshots/Confirm.png) | ![Dynamo Confirm](screenshots/Dynamo_Confirm.png) |
|------------------------------------|---------------------------------------------|
| Confirm Workflow                     | DynamoDB Confirmation                        |

| ![IAM Roles](screenshots/IAM_Roles.png) | ![Python](screenshots/Python.png) |
|----------------------------------------|----------------------------------|
| IAM Roles & Policies                     | Python Script Execution          |

| ![S3 Buckets](screenshots/S3_Buckets.png) | ![Terraform Installed](screenshots/Terraform_Installed.png) |
|------------------------------------------|------------------------------------------------------------|
| S3 Bucket Management                      | Terraform Setup Verification                                  |

> Full screenshot gallery available in the `screenshots/` folder

</div>

---

## Installation ⚡

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Usage 🖥️
Launch the simulator:

bash
Copy code
python aws_support_sim.py
Follow AI-assisted prompts to simulate incidents such as:

Unauthorized IAM access

EC2 instance failures

S3 misconfigurations

Lambda errors

CloudWatch alerts

Project Structure 📂
bash
Copy code
AWS_Cloud_Support_Sim/
│
├─ screenshots/          # Visual walkthroughs and scenario references
├─ scripts/              # Python automation scripts
├─ notebooks/            # Jupyter notebooks for exercises
├─ requirements.txt      # Python dependencies
├─ README.md
└─ aws_support_sim.py    # Main entry point
Roadmap 🛠️
Add RDS, VPC, Route53 simulations

Hands-on challenges with scoring

Multi-user collaboration

Web interface for browser access

License 📄
MIT License

Author 👨‍💻
Charles Bucher – self-taught cloud support engineer.
GitHub | Twitter

“Hands-on practice beats theory 10x when learning cloud operations.”

yaml
Copy code

---

