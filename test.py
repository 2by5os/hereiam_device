import restful_service, time, json

api_service = restful_service.ApiService("device1", "8fe63a92-b916-11e6-80f5-76304dec7eb7")

print (api_service.authentication)

course_info = {'studentNum': '21360017', 'attendAt': int(time.time() * 1000),
             'courseInfo': {'day': 3, 'room': 'I203', 'courseName': '클라우드컴퓨팅', 'deviceAddr': '', 'time': 2}}

print("json data [%s]" % json.dumps(course_info))
response = api_service.send_attendance_request(course_info)
print(response.text)