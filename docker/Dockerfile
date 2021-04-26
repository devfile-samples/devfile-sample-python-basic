FROM python:slim

WORKDIR /projects
COPY . .
RUN pip install --user -r requirements.txt

EXPOSE 8080
CMD [ "python", "app.py" ]
