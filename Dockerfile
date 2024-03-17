FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install PyPDF2

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "wsgi:app"]

