# Sankhya_Project
=======
## Prerequisites
Ensure you have the following installed on your system:
- Python (version 3.8 or higher)
- Git
- MongoDB Compass
- A MongoDB Atlas account

---

## Setup Instructions

### Step 1: Clone the Repository
Clone the repository from GitHub:
```bash
git clone https://github.com/its-tapas/Sankhya_Project.git
cd Sankhya_Project
```

Step 2: Create and Activate a Virtual Environment
Set up a virtual environment to isolate dependencies:
```
python -m venv sankhya_env
sankhya_env\Scripts\activate
```
Step 3: Install Dependencies
Install all required Python packages:
```
pip install -r requirements.txt

```
step 4: Test Run the Server
Start the Django development server:
```
python manage.py runserver

```
Project Structure
```
Sankhya-Project/        #this should be your current working directory while executing any cmds
├── core/               # Django app containing models and views
├── sankhya_env/        # Virtual environment directory
├── sankhya_project/    # Main project directory with settings and URLs
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── manage.py           # Django management script
```


Contribution Guidelines
Follow these steps to contribute:

> Fork the repository.
> Create a new branch:
```
git checkout -b feature/your-feature-name
```
> Make your changes and commit:
```
pip freeze > requirements.txt
git add .
git commit -m "Add your commit message here"
```
> Push to your branch:
```
git push origin feature/your-feature-name
```
> Open a pull request on GitHub.

## NOTE: Do not push Virtual environment into repo, delete that before commits and use below command before committing your changes to update the requirement file
```
pip freeze > requirements.txt
```

//Troubleshooting
```
Failed to push refs: fetch first
Solution: Run git pull origin main --allow-unrelated-histories before pushing.
```
