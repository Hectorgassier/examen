import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros
T = 2  # Periodo
A = 1  # Amplitud
w0 = 2 * np.pi / T  # Frecuencia angular fundamental
t = np.linspace(-T, T, 1000)  # Vector de tiempo

# Función de la señal triangular
def triangular_wave(t, T, A):
    return (4 * A / T) * np.abs((t % T) - T/2) - A

# Función de la Serie de Fourier
def fourier_series(t, A, T, N):
    sumatoria = np.zeros_like(t)
    for n in range(1, N + 1, 2):  # Solo términos impares
        an = (8 * A) / (np.pi**2 * n**2) * (-1)**n
        sumatoria += an * np.cos(n * w0 * t)
    return sumatoria

# Parámetros
N = 10  # Número de términos en la serie

# Calcular la señal triangular y la serie de Fourier
x_t = triangular_wave(t, T, A)
x_fourier = fourier_series(t, A, T, N)

# Graficar la señal original y la serie de Fourier
plt.figure(figsize=(10, 5))
plt.plot(t, x_t, label="Señal Triangular Original", linestyle="dashed", color="black")
plt.plot(t, x_fourier, label=f"Serie de Fourier (N={N})", color="blue")
plt.xlabel("Tiempo t")
plt.ylabel("x(t)")
plt.legend()
plt.title("Aproximación de la Señal Triangular con Serie de Fourier")
plt.grid()
plt.show()
