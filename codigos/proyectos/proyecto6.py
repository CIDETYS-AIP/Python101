#conseguir data de covid y presentarlo de manera grafica
import pandas as pd

data=pd.read_html(r'https://datosmacro.expansion.com/otros/coronavirus/panama')

print(data[0])