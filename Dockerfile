FROM python:3.9

WORKDIR /src

RUN echo "Copying source code..."
COPY requirements.txt .
COPY requirements_dev.txt .
COPY setup.cfg .
COPY Makefile .
COPY scripts  ./scripts
COPY app/ ./app
RUN  mkdir -p /src/data

RUN echo "Installing  dependencies..."

RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements_dev.txt

RUN echo "Downloading  datasets..."
RUN python3 scripts/download_trips_data.py

RUN echo "Running linting..."

RUN make lint

RUN echo "Running tests..."

RUN make test

ENV PORT_NUM=8080
ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
ENV ERROR_LOG=${ERROR_LOG:-/proc/1/fd/2}

ENTRYPOINT /usr/local/bin/gunicorn \
  -b 0.0.0.0:"$PORT_NUM" \
  -w 4 \
  -k uvicorn.workers.UvicornWorker main:app \
  --chdir ./app \
  --access-logfile "$ACCESS_LOG" \
  --error-logfile "$ERROR_LOG"