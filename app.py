import streamlit as st

st.write("""
# Hello World
# Welcome to my firts website
Hello, my name is M. Rafi Afandi, on this website I'm gonna help you to do simple calculate on math
""")

alas = st.number_input("Masukkan Nilai Alas", 0)
tinggi = st.number_input("Masukkan Nilai Tinggi", 0)
hitung = st.button("Hitung Luas Segitiga")

if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f"Luas Segitiga Adalah {luas}")