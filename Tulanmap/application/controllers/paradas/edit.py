import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_parada, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_parada) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_parada, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_parada) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_parada, **k):

    @staticmethod
    def POST_EDIT(id_parada, **k):
        
    '''

    def GET(self, id_parada, **k):
        message = None # Error message
        id_parada = config.check_secure_val(str(id_parada)) # HMAC id_parada validate
        result = config.model.get_paradas(int(id_parada)) # search for the id_parada
        result.id_parada = config.make_secure_val(str(result.id_parada)) # apply HMAC for id_parada
        return config.render.edit(result, message) # render paradas edit.html

    def POST(self, id_parada, **k):
        form = config.web.input()  # get form data
        form['id_parada'] = config.check_secure_val(str(form['id_parada'])) # HMAC id_parada validate
        # edit user with new data
        result = config.model.edit_paradas(
            form['id_parada'],form['nombre_parada'],form['latitud_parada'],form['longitud_parada'],form['identificador_p'],form['activo'],form['id_ruta'],
        )
        if result == None: # Error on udpate data
            id_parada = config.check_secure_val(str(id_parada)) # validate HMAC id_parada
            result = config.model.get_paradas(int(id_parada)) # search for id_parada data
            result.id_parada = config.make_secure_val(str(result.id_parada)) # apply HMAC to id_parada
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/paradas') # render paradas index.html
