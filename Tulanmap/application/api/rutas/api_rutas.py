import web
import config
import json


class Api_rutas:
    def get(self, id_ruta):
        try:
            # http://localhost:8080/api_rutas?user_hash=12345&action=get
            if id_ruta is None:
                result = config.model.get_all_rutas()
                rutas_json = []
                for row in result:
                    tmp = dict(row)
                    rutas_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(rutas_json)
            else:
                # http://0.0.0.0:8080/api_rutas?user_hash=12345&action=get&id_ruta=1
                result = config.model.get_rutas(int(id_ruta))
                rutas_json = []
                rutas_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(rutas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            rutas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutas_json)

# http://0.0.0.0:8080/api_rutas?user_hash=12345&action=put&id_ruta=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_ruta,hora_inicio,hora_fin,intervalo,latitud_inicio,longitud_inicio,latitud_final,longitud_final,tiempo_recorrido,distancia_km,activo):
        try:
            config.model.insert_rutas(nombre_ruta,hora_inicio,hora_fin,intervalo,latitud_inicio,longitud_inicio,latitud_final,longitud_final,tiempo_recorrido,distancia_km,activo)
            rutas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutas_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_rutas?user_hash=12345&action=delete&id_ruta=1
    def delete(self, id_ruta):
        try:
            config.model.delete_rutas(id_ruta)
            rutas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutas_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_rutas?user_hash=12345&action=update&id_ruta=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_ruta, nombre_ruta,hora_inicio,hora_fin,intervalo,latitud_inicio,longitud_inicio,latitud_final,longitud_final,tiempo_recorrido,distancia_km,activo):
        try:
            config.model.edit_rutas(id_ruta,nombre_ruta,hora_inicio,hora_fin,intervalo,latitud_inicio,longitud_inicio,latitud_final,longitud_final,tiempo_recorrido,distancia_km,activo)
            rutas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            rutas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutas_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_ruta=None,
            nombre_ruta=None,
            hora_inicio=None,
            hora_fin=None,
            intervalo=None,
            latitud_inicio=None,
            longitud_inicio=None,
            latitud_final=None,
            longitud_final=None,
            tiempo_recorrido=None,
            distancia_km=None,
            activo=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_ruta=user_data.id_ruta

            nombre_ruta=user_data.nombre_ruta

            hora_inicio=user_data.hora_inicio

            hora_fin=user_data.hora_fin

            intervalo=user_data.intervalo

            latitud_inicio=user_data.latitud_inicio

            longitud_inicio=user_data.longitud_inicio

            latitud_final=user_data.latitud_final

            longitud_final=user_data.longitud_final

            tiempo_recorrido=user_data.tiempo_recorrido

            distancia_km=user_data.distancia_km

            activo=user_data.activo

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_ruta)
                elif action == 'put':
                    return self.put(nombre_ruta,hora_inicio,hora_fin,intervalo,latitud_inicio,longitud_inicio,latitud_final,longitud_final,tiempo_recorrido,distancia_km,activo)
                elif action == 'delete':
                    return self.delete(id_ruta)
                elif action == 'update':
                    return self.update(id_ruta, nombre_ruta,hora_inicio,hora_fin,intervalo,latitud_inicio,longitud_inicio,latitud_final,longitud_final,tiempo_recorrido,distancia_km,activo)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
