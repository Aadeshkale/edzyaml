FROM python:3.11.7-alpine
ENV APP_PATH="/app/edzyaml"
RUN mkdir -p ${APP_PATH}
WORKDIR ${APP_PATH}
COPY main.py ./
CMD ["python3","main.py"]