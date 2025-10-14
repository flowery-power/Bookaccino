FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /bookaccino-app    

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
#python manage.py check

COPY . .

EXPOSE 8000

CMD ["sh","-lc","python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
