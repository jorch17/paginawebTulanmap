import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_tarifa, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_tarifa) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tarifa, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_tarifa) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_tarifa, **k):

    @staticmethod
    def POST_DELETE(id_tarifa, **k):
    '''

    def GET(self, id_tarifa, **k):
        message = None # Error message
        id_tarifa = config.check_secure_val(str(id_tarifa)) # HMAC id_tarifa validate
        result = config.model.get_tarifas(int(id_tarifa)) # search  id_tarifa
        result.id_tarifa = config.make_secure_val(str(result.id_tarifa)) # apply HMAC for id_tarifa
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_tarifa, **k):
        form = config.web.input() # get form data
        form['id_tarifa'] = config.check_secure_val(str(form['id_tarifa'])) # HMAC id_tarifa validate
        result = config.model.delete_tarifas(form['id_tarifa']) # get tarifas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_tarifa = config.check_secure_val(str(id_tarifa))  # HMAC user validate
            id_tarifa = config.check_secure_val(str(id_tarifa))  # HMAC user validate
            result = config.model.get_tarifas(int(id_tarifa)) # get id_tarifa data
            result.id_tarifa = config.make_secure_val(str(result.id_tarifa)) # apply HMAC to id_tarifa
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/tarifas') # render tarifas delete.html 
