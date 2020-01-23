FROM osgeo/gdal:latest

# Set app directory
WORKDIR /usr/src/gdal_playground

# Install server dependencies
RUN apt-get update \
    && apt-get install -y python3-pip wget less;

# Install python dependencies
RUN pip3 install flask

# Copy labelwriter app
COPY app.py app.py
COPY bin/ bin/
COPY static/ static/
COPY templates/ templates/

# Expose app port
EXPOSE 5000

# Start Flask app
CMD env FLASK_APP=app.py flask run --host=0.0.0.0;