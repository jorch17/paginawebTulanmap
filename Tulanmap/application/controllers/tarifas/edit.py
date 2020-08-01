import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_tarifa, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_tarifa) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tarifa, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_tarifa) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_tarifa, **k):

    @staticmethod
    def POST_EDIT(id_tarifa, **k):
        
    '''

    def GET(self, id_tarifa, **k):
        message = None # Error message
        id_tarifa = config.check_secure_val(str(id_tarifa)) # HMAC id_tarifa validate
        result = config.model.get_tarifas(int(id_tarifa)) # search for the id_tarifa
        result.id_tarifa = config.make_secure_val(str(result.id_tarifa)) # apply HMAC for id_tarifa
        return config.render.edit(result, message) # render tarifas edit.html

    def POST(self, id_tarifa, **k):
        form = config.web.input()  # get form data
        form['id_tarifa'] = config.check_secure_val(str(form['id_tarifa'])) # HMAC id_tarifa validate
        # edit user with new data
        result = config.model.edit_tarifas(
            form['id_tarifa'],form['descripcion_tarifa'],form['tarifa'],form['activo'],form['id_ruta'],
        )
        if result == None: # Error on udpate data
            id_tarifa = config.check_secure_val(str(id_tarifa)) # validate HMAC id_tarifa
            result = config.model.get_tarifas(int(id_tarifa)) # search for id_tarifa data
            result.id_tarifa = config.make_secure_val(str(result.id_tarifa)) # apply HMAC to id_tarifa
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/tarifas') # render tarifas index.html
