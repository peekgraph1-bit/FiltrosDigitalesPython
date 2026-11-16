import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

# Frecuencia de muestreo
fs = 1000

# Filtro pasa bajos
fc = 100

b, a = butter(
    4,
    fc / (fs / 2),
    btype='low'
)

# Respuesta en frecuencia
w, h = freqz(b, a)

# Gráfica
plt.figure(figsize=(8,4))

plt.plot((w/np.pi)*(fs/2), abs(h))

plt.title("Respuesta en frecuencia del filtro pasa bajos")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Ganancia")
plt.grid()

plt.show()
