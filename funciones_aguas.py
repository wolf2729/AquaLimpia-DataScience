import pandas as pd

# CARGA DATOS

def cargar_datos(ruta):
    return pd.read_excel(ruta)

# CALIDAD DATOS

def evaluar_calidad_datos(df):

    print("Valores nulos")
    print(df.isnull().sum())

    print("Duplicados")
    print(df.duplicated().sum())

# METRICAS

def calcular_metricas(df):

    resumen = df.groupby("planta").agg({
    "DBO_entrada_mg_L":"mean",
    "DBO_salida_mg_L":"mean",
    "caudal_entrada_m3_d":"mean",
    "energia_aeracion_kWh":"mean"
})

    resumen["eficiencia"] = (
        (resumen["DBO_entrada_mg_L"] - resumen["DBO_salida_mg_L"])
        / resumen["DBO_entrada_mg_L"]
    ) * 100

    return resumen.reset_index()

# EXPORTAR REPORTES

def exportar_reportes(df):

    reporte_operaciones = df[[
        "fecha_registro",
        "caudal_entrada_m3_d",
        "DBO_entrada_mg_L",
        "DBO_salida_mg_L",
        "energia_aeracion_kWh",
        "lodos_generados_kg_d"
    ]]

    reporte_ambiental = df[[
        "fecha_registro",
        "planta",
        "DBO_salida_mg_L",
        "cumplimiento_norma"
    ]]

    reporte_operaciones.to_excel(
        "reporte_operaciones.xlsx",
        index=False
    )

    reporte_ambiental.to_excel(
        "reporte_gestion_ambiental.xlsx",
        index=False
    )