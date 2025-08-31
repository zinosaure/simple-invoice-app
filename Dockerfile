FROM python:latest

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN python -m ensurepip --upgrade
RUN pip install requests
RUN pip install fastapi
RUN pip install jinja2
RUN pip install uvicorn[standard]
RUN pip install git+https://github.com/zinosaure/flex-polars.git@main

COPY ./src /app/src
WORKDIR /app/src

EXPOSE 80
CMD ["uvicorn", "main:app", "--host" , "0.0.0.0", "--port", "80", "--reload"]
