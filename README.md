# Web Automation Portfolio: Playwright & Pytest Framework

A professional UI Test Automation Framework built from scratch using **Python**, **Playwright**, and **Pytest**. This project implements the **Page Object Model (POM)** design pattern to test an e-commerce workflow on the SauceDemo web application.

## Key Features
* **Page Object Model (POM):** Clean separation of test logic and UI element locators for high maintainability.
* **Locators:** Uses CSS and ID selectors to interact with web elements.
* **Coverage:** Includes both "Happy Path" (successful login & cart addition) and "Sad Path" (error handling for locked-out users) test cases.

## Project Architecture
The project is structured to isolate the web elements from the actual test executions:

```plaintext
my-qa-portfolio/
├── pages/                  # Page Object Classes (UI locators & actions)
│   ├── login_page.py
│   └── inventory_page.py
│   └── checkout_page.py
├── tests/                  # Pytest execution scripts
│   └── test_ecommerce_flow.py
│   └── test_checkout_flow.py
├── pytest.ini              # Pytest environment configuration
└── README.md               # Project documentation
```

## Setup & Installation

Run the following commands sequentially in your terminal to clone the repository, set up the virtual environment, install dependencies, and download the required browser binaries:

```bash
# 1. Clone the repository and enter the directory
git clone https://github.com/zdelo01/my_first_qa_project.git
cd my_first_qa_project

# 2. Create a Python Virtual Environment
python -m venv venv

# 3. Activate the Virtual Environment
# (Use first line for Windows PowerShell, or second for Mac/Linux/GitBash)
.\venv\Scripts\activate
source venv/bin/activate

# 4. Install Pytest and Playwright packages
pip install pytest pytest-playwright

# 5. Download the Playwright browser binaries
playwright install
