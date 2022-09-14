from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
#from django.conf import settings
import mysql.connector
import json

api_view()

def dbconnection():
    db1 = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "whocares@MySQL98!",
        database = "db1"
    )
    return db1

@csrf_exempt
def get_none (request):
    db = dbconnection()
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Employee")
    lst = []
    for i in mycursor:
        result = {"Employee ID ": i[0], "Employee Name " : i[1], "Department Name" : i[2], "Image Name" : i[3]}
        lst.append(result)
    finallst = {"Retrieved data" : lst }
    return JsonResponse( finallst )

def get (request):
    db = dbconnection()
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Employee")
    id = result = 0
    id = request.GET['Employee_ID']
    print (id)
    if (id != 0):
        for i in mycursor:
            if ( i[0] ==  int(id )):
                result = {"Employee ID ": i[0], "Employee Name " : i[1], "Department Name" : i[2], "Image Name" : i[3]}
                break
            else:
                result = {"Error ": "Enter a valid ID number."}
    finallst = {"Retrieved data" : result }
    return JsonResponse( finallst )

@csrf_exempt
def post (request):
    db = dbconnection()
    mycursor = db.cursor()
    name = request.GET['Employee_Name']
    deptName = request.GET['Department_Name']
    mycursor.execute("INSERT INTO Employee (Name, Dept) VALUES (%s, %s)", (name, deptName))
    db.commit()
    response = { "POST": "The below data has been inserted.", "Employee Name": name, "Department Name": deptName }
    return JsonResponse( response )

@csrf_exempt
def put_raw (request):   
    db = dbconnection()
    mycursor = db.cursor() 
    respond = json.loads(request.body.decode('utf-8'))
    id = respond['Employee_ID']
    deptName = respond['Department_Name']
    mycursor.execute("""UPDATE Employee SET Dept = %s WHERE EmpID = %s""", (deptName, id))
    db.commit()
    response = { "PUT": "The data has been updated." }
    return JsonResponse( response )

@csrf_exempt
def delete (request):
    db = dbconnection()
    mycursor = db.cursor() 
    id = request.GET['Employee_ID']
    mycursor.execute("""DELETE FROM Employee WHERE EmpID = %s""", (id, ))
    db.commit()
    response = { "DELETE": "The data has been deleted!" }
    return JsonResponse( response )

@csrf_exempt
def post_form (request):
    db = dbconnection()
    mycursor = db.cursor() 
    respond = request.POST
    response = respond.dict()
    name = response['Employee_Name']
    deptName = response['Department_Name']
    mycursor.execute("INSERT INTO Employee (Name, Dept) VALUES (%s, %s)", (name, deptName))
    db.commit()
    response = { "POST": "The below data has been inserted.", "Employee Name": name, "Department Name": deptName }
    return JsonResponse( response )

@csrf_exempt
def put (request):
    db = dbconnection()
    mycursor = db.cursor() 
    EID = request.GET['Employee_ID']
    DName = request.GET['Department_Name']
    mycursor.execute("""UPDATE Employee SET Dept = %s WHERE EmpID = %s""", (DName, EID))
    db.commit()
    response = { "PUT": "The data has been updated." }
    return JsonResponse( response )

@csrf_exempt
def upload (request):
    db = dbconnection()
    mycursor = db.cursor() 
    temp = request.FILES["image"]
    img = temp.name
    path = default_storage.save(temp, ContentFile(temp.read()))
    print ("\n\n", path, "\n\n")
    respond = request.POST
    response = respond.dict()
    name = response['Employee_Name']
    deptName = response['Department_Name']
    mycursor.execute("INSERT INTO Employee (Name, Dept, ImageName) VALUES (%s, %s, %s)", (name, deptName, img))
    db.commit()
    response = { "POST": "The below data has been inserted.", "Employee Name": name, "Department Name": deptName, "Image Name": img }
    return JsonResponse( response )