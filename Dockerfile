FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Install the application in development mode
RUN pip install -e .

# Set the Python path to include the app directory
ENV PYTHONPATH=/app

# Expose the port
EXPOSE 5000

# Make sure templates directory is accessible
RUN mkdir -p app/templates
COPY templates/* app/templates/

# Use gunicorn with debug logging to help diagnose issues
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--log-level", "debug", "wsgi:app"]