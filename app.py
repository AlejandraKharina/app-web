import streamlit as st
import random

st.title("Lanzamiento de Moneda")

num_lanzamientos = st.number_input("¿Cuántas veces quieres lanzar la moneda?", min_value=1, step=1)
if st.button("Lanzar"):
    resultados = [random.choice(["Cara", "Cruz"]) for _ in range(int(num_lanzamientos))]
    st.write("Resultados:")
    st.write(resultados)
