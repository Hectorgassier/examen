import numpy as np
import matplotlib.pyplot as plt

# Definir la función periódica (ejemplo con función escalón)
def f(x):
    # Esto es un ejemplo - debes reemplazarlo con tu función real
    if x % 4 < 2:
        return 1
    else:
        return 0

# Parámetros para la serie de Fourier
L = 2  # Semi-periodo (ajustar según tu problema)
n_terms = 10  # Número de términos en la serie

# Calcular coeficiente a0 (Q0 en tu imagen)
def calculate_a0(f, L):
    # Integral sobre un periodo completo [-L, L]
    x = np.linspace(-L, L, 1000)
    y = f(x)
    a0 = (1/L) * np.trapz(y, x) / 2  # Dividido por 2 para la media
    return a0

# Calcular coeficientes an
def calculate_an(f, L, n):
    x = np.linspace(-L, L, 1000)
    y = f(x) * np.cos(n * np.pi * x / L)
    an = (1/L) * np.trapz(y, x)
    return an

# Calcular coeficientes bn
def calculate_bn(f, L, n):
    x = np.linspace(-L, L, 1000)
    y = f(x) * np.sin(n * np.pi * x / L)
    bn = (1/L) * np.trapz(y, x)
    return bn

# Calcular la serie de Fourier
def fourier_series(x, f, L, n_terms):
    a0 = calculate_a0(f, L)
    series = a0 / 2
    
    for n in range(1, n_terms + 1):
        an = calculate_an(f, L, n)
        bn = calculate_bn(f, L, n)
        series += an * np.cos(n * np.pi * x / L) + bn * np.sin(n * np.pi * x / L)
    
    return series

# Calcular Q0 (a0 en la notación estándar)
Q0 = calculate_a0(f, L)
print(f"Q0 = {Q0}")

# Graficar la función original y la aproximación de Fourier
x_plot = np.linspace(-3, 3, 1000)
y_original = np.array([f(x) for x in x_plot])
y_fourier = fourier_series(x_plot, f, L, n_terms)

plt.figure(figsize=(10, 5))
plt.plot(x_plot, y_original, label='Función original')
plt.plot(x_plot, y_fourier, label=f'Aproximación Fourier ({n_terms} términos)')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Serie de Fourier')
plt.grid()
plt.show()




# Si conoces directamente el valor de Q0
Q0 = (1/3) * 4
print(f"El valor de Q0 es: {Q0}")

# O si necesitas calcularlo a partir de una función específica
def tu_funcion(x):
    # Define aquí tu función específica basada en los puntos de la imagen
    if x >= -3 and x < -1:
        return 2
    elif x >= -1 and x < 1:
        return 4
    elif x >= 1 and x <= 3:
        return 2
    else:
        # Para periodicidad fuera de [-3, 3]
        return tu_funcion(x % 6 - 3)  # Asumiendo periodo 6

# Luego calculas Q0 para tu función
L = 3  # Semi-periodo (ajustar según tu problema)
Q0_calculado = calculate_a0(tu_funcion, L)
print(f"Q0 calculado: {Q0_calculado}")