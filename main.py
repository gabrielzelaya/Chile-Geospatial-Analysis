import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from geopandas.tools import sjoin

# Cargar datos de las áreas pobladas y las regiones
areas_pobladas = gpd.read_file("Areas_Pobladas.shp")
regiones = gpd.read_file("Regional.shp")

# Crear áreas buffer alrededor de las áreas pobladas
buffer_distance = 5000  # Radio de buffer en metros
areas_pobladas["geometry_buffer"] = areas_pobladas.buffer(buffer_distance)

# Realizar intersección espacial entre áreas buffer y regiones
intersections = gpd.overlay(areas_pobladas, regiones, how="intersection")

# Visualización con interacción y colores destacados
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(regiones.total_bounds[0], regiones.total_bounds[2])
ax.set_ylim(regiones.total_bounds[1], regiones.total_bounds[3])

# Plotear las regiones no afectadas en color claro
regiones.plot(ax=ax, color='lightgrey')

# Plotear las áreas buffer y las regiones afectadas en colores distintos
intersections.plot(ax=ax, color='blue', alpha=0.7, edgecolor='black', linewidth=0.5)
areas_pobladas.plot(ax=ax, color='red', alpha=0.5, edgecolor='black', linewidth=0.5)

# Agregar título y etiquetas de ejes
plt.title("Áreas Buffer y Regiones")
plt.xlabel("Longitud")
plt.ylabel("Latitud")

# Habilitar el zoom y el desplazamiento lateral
plt.axis('on')

plt.show()

"""
Documentación de funciones y conceptos utilizados:

geopandas: Una biblioteca para trabajar con datos geoespaciales en Python.

gpd.read_file(): Carga datos geoespaciales desde un archivo en el DataFrame de GeoPandas.
overlay(): Realiza una superposición espacial entre dos GeoDataFrames.
matplotlib: Una biblioteca para la visualización de datos en Python.

plt.subplots(): Crea una nueva figura y un conjunto de ejes.
ax.set_xlim() y ax.set_ylim(): Establecen los límites de los ejes.
ax.set_title(), ax.set_xlabel(), ax.set_ylabel(): Agregan título y etiquetas de ejes al gráfico.
plt.axis(): Habilita o deshabilita las funciones de zoom y desplazamiento lateral.
plt.show(): Muestra la figura y activa la interacción.
shapely: Una biblioteca para manipular geometrías geoespaciales.

Point(): Crea un objeto Point para representar una ubicación.
gpd.tools.sjoin(): Realiza una operación de unión espacial entre dos GeoDataFrames, similar a la operación JOIN en bases de datos.

Al ejecutar este código, obtendrás un mapa interactivo que te permite hacer zoom, 
desplazar el mapa y explorar las áreas buffer y las regiones resaltadas en colores distintos.
 Puedes ajustar los valores de buffer_distance, colores, alphas y otros parámetros según tus preferencias y necesidades.
"""
