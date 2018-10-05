# Recuperacion-1
Recuperacion Parcial 

### Requisitos
* Tener instalado pip
* Tener instalado el framework
* Tener un .txt con oraciones separadas por comas ','

### Frameworks
* [Dask] (https://docs.dask.org/en/latest/)
## Instalación
Utilizando Pip se instala Dask
* [Dask](http://docs.dask.org/en/latest/install.html)
```
$ pip install "dask[complete]"    # Install everything
```
## Implementacion

El framework funciona con un Scheduler quien es el orquestador. El se comunica con los Workers de maquinas externas, quienes por medio de Dask ejecutan tareas que el Scheduler les proporciona. Tambien se tiene una ventana para el Client, el se encarga de interactuar con el Usuario, en esta linea de comando se escriben las funciones deseadas para implementar. 

# Pasos para la implementación:
* Levantar el Scheduler en una maquina (Maquina 1)
```
$ dask-Scheduler #este proporciona una IP y un puerto para comunicarse
```
* Levantar los worker en maquinas externas (Maquina 2 & 3, para este ejemplo)
```
$ dask-worker /IP Y PUERTO PROPORCIONADO POR EL SCHEDULER/
```
* Levantar el Cliente (Puede ser en una maquina externa o en la misma del Scheduler)
```
$ python-
>> from dask.distributed import Client
>> client = Client('/IP & PUERTOS DEL SCHEDULER/')
```
# Listo para usar
Ahora ya podemos utilizar funcinoes y crea variables y enviarlos al Scheduler con comandos como:
```
>> miVariable = client.submit(funcion, args)   #para mandar funciones al scheduler
>> result = client.gather(miVariable)          #para recuperar data ya procesada
```

# Explicación de codigo
*dentro del .py se explica

# Video de demostración
https://youtu.be/3hNEp4wzB3A
