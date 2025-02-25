# Use the official lightweight Python image
FROM python:3.11-windowsservercore

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY CommitFetcher.py .

# Command to run your Python script
CMD ["python", "CommitFetcher.py"]
