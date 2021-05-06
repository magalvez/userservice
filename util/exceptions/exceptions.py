from werkzeug.exceptions import HTTPException


class BadRequest(HTTPException):
    def __init__(self):
        HTTPException.__init__(self)
        self.code = 400
        self.data = dict()
        self.data['message'] = 'The request cannot be fulfilled due to bad syntax.'


class ApiResponseNotFound(HTTPException):
    def __init__(self, data_request_id):
        HTTPException.__init__(self)
        self.code = 404
        self.data = dict()
        self.data['message'] = "There is not an api response associated to the data request with id '{0}'".format(
            data_request_id)


class UserAuthNotFound(HTTPException):
    def __init__(self, user_name, password):
        HTTPException.__init__(self)
        self.code = 404
        self.data = {
            'message': "The User with user_name: {} and password: {} was not found.".format(
                user_name, password
            )
        }


class UserNotFound(HTTPException):
    def __init__(self, user_id, pin):
        HTTPException.__init__(self)
        self.code = 404
        self.data = {
            'message': "The User with user_id: {} and pin: {} was not found.".format(
                user_id, pin
            )
        }


class UserInvalidVerification(HTTPException):
    def __init__(self, user_id, pin):
        HTTPException.__init__(self)
        self.code = 401
        self.data = {
            'message': "The User your trying to process is not validate. [user_id: {} and pin: {}].".format(
                user_id, pin
            )
        }
