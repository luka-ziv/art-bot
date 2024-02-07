FROM python:latest

# Copies files from local dest. (first arg) to container dest. (second arg)
ADD . ./app

# Sets working directory IN container. If WORKDIR not set to location of server py file, causes problems with uvicorn run command.
WORKDIR /app

EXPOSE 80

# Receives build-arg from command line stores to variable API_KEY `set in shell with --build-arg API_KEY=...`
ARG API_KEY
# Sets stored variable as environment variable. Need to pass shell variable on container run command.
ENV API_KEY=${API_KEY}

# Command is being run IN the container, so paths need to reflect this.
RUN pip install --no-cache-dir -r requirements.txt

# Port on run command must match exposed port.
CMD ["uvicorn", "src.main:app", "--port", "80"]