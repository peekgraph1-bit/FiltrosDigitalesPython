import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

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

# FILTRO PASA ALTOS
fc = 100

b, a = butter(
    4,
    fc / (fs / 2),
    btype='high'
)

senal_filtrada = filtfilt(
    b,
    a,
    senal_ruidosa
)

# GRÁFICAS
plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
plt.plot(t, senal_ruidosa)
plt.title("Señal original con ruido")
plt.grid()

plt.subplot(2,1,2)
plt.plot(t, senal_filtrada, color="green")
plt.title("Señal filtrada (Pasa Altos)")
plt.grid()

plt.tight_layout()
plt.show()
