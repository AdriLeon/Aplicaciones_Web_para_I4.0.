import web
from datetime import datetime

class Visitas:
  def GET(self, nombre):
    try:
      fecha_hora = datetime.now()
      cookie = web.cookies()
      visitas = 0
      print(cookie)
      if nombre:
        web.setcookie("nombre", nombre, expires="", domain=None)
      else:
        nombre = "Anonimo"
        web.setcookie("nombre", nombre, expires="", domain=None)

      if cookie.get("visitas"):
        visitas = int(cookie.get("visitas"))
        visitas += 1
        web.setcookie("visitas", str(visitas), expires="", domain=None)
      else:
        web.setcookie("visitas", str(1), expires="", domain=None)

      return "Numero de visitas: " + str(visitas) + " Nombre: " + nombre + " Fecha y Hora de la visita: " + str(fecha_hora) 
    except Exception as e:
      return "Error " + str(e.args)