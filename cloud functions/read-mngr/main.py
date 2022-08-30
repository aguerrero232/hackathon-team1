import sys
from google.cloud import firestore
import traceback

projectid="dell-hackathon-2022"
tableid="Managers"
db=firestore.Client(projectid)

def entry_point(request): 
    #https://brianli.com/how-to-enable-cors-for-a-google-cloud-function-using-http-invocation/
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
    id = request.args.get('id')
    try:
        if id:
            doc_ref = db.collection(tableid).document(id) #open ownership table
            data = doc_ref.get().to_dict() #get this document
            return (data, 200, headers) #return JSON
        else:
            return("Error: No ID provided", 400, headers)
    except BaseException as e:
      traceback.print_exception(*sys.exc_info())
      return ("Exception:" + str(e), 500, headers)