FROM python:3.11.7-alpine
ENV APP_PATH="/app/edzyaml"
RUN mkdir -p ${APP_PATH}
WORKDIR ${APP_PATH}
COPY ./ ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python3","main.py"]