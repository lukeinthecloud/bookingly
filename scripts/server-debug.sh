#!/bin/bash

export FLASK_APP=bookingly
export FLASK_ENV=development
export DATABASE_URL=test

flask run --port 8085
