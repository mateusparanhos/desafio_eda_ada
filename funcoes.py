import pandas as pd
import seaborn as sns


def carrega_dataset():
    descript = pd.read_csv('metadata.csv', sep = ',')
    dataf = pd.read_csv('new_train.csv', sep =',')
    """Carrega uma base de dados do seaborn de acordo com o nome
    do dataset.

    Args:
        nome_dataset (str): nome do dataset a ser carregado

    Returns:
        pandas.DataFrame: dataset
    """
    return dataf