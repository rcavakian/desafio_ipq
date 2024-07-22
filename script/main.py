import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sinasc_dados = '../data/sinasc_2016.csv'
municipios_uf = '../data/municipios.csv'

sinasc_df = pd.read_csv(sinasc_dados, sep=',', encoding='ISO-8859-1')
municipios_df = pd.read_csv(municipios_uf, sep=';', encoding='ISO-8859-1')

