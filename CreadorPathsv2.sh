#!/bin/bash

# Verifica fichero
if [[ ! -f output.kml ]]; then
  echo "❌ Error: output.kml no encontrado en $(pwd)"
  exit 1
fi

# Extrae coordenadas (con manejo de errores)
if ! ruta=$(grep -oP '(?<=<coordinates>)[^<]+(?=</coordinates>)' output.kml 2>/dev/null | tr '\n' ' ' | tr -d '\r'); then
  echo "❌ Error extrayendo coordenadas"
  exit 1
fi

if [[ -z "$ruta" ]]; then
  echo "❌ No se encontraron coordenadas en output.kml"
  exit 1
fi

echo "✅ Coordenadas extraídas: ${#ruta} caracteres"

# Genera KML
printf '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n  <Document>\n    <Placemark>\n      <name>Path combinado</name>\n      <LineString>\n        <coordinates>%s</coordinates>\n      </LineString>\n    </Placemark>\n  </Document>\n</kml>\n' "$ruta" > rutas.kml

echo "✅ KML creado: rutas.kml"
