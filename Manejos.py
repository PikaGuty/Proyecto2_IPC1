from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from Persona import Persona
from Medicamento import Medicamento
from Cita import Cita
from Receta import Receta
from Stonks import Stonks
Personas = []
Medicamentos = []
Citas=[]
Recetas=[]
Stonkss=[]
app = Flask(__name__)
CORS(app)

#Personas.append(Persona(1,'Javier','Gutierrez',"2001-03-14","Masculino",'PikaGuty','1234','N',42543549,1))
#Personas.append(Persona(3,'Andrea','Lopez','2001-03-12',"Mujer",'Femenino','1234','N',42751345,2))
#Personas.append(Persona(2,'Alejandro','de León','2001-03-12',"Masculino",'Gohanale','1234','Neurólogo',42751345,3))
#Personas.append(Persona(2,'Gabriela','Herrera','28-12-1996','Femenino','Gaby','123456','Pediatra',51231,3))
#Personas.append(Persona(2,'Daniel','Gutierrez','02-07-1992',"Masculino",'Dane','123456','N',55555950,1))
#Personas.append(Persona(2,'Abel','Gutierrez','13-03-1994',"Masculino",'VegetaLink','123456','N',4254,1))
#Personas.append(Persona(2,'Samuel','Herrera','11-06-1994',"Masculino",'Samuel','123456','N',51231,1))
#Personas.append(Persona(2,'Jorge','León','18-12-1964',"Masculino",'Leon','123456','Neurólogo',15152,3))

#Medicamentos.append(Medicamento('Paracetamol',25.5,'No c sirve para todo no?',8))
#Medicamentos.append(Medicamento('Tabcin',80,'Para la gripe',15))

#Citas.append(Cita('PikaGuty','23-04-2021','15:15','tengo amsiedad aiudaaaaa',2,'Gohanale','Alejandro de León'))
#Citas.append(Cita('Dane','23-04-2021','15:15','tengo amsiedad aiudaaaaa',2,'Gaby','Gabriela Herrera'))
#Citas.append(Cita('VegetaLink','23-04-2021','15:15','tengo amsiedad aiudaaaaa',2,'Gaby','Gabriela Herrera'))
#Citas.append(Cita('Samuel','23-04-2021','15:15','tengo amsiedad aiudaaaaa',2,'Leon','Jorge León'))

#Recetas.append(Receta('Amsiedad'))
#Recetas.append(Receta('Amsiedad'))
#Recetas.append(Receta('SIDA'))
#Recetas.append(Receta('Amsiedad'))
#Recetas.append(Receta('SIDA'))
#Recetas.append(Receta('Amsiedad'))
#Recetas.append(Receta('Hepatitis_A'))

#Stonkss.append(Stonks('Paracetamol',5))
#Stonkss.append(Stonks('Tabcin',7))
#Stonkss.append(Stonks('Panadol',3))
#Stonkss.append(Stonks('Celebra',7))
#Stonkss.append(Stonks('Winasorb',3))


@app.route('/Personas',methods=['GET'])
def getPersonas():
    global Personas
    Datos = []
    for i in Personas:
        objeto={
            'Id':i.getId(),
            'Nombre':i.getNombre(),
            'Apellido':i.getApellido(),
            'Fecha':i.getFechan(),
            'Sexo':i.getSexo(),
            'Nombre_us':i.getNombre_us(),
            'Contrasena ':i.getContraseña(),
            'Especialidad':i.getEspecialidad(),
            'Telefono':i.getTelefono(),
            'Tipo':i.getTipo()
        }
        Datos.append(objeto)
    return (jsonify(Datos))

@app.route('/Medicamentos',methods=['GET'])
def getMedicamentos():
    global Medicamentos
    Datos = []
    for i in Medicamentos:
        objeto={
            'Nombre':i.getNombre(),
            'Precio':i.getPrecio(),
            'Descripcion':i.getDescripcion(),
            'Cantidad':i.getCantidad()
        }
        Datos.append(objeto)
    return (jsonify(Datos))

