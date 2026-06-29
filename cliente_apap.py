import requests

URL_API = "http://127.0.0.1:5000/nomina"

def leer_nomina(archivo):
    empleados = []
    with open(archivo, "r") as f:
        lineas = f.readlines()
  
        for linea in lineas[1:]:
            datos = linea.strip().split("|")
            empleado = {
                "id": datos[0],
                "nombre": datos[1],
                "cuenta": datos[2],
                "salario": datos[3]
            }
            empleados.append(empleado)
    return empleados

def enviar_nomina(empleados):
    print("Enviando datos de nómina a APAP...")
    for empleado in empleados:
        respuesta = requests.post(URL_API, json=empleado)
        if respuesta.status_code == 201:
            print(f"Enviado correctamente: {empleado['nombre']}")
        else:
            print(f"Error al enviar: {empleado['nombre']} — {respuesta.status_code}")

if __name__ == "__main__":
    empleados = leer_nomina("nomina_unapec.txt")
    enviar_nomina(empleados)
    print("Proceso finalizado.")