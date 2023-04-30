# Use the official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Create a non-root user and set permissions
RUN useradd --create-home eoluser
RUN chown -R eoluser:eoluser /app
USER eoluser

# Copy the requirements file into the container
COPY --chown=appuser:appuser requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --user --trusted-host pypi.python.org -r requirements.txt

# Copy the Python script into the container
COPY --chown=eoluser:eoluser eol.py .

# Run the script when the container is launched
CMD ["python", "./eol.py"]
