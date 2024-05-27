FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY pipeline.py pipeline.py

# Make port 80 available to the world outside this container
EXPOSE 80

ENTRYPOINT [ "python", "pipeline.py" ]