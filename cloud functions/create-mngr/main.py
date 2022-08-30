from google.cloud import firestore

import traceback

import sys



projectid = "dell-hackathon-2022"

db = firestore.Client(projectid)

collection="Managers"



def entry_point(request):

  if request.method == 'OPTIONS':

    headers = {

      'Access-Control-Allow-Origin': '*',

      'Access-Control-Allow-Methods': 'GET',

      'Access-Control-Allow-Headers': 'Content-Type',

      'Access-Control-Max-Age': '3600'

    }

    return ('', 204, headers)

  headers = {

    'Access-Control-Allow-Origin': '*'

  }



  request_json = request.get_json()

  

  print(f'req: {request_json}')

  

  print(f"uid: {request_json['id']}")



  try:

    if 'id' in request_json:

      uid = request_json['id']

      data =  {

        u'name': request_json['name'],  

        u'l4': request_json['l4'],

        u'l5': request_json['l5'],

        u'country':request_json['country'],

        u'work_region': request_json['work_region'], 

      }

      db.collection(collection).document(uid).set(data)

      return(f"Success: created new manager {uid}.", 200, headers)

    else:

      return("Error: No ID provided", 400, headers)

  except BaseException as e:

    traceback.print_exception(*sys.exc_info())

    return ("Exception:" + str(e), 500, headers)