import json

class Usuario:
    """
    Clase que representa a un usuario.

    Atributos:
    ----------
    nombre : str
        Nombre del usuario.
    apellidos : str
        Apellido del usuario.
    email : str
        Dirección de correo electrónico del usuario.
    genero : str
        Género del usuario.
    """

    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        """
        Inicializa un objeto de la clase Usuario.

        Parámetros:
        -----------
        nombre : str
            Nombre del usuario.
        apellido : str
            Apellido del usuario.
        email : str
            Dirección de correo electrónico del usuario.
        genero : str
            Género del usuario.
        """
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

    def __repr__(self):
        """
        Representación en cadena de texto de un objeto Usuario.
        
        Retorna:
        --------
        str
            Representación del objeto Usuario en formato legible.
        """
        return (f"Usuario(nombre={self.nombre}, apellidos={self.apellidos}, "
                f"email={self.email}, genero={self.genero})")


def crear_instancias_usuarios(archivo_entrada, archivo_log):
    """
    Crea una lista de instancias de Usuario a partir de un archivo JSON.

    Lee un archivo de entrada donde cada línea contiene información de un usuario
    en formato JSON, crea instancias de la clase Usuario y las almacena en una lista.

    Parámetros:
    -----------
    archivo_entrada : str
        Ruta al archivo de texto que contiene datos de usuarios en formato JSON.
    archivo_log : str
        Ruta al archivo de log donde se registran los errores encontrados durante el proceso.

    Retorna:
    --------
    list
        Lista de instancias de la clase Usuario creadas a partir del archivo de entrada.
    """
    usuarios = []  # Lista para almacenar los objetos Usuario
    
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            # Procesar cada línea del archivo
            for linea in f:
                try:
                    # Convertir la línea de JSON a un diccionario
                    datos_usuario = json.loads(linea.strip())
                    # Crear una instancia de Usuario usando el diccionario
                    usuario = Usuario(**datos_usuario)
                    usuarios.append(usuario)
                except (json.JSONDecodeError, TypeError, KeyError) as e:
                    # Registrar el error en el archivo de log
                    with open(archivo_log, 'a', encoding='utf-8') as log:
                        log.write(f"Error al procesar la línea: {linea.strip()} - {str(e)}\n")
    except FileNotFoundError:
        print(f"El archivo {archivo_entrada} no fue encontrado.")
    
    return usuarios


if __name__ == "__main__":
    # Archivos de entrada y log
    archivo_entrada = "usuarios.txt"
    archivo_log = "error.log"
    
    # Crear la lista de usuarios desde el archivo de entrada
    lista_usuarios = crear_instancias_usuarios(archivo_entrada, archivo_log)
    
    # Mostrar los usuarios creados
    for usuario in lista_usuarios:
        print(usuario)
