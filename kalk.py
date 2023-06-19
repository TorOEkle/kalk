import streamlit as st

st.header("Adrianas Kalkulator 	:heart:")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sett inn åpne m2")
    a = st.number_input("åpne m2", help="Sett inn åpne m2", value=0.0, step=0.1, key="open")

with col2:
    st.subheader("Sett inn lukkede m2")
    b = st.number_input("lukkede m2", help="Sett inn lukkede m2", value=0.0, step=0.1, key="closed")

if b == 0:
    st.stop()
st.subheader(f"Totalt åpne m2: {round((a/(a+b))*100,2)} %")
st.subheader(f"Antall m2 for å få 30% åpenhet = {round((a+b)*0.3,2)} m2")