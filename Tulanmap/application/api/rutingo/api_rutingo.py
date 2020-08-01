import web
import config
import json


class Api_rutingo:
    def get(self, id):
        try:
            # http://localhost:8080/api_rutingo?user_hash=12345&action=get
            if id is None:
                result = config.model.get_all_rutingo()
                rutingo_json = []
                for row in result:
                    tmp = dict(row)
                    rutingo_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(rutingo_json)
            else:
                # http://0.0.0.0:8080/api_rutingo?user_hash=12345&action=get&id=1
                result = config.model.get_rutingo(int(id))
                rutingo_json = []
                rutingo_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(rutingo_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            rutingo_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutingo_json)

# http://0.0.0.0:8080/api_rutingo?user_hash=12345&action=put&id=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,costo,hora_inicio,hora_final,tiempo_recorrido):
        try:
            config.model.insert_rutingo(nombre,costo,hora_inicio,hora_final,tiempo_recorrido)
            rutingo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutingo_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_rutingo?user_hash=12345&action=delete&id=1
    def delete(self, id):
        try:
            config.model.delete_rutingo(id)
            rutingo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutingo_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_rutingo?user_hash=12345&action=update&id=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id, nombre,costo,hora_inicio,hora_final,tiempo_recorrido):
        try:
            config.model.edit_rutingo(id,nombre,costo,hora_inicio,hora_final,tiempo_recorrido)
            rutingo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutingo_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            rutingo_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(rutingo_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id=None,
            nombre=None,
            costo=None,
            hora_inicio=None,
            hora_final=None,
            tiempo_recorrido=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id=user_data.id

            nombre=user_data.nombre

            costo=user_data.costo

            hora_inicio=user_data.hora_inicio

            hora_final=user_data.hora_final

            tiempo_recorrido=user_data.tiempo_recorrido

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id)
                elif action == 'put':
                    return self.put(nombre,costo,hora_inicio,hora_final,tiempo_recorrido)
                elif action == 'delete':
                    return self.delete(id)
                elif action == 'update':
                    return self.update(id, nombre,costo,hora_inicio,hora_final,tiempo_recorrido)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
