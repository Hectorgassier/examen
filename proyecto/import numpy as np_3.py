import numpy as np
import matplotlib.pyplot as plt
# Función para calcular la Serie de Fourier de una onda senoidal
def fourier_series_sine(t, T, N, A=10):
    """
    Calcula la Serie de Fourier de una onda senoidal de periodo T y amplitud A.
    
    Parámetros:
    t: vector de tiempo
    T: período de la señal
    N: número de armónicos (términos en la serie)
    A: amplitud máxima de la señal
    
    Retorna:
    f_approx: señal aproximada con la serie de Fourier
    """
    w0 = 2 * np.pi / T  # Frecuencia fundamental
    f_approx = np.zeros_like(t)  # Inicializar la serie con ceros
    
    # Sumar los términos de la serie de Fourier
    for n in range(1, N+1):
        bn = (2 * A) / (n * np.pi) * (1 - (-1)**n)  # Coeficiente para onda senoidal
        f_approx += bn * np.sin(n * w0 * t)  # Suma de términos senoidales
    
    return f_approx

# Definir los parámetros de la señal
T = 2 * np.pi  # Período de la onda senoidal
N = 10  # Número de términos en la serie
A = 10  # Amplitud máxima
t = np.linspace(-2*T, 2*T, 1000)  # Vector de tiempo para la gráfica

# Calcular la Serie de Fourier
f_approx = fourier_series_sine(t, T, N, A)

# Graficar la señal aproximada con la serie de Fourier
plt.plot(t, f_approx, label=f"Aproximación con {N} términos")
plt.axhline(A, color='r', linestyle='--', label='Amplitud máxima')
plt.axhline(-A, color='r', linestyle='--')
plt.title("Serie de Fourier de una onda senoidal")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()
plt.show()
