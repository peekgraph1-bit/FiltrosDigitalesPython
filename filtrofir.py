import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, filtfilt

# Frecuencia de muestreo
fs = 1000

# Tiempo
t = np.linspace(0, 1, fs)

# Señales
senal1 = np.sin(2 * np.pi * 50 * t)
senal2 = 0.5 * np.sin(2 * np.pi * 200 * t)

# Señal compuesta
senal = senal1 + senal2

# Ruido
ruido = 0.3 * np.random.randn(len(t))

senal_ruidosa = senal + ruido

# Diseño FIR
coeficientes = firwin(
    numtaps=101,
    cutoff=100,
    fs=fs
)

# Filtrado
senal_fir = filtfilt(
    coeficientes,
    1,
    senal_ruidosa
)

# Gráficas
plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
plt.plot(t, senal_ruidosa)
plt.title("Señal original con ruido")
plt.grid()

plt.subplot(2,1,2)
plt.plot(t, senal_fir, color="orange")
plt.title("Señal filtrada con FIR")
plt.grid()

plt.tight_layout()
plt.show()
