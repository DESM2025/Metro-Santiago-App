import streamlit as st
import metro_solver 
from metro_map import metro_map 

# configuracion
st.set_page_config(
    page_title="Metro",
    layout="wide"
)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.title("Metro de Santiago")
    st.markdown("""
    Esta pequeña aplicacion encuentra la ruta optima entre dos estaciones del Metro de Santiago.
    Utilizando el algoritmo de Dijkstra para calcular el camino más corto o con menos transbordos.
    """)

with col2:
    st.image("mapa_metro.jpg", use_container_width=True)

st.divider() 

# sidebar
with st.sidebar:
    st.header("Planifica tu viaje")
    
    #obtener lista de estaciones 
    lista_estaciones = sorted(list(metro_map.keys()))
    
    #dropdowns para elegir origen y destino
    origen = st.selectbox("Desde:", lista_estaciones, index=0)
    destino = st.selectbox("Hasta:", lista_estaciones, index=len(lista_estaciones)-1)
    
    #checkbox para la logica de transbordos
    minimizar_transbordos = st.checkbox("Minimizar transbordos", value=False)
    
    st.info("Si se activa Minimizar transbordos el sistema penalizara los cambios de linea aunque el viaje sea mas largo")

if st.button("Buscar Mejor Ruta", type="primary"):
    
    if origen == destino:
        st.warning("El origen y el destino son el mismo")
    else:
        with st.spinner('Calculando ruta óptima...'):
            ruta, tiempo = metro_solver.find_best_route(origen, destino, minimize_transfers=minimizar_transbordos)
        
        st.success(f"Ruta Encontrada, Tiempo estimado: **{tiempo:.0f} minutos**")
        
        st.subheader("Tu Itinerario")
        
        for i, estacion in enumerate(ruta):
            if i == 0:
                st.markdown(f"**Inicio:** {estacion}")
            elif i == len(ruta) - 1:
                st.markdown(f"**Llegada:** {estacion}")
            else:
                # destacar transbordos
                if "linea" in estacion and i > 0:
                    anterior = ruta[i-1]
                    try:
                        if estacion.split(" linea ")[0] == anterior.split(" linea ")[0]:
                            st.markdown(f"*Transbordo en {estacion.split(' linea ')[0]}*")
                        else:
                            st.write(f"{estacion}")
                    except:
                         st.write(f"{estacion}")
                else:
                    st.write(f" {estacion}")

st.divider()
st.caption("UTEM")