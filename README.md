# Metsenat 

## 1. Clone the Repository
```bash
git clone https://github.com/jahongiranorboyev/Metsenat.git
```
## 2. Change Directory
```bash
cd metsenat
```
## 3. Create .env file using .env.example
```bash
cp .env_example .env
```
## 4. Create a virtual environment using Python 3.10 
```bash
python3 -m venv venv 
```
## 5. Activate the Virtual Environment On Linux/MacOS
```bash
source venv/bin/activate
```
## 5. Activate the Virtual Environment On Windows
```bash
venv\Scripts\activate
```
## 6. Install Packages from requirements.txt Inside the Virtual Environment:
```bash
pip install -r requirements.txt
```

## 7. Run the makemigrations and apply the changes to the database:
```bash
./manage.py makemigrations
./manage.py migrate
```
## 8. To start the server, run the following command inside your Django project directory:
```bash
./manage.py runserver
```
