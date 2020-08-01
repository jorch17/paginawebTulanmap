import web
import config

db = config.db


def get_all_rutingo():
    try:
        return db.select('rutingo')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_rutingo(id):
    try:
        return db.select('rutingo', where='id=$id', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_rutingo(id):
    try:
        return db.delete('rutingo', where='id=$id', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_rutingo(nombre,costo,hora_inicio,hora_final,tiempo_recorrido):
    try:
        return db.insert('rutingo',nombre=nombre,
costo=costo,
hora_inicio=hora_inicio,
hora_final=hora_final,
tiempo_recorrido=tiempo_recorrido)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_rutingo(id,nombre,costo,hora_inicio,hora_final,tiempo_recorrido):
    try:
        return db.update('rutingo',id=id,
nombre=nombre,
costo=costo,
hora_inicio=hora_inicio,
hora_final=hora_final,
tiempo_recorrido=tiempo_recorrido,
                  where='id=$id',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
