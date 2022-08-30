from google.cloud import firestore

projectid = "dell-hackathon-2022"
db = firestore.Client(projectid)
collection="Courses"

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
      data =  {  
        u'course_author': request_json['course_author'],
        u'course_source':request_json['course_source'],
        u'description':request_json['description'],
        u'total_minutes': request_json['total_minutes'],
  
      }
      db.collection(collection).document(course).set(data)
      return(f"Success: created course {course}", 200, headers)
    else:
      return("Error: No course provided", 400, headers)
  except BaseException as e:
    return ("Exception:" + str(e.with_traceback()), 500, headers)