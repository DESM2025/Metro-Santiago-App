import streamlit as st
import os
import src.metro_solver as metro_solver 
from src.metro_map import metro_map 

current_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="Metro",
    layout="wide"
)
st.markdown("""
    <style>
    .stApp {
        background-color: white;
        color: black;
    }
    [data-testid="stHeader"], section[data-testid="stSidebar"] {
        background-color: #E32731;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    .main * {
        color: black !important;
    }
    hr {
        border-color: black !important;
    }
    
    div[data-testid="stAlert"] {
        background-color: #f2f2f2 !important;
        background: #f2f2f2 !important;
        border: 1px solid #E32731 !important;
        color: black !important;
    }
    div[data-testid="stAlert"] > div {
        background-color: transparent !important;
        color: black !important;
    }
    div[data-testid="stAlert"] p, div[data-testid="stAlert"] span {
        color: black !important;
    }
    div[data-testid="stAlert"] svg {
        fill: #E32731 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Metro de Santiago")
st.markdown("""
Esta pequeña aplicacion encuentra la ruta optima entre dos estaciones del Metro de Santiago
utilizando el algoritmo de Dijkstra para calcular el camino mas corto o con menos transbordos.
""")

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
    
    st.info("Si se activa Minimizar transbordos el sistema penalizara los cambios de linea aunque el viaje sea mas largo en distancia")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.image("mapa_metro.jpg", use_container_width=True)

with col2:
    if st.button("Buscar Mejor Ruta", type="primary"):
        
        if origen == destino:
            st.warning("El origen y el destino son el mismo")
        else:
            with st.spinner('Calculando ruta optima'):
                ruta, tiempo = metro_solver.find_best_route(origen, destino, minimize_transfers=minimizar_transbordos)
            
            st.success(f"Ruta Encontrada, el Tiempo estimado de viaje es de **{tiempo:.0f} minutos**")
            
            st.subheader("Ruta")
            
            ruta_texto = ""
            for i, estacion in enumerate(ruta):
                if i == 0:
                    ruta_texto += f"- **Origen:** {estacion}\n"
                elif i == len(ruta) - 1:
                    ruta_texto += f"- **Destino:** {estacion}\n"
                else:
                    # destacar transbordos
                    if "linea" in estacion and i > 0:
                        anterior = ruta[i-1]
                        try:
                            if estacion.split(" linea ")[0] == anterior.split(" linea ")[0]:
                                ruta_texto += f"- **Transbordo** en {estacion.split(' linea ')[0]}\n"
                            else:
                                ruta_texto += f"- {estacion}\n"
                        except:
                             ruta_texto += f"- {estacion}\n"
                    else:
                        ruta_texto += f"- {estacion}\n"
            
            st.markdown(ruta_texto)

st.divider()
st.caption("UTEM")