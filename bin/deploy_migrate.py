#!/bin/sh
# Use when need migration on deploy

heroku maintenance:on --app millworkpioneers
heroku run python ./millworkapp/manage.py migrate --app millworkpioneers
heroku maintenance:off --app millworkpioneers
