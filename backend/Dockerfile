# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the backend code to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x startup.sh

# Expose the default Django port
EXPOSE 8000

# Set the default command to run Django
CMD ["./startup.sh"]
