
# ANALISIS PRINCIPAL - AquaLimpia S.A.

import pandas as pd

try:
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError as e:
    print("Advertencia: no se pudo importar matplotlib/seaborn. El dashboard se omitirá.")
    print(e)
    plt = None
    sns = None

from funciones_aguas import (
    cargar_datos,
    evaluar_calidad_datos,
    calcular_metricas,
    exportar_reportes
)

# CARGA DEL DATASET

df = cargar_datos("dataset_set_A_aguas_residuales.xlsx")

# CONVERTIR FECHA

df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])

# EXPLORACION INICIAL

print(df.head())
print(df.info())

# CALIDAD DE DATOS

evaluar_calidad_datos(df)

# METRICAS

resumen = calcular_metricas(df)

print(resumen)

# DASHBOARD

if plt is not None and sns is not None:
    plt.figure(figsize=(14,8))

    plt.subplot(2,2,1)
    sns.boxplot(data=df, x="planta", y="DBO_salida_mg_L")
    plt.xticks(rotation=45)
    plt.title("DBO salida por planta")

    plt.subplot(2,2,2)
    sns.lineplot(data=df, x="fecha_registro", y="caudal_entrada_m3_d")
    plt.xticks(rotation=45)
    plt.title("Tendencia caudal entrada")

    plt.subplot(2,2,3)
    sns.scatterplot(
        data=df,
        x="DBO_entrada_mg_L",
        y="DBO_salida_mg_L",
        hue="planta"
    )
    plt.title("Relación DBO entrada/salida")

    plt.subplot(2,2,4)
    sns.barplot(data=resumen, x="planta", y="eficiencia")
    plt.xticks(rotation=45)
    plt.title("Eficiencia promedio")

    plt.tight_layout()
    plt.show()
else:
    print("Dashboard omitido porque matplotlib/seaborn no está disponible.")

# EXPORTACION REPORTES

exportar_reportes(df)