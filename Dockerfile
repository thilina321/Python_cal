FROM python:3.9
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/thilina321/Python_cal.git/app
WORKDIR /app
copy calculator.py .
CMD ["sh", "-c", "git pull && python calculator.py"]
