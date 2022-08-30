from google.cloud import firestore
import traceback
import sys

projectid = "dell-hackathon-2022"
db = firestore.Client(projectid)
table_id="TeamMembers"

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
      doc_ref = db.collection(table_id).document(uid) #open ownership table
      prev_data = doc_ref.get().to_dict() #get this document
      key_in = lambda x, y: y in x ## check if key is in dictionary
      entry_nn = lambda x, y: x[y] is not None ## check if entry is not none
      check = lambda x, y: key_in(x, y) and entry_nn(x, y) ## check if key is in dictionary and entry is not none
      choice = lambda x, y: x[y] if check(x, y) else prev_data[y] ## if key is in dictionary and entry is not none, return entry, else return previous data entry
      updated_data =  {
        u'activated': choice(request_json, 'activated'),
        u'cohort': choice(request_json, 'cohort'),
        u'country': choice(request_json, 'country'),
        u'date_joined': choice(request_json, 'date_joined'),
        u'date_last_active': choice(request_json, 'date_last_active'),
        u'l4': choice(request_json, 'l4'),
        u'l5': choice(request_json, 'l5'),
        u'name': choice(request_json, 'name'),
        u'new_course_enrolled': choice(request_json, 'new_course_enrolled'),
        u'new_course_started': choice(request_json, 'new_course_started'),
        u'supervisor_id': choice(request_json, 'supervisor_id'),
        u'video_consumed': choice(request_json, 'video_consumed'),
        u'work_region': choice(request_json, 'work_region'), 
      }
      db.collection(table_id).document(uid).update(updated_data)
      return(f"Success: updated user {uid}.", 200, headers)
    else:
      return("Error: No id provided", 400, headers)
  except BaseException as e:
    traceback.print_exception(*sys.exc_info())
    return ("Exception:" + str(e), 500, headers)