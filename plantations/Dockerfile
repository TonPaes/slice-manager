FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENV PORT 8000
EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]