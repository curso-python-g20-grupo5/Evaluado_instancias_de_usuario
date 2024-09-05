# Instancias de usuario
Este proyecto consiste en un script de Python que procesa un archivo de texto (```usuarios.txt```), el cual contiene información de usuarios en formato JSON. El script crea instancias de la clase ```Usuario``` y maneja posibles errores durante el proceso, registrándolos en un archivo de log (```error.log```).

## Estrucura del proyecto

Este repositorio está compuesto por tres archivos: 
  - ```usuario.py```: Contiene la definición de la clase ```Usuario``` y la función para procesar las líneas del archivo de entrada.
  - ```usuarios.txt```: Archivo de texto con los datos de los usuarios en formato JSON. Cada línea corresponde a un usuario.
  - ```error.log```: Archivo de log donde se registran los errores que ocurren al procesar las líneas con datos incorrectos.
  
## Clase Usuario

La clase Usuario tiene los siguientes atributos:
- ```nombre```: Nombre del usuario.
- ```apellidos```: Apellido del usuario.
- ```email```: Dirección de correo electrónico.
- ```genero```: Género del usuario.

### Ejemplo de instanciación:
```
usuario = Usuario(nombre="John", apellido="Doe", email="jdoe@example.com", genero="Male")
```

## Funcionalidad del Script

1. **Lectura de Archivo:** El script lee el archivo usuarios.txt línea por línea, procesando cada línea como una cadena JSON.
2. **Creación de Instancias:** Para cada línea válida, se crea una instancia de la clase Usuario.
3. **Manejo de Errores:** Si hay un error al procesar una línea (debido a un formato JSON incorrecto, valores ausentes, etc.), se escribe un registro en el archivo error.log.

## Manejo de Errores
El script maneja las siguientes excepciones:

- ```json.JSONDecodeError```: Si la línea no puede ser convertida correctamente a JSON.
- ```TypeError```: Si los datos no tienen el formato esperado.
- ```KeyError```: Si falta alguna de las claves necesarias para instanciar un usuario.

### Ejemplo de Entrada Incorrecta
```
{"nombre": "Nissy", "apellido": "Dell Casa", "email": "ndellcasa2@godaddy.com", "genero": "Female"  # Faltante el cierre de la llave
```

### Ejemplo de Log de Error
```
Error al procesar la línea: {"nombre": "Nissy", "apellido": "Dell Casa", "email": "ndellcasa2@godaddy.com", "genero": "Female" - Expecting ',' delimiter: line 1 column 99 (char 98)
```
## Cómo Ejecutar el Proyecto

1. Asegúrate de tener Python instalado en tu máquina.
2. Clona este repositorio.
3. Ejecuta el script ```usuario.py``` con el siguiente comando:
```
python usuario.py
```
4. El script leerá el archivo ```usuarios.txt```, creará las instancias de usuario y generará el archivo ```error.log``` si hay errores.

## Requisitos

- Python 3.x

## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)

⌨️ con ❤️ por el Grupo 5 - G20 😊
