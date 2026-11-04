# Python DevOps Mini Project – To-Do Web App

**Student:** Aryan Kadam  
**PRN:** 2125UMLM1102  
**Department:** AI & ML  
**University:** Sanjivani University, Kopargaon

## 1. Project overview
A simple task-management web application built with Python and Flask. Users can add tasks, mark tasks as complete, and delete tasks.

## 2. DevOps concepts demonstrated
- **Version control:** Git and GitHub
- **Dependency management:** `requirements.txt`
- **Continuous Integration (CI):** GitHub Actions automatically runs tests on pushes and pull requests
- **Testing:** Python `unittest`
- **Containerization:** Dockerfile

## 3. Requirements
- Python 3.11 or later
- pip
- Git
- (Optional) Docker

## 4. Run locally

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open this address in your browser:

`http://127.0.0.1:5000`

## 5. Run tests
```bash
python -m unittest discover -s tests -v
```

## 6. Run with Docker (optional)
```bash
docker build -t python-devops-todo .
docker run -p 5000:5000 python-devops-todo
```

Then open `http://127.0.0.1:5000`.

## 7. Upload to GitHub

Create a new empty repository on GitHub, for example `python-devops-todo`.

Run these commands from this project folder:
```bash
git init
git add .
git commit -m "Initial commit: Python DevOps To-Do app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/python-devops-todo.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## 8. How the CI pipeline works
Whenever code is pushed to `main` or a pull request targets `main`, GitHub Actions:
1. Downloads the repository.
2. Sets up Python 3.11.
3. Installs Flask.
4. Runs the unit tests.
5. Shows a success or failure result in the GitHub Actions tab.

## 9. Future improvements
- Save tasks in an SQLite database.
- Add user login.
- Deploy the app to a cloud platform.
- Add code-quality checks.

## 10. Important note
This starter project stores tasks in memory, so tasks reset when the application restarts. It is designed as a small learning/demo project.
