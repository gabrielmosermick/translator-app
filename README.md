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

## 🛠️ **Installation Instructions**

### 1. **Backend Setup**

To run the backend locally, follow these steps:

1. Navigate to the `backend` directory:

    ```bash
    cd translation_app
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the backend using **Uvicorn**:

    ```bash
    uvicorn app:app --reload
    ```

    This will start the backend on `http://localhost:8007`. The `--reload` flag enables automatic reloading during development.

---

### 2. **Running Backend with Docker**

If you prefer to run the backend with Docker, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t translator-backend .
    ```

2. Run the container:

    ```bash
    docker run -p 8007:8007 translator-backend
    ```

    The backend should now be accessible at `http://localhost:8007`.

---

### 3. **Frontend Setup**

To run the frontend locally, follow these steps:

1. Navigate to the `frontend` directory:

    ```bash
    cd translation_ui
    ```

2. Install the required dependencies:

    ```bash
    npm install
    ```

3. Start the development server:

    ```bash
    npm run dev
    ```

    The frontend should now be accessible at `http://localhost:3000`.

---

### 4. **Running Frontend with Docker**

If you'd like to run the frontend with Docker, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t translator-frontend .
    ```

2. Run the container:

    ```bash
    docker run -p 80:80 translator-frontend
    ```

    The frontend will be available at `http://localhost` (or port 80).

---

## 🚀 **Deployment Instructions**

Deployment is handled automatically via **Render Pipelines**. Simply push your code to the relevant Git repository, and **Render** will automatically trigger the build and deployment process.

1. Push your changes to your Git repository:

    ```bash
    git push
    ```

2. **Render** will handle the deployment pipeline, ensuring your app is built and deployed in the cloud.

> **Note**: Ensure you have linked your Git repository to Render for automatic deployments.
