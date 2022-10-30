from proceso import proceso, momentos, estacionaridad, espectro

# SECCIÓN A: Función de densidad de probabilidad

# 0. Datos de demanda de potencia
A0 = proceso.demanda()
print(A0)

# 1. Función de densidad del proceso aleatorio
A1 = proceso.densidad()
print(A1)

# 2. Gráfica de la secuencia aleatoria
A2 = proceso.grafica()
print(A2)

# 3. Probabilidad de tener un consumo p1 < P < p2 en t1 < T < t2
A3 = proceso.probabilidad()
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

# SECCIÓN D: Características espectrales 

# 9. Función de densidad espectral de potencia
D9 = espectro.psd()
print(D9)