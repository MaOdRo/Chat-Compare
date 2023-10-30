FROM python:3.10.6-slim

# upgrade pip
RUN pip install --upgrade pip

# copy all the files to the container
COPY . .

# venv
ENV VIRTUAL_ENV=/home/app/venv

# python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

CMD ["python", "app.py"]