@app.route('/Citas',methods=['GET'])
def getCita():
    global Citas
    Datos = []
    for i in Citas:
        objeto={
            'UsuarioP':i.getUsuarioP(),
            'Fecha':i.getFecha(),
            'Hora':i.getHora(),
            'Motivo':i.getMotivo(),
            'Estado':i.getEstado(),
            'IDoc':i.getDoc(),
            'Doctor':i.getNom()
        }
        Datos.append(objeto)
    return (jsonify(Datos))

@app.route('/Citas/top',methods=['GET'])
def getTopD():
    global Citas
    Datos = []
    da=[]
    dev=[]
    for i in Citas:
        if i.getNom()!="No asignado":
            objeto={
                'IDoc':i.getDoc(),
            }
            da.append(i.getDoc())
            Datos.append(objeto)
    print(da)
    from statistics import mode
    dev.append(mode(da))
    da.remove(mode(da))
    dev.append(mode(da))
    da.remove(mode(da))
    da.remove(dev[0])
    dev.append(mode(da))
    return (jsonify(dev))

@app.route('/Recetas',methods=['GET'])
def getReceta():
    global Recetas
    Datos = []
    for i in Recetas:
        objeto={
            'Padecimiento':i.getPadecimiento()
        }
        Datos.append(objeto)
    return (jsonify(Datos))

@app.route('/Stonks',methods=['GET'])
def getStonks():
    global Stonkss
    Datos = []
    arm=[]
    arc=[]

    arml=[]
    arcl=[]

    for i in Stonkss:
        objeto={
            'Medicamento':i.getMedicamento(),
            'Cantidad':i.getCantidad()
        }
        arm.append(i.getMedicamento())
        arc.append(i.getCantidad())           
        Datos.append(objeto)
    from statistics import mode
    arcl.append(max(arc, key=int))
    arml.append(arm[arc.index(arcl[0])])
    arc.remove(arcl[0])
    arm.remove(arml[0])      
    arcl.append(max(arc, key=int))
    arml.append(arm[arc.index(arcl[1])])
    arc.remove(arcl[1])
    arm.remove(arml[1]) 
    arcl.append(max(arc, key=int))
    arml.append(arm[arc.index(arcl[2])])
    arc.remove(arcl[2])
    arm.remove(arml[2])  
    arcl.append(max(arc, key=int))
    arml.append(arm[arc.index(arcl[3])])
    arc.remove(arcl[3])
    arm.remove(arml[3])
    arcl.append(max(arc, key=int))
    arml.append(arm[arc.index(arcl[4])])
    arc.remove(arcl[4])
    arm.remove(arml[4])   


    print("cantidad 1",arcl[0])
    print("medicamento 1",arml[0])
    print("cantidad 2",arcl[1])
    print("medicamento 2",arml[1])
    print("cantidad 3",arcl[2])
    print("medicamento 3",arml[2])
    print("cantidad 4",arcl[3])
    print("medicamento 4",arml[3])
    print("cantidad 5",arcl[4])
    print("medicamento 5",arml[4])

    return (jsonify(arml))

