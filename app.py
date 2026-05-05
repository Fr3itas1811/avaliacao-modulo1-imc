import streamlit as st

st.title("calculadora imc")
st.subheader("feito com streamlit")

altura =st.number_input("digite sua altura" , min_value = 0.0)
peso = st.number_input("digite seu peso", min_value = 0.0)

if st.button("calcular"):
    imc = peso / altura **2
    st.success (f"seu imc e {imc:.2f}") 
    
    if imc < 18.5:
        st.error("abaixo do peso ")

    elif imc < 24.9:
        st.success("seu imc esta correto ")
   
    elif imc < 29.9:
        st.error("sobre peso")
     
    elif imc< 34.9:
        st.error("Obesidade grau 1")
   
    elif imc < 39.9:
        st.error("Obesidade grau 2")

    elif imc > 40.0:
        st.error("cuidado, vai morrer")
