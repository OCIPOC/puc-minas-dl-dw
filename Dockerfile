ARG VERSION_SPARK=3.1.2

FROM jupyter/pyspark-notebook:${VERSION_SPARK}

USER root

RUN pip install "jupyterlab>=3" "ipywidgets>=7.6"
