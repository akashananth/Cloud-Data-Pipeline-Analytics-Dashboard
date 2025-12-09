FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all API code into the container
COPY . .

# Environment variables for DB inside Docker network
ENV DB_HOST=db
ENV DB_NAME=salesdb
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_PORT=5432

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
