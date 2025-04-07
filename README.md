# Translator App 🧠🌍

A simple translator web app built with **Vue.js** frontend and **Python (FastAPI)** backend.

## 🌐 Live Demo

- **Frontend**: https://translator-ui.onrender.com
- **Backend**:  https://translator-app-eup1.onrender.com

---

## 🛠 Tech Stack

- **Frontend**: Vue.js (Vite)
- **Backend**: Python (FastAPI / Flask)
- **Dockerized**: Fully containerized
- **Deployment**: Render.com (supports Docker)

---

## 🚀 Local Development

### Backend

```bash
cd translation_app
pip install -r requirements.txt
uvicorn app:app --reload

Run with Docker:
docker run -p 8007:8007 translator-backend

### Frontend

cd translation_ui
npm install
npm run dev

Run with Docker:
docker run -p 80:80 translator-frontend

---

## 🚀 Deployment
Deployment is automatic with git push and Render pipelines.


