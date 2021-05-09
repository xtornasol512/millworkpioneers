# Official MillworkPioneer WebPage



### Technologies

- Django 1.11+ It rocks!
- Python 3.6+ yeah!
- PostgreSQL 10+
- ColorLib Theme
- Vagrant for development

### Hosting & services

- Heroku
- AWS s3 for Media Files
- AWS SES for Send Mails


# Start development mode

- Install virtualenviroment with python3 and activate it

```
$ python3 -m venv .venv
$ source .venv/bin/activate
# The activated shell will look like follow:
(.venv) $ 
```
- Install Requirements
```
(.venv) $ pip install -r requirements.txt
```

### Set Enviroment Vars

Load the following envs with the `export` shell command

- DJANGO_SECRET_KEY
- DEBUG_STATE
- PRODUCTION
- DATABASE_URL


