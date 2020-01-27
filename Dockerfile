FROM osgeo/gdal:latest

# Set app directory
WORKDIR /usr/src/tiff-labelwriter

# Install server dependencies
RUN apt-get update \
    && apt-get install -y python3-pip wget less;

# Install python dependencies
RUN pip3 install flask

# Copy labelwriter app
COPY *.py ./
COPY bin/ bin/
COPY static/ static/
COPY templates/ templates/

RUN mkdir tmp

# Expose app port
EXPOSE 5000

# Start Flask app
CMD flask run --host=0.0.0.0;