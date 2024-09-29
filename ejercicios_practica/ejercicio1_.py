# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado

    mi_informacion = {
                  "nombre": "Mayra",
                  "apellido": "Cruz",
                  "DNI": "37513845",
                  "elementos_vestir": [
                      {
                       "prenda": "sweater", 
                       "cantidad": 2
                      },
                      {
                       "prenda": "zapatos",
                       "cantidad": 3
                      },
                      {
                        "prenda": "camisetas",
                        "cantidad": 5
                      },
                      {
                        "prenda": "zapatillas",
                        "cantidad": 3
                      }
                      ]
                   }

    with open('mi_informacion.json', 'w') as mi_archivo:
        data = [mi_informacion]
        json.dump(data, mi_archivo, indent=4)
      
    print(mi_informacion)

def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

    mi_informacion = {
                  "nombre": "Mayra",
                  "apellido": "Cruz",
                  "DNI": "37513845",
                  "elementos_vestir": [
                      {
                       "prenda": "campera", 
                       "cantidad": 2
                      },
                      {
                       "prenda": "buzo",
                       "cantidad": 5
                      },
                      {
                        "prenda": "remera",
                        "cantidad": 10
                      },
                      ]
                   }

    with open('mi_informacion.json', 'r') as mi_archivo:
        current_data = json.load(mi_archivo)
        current_data.append(mi_informacion)

    with open('mi_informacion.json', 'w') as mi_archivo:
        json.dump(current_data, mi_archivo, indent=4)

    with open('mi_informacion.json', 'r') as mi_archivo:
        json_data = json.load(mi_archivo)

    print('Mostrar el contenido del archivo mi_informacion')
    print(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    
    serializar()
    deserializar()

    print("Ejercicio finalizado")
