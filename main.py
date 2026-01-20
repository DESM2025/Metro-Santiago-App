from metro_solver import get_valid_station, find_best_route, get_valid_time  
from datetime import timedelta

#Diego Silva Madariaga 
#20.965.500-4

def main():
    print("Bienvenido al sistema de rutas del Metro de Santiago")

    start_time = get_valid_time("Ingrese la hora de salida HH:MM en formato 24 horas:\n")
    start_station = get_valid_station("Ingrese la estacion de origen:\n")
    end_station = get_valid_station("Ingrese la estacion de destino:\n")
    minimize_transfers = input("¿Desea minimizar transbordos? (si/no): \n").lower() == 'si'

    # Encontrar la mejor ruta
    path, time = find_best_route(start_station, end_station, minimize_transfers)

    # Calcular la hora de llegada sumando el tiempo estimado en minutos
    arrival_time = start_time + timedelta(minutes=time)

    print(f"Ruta: {' -> '.join(path)}")
    print(f"Tiempo estimado: {time} minutos")
    print(f"Hora de llegada estimada: {arrival_time.strftime('%H:%M')}")

if __name__ == "__main__":
    main()
