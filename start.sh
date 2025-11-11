#!/usr/bin/env bash
# start server using gunicorn
gunicorn app:app --bind 0.0.0.0:$PORT