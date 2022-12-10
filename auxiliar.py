import pandas as pd

def carrega_dataset():
    dataframe = pd.read_csv('new_train.csv', sep = ',')
    description = pd.read_csv('metadata.csv', sep= ';')


    """Carrega duas bases de dados do csv de acordo com o nome
    do dataset.

    Args:
        nome_dataset (str): nome do dataset a ser carregado

    Returns:
        pandas.DataFrame: dataset
    """
    return description, dataframe