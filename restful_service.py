import requests, json

METHOD_GET = "get"
METHOD_POST = "post"
METHOD_PUT = "put"
METHOD_DELETE = "delete"

class ApiService :
    # if this instance doesn't get authentication, return None
    def __new__(cls, device_name, device_uuid):
        instance = super(ApiService, cls).__new__(cls)
        instance.__init__(device_name, device_uuid)

        if hasattr(instance, "authentication"):
            return instance

    def __init__(self, device_name, device_uuid):
        # if this created before (maybe __new__), pass initializing
        if hasattr(self, "authentication"):
            return

        # declare field info
        self.API_SEVER_URL = "http://210.89.176.83:8080/hereiam"
        self.AUTH_URL = self.API_SEVER_URL + "/auth/authenticate"

        self.deviceName = device_name
        self.deviceUUID = device_uuid

        device_info = {"id" : self.deviceName, "password" : self.deviceUUID, "role" : "ROLE_DEVICE"}
        resp = requests.post(self.AUTH_URL, json=device_info)

        if resp.status_code != 200 :
            print ("POST " + self.AUTH_URL + " : " + str(resp.status_code))
            self.authentication = None
            return

        print ('Created connection info')

        self.authentication = resp.json()['token']

    def _url(self, path):
        return self.API_SEVER_URL + path

    def send_request(self, url, body="", request_method=METHOD_GET):
        response = None
        headers = {"Authorization":self.authentication,"Content-Type":"application/json"}
        url = self._url(url)

        print (headers)
        print (url)

        if request_method == METHOD_GET:
            response = requests.get(url, headers=headers)
        elif request_method == METHOD_POST:
            response = requests.post(url, headers=headers, data=body)
        elif request_method == METHOD_DELETE:
            response = requests.delete(url, headers=headers, data=body)
        elif request_method == METHOD_PUT:
            response = requests.put(url, headers=headers, data=body)

        return response

    def send_attendance_request(self, course_info):
        return self.send_request("/attend", json.dumps(course_info), METHOD_POST)
