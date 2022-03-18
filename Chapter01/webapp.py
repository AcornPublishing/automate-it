__author__ = 'Chetan'

from bottle import route, run
from bottle import response, request
import json

tasks = {
    "tasks":
    [
        {"id": 1, "task": "Write a book", "status": "OPEN"},
        {"id": 2, "task": "Wash my clothes", "status": "COMPLETE"},
        {"id": 3, "task": "Go for a movie", "status": "INPROGRESS"}
    ]
}

@route('/tasks')
def task():
    response.content_type = 'application/json'
    return json.dumps(tasks)

@route('/tasks/<id>', method='GET')
def task_list(id):
    for data in tasks["tasks"]:
        if data["id"] == int(id):
            response.content_type = 'application/json'
            return json.dumps(data)

@route('/tasks/<id>', method='PUT')
def task_update(id, status="COMPLETE"):
    for data in tasks["tasks"]:
        if data["id"] == int(id):
            data["status"] = status
            response.content_type = 'application/json'
            return json.dumps(data)

@route('/tasks', method='POST')
def task_create():
    task = request.forms.get("task")
    new_task = {
        "id": 999,
        "task": task,
        "status": "OPEN",
    }
    tasks["tasks"].append(new_task)
    response.content_type = 'application/json'
    return json.dumps(tasks)

@route('/tasks/<id>', method='DELETE')
def task_delete(id):
    for data in tasks["tasks"]:
        if data["id"] == int(id):
            tasks["tasks"].remove(data)
        response.content_type = 'application/json'
    return json.dumps(tasks)

run(host='localhost', port=8080, debug=True)