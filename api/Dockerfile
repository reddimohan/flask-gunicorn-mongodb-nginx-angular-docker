FROM python:3.7-alpine

# Setting an environment variable with the directory
# where we will be running the app
ENV APP /app

# Creating a directory and instructing Docker to work on this from now on
RUN mkdir $APP
WORKDIR $APP

# Exposing the port for Gunicorn
EXPOSE 5000

# Copying requirements to the APP directory in order to install the required libs
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copying rest of the code to WORKDIR
COPY . .

# Finally, run the app with Gunicorn command
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "wsgi:app" ]