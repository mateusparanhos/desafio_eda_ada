import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from auxiliar import carrega_dataset


# CORPO
st.markdown("""# Projeto Modulo4
Análise Exploratória de uma campanha de marketing de um banco privado 

Turma: 892 - Lets Code - Suzano

Alunos: 

Paulo Roberto P. Alves Jr

Lucas Guimarães 

Mateus Paranhos

Francisco

Jean Kalyson


   ---
    """)

st.markdown('''### Introdução 

Fonte dos dados: https://www.kaggle.com/datasets/rashmiranu/banking-dataset-classification?select=new_train.csv 

Houve uma queda de receita no Banco Português. Após investigação, descobriram que seus clientes não estavam investindo o suficiente para depósitos de longo prazo. 

Assim, o banco gostaria de identificar os clientes existentes com maior chance de subscrever um depósito de longo prazo e então, concentrar os esforços de marketing nesses clientes. 

Iremos realizar a análise exploratória a fim de encontrar onde os esforços de marketing podem obter melhor retorno.''')

## CORPO - Carregando o dataset
st.header('Dataset')
description, dataframe = carrega_dataset()#


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

with st.expander('Questões a serem respondidas:'):
    st.markdown("""
            - Há um padrão de idade, ou de ligações que foram feitas na campanha?
            - Há um padrão no nível de educação?
            - Como estão sendo feitas as ligações?
            - Como é o perfil etário?
    
    """)

with st.expander('Análises Estatísticas Univariadas'):
    st.plotly_chart(px.box(data_frame=dataframe, x=dataframe['duration']))
    st.markdown("Observa-se uma média de mais de 4 minutos em ligação telefônica, apesar de ter-se, no geral, durações mais curtas nas ligações. Com o terceiro quartil fechando em aproximadamente 5 minutos e 20 segundos, havendo acima disso um outlier gigantesco.")
    st.plotly_chart(px.histogram(data_frame=dataframe, x=dataframe['education']))
    st.markdown("Observa-se uma concentração maior de indivíduos com graus de educação já focados em ensino superior e ensino médio finalizado.")
    st.plotly_chart(px.box(data_frame=dataframe, x=dataframe['age']))
    st.markdown("Observa-se que mesmo com um range entre 17 a 98 anos, mas 50% foram entre 30 e 50 anos e, tirando outliers, pode-se afirmar que a pesquisa foi direcionada para um público entre 17 a 70 anos, o que faz sentido ao avaliar que se trata de produtos de longo-prazo.")
    st.plotly_chart(px.box(data_frame=dataframe, x=dataframe['campaign']))
    st.markdown("A presença de muitos outliers e com grande quantidade de ligações. Cerca de 75% dos clientes receberam até 3 ligações, será que o esforço é efetivo?")
    st.plotly_chart(px.histogram(data_frame=dataframe, x=dataframe['job']))
    st.markdown("Nota-se uma predominância de técnicos, administradores e trabalhadores braçais para contato.")


