FROM python:3.12

WORKDIR /contelizer

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt && \
    pip install -r requirements_dev.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

HEALTHCHECK --interval=5m --timeout=15s \
    CMD curl -f http://0.0.0.0:8000/api || exit 1
