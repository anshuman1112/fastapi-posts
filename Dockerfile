FROM python:3.9-slim

WORKDIR /c/Users/anshu/Documents/fastapi

COPY requirements.txt .

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

EXPOSE 8000
# EXPOSE 5432

#ENTRYPOINT ["alembic", "upgrade", "head", "&&", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]

ENTRYPOINT ["./docker-entrypoint.sh"]