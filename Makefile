setup:
	curl -sSL https://install.python-poetry.org | python3 - ; \
	pip install --upgrade pip ; \
	pip install poetry keyring keyrings.google-artifactregistry-auth ; \
	poetry config repositories.google https://us-east1-python.pkg.dev/celero-main/celero-finance/

local-install: setup
	poetry install --with dev

lint:
	poetry run black .

test:
	poetry run pytest -s --cov=celero_bfm_fi_proto --cov-report=html -W ignore::DeprecationWarning

clean-protos:
	@read -p "All .py and .pyi files in all folders in celero_bfm_fi_proto will be deleted. Do you want to continue? [yes, no, y, n]: " confirm; \
  case "$$confirm" in \
    [yY][eE][sS]|[yY]) \
      find ./celero_bfm_fi_proto/ -name "*.py" ! -name "__init__.py" -exec rm -f {} + -o -name "*.pyi" -exec rm -f {} +; \
      ;; \
    *) \
      echo "Operation cancelled."; \
      exit 1; \
      ;; \
  esac

build-protos: clean-protos
	@for proto_file in $(shell find ./celero_bfm_fi_proto -name "*.proto"); do \
	  echo "Building $$proto_file"; \
		poetry run python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. --pyi_out=. $$proto_file > /dev/null 2>&1; \
	done

build-proto:
	@read -p "All .py and .pyi files in the folder celero_bfm_fi_proto/$${folder} will be deleted. Do you want to continue? [yes, no, y, n]: " confirm; \
	case "$$confirm" in \
		[yY][eE][sS]|[yY]) \
			find ./celero_bfm_fi_proto/$(folder)/ -name "*.py" ! -name "__init__.py" -exec rm -f {} + -o -name "*.pyi" -exec rm -f {} +; \
			for proto_file in $(shell find ./celero_bfm_fi_proto/$(folder) -name "*.proto"); do \
				echo "Building $$proto_file"; \
				poetry run python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. --pyi_out=. $$proto_file > /dev/null 2>&1; \
			done \
			;; \
		*) \
			echo "Operation cancelled."; \
			exit 1; \
			;; \
	esac