

# 🚀 Flask CI/CD Demo with GitHub Actions

A simple Flask web application integrated with a CI/CD pipeline using **GitHub Actions**. This project demonstrates how to automate testing and deployment of a Python Flask app.

---

## 📁 Project Structure

```bash
flask-ci-cd-demo/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── .github/
│   └── workflows/
│       └── ci-cd.yml    # GitHub Actions workflow for CI/CD
└── README.md            # Project documentation
```

---

## ⚙️ Tech Stack

* **Python 3**
* **Flask**
* **GitHub Actions**
* **Docker** (optional for containerized deployment)
* **Heroku / AWS / Any server** (deployment target - customize as needed)

---

## 🛠️ Features

✅ Simple Flask Web App
✅ GitHub Actions CI/CD Pipeline
✅ Automatic Installation & Testing
✅ Deployment Ready (can be extended for Heroku, AWS, etc.)

---

## 🔁 CI/CD Pipeline Flow

```mermaid
graph TD
A[Code Commit] --> B[GitHub Actions Trigger]
B --> C[Install Dependencies]
C --> D[Run Tests]
D --> E[Deploy to Production]
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sadanki/flask-ci-cd-demo.git
cd flask-ci-cd-demo
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Flask App Locally

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## ⚙️ GitHub Actions Workflow

The workflow file `.github/workflows/ci-cd.yml` performs the following:

* ✅ Trigger on push to `main` or pull requests
* ⚙️ Set up Python environment
* 📦 Install dependencies
* 🧪 Run unit tests
* 🚀 Deploy step placeholder (customize as needed)

You can customize the `deploy` step to suit your environment (e.g., Heroku CLI, AWS CLI, SSH to EC2, etc.)

---

## 🧪 Sample Test Integration (Optional)

You can add a `test_app.py` like below to include basic test cases:

```python
def test_home():
    from app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
```

Then install `pytest` and include in the GitHub workflow:

```bash
pip install pytest
pytest
```

---

## 🚀 Deployment Options

Modify the final step in `.github/workflows/ci-cd.yml` based on your hosting platform:

### 🔸 Deploy to Heroku (example)

```yaml
- name: Deploy to Heroku
  uses: akhileshns/heroku-deploy@v3.12.12
  with:
    heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
    heroku_app_name: "your-app-name"
    heroku_email: "your-email@example.com"
```

---

## 🔐 Secrets Configuration

Configure the following **GitHub Secrets** under your repo settings:

* `HEROKU_API_KEY` – for Heroku deployment
* Any others depending on your deployment target (e.g., AWS credentials, SSH keys)

---

## 📸 Screenshot

![Flask App Screenshot](https://via.placeholder.com/800x400.png?text=Hello+World+Flask+App)

---

## 🙌 Acknowledgments

* [Flask Documentation](https://flask.palletsprojects.com/)
* [GitHub Actions Docs](https://docs.github.com/en/actions)

---

## 📬 Contact

**Author:** Sadanki
📧 Email: [your.email@example.com](mailto:your.email@example.com)
🔗 GitHub: [Sadanki](https://github.com/Sadanki)

---


