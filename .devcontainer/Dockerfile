FROM python:3.11.14-trixie

# install pre-commit
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt --no-cache-dir

WORKDIR /app
