from fastapi import FastAPI,Path,HTTPException,Query
import pydantic
import json
import os
app=FastAPI()

# PATH:- used to provide documentation,validation rules(eg,description)

# HTTPException:- used to return custom HTTP error resposnses when something gets wrong in your API.(400,404,403 etc)

# Relative paths follow you (the terminal). Absolute paths follow the file.

# LOAD DATASET
# ABSOLUTE WAY
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(base_dir, 'patients.json')   
    with open(file_path, 'r') as f:
        data = json.load(f)

    return data

# RELATIVE
'''
def load_data():
    with open('patients.json', 'r) as f:
        data=json.load(f)
    
        return data
'''

# endpoints-user hits

# route-CRUD
# GET
# POST
# PUT
# DELETE

# fetch
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/about")

def about():
    return {'message':'A fully functional API to manage your patients records.'}

@app.get('/view')
def view():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')
# ... :- path parameters is required(COMPULSORY)
def view_patient(patient_id:str = Path(...,description='ID of the patients in database',example='P001')):
    # load all the patients

    data=load_data()

    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404,detail="Patient not found")

# /docs :- documentation of the webapp

# QUERY PARAMETERS(?): key-value pair: filter,sort,search,paging  1) sort_by   2) order

@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description="Sort on the basis of height,weight or bmi"),order:str=Query('asc',description="sort in asc or desc order")):

    valid_fields=['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select between asc or desc')
    
    data=load_data()
    # reverse = FALSE: ASCENDING else desc
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data
        

# CREATE-POST