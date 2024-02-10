# Dockerfile
FROM python:3.9

WORKDIR /app

COPY add_numbers.py .

CMD ["python", "add_numbers.py"]
