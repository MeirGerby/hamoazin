FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/

WORKDIR /app 

COPY ./requirements.txt .

RUN python -m pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt 

FROM base AS metadata-service
COPY ./shared ./shared/
COPY metadata_service/ ./metadata_service
CMD ["python", "-m", "metadata_service.main" ]

FROM base AS mongo-loader
COPY ./shared ./shared/
COPY mongo_loader/ ./mongo_loader
CMD ["python", "-m", "mongo_loader.main" ]

FROM base AS information-processing
COPY ./shared ./shared/
COPY information_processing/ ./information_processing
CMD ["python", "-m", "information_processing.main" ]

FROM base AS transcription
COPY ./shared ./shared/ 
COPY transcription_computer/ ./transcription_computer 
CMD ["python", "-m", "transcription_computer.main"]

FROM base AS content-clasification 
COPY ./shared ./shared/ 
COPY content_clasification ./content_clasification 
CMD ["python", "-m", "content_clasification.main"]

