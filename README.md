# SOC Classification Library

Standard Occupational Classification (SOC) Library, initially developed for Survey Assist API but can be used elsewhere.

## Overview

SOC classification library, utilities used to classify occupation code based off of ${\small\color{red}\text{TODO}}$.

## Features

- SOC Lookup.  A utility that uses a well-known set of SOC mappings of ${\small\color{red}\text{TODO}}$ to SOC classification codes.
- SOC Classification. A RAG approach to classification of SOC using input data, semantic search and LLM. ${\small\color{red}\text{TODO: confirm this is correct for SOC}}$.

## Prerequisites

Ensure you have the following installed on your local machine:

- [ ] Python 3.12 (Recommended: use `pyenv` to manage versions)
- [ ] `poetry` (for dependency management)
- [ ] Colima (if running locally with containers)
- [ ] Terraform (for infrastructure management)
- [ ] Google Cloud SDK (`gcloud`) with appropriate permissions

### Local Development Setup

The Makefile defines a set of commonly used commands and workflows.  Where possible use the files defined in the Makefile.

#### Clone the repository

```bash
git clone https://github.com/ONSdigital/soc-classification-library.git
cd soc-classification-library
```

#### Install Dependencies

```bash
poetry install
```

#### Add Git Hooks

Git hooks can be used to check code before commit. To install run:

```bash
pre-commit install
```

### Run Locally

${\small\color{red}\text{TODO: implement local example script(s)}}$


### GCP Setup

${\small\color{red}\text{TODO}}$

### Code Quality

Code quality and static analysis will be enforced using isort, black, ruff, mypy and pylint. Security checking will be enhanced by running bandit.

To check the code quality, but only report any errors without auto-fix run:

```bash
make check-python-nofix
```

To check the code quality and automatically fix errors where possible run:

```bash
make check-python
```

### Documentation

Documentation is available in the docs folder and can be viewed using mkdocs

${\small\color{red}\text{TODO: write documentation}}$

```bash
make run-docs
```

### Testing

${\small\color{red}\text{TODO: implement tests}}$

Pytest is used for testing alongside pytest-cov for coverage testing.  [/tests/conftest.py](/tests/conftest.py) defines config used by the tests.

Unit testing for utility functions is added to the [/tests/tests_utils.py](./tests/tests_utils.py)

```bash
make unit-tests
```

All tests can be run using

```bash
make all-tests
```

### Environment Variables

${\small\color{red}\text{TODO}}$
