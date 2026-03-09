# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/src/ .

# Create non-root user for security
RUN useradd --no-create-home appuser
USER appuser

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
