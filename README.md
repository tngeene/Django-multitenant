# Multitenant application

A multitenant app built with django. Uses Isolated db for each tenant with a shared app server.

## Requirements

- Python 3.6+ installed
- Text editor such as [vs code](https://code.visualstudio.com/) or sublime text
- Git

## Setup

1. Clone the repository.
2. Change directory to the location of this repository.
3. Create a `.env` file using the included `.env.example` as an example.
4. Create and start your preferred Python virtual environment. Install the required libraries.

```bash
pip install -r requirements.txt
```

## Usage

To run locally:

- After installation ``cd`` into the project path and run the following commands:

 ``` python
 python manage.py migrate --database={dbname}
```

- Create a superuser by running the ``python manage.py createsuperuser --database={dbname}`` and fill in the details.

- Run ``python manage.py runserver``

- open the browser and run  ``localhost:8000`` or ``{schema_name}.localhost:8000`` (schema referring to the database you're using) , login with the credentials created for each db.

## Development

Pull the latest master version:

```bash
git pull origin master
```

Create local development branch and switch to it:

```bash
git branch dev
git checkout dev
```

Make desired changes then commit the branch.

```bash
git add .
git commit -m "changes to dev branch"
git push origin dev
```
