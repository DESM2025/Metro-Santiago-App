import heapq
from datetime import datetime, timedelta
from metro_map import metro_map  #importar el mapa desde metro_map.py

#algoritmo de Dijkstra para encontrar la ruta mas corta en un grafo
def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {station: float('inf') for station in graph}
    distances[start] = 0
    previous_nodes = {station: None for station in graph}

    while queue:
        current_distance, current_station = heapq.heappop(queue)

        if current_station == end:
            break

        for neighbor, weight in graph[current_station].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_station
                heapq.heappush(queue, (distance, neighbor))

    path = []
    station = end
    while previous_nodes[station]:
        path.insert(0, station)
        station = previous_nodes[station]
    path.insert(0, station)

    return path, distances[end]

#encontrar la mejor ruta entre las 2 estaciones
def find_best_route(start, end, minimize_transfers=False):
    if minimize_transfers:
        #se tienen que penalizar los transbordos 
        graph_with_penalized_transfers = {}

        for station, neighbors in metro_map.items():
            graph_with_penalized_transfers[station] = {}
            for neighbor, time in neighbors.items():
                if "linea" in station and "linea" in neighbor:
                    #si se requiere transbordo entre lineas diferentes añadir penalizacion de 10 minutos
                    if station.split(" linea ")[1] != neighbor.split(" linea ")[1]:
                        graph_with_penalized_transfers[station][neighbor] = time + 10 
                    else:
                        graph_with_penalized_transfers[station][neighbor] = time
                else:
                    graph_with_penalized_transfers[station][neighbor] = time
        return dijkstra(graph_with_penalized_transfers, start, end)
    else:
        # Encontrar la ruta mas rapida 
        return dijkstra(metro_map, start, end)

def valid_station(station):
    return station in metro_map

def get_valid_station(prompt):
    while True:
        station = input(prompt).strip()
        if valid_station(station):
            return station
        else:
            print("la estacion que usted seleciono no es valida,ingrese una estacion existente")

def get_valid_time(prompt):
    while True:
        time_str = input(prompt)
        try:
            # Convertir la entrada a un objeto datetime con formato de 24 horas
            return datetime.strptime(time_str, "%H:%M")
        except ValueError:
            print("Formato invalido,ingrese la hora en formato HH:MM de 24 horas")
