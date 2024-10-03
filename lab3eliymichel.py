""" LABORATORIO #3 - Señales electromiográficas EMG
Presentado por: Eliana Domínguez Sabalza (5600587) y Michel Alejandra Ciabato Jiménez (5600595)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt, windows
from scipy import stats


data = np.loadtxt('señallab3emg.txt', delimiter=',', skiprows=3)


tiempo = data[:, 0]
valores = data[:, 1]


plt.figure(figsize=(20, 6)) 


plt.plot(tiempo, valores, label='Señal EMG', color='blue')
plt.title('Gráfico de datos de señal EMG del músculo Braquioradial')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.grid(True)


Ts = tiempo[1] - tiempo[0]
fs = 1 / Ts
longitud_senal = len(valores)
num_contracciones = 24


info_text = f"Frecuencia de muestreo: {fs:.2f} Hz\n"
info_text += f"Tiempo de muestreo: {Ts:.6f} s\n"
info_text += f"Longitud de la señal: {longitud_senal} muestras\n"
info_text += f"Número de contracciones: {num_contracciones}"


plt.text(0.05 * max(tiempo), 0.95 * max(valores), info_text,
         fontsize=10, bbox=dict(facecolor='white', alpha=0.8), verticalalignment='top')

plt.legend()  
plt.show()


print(f"Frecuencia de muestreo (fs): {fs} Hz")
print(f"Tiempo de muestreo (Ts): {Ts} segundos")
print(f"Longitud de la señal: {longitud_senal} muestras")
print("El número de contracciones es: 24")




#FILTROS: 


Fs = 596  # Frecuencia de muestreo de 596 Hz

Omega1 = 200  
Omega2 = 250  
Omega_c = np.sqrt(Omega1 * Omega2)  # Frecuencia de corte central
n = 4  

K1 = 10 * np.log10(1 / (1 + (Omega1 / Omega_c) ** (2 * n)))
K2 = 10 * np.log10(1 / (1 + (Omega2 / Omega_c) ** (2 * n)))


def butter_bandpass(lowcut, highcut, Fs, order=4):
    nyquist = 0.5 * Fs  # Frecuencia de Nyquist
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a


def aplicar_filtro(data, lowcut, highcut, Fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, Fs, order=order)
    y = filtfilt(b, a, data)
    return y

lowcut = Omega1  # 200 Hz (Ω1)
highcut = Omega2  # 250 Hz (Ω2)

valores_filtrados = aplicar_filtro(valores, lowcut, highcut, Fs)

# Gráfico de la señal filtrada
plt.figure(figsize=(20, 6))  # Aumentar el tamaño del gráfico
plt.plot(tiempo, valores_filtrados, label='Señal Filtrada', color='green')
plt.title(f'Señal EMG Filtrada (Pasabanda {lowcut}-{highcut} Hz)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.grid(True)
plt.legend()

plt.show()

#Riple del filtro:

ripple = K1 - K2
print(f"Tamaño del ripple: {ripple:.2f} dB")


#VENTANA HANNING SIN CONVOLUCIÓN:
    


def dividir_en_contracciones(data, num_contracciones):
    longitud = len(data)
    tamaño_ventana = longitud // num_contracciones
    contracciones = [data[i*tamaño_ventana:(i+1)*tamaño_ventana] for i in range(num_contracciones)]
    return contracciones

# Generar ventanas de Hanning para cada contracción sin multiplicarlas por la señal
def generar_ventanas_para_contracciones(contracciones):
    ventanas = []
    for contraccion in contracciones:
        ventana = windows.hann(len(contraccion)) 
        ventanas.append(ventana)  
    return ventanas


num_contracciones = 24
contracciones_filtradas = dividir_en_contracciones(valores_filtrados, num_contracciones)

ventanas_hanning = generar_ventanas_para_contracciones(contracciones_filtradas)

ventanas_hanning_concatenadas = np.concatenate(ventanas_hanning)

# Graficar solo las ventanas
plt.figure(figsize=(20, 6))  
plt.plot(ventanas_hanning_concatenadas, label='Ventanas de Hanning', color='red')
plt.title('Ventanas de Hanning aplicadas a cada contracción (Concatenadas)')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.show()


#VENTANA HANNING Y CONVOLUCIÓN  POR CONTRACCIÓN


# Aplicar la ventana de Hanning
def aplicar_ventana_hanning(data):
    ventana = windows.hann(len(data))
    return data * ventana  

# Aplicar aventanamiento a cada contracción
def aplicar_ventana_a_contracciones(contracciones):
    contracciones_aventanadas = []
    for contraccion in contracciones:
        ventana = windows.hann(len(contraccion))  
        contracciones_aventanadas.append(contraccion * ventana)  
    return contracciones_aventanadas


contracciones_filtradas_hanning = aplicar_ventana_a_contracciones(contracciones_filtradas)

for i, contraccion_hanning in enumerate(contracciones_filtradas_hanning):
    plt.figure(figsize=(20, 6))  # Ajustar el tamaño del gráfico
    plt.plot(contraccion_hanning, label=f'Contracción {i+1} - Filtrada con Ventana Hanning', color='orange')
    plt.title(f'Contracción {i+1} - Señal EMG Filtrada con Ventana Hanning')
    plt.xlabel('Tiempo (muestras)')
    plt.ylabel('Voltaje (mV)')
    plt.grid(True)
    plt.legend()
    
    plt.show()


# MOSTRAR SEÑAL TOTAL CON AVENTANAMIENTO


def concatenar_contracciones(contracciones):
    return np.concatenate(contracciones)

señal_filtrada_hanning_contracciones = concatenar_contracciones(contracciones_filtradas_hanning)


plt.figure(figsize=(20, 6))  
plt.plot(señal_filtrada_hanning_contracciones, label='Señal Filtrada con Ventana Hanning en cada contracción', color='orange')
plt.title('Señal EMG Filtrada con Ventana Hanning en Cada Contracción (Concatenada)')
plt.xlabel('Tiempo (muestras)')
plt.ylabel('Voltaje (mV)')
plt.grid(True)
plt.legend()

plt.show()


#TRANSFORMADA DE FOURIER A LA SEÑAL CON AVENTANAMIENTO:

    
for i, contraccion_hanning in enumerate(contracciones_filtradas_hanning):
    frecuencia = np.fft.fftfreq(len(contraccion_hanning), 1 / Fs)  
    transformada = np.fft.fft(contraccion_hanning) 
    
    # Magnitud de la Transformada de Fourier
    magnitude = np.abs(transformada)
    
    # Frecuencias positivas
    freqs_pos = frecuencia[:len(frecuencia)//2]
    mag_pos = magnitude[:len(magnitude)//2]

    # Cálculo de la frecuencia dominante
    freq_dominante = freqs_pos[np.argmax(mag_pos)]
    
    # Cálculo de la frecuencia media 
    freq_media = np.sum(freqs_pos * mag_pos) / np.sum(mag_pos)
    
    # Cálculo de la frecuencia mediana
    freq_mediana = np.median(freqs_pos)
    
    # Cálculo de la desviación estándar de las frecuencias:
    freq_std = np.sqrt(np.sum(mag_pos * (freqs_pos - freq_media)**2) / np.sum(mag_pos))

    print(f"Contracción {i+1}:")
    print(f"  Frecuencia dominante: {freq_dominante:.2f} Hz")
    print(f"  Frecuencia media: {freq_media:.2f} Hz")
    print(f"  Frecuencia mediana: {freq_mediana:.2f} Hz")
    print(f"  Desviación estándar de las frecuencias: {freq_std:.2f} Hz")
    
    # Gráfico de la magnitud de la Transformada de Fourier para cada contracción
    plt.figure(figsize=(20, 6))
    plt.plot(freqs_pos, mag_pos, color='purple')
    plt.title(f'Transformada de Fourier - Contracción {i+1}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.grid(True)
    plt.show()


#TEST DE MEDIAS:


# Obtener la magnitud de la Transformada de Fourier para la primera y última contracción
mag_primera = np.abs(np.fft.fft(contracciones_filtradas_hanning[0])[:len(freqs_pos)])
mag_ultima = np.abs(np.fft.fft(contracciones_filtradas_hanning[-1])[:len(freqs_pos)])

# Calcular la frecuencia media para la primera y última contracción (ponderada por la magnitud)
freq_media_primera = np.sum(freqs_pos * mag_primera) / np.sum(mag_primera)
freq_media_ultima = np.sum(freqs_pos * mag_ultima) / np.sum(mag_ultima)

# Realizar el test t de muestras independientes usando las magnitudes de la FFT
t_stat, p_valor = stats.ttest_ind(mag_primera, mag_ultima, alternative='greater')

# Mostrar los resultados
print(f"Frecuencia media de la primera contracción: {freq_media_primera:.2f} Hz")
print(f"Frecuencia media de la última contracción: {freq_media_ultima:.2f} Hz")
print(f"Estadístico t: {t_stat:.2f}")
print(f"p-valor: {p_valor:.4f}")

# Interpretación del resultado
alpha = 0.05  # Nivel de significancia (5%)
if p_valor < alpha:
    print("La frecuencia media de la primera contracción es significativamente mayor que la última. Se observa fatiga.")
else:
    print("No hubo un cambio significativo entre la frecuencia media de la primera y la última contracción. No se observa fatiga.")
