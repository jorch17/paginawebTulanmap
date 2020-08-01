import web
import config

db = config.db


def get_all_rutas():
    try:
        return db.select('rutas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_rutas(id_ruta):
    try:
        return db.select('rutas', where='id_ruta=$id_ruta', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_rutas(id_ruta):
    try:
        return db.delete('rutas', where='id_ruta=$id_ruta', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_rutas(nombre_ruta,hora_inicio,hora_fin,intervalo,latitud_inicio,longitud_inicio,latitud_final,longitud_final,tiempo_recorrido,distancia_km,activo):
    try:
        return db.insert('rutas',nombre_ruta=nombre_ruta,
hora_inicio=hora_inicio,
hora_fin=hora_fin,
intervalo=intervalo,
latitud_inicio=latitud_inicio,
longitud_inicio=longitud_inicio,
latitud_final=latitud_final,
longitud_final=longitud_final,
tiempo_recorrido=tiempo_recorrido,
distancia_km=distancia_km,
activo=activo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_rutas(id_ruta,nombre_ruta,hora_inicio,hora_fin,intervalo,latitud_inicio,longitud_inicio,latitud_final,longitud_final,tiempo_recorrido,distancia_km,activo):
    try:
        return db.update('rutas',id_ruta=id_ruta,
nombre_ruta=nombre_ruta,
hora_inicio=hora_inicio,
hora_fin=hora_fin,
intervalo=intervalo,
latitud_inicio=latitud_inicio,
longitud_inicio=longitud_inicio,
latitud_final=latitud_final,
longitud_final=longitud_final,
tiempo_recorrido=tiempo_recorrido,
distancia_km=distancia_km,
activo=activo,
                  where='id_ruta=$id_ruta',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
