import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Frecuencia de muestreo
fs = 1000

# Tiempo
t = np.linspace(0, 1, fs)

# Señal de 50 Hz
senal1 = np.sin(2 * np.pi * 50 * t)

# Señal de 200 Hz
senal2 = 0.5 * np.sin(2 * np.pi * 200 * t)

# Señal compuesta
senal = senal1 + senal2

# Ruido
ruido = 0.3 * np.random.randn(len(t))

# Señal con ruido
senal_ruidosa = senal + ruido

# ---------------------
# FILTRO PASA BAJOS
# ---------------------

fc = 100  # frecuencia de corte

b, a = butter(
    4,
    fc / (fs / 2),
    btype='low'
)

senal_filtrada = filtfilt(
    b,
    a,
    senal_ruidosa
)

# ---------------------
# GRÁFICAS
# ---------------------

plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
plt.plot(t, senal_ruidosa)
plt.title("Señal original con ruido")
plt.grid()

plt.subplot(2,1,2)
plt.plot(t, senal_filtrada, color="red")
plt.title("Señal filtrada (Pasa Bajos)")
plt.grid()

plt.tight_layout()
plt.show()
