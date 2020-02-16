from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def setup():
    global creds
    global SCOPES
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

def getTasksList():
    global service
    results= service.tasklists().list().execute()
    items= results.get('items', [])
    return items

def getTasks(listID):
    global service
    tasks= service.tasks().list(tasklist=listID).execute()
    return tasks

def printTasklist(tasks):
    for task in tasks:
        print(task['title'])

def makeUsableList():
    global service
    lists= getTasksList()
    retList= []
    for each in lists:
        thisTasks= getTasks(each['id'])
        tasks= []
        try:
            for x in thisTasks['items']:
                tasks.append({
                    'title': x['title'],
                    'id': x['id']
                })
        except KeyError:
            pass
        
        yield {
            'title': each['title'],
            'id': each['id'],
            'items': tasks
        }

def addTask(title='', notes='', due= None, listID='@default'):
    global service
    task= {
        'title': title,
        'notes': notes,
        'due': due
    }
    result= service.tasks().insert(tasklist= listID, body= task).execute()
    return result['id']

def getTask(listID, taskID):
    global service
    return service.tasks().get(tasklist=listID, task=taskID).execute()

def updateTask(listID, taskID, updates):
    global service
    task= getTask(listID, taskID)
    try:
        task['title']= updates['title']
        task['status']= updates['status']
    except KeyError:
        pass
    result= service.tasks().update(tasklist=listID, task=taskID, body=task).execute()
    return result

def deleteTask(listID, taskID):
    global service
    return True if(service.tasks().delete(tasklist=listID, task=taskID).execute()=="") else False

def clearCompleted(listID):
    global service
    return True if(service.tasks().clear(tasklist=listID).execute()=="") else False


SCOPES= ['https://www.googleapis.com/auth/tasks']
creds= None
setup()
service= build('tasks', 'v1', credentials=creds)
tasklist= makeUsableList()
for x in tasklist:
    print(x)

