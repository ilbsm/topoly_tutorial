# Test Topoly PIP Package

### Requirements
- Python 3 (3.5 or later)

### Setup Python Virtual Environment (Optional)

0. Install virtual environment package:
``python3 -m pip install -u virtualenv``
1. Create a new virtual environment in the venv folder: 
``python3 -m venv venv``
2. Activate this environment:
``source venv/bin/activate``
3. You may need to update pip before installing topoly:
``pip3 install --upgrade pip``

### Install Topoly package

Install topoly package
``pip install topoly``

### Run tutorial examples

1. Loading data
and
2. Finding loops (and other loop-like structures) 
``python import_and_find.py``
3. Knots, links and their polynomials
``python knots_links.py``
4. Gaussian linking number (GLN)
``python GLN.py``
5. Lassos and minimal surfaces
``python lasso_minimal_surface.py``
6. Map manipulation: Knot maps, GLN maps
``python matrices.py``
