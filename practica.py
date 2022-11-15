#consume los datos del archivo inversiones
#almacena en un dataFrame el NOM_ENS, la superficie y el TIPUSSOL
#gráfico de dispersión los totales de la superficie de TIPUSSOL
#gráfico de barras de la superficie media de los 10 primeros NOM_ENS
#gráfico circular de las superficie de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

def consumirDispersion():
    datos = pd.read_csv('suelo.csv')
    df=datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL']]
    df.plot.scatter(x='SUPERFICIE', y='TIPUSSOL', alpha=0.3)
    plt.show()

consumirDispersion()
