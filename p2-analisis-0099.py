# import librerias
import pandas as pd
import numpy as np 
print("Analisis de datos vehiculos por Anais Medina NC 0099")
vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Hibrido", "Gasolina", "Diesel", "Electrico", "Gasolina"],
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]
}

df = pd.DataFrame(vehiculos)
print(df)
print("---------- agrupar por una sola colunma----------")
agrupado = df.groupby('Precio_USD')
print(agrupado)
print("----------por agregacion----------")
# Autonomia_km promedio por Precio_USD 
print(agrupado["Autonomia_Km"].mean())

# Precio_USD maximo en cada Precio_USD
print(agrupado['Precio_USD'].max())
