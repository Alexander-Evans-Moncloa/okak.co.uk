# Use the official Python image
FROM python:3.12.4

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements.txt first to install dependencies
COPY requirements.txt .

# Install Django dependencies
RUN pip install -r requirements.txt

# Copy the Django app files into the container
COPY . .

# Expose only the internal Django port
EXPOSE 8081

# Run Django migrations and then start the Django app
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py create_superuser && python manage.py runserver 0.0.0.0:8081"]
