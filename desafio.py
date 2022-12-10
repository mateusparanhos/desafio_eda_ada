import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
from auxiliar import carrega_dataset


# CORPO
st.markdown("""
    # iNalyze
    ### *A sua ferramenta para análise dados*
   ---
    """)

## CORPO - Carregando o dataset
st.header('Dataset')
description, dataframe = carrega_dataset()

## CORPO - Info do dataset
with st.expander('Dados do Dataset'):
    view_dataframe = st.radio('Escolha qual dataset desejas observar préviamente:', options=['Descritivo dos Dados', 'Banco de Dados'])
    if view_dataframe =='Descritivo dos Dados':
        st.header('Como funciona o Dataset')
        st.write(description)
    elif view_dataframe =='Banco de Dados':
        st.header('Destinchando do Dataset')
        st.subheader('O Dataset em si')
        st.write(dataframe)
        st.subheader('Tamanho do Dataset')
        st.write(dataframe.shape[0])
        st.subheader('Existem dados nulos?')
        st.write(dataframe.isnull().sum().to_frame().T)
        st.subheader('Valores Únicos por Coluna')
        st.write(dataframe.nunique().to_frame().T)


with st.expander('Análises Estatísticas Descritivas Básicas do Dataset Univariada'):
     view_stats = st.radio('Escolha qual análise desejas observar:', options=['Categórica', 'Numérica'])
     if view_stats == 'Categórica':
        st.header('Análise Categórica do Dataset')
        st.write(dataframe.describe(exclude='number'))
        col_select = st.selectbox('Selecione a variável que desejas avaliar:', options=list(dataframe.select_dtypes(exclude = np.number).columns))
        st.plotly_chart(px.histogram(data_frame=dataframe, x=col_select))
     elif view_stats == 'Numérica':
        st.header('Análise Numéricas do Dataset')
        st.write(dataframe.describe(include='number'))
        col_select = st.selectbox('Selecione a variável que desejas avaliar:', options=list(dataframe.select_dtypes(include = np.number).columns))
        view_graf_uni = st.radio('Escolha qual gráfico univariável desejas observar:', options=['Boxplot', 'Histograma'])
        if view_graf_uni == 'Boxplot':
            st.plotly_chart(px.box(data_frame=dataframe, y=col_select))
        elif view_graf_uni == 'Histograma':
            st.plotly_chart(px.histogram(data_frame=dataframe, x=col_select))





    