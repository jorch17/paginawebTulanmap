import web

db_host = 'u3r5w4ayhxzdrw87.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'bix2j6yp4ioah07i'
db_user = 'glf2q4q93bhipqmm'
db_pw = 'y8i4y8lqboy4y4u3'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )