



# Setup with pyenv

1. Install pyenv (reference)
2. Install correct python version `pyenv install 3.9`
3. Set python version on local repo `pyenv local 3.9`
4. Test by running `python --version` to check the python version. (Optional)
5. Install poetry `pip install poetry`.
6. Install dependencies and create virtualenv `poetry install`.
7. Activate virtualenvironment `poetry env activate` . For deactivate it just `deactivate`.



# Cheatsheet 

### Run Tests
Requirements : # Setup with pyenv

Run all the tests `poetry run pytest tests`
Run specific test `poetry run pytest tests/test_example/test_case.py`
Usign Makefile `make test`

### Add Dependecies
Requirements : # Setup with pyenv

1. Add requirements to the project and version it `poetry add pytest`.


### Formatter and Validator
Requirements : # Setup with pyenv

1. Using makefile `make format` and `make lint`




