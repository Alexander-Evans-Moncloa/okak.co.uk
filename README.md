# okak.co.uk

This repository contains all the necessary Django files for Dockerization, currently deployed at [okak.co.uk](https://okak.co.uk/). Please note that due to file size limitations, not all static files could be uploaded to GitHub. This repository aims to assist you in creating a similar product or portfolio website, a unique combination that may not have many examples available online.

## Dockerization Instructions (for Linux Ubuntu)

Follow these steps to Dockerize the application:

1. **Open Docker Desktop and log in:**
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

4. **Run the Docker container:**
   ```bash
   docker run -d -p 8081:8081 YOUR_DOCKER_USERNAME/docker-django:0.1.2
   ```

5. **Push the Docker image to your repository:**
   ```bash
   docker push YOUR_DOCKER_USERNAME/docker-django:0.1.2
   ```

6. **If Docker storage is full, remove an older image:**
   ```bash
   docker image rm YOUR_DOCKER_USERNAME/docker-django:0.1.0
   ```

## Server Deployment

To deploy on the server, run the following command:

*(Add the specific command or instructions for server deployment here.)*

---

Feel free to customize any sections further or add additional information as needed!
