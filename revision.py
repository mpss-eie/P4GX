from proceso import proceso, momentos, estacionaridad
import pandas as pd

# SECCIÓN A: Función de densidad de probabilidad

# 0. Lectura de datos
df = pd.read_csv('seoul.csv')
df['dt'] = pd.to_datetime(df['dt'], format='%Y%m%d%H')
df.set_index(['dt', 'loc'], inplace=True)

# 1. Obtención de la muestra
A1 = proceso.muestra()
print(A1)

# 2. Obtención del proceso
A2 = proceso.proceso()
print(A2)

# 3. Gráfica de las funciones muestra
A3 = proceso.grafica()
print(A3)

# SECCIÓN B: Momentos

# 4. Autocorrelación
B4 = momentos.autocorrelacion()
print(B4)

# 5. Autocovarianza
B5 = momentos.autocovarianza()
print(B5)

# SECCIÓN C: Estacionaridad

# 6. Estacionaridad en sentido amplio
C6 = estacionaridad.wss()
print(C6)

# 7. Promedio temporal
C7 = estacionaridad.prom_temporal()
print(C7)

# 8. Ergodicidad
C8 = estacionaridad.ergodicidad()
print(C8)
