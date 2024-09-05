import json

class Usuario:
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

    def __repr__(self):
        return (f"Usuario(nombre={self.nombre}, apellidos={self.apellidos}, "
                f"email={self.email}, genero={self.genero})")

def crear_instancias_usuarios(archivo_entrada, archivo_log):
    usuarios = []
    
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            for linea in f:
                try:
                    datos_usuario = json.loads(linea.strip())
                    usuario = Usuario(**datos_usuario)
                    usuarios.append(usuario)
                except (json.JSONDecodeError, TypeError, KeyError) as e:
                    with open(archivo_log, 'a', encoding='utf-8') as log:
                        log.write(f"Error al procesar la línea: {linea.strip()} - {str(e)}\n")
    except FileNotFoundError:
        print(f"El archivo {archivo_entrada} no fue encontrado.")
    
    return usuarios

if __name__ == "__main__":
    archivo_entrada = "usuarios.txt"
    archivo_log = "error.log"
    lista_usuarios = crear_instancias_usuarios(archivo_entrada, archivo_log)
    
    # Mostrar los usuarios creados
    for usuario in lista_usuarios:
        print(usuario)
