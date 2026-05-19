# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    resultado = []

    with open(filename, "r") as archivo:

        lineas = archivo.readlines()

        # Si el archivo está vacío
        if not lineas:
            return []

        # Leer header
        header = lineas[0].strip().split(",")

        # Recorrer las líneas de datos
        for linea in lineas[1:]:

            linea = linea.strip()

            # Ignorar líneas vacías
            if linea != "":
                valores = linea.split(",")

                persona = {}

                persona[header[0]] = valores[0].strip()
                persona[header[1]] = int(valores[1].strip())
                persona[header[2]] = valores[2].strip()

                resultado.append(persona)

    return resultado
