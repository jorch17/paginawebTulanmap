import web
import config

db = config.db


def get_all_paradas():
    try:
        return db.select('paradas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_paradas(id_parada):
    try:
        return db.select('paradas', where='id_parada=$id_parada', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_paradas(id_parada):
    try:
        return db.delete('paradas', where='id_parada=$id_parada', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_paradas(nombre_parada,latitud_parada,longitud_parada,identificador_p,activo,id_ruta):
    try:
        return db.insert('paradas',nombre_parada=nombre_parada,
latitud_parada=latitud_parada,
longitud_parada=longitud_parada,
identificador_p=identificador_p,
activo=activo,
id_ruta=id_ruta)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_paradas(id_parada,nombre_parada,latitud_parada,longitud_parada,identificador_p,activo,id_ruta):
    try:
        return db.update('paradas',id_parada=id_parada,
nombre_parada=nombre_parada,
latitud_parada=latitud_parada,
longitud_parada=longitud_parada,
identificador_p=identificador_p,
activo=activo,
id_ruta=id_ruta,
                  where='id_parada=$id_parada',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
