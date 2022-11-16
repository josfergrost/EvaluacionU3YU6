import json
from mongodb import PyMongo
from conf import variables

def datos_estudiante():
    no_control_buscado = input("Numero de control a buscar")
    obj = PyMongo(variables)
    obj.conectar_mongodb()
    estudiante = {
        'control': no_control_buscado
    }
    dat_estudiante = {}
    #obj.consultageneral_mongodb(tabla='estudiantes')
    arreglo=obj.consulta_mongodb(tabla='estudiantes',filtro=estudiante)
    obj.desconectar_mongodb()
    obj.conectar_mongodb()
    cal=obj.consulta_mongodb(tabla='kardex',filtro=estudiante)
    calificaciones = []
    if(arreglo['status']==True & cal['status']==True):
      for x in cal['resultado']:
         lista ={'materia': x['materia'],'calificacion': x['calificacion']}
         calificaciones.append(lista)
          
      dat_estudiante = {
        'nombre' : arreglo['resultado'][1]['nombre'],
        'control' : no_control_buscado,
        'calificaciones' : calificaciones
        
      }
    with open('evaluacion.json', 'w') as file:
        json.dump(dat_estudiante, file, indent=4)
datos_estudiante()

