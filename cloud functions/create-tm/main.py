from google.cloud import firestore

projectid = "dell-hackathon-2022"
db = firestore.Client(projectid)
collection="TeamMembers"

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
        u'activated': request_json['activated'],
        u'cohort':request_json['cohort'],
        u'country':request_json['country'],
        u'date_joined': request_json['date_joined'],
        u'date_last_active': request_json['date_last_active'],
        u'l4': request_json['l4'],
        u'l5': request_json['l5'],
        u'name': request_json['name'],
        u'new_course_enrolled': request_json['new_course_enrolled'],
        u'new_course_started': request_json['new_course_started'],
        u'supervisor_id': request_json['supervisor_id'],
        u'video_consumed': request_json['video_consumed'],
        u'work_region': request_json['work_region'], 
      }
      db.collection(collection).document(uid).set(data)
      return(f"Success: created new user {uid}.", 200, headers)
    else:
      return("Error: No ID provided", 400, headers)
  except BaseException as e:
    return ("Exception:" + str(e.with_traceback()), 500, headers)