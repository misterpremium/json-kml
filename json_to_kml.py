import json
import xml.etree.ElementTree as ET

# Función para convertir coordenadas de latLng (Formato: "lat°, lon°" a "lat, lon")
def convert_coordinates(coord_str):
    coord_str = coord_str.replace("°", "")  # Eliminar el símbolo de grados
    coords = coord_str.split(", ")
    return f"{coords[1]},{coords[0]},0.0"  # KML usa longitud, latitud, altitud

# Función para crear el KML a partir del JSON
def json_to_kml(data):
    # Crear la estructura básica del KML
    kml = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, "Document")

    for entry in data:
        try:
            # Verificamos que entry sea un diccionario
            if isinstance(entry, dict):
                start_time = entry["startTime"]
                end_time = entry["endTime"]

                if "visit" in entry:
                    # Crear un Placemark para la visita
                    placemark = ET.SubElement(document, "Placemark")
                    name = ET.SubElement(placemark, "name")
                    name.text = f"Visit from {start_time} to {end_time}"

                    # Obtenemos la ubicación de la visita
                    place_location = entry["visit"]["topCandidate"]["placeLocation"]["latLng"]
                    coordinates = convert_coordinates(place_location)

                    point = ET.SubElement(placemark, "Point")
                    coords = ET.SubElement(point, "coordinates")
                    coords.text = coordinates
                elif "timelinePath" in entry:
                    # Crear un Placemark para cada punto en el timelinePath
                    placemark = ET.SubElement(document, "Placemark")
                    name = ET.SubElement(placemark, "name")
                    name.text = f"Path from {start_time} to {end_time}"

                    line_string = ET.SubElement(placemark, "LineString")
                    coordinates = ""

                    for point in entry["timelinePath"]:
                        point_coords = point["point"]
                        coordinates += convert_coordinates(point_coords) + " "

                    coords = ET.SubElement(line_string, "coordinates")
                    coords.text = coordinates.strip()

            else:
                print(f"Se esperaban diccionarios, pero se encontró: {type(entry)} con valor {entry}")

        except KeyError as e:
            print(f"Error de clave en los datos de entrada: {e} para la entrada {entry}")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e} para la entrada {entry}")

    # Crear un árbol XML y escribirlo en un archivo KML
    tree = ET.ElementTree(kml)
    with open("output.kml", "wb") as f:
        tree.write(f)

# Leer el JSON desde un archivo
def read_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Ruta del archivo JSON de entrada
json_file_path = 'input.json'  # Asegúrate de que este archivo exista

# Leer el archivo JSON
data = read_json_file(json_file_path)

# Convertir el JSON a KML
json_to_kml(data)
