# Test Topoly PIP Package

### Requirements
Python 3 (3.5 or later)

### Setup Python Virtual Environment (Optional)

1. Create a new virtual environment in the venv folder:  
``python3 -m venv venv`` 
or:  
``python3 -m virtualenv venv``   
depending whether you use the python3 built-in ``venv`` module or the optional ``virtualenv``.
If ``venv`` is not available you can install ``virtualenv`` by running:  
``python3 -m pip install --user virtualenv``   
2. Activate this environment:
``source venv/bin/activate``


### Install Topoly package

1. You may need to update pip before installing topoly:
``pip3 install --upgrade pip``

2. Install topoly package
``pip3 install topoly``

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
