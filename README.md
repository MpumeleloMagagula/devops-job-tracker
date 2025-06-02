# DevOps Job Tracker

A fullstack DevOps-focused job tracking app to help tech professionals monitor and manage their job search process. Built with FastAPI (backend), React (frontend), and deployed using modern CI/CD and cloud tools.

---

## 📅 Description

The **DevOps Job Tracker** provides a centralized dashboard to:

* Track job applications
* Monitor application progress
* Log notes or interview stages
* Gain insights into your job-hunting activity

It's also a showcase of modern DevOps practices:

* CI/CD pipelines
* Infrastructure-as-Code
* Monitoring & Observability
* Containerized deployments

---

## ✨ Features

* Add, update, delete job applications
* View job listings with statuses (e.g., Applied, Interview, Offer)
* Analytics and visual job-hunting insights (optional)
* Real-world DevOps stack integration

---

## ⚙️ Tech Stack

### Backend

* **Framework**: FastAPI (Python)
* **Database**: PostgreSQL (cloud/Docker)
* **ORM**: SQLAlchemy (async)
* **Monitoring**: Prometheus + Grafana
* **Metrics**: Prometheus FastAPI Instrumentator
* **Containerization**: Docker
* **Testing**: unittest, pytest
* **CI/CD**: GitHub Actions
* **Deployment**: Fly.io

### Frontend

* **Framework**: React (with Vite)
* **UI Styling**: TailwindCSS
* **HTTP Client**: Axios
* **Deployment**: Netlify

### DevOps & Infrastructure

* **CI/CD Pipelines**: GitHub Actions
* **Infrastructure as Code**: Terraform
* **Monitoring Tools**: Prometheus, Grafana

---

## 🚀 Deployment Instructions

### 1. Backend (FastAPI)

* Dockerize the backend
* Deploy using Fly.io:

  ```bash
  flyctl launch
  flyctl deploy
  ```
* Set up PostgreSQL (Docker or managed)
* Expose `/metrics` endpoint for Prometheus

### 2. Frontend (React)

* Build the frontend:

  ```bash
  npm run build
  ```
* Deploy to Netlify:

  * Connect GitHub repo
  * Use `build/` folder for deploy output

### 3. CI/CD (GitHub Actions)

* Backend:

  * Lint, test, build & deploy to Fly.io
* Frontend:

  * Build & deploy to Netlify

### 4. Monitoring

* Run Prometheus & Grafana (via Docker or IaC)
* Visualize API metrics (requests/sec, latency, errors)

---

## 🌐 Example Use Cases

* Track when and where you've applied
* See how many interviews you've landed this month
* View charts for remote vs onsite opportunities

---

## ✍️ Author

Mpumelelo Magagula
[GitHub](https://github.com/MpumeleloMagagula)
[Portfolio](https://mpumelelomagagula.github.io/MpumeleloMagagula.io/)

---

## ⚡ Want to Contribute?

Feel free to fork and submit a PR. Feedback and improvements welcome!

---

## 📊 License

[MIT License](LICENSE)
