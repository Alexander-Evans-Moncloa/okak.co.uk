
# okak.co.uk

This repository contains all the necessary Django files for Dockerization, currently deployed at [okak.co.uk](https://okak.co.uk/). Due to file size limitations, not all static files could be uploaded to GitHub. This repository aims to assist you in creating a similar product or portfolio website, which may not have many examples available online.

## Dockerization Instructions (for Linux Ubuntu)

Follow these steps to Dockerize the application:

1. **Open Docker Desktop then also log in through terminal:**
   ```bash
   docker login
   ```

2. **Navigate to the directory containing the files:**
   ```bash
   cd /home/YOUR_COMPUTER_NAME/FOLDER_ALL_THESE_FILES_ARE_IN
   ```

3. **Build the Docker image:**
   ```bash
   docker build --no-cache -t YOUR_DOCKER_USERNAME/docker-django:0.1.2 .
   ```
   *(You can use your preferred versioning system.)*

4. **Update the Django settings for local testing:**
   Add the following to your `settings.py` file to allow local access:
   ```python
   # Security settings
   ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']  # Add your domain if applicable
   ```

5. **Run the Docker container for testing:**
   ```bash
   docker run -d -p 8000:8000 YOUR_DOCKER_USERNAME/docker-django:0.1.2
   ```

6. **Push the Docker image to your repository:**
   ```bash
   docker push YOUR_DOCKER_USERNAME/docker-django:0.1.2
   ```

7. **If Docker storage is full, remove an older image:**
   ```bash
   docker image rm YOUR_DOCKER_USERNAME/docker-django:0.1.0
   ```

## Server Deployment

To deploy on the server, run the following command, adjusting the port as necessary (e.g., `8000:8000`):
```bash
docker run -d -p 8000:8000 YOUR_DOCKER_USERNAME/docker-django:0.1.2
```

