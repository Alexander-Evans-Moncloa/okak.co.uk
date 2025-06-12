# okak.co.uk
All django files, ready for Dockerisation.

These exact files are running on https://okak.co.uk/ right now, however GitHub doesn't let me upload all of the files in static (too large). Should help you if you desire to make a similar product/portfolio website (a weird combination that I was unable to find many examples of online).

Instructions to Dockerise (on Linux Ubuntu):

#open docker desktop and log in
docker login 
cd /home/YOUR_COMPUTER_NAME/FOLDER_ALL_THESE_FILES_ARE_IN
docker build --no-cache -t YOUR_DOCKER_USERNAME/docker-django:0.1.2 . #use whatever number system you want
docker run -d -p 8081:8081 YOUR_DOCKER_USERNAME/docker-django:0.1.2
docker push YOUR_DOCKER_USERNAME/docker-django:0.1.2


#if docker is full, remove an older image
docker image rm YOUR_DOCKER_USERNAME/docker-django:0.1.0

#on the server, run this:


