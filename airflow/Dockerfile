FROM apache/airflow:3.2.2

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jdk procps && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

USER airflow

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD python -c "import importlib.util; import sys; sys.exit(0 if importlib.util.find_spec('pyspark') else 1)" || exit 1