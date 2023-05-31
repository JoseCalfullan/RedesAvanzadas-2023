import urllib.parse
import requests

# Función para obtener la ruta entre dos ciudades
def obtener_ruta(origen, destino, apikey):
    # URL base de la API de MapQuest
    API = "https://www.mapquestapi.com/directions/v2/route?"
    
    # Construir la URL completa con los parámetros de origen, destino y clave de API
    url = API + urllib.parse.urlencode({"key": apikey, "from": origen, "to": destino})
    
    # Realizar la solicitud GET a la API y obtener la respuesta en formato JSON
    response = requests.get(url)
    datajson = response.json()
    
    # Obtener el estado de la respuesta JSON
    statusjson = datajson["info"]["statuscode"]
    
    # Verificar si la respuesta fue exitosa (estado 0)
    if statusjson == 0:
        # Imprimir la información de la ruta
        print("****** SU VIAJE **********")
        print("Inicio del viaje desde", origen, "hasta", destino)
        print("Tiempo estimado del viaje:", datajson["route"]["formattedTime"])
        print("Kilómetros:", "{:.1f}".format(datajson["route"]["distance"] * 1.61))#Se pasa de millas a kilometros
        print("****** INDICACIONES **********")
        print("Indicaciones:")
        for maneuver in datajson["route"]["legs"][0]["maneuvers"]:
            print(maneuver["narrative"], "({:.1f}km)".format(maneuver["distance"] * 1.61))
        print("*******\n")
    else:
        # Imprimir mensaje de error en caso de respuesta no exitosa
        print("Error al obtener la ruta. Código de estado:", statusjson, "\n")

# Función principal
def main():
    # Clave de API de MapQuest
    apikey = "64qBsHtbjm0AjJTNxUKesxojyuPfYQ1p"

    while True:
        # Solicitar al usuario las ciudades de origen y destino
        origen = input("Ciudad de origen: ")
        if origen.lower() == "salida" or origen.lower() == "s":
            break
        destino = input("Ciudad de destino: ")
        if destino.lower() == "salida" or destino.lower() == "s":
            break

        # Obtener la ruta entre las ciudades especificadas
        obtener_ruta(origen, destino, apikey)

# Llamada a la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
