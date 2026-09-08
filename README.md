# API Test Automation using PyTest and Requests

## Project Overview

This project is a Python-based REST API test automation framework developed using **PyTest** and **Requests**.

The framework validates common API operations including **GET, POST, PUT, and DELETE**, along with negative testing. It performs status code, response body, response data type, and response time validations.

The project also includes **HTML test reporting** and **GitHub Actions** for automated test execution.

## Technologies Used

* Python
* PyTest
* Requests
* pytest-html
* REST APIs
* GitHub Actions
* Git & GitHub

## API Test Scenarios

| Test Scenario | Method | Validation                                                          |
| ------------- | ------ | ------------------------------------------------------------------- |
| Get Users     | GET    | Status code, response type, required fields, response time          |
| Create User   | POST   | Status code, response body, created ID, request data, response time |
| Update User   | PUT    | Status code, updated data, response body, response time             |
| Delete User   | DELETE | Status code, response body, response time                           |
| Invalid User  | GET    | 404 status code, error response, response time                      |

## Project Structure

```text
API-Test-Automation/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── tests/
│   ├── test_get.py
│   ├── test_post.py
│   ├── test_put.py
│   ├── test_delete.py
│   └── test_negative.py
│
├── reports/
│   └── report.html
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Test Validations

The framework validates:

* HTTP status codes
* JSON response structure
* Required response fields
* Response data types
* Request and response data consistency
* Response time
* Negative API scenarios
* Error responses

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/srivarshinichary-cpu/api-test-automation.git
```

### 2. Navigate to the project

```bash
cd api-test-automation
```

### 3. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run all tests

```bash
pytest -v
```

## Generate HTML Test Report

Run:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

The generated report can be opened in a browser to review test execution results.

## Continuous Integration

GitHub Actions is configured to automatically execute the PyTest test suite when changes are pushed to the repository.

This helps verify that the API tests continue to pass after code changes.

## Test Result

The current test suite contains **5 automated API tests** covering:

* GET
* POST
* PUT
* DELETE
* Negative testing

All tests are currently passing successfully.

## Learning Outcomes

Through this project, I gained practical experience in:

* REST API testing
* Python test automation
* PyTest framework
* API request and response validation
* Negative testing
* Test reporting
* Debugging test failures
* Git and GitHub
* Basic CI automation using GitHub Actions
