FROM python:3.11-slim

RUN pip install pandas

WORKDIR /app
COPY pipeline.py pipeline.py
COPY wine_data.csv wine_data.csv

# Make port 80 available to the world outside this container
EXPOSE 80

ENTRYPOINT [ "python", "pipeline.py" ]