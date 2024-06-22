import os


def print_directory_structure(startpath, prefix='', ignore_list=None):
    if ignore_list is None:
        ignore_list = ['__pycache__', 'env']

    # Recorremos cada elemento del directorio
    for item in os.listdir(startpath):
        # Saltamos los elementos en la lista de ignorados
        if item in ignore_list:
            continue

        # Obtenemos la ruta completa del elemento
        itempath = os.path.join(startpath, item)
        if os.path.isdir(itempath):
            # Si es un directorio, imprimimos el nombre del directorio y lo recorremos recursivamente
            print(prefix + '|-- ' + item + '/')
            print_directory_structure(itempath, prefix + '    ', ignore_list)
        else:
            # Si es un archivo, simplemente lo imprimimos
            print(prefix + '|-- ' + item)


# Ejemplo de uso
project_path = '.'  # Aquí puedes poner la ruta de tu proyecto si no es el directorio actual
ignore_items = ['__pycache__', 'env']  # Lista de carpetas/archivos a ignorar
print_directory_structure(project_path, ignore_list=ignore_items)
