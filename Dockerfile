FROM python:2.7-onbuild
COPY . /usr/src/app
EXPOSE 5000
CMD ["python", "app.py"]
