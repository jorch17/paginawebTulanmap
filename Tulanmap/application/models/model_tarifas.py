import web
import config

db = config.db


def get_all_tarifas():
    try:
        return db.select('tarifas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_tarifas(id_tarifa):
    try:
        return db.select('tarifas', where='id_tarifa=$id_tarifa', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_tarifas(id_tarifa):
    try:
        return db.delete('tarifas', where='id_tarifa=$id_tarifa', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_tarifas(descripcion_tarifa,tarifa,activo,id_ruta):
    try:
        return db.insert('tarifas',descripcion_tarifa=descripcion_tarifa,
tarifa=tarifa,
activo=activo,
id_ruta=id_ruta)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_tarifas(id_tarifa,descripcion_tarifa,tarifa,activo,id_ruta):
    try:
        return db.update('tarifas',id_tarifa=id_tarifa,
descripcion_tarifa=descripcion_tarifa,
tarifa=tarifa,
activo=activo,
id_ruta=id_ruta,
                  where='id_tarifa=$id_tarifa',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
