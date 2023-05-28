FROM python:3.10.5
ADD presentation2.py .
RUN pip install flask
RUN pip install jsonify


#COPY Attendance.xlsx /

EXPOSE 3333
CMD ["python","./presentation2.py"]