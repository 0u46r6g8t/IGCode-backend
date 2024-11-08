FROM python:3.10.12 AS base

# [1] - Configuration virtualenv
RUN pip install virtualenv

RUN python -m venv env

RUN /bin/bash -c "source /env/bin/activate"

# [2] - Create application
WORKDIR /app

COPY ./container/requirements.txt /app/requirements.txt 

COPY ./src /app/

# [3] - Installation of requirements
RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

RUN mkdir /app/logs/

# [5] - Running the application
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]