# pip install MySQL-python
"""print("Resultados de MySQLdb:")
import MySQLdb
miConexion = MySQLdb.connect( host='localhost', user= 'USUARIO', passwd='PASS', db='neoguias' )
cur = miConexion.cursor()
cur.execute( "SELECT nombre, apellido FROM usuarios" )
for nombre, apellido in cur.fetchall() :
    print(nombre, apellido)
miConexion.close()"""