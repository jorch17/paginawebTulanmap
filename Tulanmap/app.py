# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/rutas', 'application.controllers.rutas.index.Index',
    '/rutas/view/(.+)', 'application.controllers.rutas.view.View',
    '/rutas/edit/(.+)', 'application.controllers.rutas.edit.Edit',
    '/rutas/delete/(.+)', 'application.controllers.rutas.delete.Delete',
    '/rutas/insert', 'application.controllers.rutas.insert.Insert',
    '/paradas', 'application.controllers.paradas.index.Index',
    '/paradas/view/(.+)', 'application.controllers.paradas.view.View',
    '/paradas/edit/(.+)', 'application.controllers.paradas.edit.Edit',
    '/paradas/delete/(.+)', 'application.controllers.paradas.delete.Delete',
    '/paradas/insert', 'application.controllers.paradas.insert.Insert',
        '/tarifas', 'application.controllers.tarifas.index.Index',
    '/tarifas/view/(.+)', 'application.controllers.tarifas.view.View',
    '/tarifas/edit/(.+)', 'application.controllers.tarifas.edit.Edit',
    '/tarifas/delete/(.+)', 'application.controllers.tarifas.delete.Delete',
    '/tarifas/insert', 'application.controllers.tarifas.insert.Insert',
    '/api_rutas/?', 'application.api.rutas.api_rutas.Api_rutas',
    '/api_tarifas/?', 'application.api.tarifas.api_tarifas.Api_tarifas',
    '/api_paradas/?', 'application.api.paradas.api_paradas.Api_paradas',
    '/api_rutingo/?', 'application.api.rutingo.api_rutingo.Api_rutingo',
   '/rutingo', 'application.controllers.rutingo.index.Index',
'/rutingo/view/(.+)', 'application.controllers.rutingo.view.View',
'/rutingo/edit/(.+)', 'application.controllers.rutingo.edit.Edit',
'/rutingo/delete/(.+)', 'application.controllers.rutingo.delete.Delete',
'/rutingo/insert', 'application.controllers.rutingo.insert.Insert',
    


)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