with st.expander('Análises Descritivas Bivariadas'):
    st.subheader('Correlações entre variáveis numéricas')
    st.write(dataframe.corr())
    st.markdown("Nota-se uma correlação alta entre pdays e previous.")
    st.subheader('Correlações entre variáveis numéricas corrigida')
    st.write(dataframe[dataframe['pdays']!=999].corr())
    st.markdown("Nota-se que a correlação deixa de existir, pois há um código em pdays em 999 quando não houve contato anterior, o que altera o valor da correlação e da estatística drasticamente.")
    st.subheader('Qual a profissão influencia mais a aquisição?')
    st.plotly_chart(px.histogram(data_frame=dataframe, x='job', color ='y', barmode = 'group'))
    st.markdown('A profissão de administrador aparenta influenciar na aquisição de produtos.')
    st.subheader('Qual o perfil educacional que mais a adquire o produto?')
    st.plotly_chart(px.histogram(data_frame=dataframe, x='education', color ='y', barmode = 'group'))
    educ_y = pd.crosstab(index=dataframe["education"], columns=dataframe["y"],margins=True)
    educ_y['yes %'] = educ_y['yes']*100/educ_y['All']  
    st.write(educ_y) 
    st.markdown('Observa-se que as maiores taxas de aceitação são dos iletrados, universitários e indivíduos de cujo grau de escolaridade não consta no registro.')
    st.subheader('Qual foi a efetividade das campanhas?')
    st.plotly_chart(px.histogram(data_frame=dataframe, x='campaign', color ='y', barmode = 'overlay'))
    camp_sample = st.slider('Defina a quantidade mínima de contatos do dataset para análise:', min_value=1, max_value=58, value=1, step=1)
    qtd_camp = dataframe['campaign'][dataframe['campaign']>=camp_sample].count()
    qtd_camp_yes = dataframe['campaign'][(dataframe['campaign']>=camp_sample) & (dataframe['y']=='yes')].count()
    percentual_campmais_yes = qtd_camp_yes*100/qtd_camp
    st.write(f'Percentual de indivíduos que adquiriram o produto após {camp_sample} contatos foi de {percentual_campmais_yes:.2f}%.')

    st.markdown('Observa-se que as aceitações seguem o mesmo padrão das chamadas e tempo de chamada não corresponde em conversão.')
    st.subheader('Qual a taxa de retorno de clientes?')
    st.plotly_chart(px.histogram(data_frame=dataframe, x='poutcome', color ='y', barmode = 'group'))
    st.markdown('Observa-se um comportamento interessante, a maioria das pessoas que fechou esse produto no passado fechou novamente agora. Isso dá uma ideia de aceitação ou qualidade do produto. Mas será que é um público expecífico?')
    st.write(dataframe[dataframe['poutcome']=='success'].describe(include='number'))
    st.write(dataframe[dataframe['poutcome']=='success'].describe(exclude='number'))
    st.markdown('Respondendo o questionamento anterior: não há um perfil de compra.')
    st.subheader('Influência da idade na aquisição do produto')
    st.plotly_chart(px.histogram(data_frame=dataframe, x='age', color ='y', barmode = 'overlay'))
    st.markdown('Embora a parcela mais expressiva seja entre 20 e 40 anos, parece haver uma participação percentual de fechamento maior a partir dos 60 anos.')

    age_sample = st.slider('Defina a idade mínima de consulta do dataset para análise:', min_value=17, max_value=98, value=50, step=1)
    qtd_age = dataframe['age'][dataframe['age']>=age_sample].count()
    qtd_age_yes = dataframe['age'][(dataframe['age']>=age_sample) & (dataframe['y']=='yes')].count()
    percentual_agemais_yes = qtd_age_yes*100/qtd_age
    st.write(f'Percentual de indivíduos que adquiriram o produto acima de {age_sample} anos foi de {percentual_agemais_yes:.2f}%.')


with st.expander('Análise Multivariada'):
     st.subheader('Influência do nível educacional e a idade na compra.')
     st.pyplot(sns.relplot(data=dataframe,x="age", y="education", hue="y"))
     st.markdown("Percebe-se que os níveis educacionais desconhecido, ensino médio, básico de 4 anos e curso profissional entre os idosos são os mais efetivos na aquisição.")
     st.subheader('Influência da vida matrimonial e a idade na compra do produto.')
     st.pyplot(sns.catplot(x="age", y="marital", data=dataframe, hue="y"))
     st.markdown("Percebe-se um padrão de compra maior em indivíduos idosos casados e divorciados e ligeiramente menor em solteiros jovens.")

with st.expander('Conclusão'):
    st.markdown('''
    Nota-se que foi uma campanha heterogênea, atingindo a todos os públicos possíveis, contudo observaram-se algumas tendências de consumo, como o caso de indivíduos acima de 60 anos de idade, de escolaridades diversas, preferencialmente casados e divorciados e jovens solteiros numa minoria, sendo que estes públicos poderão ser alvos em campanhas posteriores separadamente.
    
    Outro ponto a se destacar para futuras campanhas é o índice de aceitação pelo público já cativo de campanhas anteriores. 
    
    Deve-se destacar também o alto grau de esforço no grande número de contatos efetuados e na duração alta dos mesmos sendo não convertidos em clientes para o banco, o que gera prejuízo ao mesmo.

    
    ''')

    