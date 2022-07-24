FROM python:3.10.2

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/vmss_vac

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD [ "python", "manage.py", "runserver", "0.0.0.0:5001" ]