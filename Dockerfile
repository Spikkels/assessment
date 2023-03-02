# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /code
WORKDIR /usr/src/app/

# Copy the current directory contents into the container at /code
COPY . .

# Set the working directory to /usr/src/app/geousers
WORKDIR /usr/src/app/geousers/

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils \
    libproj-dev \
    gdal-bin \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000


