# Test Topoly PIP Package

### Requirements
- Python 3 (3.5 or later)

### Setup Python Virtual Environment

Run:
``./setup.sh``

### Install Topoly package
Build topoly package:
1. In topoly project (main folder):
``python3 setup.py bdist_wheel``

Install Package
1. Navigate back to topoly_test and activate Python virtual environment:
``source venv/bin/activate``
  
2. Install topoly package
``pip install TOPOLY_PROJECT/dist/topoly*.whl``

### Run tests

python test_py_preprocess.py
