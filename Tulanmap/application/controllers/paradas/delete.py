import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_parada, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_parada) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_parada, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_parada) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_parada, **k):

    @staticmethod
    def POST_DELETE(id_parada, **k):
    '''

    def GET(self, id_parada, **k):
        message = None # Error message
        id_parada = config.check_secure_val(str(id_parada)) # HMAC id_parada validate
        result = config.model.get_paradas(int(id_parada)) # search  id_parada
        result.id_parada = config.make_secure_val(str(result.id_parada)) # apply HMAC for id_parada
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_parada, **k):
        form = config.web.input() # get form data
        form['id_parada'] = config.check_secure_val(str(form['id_parada'])) # HMAC id_parada validate
        result = config.model.delete_paradas(form['id_parada']) # get paradas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_parada = config.check_secure_val(str(id_parada))  # HMAC user validate
            id_parada = config.check_secure_val(str(id_parada))  # HMAC user validate
            result = config.model.get_paradas(int(id_parada)) # get id_parada data
            result.id_parada = config.make_secure_val(str(result.id_parada)) # apply HMAC to id_parada
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/paradas') # render paradas delete.html 
