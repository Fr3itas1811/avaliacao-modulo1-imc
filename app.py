import streamlit as st

st.title("calculadora imc")
st.subheader("feito com streamlit")

altura =st.number_input("digite sua altura" , min_value = 0.0)
peso = st.number_input("digite seu peso", min_value = 0.0)

if st.button("calcular"):
    imc = peso / altura **2
    st.success (f"seu imc e {imc:.2f}") 
    
    if imc < 18.5:
        st.error("abaixo do peso ☠️")
        st.image("https://i.pinimg.com/originals/fe/0f/26/fe0f260522b4c72d7a50acfdffe756d3.jpg",width=250)
    
    elif imc < 24.9:
        st.success("seu imc esta correto 👏🏻")
        st.image("https://s2-ge.glbimg.com/VEEO0fc1v4xKLAg7_Jie2-lq6NA=/1200x/smart/filters:cover():strip_icc()/s.glbimg.com/es/ge/f/original/2017/05/14/neymar.jpg",width=250 )

    elif imc < 29.9:
        st.error("sobre peso")
        st.image("https://preview.redd.it/neymar-gordo-v0-xhnujxaucp7a1.jpg?width=1080&crop=smart&auto=webp&s=8f23eb5d36eea155ac278dc1067c144d296f9815", width= 154)

    elif imc< 34.9:
        st.error("Obesidade grau 1")
        st.image("https://preview.redd.it/neymar-gordo-v0-xhnujxaucp7a1.jpg?width=1080&crop=smart&auto=webp&s=8f23eb5d36eea155ac278dc1067c144d296f9815", width= 154)


    elif imc < 39.9:
        st.error("Obesidade grau 2")
        st.image("https://preview.redd.it/neymar-gordo-v0-xhnujxaucp7a1.jpg?width=1080&crop=smart&auto=webp&s=8f23eb5d36eea155ac278dc1067c144d296f9815", width= 100)


    elif imc > 40.0:
        st.error("cuidado, vai morrer")
        st.image("https://tse2.mm.bing.net/th/id/OIP.u3z9sMYn4A-e5ws9yqZBKQHaJQ?pid=ImgDet&w=474&h=592&rs=1&o=7&rm=3", width= 154)



