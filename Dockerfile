FROM python:3.11
 
WORKDIR ./python_rds
 
ADD . .
 
RUN pip install -r requirements.txt
 
CMD ["python", "./src/main.py"]
