FROM python:latest
LABEL authors="gvazuk"
COPY "." "/app"
WORKDIR "/app"
RUN ["pip", "install", "-r", "requerments.txt"]
CMD ["python", "run.py"]
