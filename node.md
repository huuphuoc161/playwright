# Using Python virtual environment
## for macOs
``
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
``

### Install Pytest:
+ pip install pytest
+ Check Pytest
+ pytest --version
+ Run Pytest
+ pytest [test_file]

### set up configuration to get html report
``
argument: -s -v  --headed --html=./report-results/report.html --capture=tee-sys --browser=firefox``
