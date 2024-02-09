FROM python:3.9
RUN apt update
RUN apt install -y python3-pip

# Set the working directory inside the container
WORKDIR /app

# Copy your application files into the container
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
# Define a command to run when the container starts
CMD ["echo", "Hello, Docker!"]
