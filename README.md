## Setup

To set up and run the Django quiz application on your local machine, follow the steps below:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash



git clone <repository_url>
cd <project_directory>

```

### a. On macOS/Linux:
```bash
# Create a virtual environment
python3 -m venv env
# Activate the virtual environment
source env/bin/activate
```


### b. On Windows:
```bash
# Create a virtual environment
python -m venv env
# Activate the virtual environment
env\Scripts\activate
```



### 3. Install Dependencies
Install all required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Run the following command to apply the migrations and set up the database:

```bash
python manage.py migrate
```
If you want to add a superuser to access the Django admin panel, run the following:
```bash
python manage.py createsuperuser
```
You will be prompted to enter a username, email, and password.

### 5. Run the Development Server
Start the Django development server by running the following command:
```bash
python manage.py runserver
```
Now, you can access the application in your browser at http://127.0.0.1:8000/.