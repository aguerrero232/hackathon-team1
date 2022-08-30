from google.cloud import firestore
import traceback
import sys

projectid = "dell-hackathon-2022"
db = firestore.Client(projectid)
table_id="Courses"

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

  try:
    if 'course_name' in request_json:
      course = request_json['course_name']
      doc_ref = db.collection(table_id).document(course) #open ownership table
      prev_data = doc_ref.get().to_dict() #get this document
      key_in = lambda x, y: y in x ## check if key is in dictionary
      entry_nn = lambda x, y: x[y] is not None ## check if entry is not none
      check = lambda x, y: key_in(x, y) and entry_nn(x, y) ## check if key is in dictionary and entry is not none
      choice = lambda x, y: x[y] if check(x, y) else prev_data[y] ## if key is in dictionary and entry is not none, return entry, else return previous data entry
      updated_data =  {
        u'course_author': choice(request_json, 'course_author'),
        u'course_source': choice(request_json, 'course_source'),
        u'description': choice(request_json, 'description'),
        u'total_minutes': choice(request_json, 'total_minutes'),
      }
      db.collection(table_id).document(course).update(updated_data)
      return(f"Success: updated course '{course}'.", 200, headers)
    else:
      return("Error: No course provided", 400, headers)
  except BaseException as e:
    traceback.print_exception(*sys.exc_info())
    return ("Exception:" + str(e), 500, headers)