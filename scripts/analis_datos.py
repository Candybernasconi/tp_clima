import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Rutas de archivos (siguiendo la estructura del TP)
# Buscamos el dataset en la carpeta 'datos' que armó Hugo
ruta_datos = os.path.join("datos", "clima.csv")  # <-- Si tu archivo no se llama clima.csv, cambialo acá
ruta_resultados = os.path.join("resultados")

# Aseguramos que la carpeta de resultados exista para que no falle al guardar
os.makedirs(ruta_resultados, exist_ok=True)

print("--- Iniciando el análisis de datos climáticos ---")

try:
    # 2. Carga del Dataset
    df = pd.read_csv(ruta_datos) 
    print("¡Dataset cargado con éxito!")
    
    # 3. Transformación de datos
    df['Year'] = pd.to_datetime(df['Year'], format='%Y-%m')
    
    # 4. Cálculo de Estadísticas (Análisis Estadístico)
    promedio_anomalia = df['Mean'].mean()
    max_anomalia = df['Mean'].max()
    min_anomalia = df['Mean'].min()
    
    print("\n--- Resultados Estadísticos ---")
    print(f"Cantidad total de registros analizados: {len(df)}")
    print(f"Anomalía promedio global: {promedio_anomalia:.4f}")
    print(f"Anomalía máxima registrada: {max_anomalia:.4f}")
    print(f"Anomalía mínima registrada: {min_anomalia:.4f}")
    
    # 5. Generación del Gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['Mean'], color='darkred', linewidth=1, label='Anomalía Mensual')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    
    plt.title('Evolución Histórica de las Anomalías de Temperatura Global (Desde 1850)', fontsize=14)
    plt.xlabel('Año / Tiempo', fontsize=12)
    plt.ylabel('Anomalía de Temperatura (°C)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    # 6. Guardar el gráfico automáticamente en la carpeta que pide el TP
    ruta_grafico = os.path.join(ruta_resultados, "grafico_anomalias.png")
    plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n¡Análisis completo! El gráfico se guardó en: {ruta_grafico}")

except FileNotFoundError:
    print(f"\n[ERROR]: No se encontró el archivo de datos en '{ruta_datos}'.")
    print("Asegúrate de que el archivo del dataset esté guardado dentro de la carpeta 'datos' con el nombre correcto.")
except Exception as e:
    print(f"\n[ERROR INESPERADO]: {e}")