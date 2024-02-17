
FROM python:3.10

WORKDIR /api

# copying the requirements.txt file separately and installing dependencies before copying the rest of the application code 
# is a good practice. It allows Docker to take advantage of caching during the build process, making the build faster when 
# the requirements.txt file hasn't changed.

COPY requirements.txt /api/

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /api

# Expose the port on which the FastAPI application will run inside the container
EXPOSE 80

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port","8000"]
