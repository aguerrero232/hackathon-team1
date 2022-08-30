import sys
from google.cloud import firestore

projectid="dell-hackathon-2022"
tableid="Courses"
db=firestore.Client(projectid)

def entry_point(request): 
    if request.method == 'OPTIONS':
        ## Allows GET requests from any origin with the Content-Type
        headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    ## Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    print(f"req: {request}")
    course_name = request.args.get('course_name')
    try:
        if course_name:
            doc_ref = db.collection(tableid).document(course_name) #open ownership table
            data = doc_ref.get().to_dict() #get this document
            return (data, 200, headers) #return JSON
        else:
            return("Error: No Course name provided", 400, headers)
    except BaseException as e:
      return ("Exception:" + str(e.with_traceback()), 500, headers)
