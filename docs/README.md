#     

## Requirements

Install Python 3.11 using brew

```bash
brew install python@3.11
```

Inside the directory for this repo,
create and activate a virtual environment called `venv`
and load the dependencies needed for these scripts therein

```bash
/usr/local/bin/python3.11 -m venv venv
```

```bash
source venv/bin/activate
pip install -r requirements.dev.txt
```

Also, run this pre-commit setup script so that code quality
can be enforced using `black` before contributions are added to version control

```bash
pre-commit install --config .hooks-config.yaml --hook-type pre-commit
pre-commit install --config .hooks-config.yaml --hook-type pre-push
```

## Environment Variables

You will need a `.env.local` file with the following variables loaded
(ask a teammate for the database URLs)

```
LOG_LEVEL=DEBUG
OPENWEATHERMAP_API_KEY=
```
