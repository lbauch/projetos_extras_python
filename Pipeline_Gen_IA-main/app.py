import streamlit as st
from contrato import Vendas
from datetime import datetime,time
from pydantic import ValidationError
from database import salvar_no_postgres

# st.write("esse é meu dashboard")
# st.button("esse é um botão")

# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title('Uber pickups in NYC')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)


def main():

    st.title("Sistema de CRM e vendas - Teste Lucas")
    email = st.text_input("Email do vendedor")
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Hora da venda", value=time(9,0)) #valor padrão = 9:00
    valor = st.number_input("Valor da venda", min_value = 0.0, format="%.2f")
    quantidade = st.number_input("Qtd de produtos vendida", min_value=1, step=1)
    produto = st.selectbox("selecionar produto", options = ["Zap com Gemini","Zap com GPT", "Zap com Llama"])

    if st.button("Salvar"):

        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email = email.lower(),
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

        # st.write("**Dados da venda**")
        # st.write(f"Email do vendedor: {email}")
        # st.write(f"Data e hora da venda: {data_hora}")
        # st.write(f"Valor da venda: {valor:.2f}")
        # st.write(f"Qtd de produtos: {quantidade}")
        # st.write(f"Produto: {produto}")
# Utilizado para rodar somente em caso de acesso direto.
# Chamada via backend desconsidera esta parte abaixo

if __name__ == "__main__":
    main() 