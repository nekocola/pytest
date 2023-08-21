FROM python:3.7
 
WORKDIR ./python_rds
 
ADD . .
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --upgrade pip 
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip install -r requirements.txt
 
CMD ["python", "./src/main.py"]