@app.route('/Personas/<int:id>',methods=['GET'])
def OptenerPersonas(id):
    global Personas
    for i in Personas:
        if i.getId() == id:
            objeto={
                'Id':i.getId(),
                'Nombre':i.getNombre(),
                'Apellido':i.getApellido(),
                'Fechan':i.getFechan(),
                'Sexo':i.getSexo(),
                'Nombre_us':i.getNombre_us(),
                'Contrasena':i.getContraseña(),
                'Especialidad':i.getEspecialidad(),
                'Telefono':i.getTelefono(),
                'Tipo':i.getTipo()
            }
            return (jsonify(objeto))
    salida = {"Mensaje":"No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Medicamentos/<string:nombre>',methods=['GET'])
def OptenerMedicamentos(nombre):
    global Medicamentos
    for i in Medicamentos:
        if i.getNombre() == nombre:
            objeto={
                'Nombre':i.getNombre(),
                'Precio':i.getPrecio(),
                'Descripcion':i.getDescripcion(),
                'Cantidad':i.getCantidad()
            }
            return (jsonify(objeto))
    salida = {"Mensaje":"No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Citas/<string:nombre>',methods=['GET'])
def ObtenerCita(nombre):
    global Citas
    for i in Citas:
        if i.getUsuarioP()==nombre:
            objeto={
                'UsuarioP':i.getUsuarioP(),
                'Fecha':i.getFecha(),
                'Hora':i.getHora(),
                'Motivo':i.getMotivo(),
                'Estado':i.getEstado(),
                'IDoc':i.getDoc(),
                'Doctor':i.getNom()
            }
            return (jsonify(objeto))
    salida = {"Mensaje":"No tiene citas"}
    return (jsonify(Datos))

@app.route('/Citas/<string:nombre>/<int:tipo>',methods=['GET'])
def ObtenerCitaa(nombre,tipo):
    global Citas
    for i in Citas:
        if i.getUsuarioP()==nombre:
            if i.getEstado()==tipo:
                objeto={
                    'UsuarioP':i.getUsuarioP(),
                    'Fecha':i.getFecha(),
                    'Hora':i.getHora(),
                    'Motivo':i.getMotivo(),
                    'Estado':i.getEstado(),
                    'IDoc':i.getDoc(),
                    'Doctor':i.getNom()
                }
                return (jsonify(objeto))
    salida = {"Mensaje":"No tiene citas"}
    return (jsonify(Datos))

@app.route('/Personas',methods=['POST'])
def AgregarUsuario():
    global Personas
    id = request.json['Id']
    nombre = request.json['Nombre']
    apellido = request.json['Apellido']
    fechan = request.json['Fechan']
    sexo = request.json['Sexo']
    nombre_us = request.json['Nombre_us']
    contraseña = request.json['Contrasena']
    especialidad = request.json['Especialidad']
    telefono = request.json['Telefono']
    tipo = request.json['Tipo']  

    nuevo = Persona(id,nombre,apellido,fechan,sexo,nombre_us,contraseña,especialidad,telefono,tipo)
    Personas.append(nuevo)
    return jsonify({
        'Mensaje':'Se agregó el usuario'
    })

@app.route('/Medicamentos',methods=['POST'])
def AgregarMedicamento():
    global Medicamentos
    nombre = request.json['Nombre']
    precio = request.json['Precio']
    descripcion = request.json['Descripcion']
    cantidad = request.json['Cantidad']
    
    nuevo = Medicamento(nombre,precio,descripcion,cantidad)
    Medicamentos.append(nuevo)
    return jsonify({
        'Mensaje':'Se agregó el medicamento'
    })

@app.route('/Citas',methods=['POST'])
def AgregarCita():
    global Citas
    usuarioP = request.json['UsuarioP']
    fecha = request.json['Fecha']
    hora = request.json['Hora']
    motivo = request.json['Motivo']
    estado = request.json['Estado']
    doc = request.json['IDoc']
    doctor = request.json['Doctor']
    
    nuevo = Cita(usuarioP,fecha,hora,motivo,estado,doc,doctor)
    Citas.append(nuevo)
    return jsonify({
        'Mensaje':'Se agregó la cita'
    })

@app.route('/Recetas',methods=['POST'])
def AgregarReceta():
    global Recetas
    padecimiento = request.json['Padecimiento']
    nuevo = Receta(padecimiento)
    Recetas.append(nuevo)
    return jsonify({
        'Mensaje':'Se agregó la receta'
    })

@app.route('/Stonks',methods=['POST'])
def AgregarStonks():
    global Stonkss
    
    for i in range(len(Stonkss)):
        if request.json['Medicamento'] == Stonkss[i].getMedicamento():
            Stonkss[i].setCantidad(Stonkss[i].getCantidad()+request.json['Cantidad'])
            return jsonify({'Mensaje':'Se agregó'})
    
    Medicamento = request.json['Medicamento']
    Cantidad = request.json['Cantidad']

    nuevo = Stonks(Medicamento,Cantidad)
    Stonkss.append(nuevo)
    return jsonify({
        'Mensaje':'Se agregó la receta'
    })

@app.route('/Personas/<string:nombre_us>', methods=['PUT'])
def ActualizarPersona(nombre_us):
    global Personas
    for i in range(len(Personas)):
        if nombre_us == Personas[i].getNombre_us():
            Personas[i].setId(request.json['Id'])
            Personas[i].setNombre(request.json['Nombre'])
            Personas[i].setApellido(request.json['Apellido'])
            Personas[i].setFechan(request.json['Fechan'])
            Personas[i].setSexo(request.json['Sexo'])
            Personas[i].setNombre_us(request.json['Nombre_us'])
            Personas[i].setContraseña(request.json['Contrasena'])
            Personas[i].setEspecialidad(request.json['Especialidad'])
            Personas[i].setTelefono(request.json['Telefono'])
            Personas[i].setTipo(request.json['Tipo'])

            return jsonify({'Mensaje':'Se actualizo la persona exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/Personas/<string:uss>',methods=['GET'])
def OptenerPersonasU(uss):
    global Personas
    for i in Personas:
        if i.getNombre_us() == uss:
            objeto={
                'Id':i.getId(),
                'Nombre':i.getNombre(),
                'Apellido':i.getApellido(),
                'Fechan':i.getFechan(),
                'Sexo':i.getSexo(),
                'Nombre_us':i.getNombre_us(),
                'Contrasena':i.getContraseña(),
                'Especialidad':i.getEspecialidad(),
                'Telefono':i.getTelefono(),
                'Tipo':i.getTipo()
            }
            return (jsonify(objeto))
    salida = {"Mensaje":"No existe el user con ese nombre"}
    return(jsonify(salida))

@app.route('/Medicamentos/<string:nombre>', methods=['PUT'])
def ActualizarMedicamento(nombre):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if nombre == Medicamentos[i].getNombre():
            Medicamentos[i].setNombre(request.json['Nombre'])
            Medicamentos[i].setPrecio(request.json['Precio'])
            Medicamentos[i].setDescripcion(request.json['Descripcion'])
            Medicamentos[i].setCantidad(request.json['Cantidad'])
            
            return jsonify({'Mensaje':'Se actualizo el medicamento exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/Citas/<string:nombre>',methods=['PUT'])
def ActualizarCita(nombre):
    global Citas
    for i in range(len(Citas)):
        if nombre == Citas[i].getUsuarioP():
            
            Citas[i].setFecha(request.json['Fecha'])
            Citas[i].setHora(request.json['Hora'])
            Citas[i].setMotivo(request.json['Motivo'])
            Citas[i].setEstado(request.json['Estado'])
            Citas[i].setUsuarioP(request.json['UsuarioP'])
            Citas[i].setDoc(request.json['IDoc'])
            Citas[i].setNom(request.json['Doctor'])
            
            return jsonify({'Mensaje':'Se actualizó la cita'})
    return jsonify({'Mensaje':'Se agregó la cita'})

@app.route('/Citas/<string:nombre>/<int:tipo>',methods=['PUT'])
def ActualizarCitaa(nombre,tipo):
    global Citas
    for i in range(len(Citas)):
        if nombre == Citas[i].getUsuarioP():
            if tipo == Citas[i].getEstado():
                Citas[i].setFecha(request.json['Fecha'])
                Citas[i].setHora(request.json['Hora'])
                Citas[i].setMotivo(request.json['Motivo'])
                Citas[i].setEstado(request.json['Estado'])
                Citas[i].setUsuarioP(request.json['UsuarioP'])
                Citas[i].setDoc(request.json['IDoc'])
                Citas[i].setNom(request.json['Doctor'])
                
                return jsonify({'Mensaje':'Se actualizó la cita'})
    return jsonify({'Mensaje':'Se agregó la cita'})

@app.route('/Personas/<string:nombre_us>', methods=['DELETE'])
def EliminarPersona(nombre_us):
    global Personas
    for i in range(len(Personas)):
        if nombre_us == Personas[i].getNombre_us():
            del Personas[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/Medicamentos/<string:nombre_us>', methods=['DELETE'])
def EliminarMedicamento(nombre_us):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if nombre_us == Medicamentos[i].getNombre():
            del Medicamentos[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)