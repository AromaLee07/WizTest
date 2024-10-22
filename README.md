# WizTest
> This is the code for front-end automated testing, used to test https://www.wizmarketplace.com/


## Installation

Front-end: Python + Selenium + Unittest
Back-end: Postman

Use Python Virtual Environment
- python3 -m venv myenv
- source myenv/bin/activate

Pip Install Package
- pip install selenium
- pip install webdriver-manager
- pip install pytest-html 
- pip install pytest


## Quick Start

- run all the test cases: python run_tests.py
- run all the test cases and generate report: pytest --html=report.html


## Features

The business covered by the test cases includes:

- Sign up / Login / Forgot password
- User Profile / Change password
- Find Products
- Favourite Products
- Add to cart
- Place order


## Test Cases and Test Reports
- Test Cases: https://lvbjv6o2rsw.feishu.cn/docx/VAqodeWOwoS4PtxWWCnciFSpnIc?from=from_copylink
- UI Test Report: WIZ_UI_TEST_REPORT.html (download it for a better reading)
- API Test Report: WIZ_API_TEST_REPORT.jpeg
  

## FAQ

- About testcases, I keep the columns for Steps/ExpectResult/ActualResult as blank for the tight schedule
- I marked it as "automated" in testcases if this case has been automated
- All the Chinese comments in this code was just for your convenience in reviewing


