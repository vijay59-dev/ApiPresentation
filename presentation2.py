import json

from flask import Flask, request
import jsonify

app = Flask(__name__)

students = { 'studentList': []}

@app.route('/', methods=['GET'])
def welcome():
    return 'Hello ABD'

@app.route('/api/showStudents', methods=['GET'])
def showStudents():
    if len(students['studentList']) > 0:
        return students['studentList']
    else:
        return 'No students present in class'


@app.route('/api/insertStudents/', methods=['POST'])
def insertStudents():
    student = {'name': request.json['name'], 'course': request.json['course']}
    students['studentList'].append(student)
    return '', 201

@app.route('/api/deleteStudent/<student_name>', methods=['DELETE'])
def deleteStudent(student_name):
    assert student_name == request.view_args['student_name']
    student_not_found = True
    for item in students['studentList']:
        if item['name'] == student_name:
            students['studentList'].remove(item)
            student_not_found = False
            return '', 204
        else:
            pass
    if student_not_found:
        return 'Student is not present in database',404


@app.route('/api/updateStudent', methods=['PUT'])
def updateStudent():
    student = request.args.to_dict()
    student_not_found = True
    for item in students['studentList']:
        if item['name'] == student['name']:
            item['course'] = student['course']
            student_not_found = False
            return '', 200
        else:
            pass
    if student_not_found:
        return 'Student is not present in database', 404


if __name__ == '__main__' :
    app.run(host='localhost',port=8080)