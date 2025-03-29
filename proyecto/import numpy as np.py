import numpy as np
import matplotlib.pyplot as plt

def sawtooth_fourier(t, A, T, N):
    """
    Calcula la aproximación de la Serie de Fourier de la señal dientes de sierra.
    
    Parámetros:
    - t: vector de tiempo
    - A: amplitud de la señal
    - T: periodo de la señal
    - N: número de términos en la aproximación
    
    Retorna:
    - Señal aproximada con N términos de la Serie de Fourier
    """
    x_t = np.zeros_like(t)
    for n in range(1, N + 1):
        bn = (-4 * A / (n * np.pi)) * (-1)**n
        x_t += bn * np.sin(2 * np.pi * n * t / T)
    return x_t

# Parámetros
A = 1  # Amplitud
T = 2   # Periodo
N = 10  # Número de términos en la serie

t = np.linspace(-T, T, 1000)  # Vector de tiempo
x_approx = sawtooth_fourier(t, A, T, N)

# Gráfica
plt.figure(figsize=(8, 4))
plt.plot(t, x_approx, label=f"Fourier N={N}", color='b')
plt.axhline(y=A, color='k', linestyle='--')
plt.axhline(y=-A, color='k', linestyle='--')
plt.title("Aproximación de la Serie de Fourier de una señal dientes de sierra")
plt.xlabel("Tiempo, t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.show()
