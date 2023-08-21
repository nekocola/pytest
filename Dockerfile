FROM python:3.7
 
WORKDIR ./python_rds
 
ADD . .
 
RUN pip install -r requirements.txt
 
CMD ["python", "./src/main.py"]
