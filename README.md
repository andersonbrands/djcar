# djcar

A car management app

## How to use

Clone the repo

```bash
git clone git@github.com:andersonbrands/djcar.git .
```

Create and activate a virtual environment

```bash
python -m venv .venv

source .venv/bin/activate
```

Install dev requirements

```bash
pip install -r requirements-dev.txt
```

Copy `.env-sample` into `.env`

```bash
cp .env-sample .env
```

Feel free to update the variables of the .env file according your needs. Ex:

```text
SECRET_KEY=l0-wtnff)#&tgad52i)!a=94yg0i+*+(3n7yx)aos26a$^dmr*
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, .localhost
```

You can generate a secret key with this:

```bash
python contrib/secret_gen.py
```

Run the pre-commit install if you intend to commit new changes

```bash
pre-commit install
```

Apply migrations

```bash
python manage.py migrate
```

Run tests with pytest

```bash
pytest
```

Finally, run the django development server.

```bash
# if you have Debug=True
python manage.py runserver

# if you have Debug=False
python manage.py runserver --insecure
```

Hit http://127.0.0.1:8000/ (or whatever address your terminal says so) on your browser, and you should have access to the app.
