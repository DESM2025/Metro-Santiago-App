Aplicacion web que encuentra la ruta optima entre dos estaciones del Metro de Santiago utilizando el algoritmo de Dijkstra.

## Caracteristicas

* Calcula la ruta mas rapida entre estaciones de origen y destino del usuario
* Opcion para minimizar transbordos
* Tiempo estimado de viaje
* Incluye todas las lineas y estaciones del Metro de Santiago 

## Como Funciona

El sistema modela la red del Metro de Santiago como un grafo ponderado donde cada estacion es un nodo y las conexiones entre estaciones son aristas con peso igual al tiempo de viaje en minutos mientras que los transbordos se representan como conexiones entre nodos de distintas lineas con una penalizacion en forma de peso

## Requisitos

* Python 3.10
* Conda o Miniconda

## Crear entorno

* conda env create -f environment.yml

### Aplicacion Web Streamlit

streamlit run app.py

La aplicacion se abrira en el navegador `http://localhost:8501`

## Estructura del Proyecto

```
.
├── app.py              # Aplicacion web Streamlit
├── environment.yml     # Configuracion del environment
├── mapa_metro.jpg      # Mapa del metro
└── src/
    ├── __init__.py
    ├── main.py         # Interfaz de linea de comandos
    ├── metro_map.py    # Grafo del metro con estaciones y conexiones
    └── metro_solver.py # Implementacion del algoritmo de Dijkstra
```

## Autor

Proyecto grafos y lenguajes formales Utem segundo semestre 2024