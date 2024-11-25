FROM python:3.9
ADD app.py .
ADD data .
RUN pip install telebot schedule pyquotegen
CMD ["python","./app.py"]