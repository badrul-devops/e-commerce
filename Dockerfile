# Stage 1: Build stage
FROM python:3.9 as builder

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY . .



# Stage 2: Production stage
FROM python:3.9-slim

WORKDIR /app

# Copy the installed Python dependencies from the builder stage
COPY --from=builder /root/.local /root/.local

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Copy the Django project code and collected static files
COPY --from=builder /app .

# Expose the Django development server port (change it if needed)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
