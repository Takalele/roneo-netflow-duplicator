FROM python:3-slim
LABEL Athor Takalele - Andreas Cymbal

WORKDIR /app
COPY . .
RUN pip install .
RUN mv roneo-config-example.yaml roneo-config.yaml
CMD ["roneo", "--configfile /app/roneo-config.yaml"]