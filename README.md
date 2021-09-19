# htn2021

## Run hidden gem backend on your local machine

### Create an isolated Python environment
- python -m venv env
- .\env\Scripts\activate

### Navigate to your project directory and install dependencies
- cd htn2021
- pip install -r requirements.txt

### Run the application
- python main.py

### In your web browser, enter the following address:
- http://localhost:8080

## How the frontend communicates with the backend
- the backend is deployed on google app engine
- a google cloud build is triggered whenever pushed to master
