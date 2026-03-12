## Project Setup
## create and activate virtual environment

```commandline
python3 -m venv venv
```

On MacOS:
```commandline
source venv/bin/activate
```

On Windows:
```commandline
venv\Scripts\activate
```

## install requirement project's packages

```commandline
pip install -r requirements.txt
```

## Run project

Go to the folder with manage.py file, run library
```commandline
python manage.py migrate 
```

```commandline
python manage.py runserver
```