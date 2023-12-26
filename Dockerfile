# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
# Your requirements.txt needs to include pytest for this to work
RUN pip install --no-cache-dir -r requirements.txt

# The CMD instruction defines the default command to run when starting the container
# Here, we use pytest to run tests with verbose output
CMD ["pytest", "-v"]
