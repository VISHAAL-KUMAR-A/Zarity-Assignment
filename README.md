# BloodTest Django Project

This is a Django project designed for managing and analyzing blood test results. It stores test data for patients and provides various statistics about test results, such as abnormal results, average values, and ranges.

## Features

- **Store Patient Test Results**: Records test results, including patient ID, test name (e.g., Glucose, Hemoglobin, Cholesterol), test value, unit, test date, and whether the result is abnormal.
- **Test Result Analysis**: Calculates statistics for each test type, including minimum, maximum, and average values, as well as abnormal counts.
- **Optimized Database**: The project includes custom database indexes for efficient querying based on patient ID and test name.

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- PostgreSQL or SQLite database
- install pandas and djangorestframework in your vscode. Install it in virtual environment which can be created by the following method that is being explained below

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bloodtest.git
cd bloodtest
```


#Create and activate an virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
If you already have the virtual environment kindly delete it and install a new virtual environment because in some cases you might face some installation errors


#Installation Dependencies
pip install -r requirements.txt


#Set up the database
python manage.py makemigrations
python manage.py migrate


#Run the development server
python manage.py runserver
