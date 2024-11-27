# Celero BFM FI Proto

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This project is a library to manage proto files for each domain in the BFM FI API. It uses tools like Poetry for dependency management and building, as well as linting and testing tools.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install the following software:

- Python 3.13
- Poetry
- Pip

To install Poetry and upgrade Pip, you can use the following command:

```sh
curl -sSL https://install.python-poetry.org | python3 - ; \
pip install --upgrade pip ; \
pip install poetry keyring keyrings.google-artifactregistry-auth ; \
poetry config repositories.google https://us-east1-python.pkg.dev/celero-main/celero-finance/
```

### Installing

Follow the steps below to set up the development environment:

1. Clone the repository:

```sh
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Install the project dependencies:

```sh
make local-install
```

3. Run linting to ensure the code is properly formatted:

```sh
make lint
```

4. Run the tests to ensure everything is working:

```sh
make test
```

## Usage <a name = "usage"></a>

To use the library, you can follow the examples below:

### Build Proto Files

To build all proto files, use:

```sh
make build-protos
```

To build proto files in a specific folder, use:

```sh
make build-proto folder=folder-name
```

### Clean Proto Files

To clean all generated `.py` and `.pyi` files, use:

```sh
make clean-protos
```
