
import os
import shutil

#Funcion para organizar los archivos por extension en subcarpetas
def organizar_archivos_por_extension(directorio):

    archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    for archivo in archivos:
# Obtiene la extensión del archivo
        extension = os.path.splitext(archivo)[1][1:]  # omite el punto
        if not extension:  # Si el archivo no tiene extensión, lo omite
            continue
# Define la ruta de la subcarpeta
        subcarpeta = os.path.join(directorio, extension)
# Crea la subcarpeta si no existe
        if not os.path.exists(subcarpeta):
            os.makedirs(subcarpeta)
# Mueve el archivo a la subcarpeta correspondiente
        shutil.move(os.path.join(directorio, archivo), os.path.join(subcarpeta, archivo))
        
        
#Identifica el directorio actual
directorio_old = os.getcwd() 
print(f"Directorio actual: {directorio_old}")

#Cambia de directorio
directorio = input("Introduce una ruta para organizar los archivos: ")
os.chdir(directorio) 
print(f"Directorio nuevo: {directorio}")
organizar_archivos_por_extension(directorio)

#Imprime los archivos existentes en el directorio
archivos = os.listdir(".") 
print(f"Archivos en la carpeta {archivos}")


#/Users/danizanon/Desktop/TestArchivos
#/Users/danizanon/Desktop
#/Users/danizanon/Documents