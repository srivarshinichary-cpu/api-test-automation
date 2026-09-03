# API Test Automation using PyTest and Requests

## Project Overview

A simple REST API test automation project developed using Python, PyTest, and Requests. The project validates API operations such as GET, POST, PUT, and DELETE with basic status code and response validation.

## Technologies Used

- Python
- PyTest
- Requests
- pytest-html
- GitHub Actions
- REST API

## Test Cases

| Test Case | API Operation | Validation |
|---|---|---|
| Get Users | GET | Status code and response data |
| Create User | POST | Status code and user name |
| Update User | PUT | Status code and updated data |
| Delete User | DELETE | Status code |
| Invalid User | GET | 404 status code |

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
