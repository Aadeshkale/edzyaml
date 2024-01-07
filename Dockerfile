FROM python:3.11.7-alpine
ENV APP_PATH="/app/edzyaml"
RUN mkdir -p ${APP_PATH} && \
    apk add git && \
    git config --global user.email "edzyaml@example.com" && \
    git config --global user.name "edzyaml"
WORKDIR ${APP_PATH}
COPY ./ ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# RUN chmod +x main.py
CMD ["python","/app/edzyaml/main.py"]