FROM ubuntu:latest
MAINTAINER SARATH KUNALA
RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask
ADD project_app.py /home/project_app.py
EXPOSE 5000
CMD ["python", "/home/project_app.py"]
