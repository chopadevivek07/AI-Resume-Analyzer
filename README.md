# 🚀 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Flask**, **Groq AI**, **Docker**, **Gunicorn**, **Nginx**, and **AWS EC2**.

The application analyzes PDF resumes, calculates an ATS score, extracts skills, generates an AI summary, compares resumes against job descriptions, provides personalized suggestions, and exports a professional PDF report.

---

## 🌟 Features

- 📄 Upload Resume (PDF)
- 🤖 AI Resume Analysis using Groq LLM
- 📊 ATS Score Calculation
- 📝 AI Professional Summary
- 💼 Skills Detection
- 🎯 Job Description Matcher
- 📈 Resume Match Score
- ✅ Matched Skills
- ❌ Missing Skills
- 💡 AI Suggestions
- 📄 PDF Report Generation
- 🐳 Docker Containerization
- ⚡ Gunicorn WSGI Server
- 🌐 Nginx Reverse Proxy
- ☁️ AWS EC2 Deployment

---

# 🛠 Tech Stack

### Backend
- Python
- Flask

### AI
- Groq API (Llama)

### PDF Processing
- PyMuPDF
- ReportLab

### Frontend
- HTML
- CSS
- Bootstrap 5
- JavaScript
- Chart.js

### Deployment
- Docker
- Gunicorn
- Nginx
- AWS EC2
- Ubuntu Linux

---

# 📂 Project Structure

```text
AI-Resume-Analyzer
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── routes/
├── services/
├── templates/
├── static/
├── uploads/
├── reports/
│
└── screenshots/
    ├── 01-home.png
    ├── 02-ats-analysis.png
    ├── 03-job-matcher.png
    ├── 04-job-match-result.png
    ├── 05-pdf-report.png
    ├── 06-docker-build.png
    ├── 07-docker-running.png
    ├── 08-nginx-test.png
    └── 09-aws-ec2.png
```
![Architecture](/img/architecture.png)
---

# 🏗 Architecture

```text
              Resume PDF
                   │
                   ▼
          Flask Application
                   │
                   ▼
      PDF Text Extraction (PyMuPDF)
                   │
                   ▼
          Groq AI (Llama Model)
                   │
                   ▼
 ATS Score + AI Summary + Skill Detection
                   │
                   ▼
      Job Description Matcher
                   │
                   ▼
         PDF Report Generation
                   │
                   ▼
      Gunicorn → Docker → Nginx
                   │
                   ▼
             AWS EC2 Instance
```
![Architecture](/img/architecture-1.png)
---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/chopadevivek07/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
SECRET_KEY=YOUR_SECRET_KEY
```

---

## Run Application

```bash
python app.py
```

Visit

```
http://localhost:5000
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t ai-resume-analyzer .
```

## Run Docker Container

```bash
docker run -d \
--name ai-resume-analyzer \
-p 5000:5000 \
--env-file .env \
ai-resume-analyzer
```

Verify

```bash
docker ps
```

---

# 🌐 Nginx Reverse Proxy

Example configuration

```nginx
server {

    listen 80;

    server_name YOUR_PUBLIC_IP;

    location / {

        proxy_pass http://127.0.0.1:5000;

        proxy_set_header Host $host;

        proxy_set_header X-Real-IP $remote_addr;

        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_set_header X-Forwarded-Proto $scheme;

    }

}
```

Reload Nginx

```bash
sudo nginx -t

sudo systemctl restart nginx
```

---

# ☁️ AWS Deployment

The project is deployed on

- Ubuntu EC2
- Docker
- Gunicorn
- Nginx

Deployment Workflow

```text
GitHub
   │
   ▼
AWS EC2
   │
   ▼
Docker Container
   │
   ▼
Gunicorn
   │
   ▼
Nginx
   │
   ▼
Browser
```

---

# 📸 Screenshots

## 🏠 Home Page

![Home](/img/home-1.png)

---

## 📊 ATS Analysis

![ATS Analysis](/img/home-2.png)
![ATS Analysis](/img/home-3.png)
![ATS Analysis](/img/home-4.png)

---

## 🎯 Job Description Matcher

![Job Matcher](/img/JD-match-1.png)
![Job Matcher](/img/JD-match-2.png)
![Job Matcher](/img/JD-match-3.png)
![Job Matcher](/img/JD-match-4.png)
---



## 🐳 Docker Build

![Docker Build](/img/docker-build-1.png)
![Docker Build](/img/docker-build-2.png)

---

## 🐳 Running Docker Container

![Docker Running](/img/docker-ps.png)

---

## 🌐 Nginx Configuration

![Nginx](/img/nginx-test.png)

---

## ☁️ AWS EC2 Deployment

![AWS EC2](/img/EC2-1.png)
![AWS EC2](/img/EC2-2.png)

---

# 🚀 Future Improvements

- User Authentication
- Resume History
- Dashboard Analytics
- Resume Comparison
- Cover Letter Generator
- AI Interview Questions
- Resume Ranking
- Multi-language Resume Analysis
- Resume Templates

---

# 👨‍💻 Author

## Vivek Chopade

**Cloud | DevOps | AI Engineer**

### GitHub

https://github.com/chopadevivek07

### LinkedIn

https://www.linkedin.com/in/vivek-chopade07/

---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.