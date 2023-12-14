# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /todoapp

# Copy only requirements file
COPY requirements.txt .

# Create and activate virtual environment, install dependencies, and run the application
RUN python -m venv env && \
    /bin/bash -c "source env/bin/activate && pip install --no-cache-dir -r requirements.txt"

# Copy only necessary application files into the container
COPY app.py /todoapp/
COPY templates/ /todoapp/templates/

# Expose the port that your Flask app is running on (change 5000 to your port if different)
EXPOSE 5000

# Command to activate virtual environment and run the application
CMD /bin/bash -c "source env/bin/activate && python app.py"
