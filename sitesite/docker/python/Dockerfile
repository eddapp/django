FROM python:3
MAINTAINER eddapp@zoho.com
ENV PYTHONUNBUFFERED 1
#RUN mkdir /sitesite
COPY /app /app
WORKDIR /app
#ADD requirements.txt /sitesite/
RUN pip install -r requirements.txt
#ADD . /sitesite/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]