#!/bin/bash

alembic upgrade a6d3f7aa52eb

alembic upgrade afa651b55254

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000