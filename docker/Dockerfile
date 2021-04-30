####
# This Dockerfile is used in order to build a container that runs the Spring Boot application
#
# Build the image with:
#
# docker build -f docker/Dockerfile -t python/sample-basic .
#
# Then run the container using:
#
# docker run -i --rm -p 8080:8080 python/sample-basic
####
FROM python:slim

WORKDIR /projects
COPY . .

RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python", "app.py"]

