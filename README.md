# LABORATORIO 3 PROCESAMIENTO DE SEÑALES
## TABLA DE CONTENIDOS
1. [Objetivo y Metodología del Experimento](#objetivo-y-metodología-del-experimento)
2. [Adquisición de la señal](#adquisición-de-la-señal)
3. [Filtrado de la señal](#filtrado-de-la-señal)
4. [Aplicación de ventanas](#aplicación-de-ventanas)
5. [Análisis espectral](#análisis-espectral)
6. [Análisis De Los Resultados](#análisis-de-resultados)
7. [Aplicación Biomédica](#aplicación-biomédica)
## OBJETIVO Y METODOLOGÍA DEL EXPERIMENTO
En esencia, la presente práctica tiene como objetivo extrapolar la capacidad de medir y explicar una señal EMG, determinando y/o analizando la fatiga muscular a través de la adquisición y procesamiento de dicha señal, empleando técnicas, tales como, aventanamiento y Transformada de Fourier (FFT) para el análisis espectral. La disminución en la capacidad de un músculo para mantener una contracción durante un esfuerzo prolongado (fatiga), se relaciona directamente con cambios en las frecuencias de la señal EMG. En concordancia, el objetivo específico es monitorear cómo el espectro de frecuencias de dicha señal varía en intervalos de tiempo a medida que se aproxima a la fatiga teniendo como referencia la frecuencia mediana. Además de monitorear este cambio, el experimento busca validar la relación entre la frecuencia mediana y la fatiga muscular mediante una prueba de hipótesis que determine si este cambio es estadísticamente significativo.

Para eliminar interferencias y artefactos no deseados, se aplicaron filtros pasaaltos y pasabajos. El filtro pasaaltos fue implementado para eliminar componentes de baja frecuencia, como el ruido de movimiento, mientras que el filtro pasabajos permitió atenuar el ruido de alta frecuencia proveniente de fuentes externas.

La señal filtrada fue segmentada en ventanas temporales utilizando una ventana de Hanning, elegida para minimizar las discontinuidades en los bordes de cada ventana. Además, la ventana de Hanning lleva los valores de la señal a cero en los bordes, lo que suaviza mucho más las transiciones. Esto ayuda a evitar discontinuidades grandes cuando se divide la señal en ventanas. Mientras que, La ventana de Hamming, aunque también suaviza los bordes, no baja completamente a cero en los extremos. Esto puede permitir pequeñas discontinuidades, lo que genera más "ruido" en el análisis espectral.

Se aplicaron ventanas de tamaño de 250 muestras para mantener la continuidad de la señal en el análisis espectral. A continuación, se aplicó la Transformada Rápida de Fourier (FFT) a cada ventana para obtener el espectro de frecuencias en intervalos específicos. El espectro de frecuencias de cada ventana fue analizado para evaluar los cambios en la distribución de energía conforme se aproximaba la fatiga muscular. Particularmente, se observó el comportamiento de la frecuencia mediana, un indicador clave de fatiga.

En el mismo orden de ideas, para verificar si el cambio en la frecuencia mediana fue estadísticamente significativo, se implementó una prueba de hipótesis. Se estableció una hipótesis nula (H0), donde se asumió que no había diferencia significativa en las frecuencias medianas antes y después del inicio de la fatiga, y una hipótesis alternativa (H1), donde se planteó que la frecuencia mediana disminuía significativamente conforme avanzaba el tiempo. Los datos fueron analizados utilizando un test estadístico adecuado (test de medias), con un nivel de significancia de α = 0.05.

## ADQUISICIÓN DE LA SEÑAL 
La señal electromiográfica (EMG) fue adquirida utilizando el sensor AD8232 conectado a un microcontrolador (STM32) donde la señal fue grabada mientras el estudiante realizaba una contracción isométrica del músculo braquioradial haciendo repeticiones con una mancuerna de 5Kg. A lo largo de la toma de datos, se mantuvo la contracción hasta que se evidenciaron signos de fatiga muscular, la señal fue muestreada a una frecuencia de 596 Hz, con una duración total de 10 seg. Para la adquisición se tuvo en cuenta la siguiente configuración: 

<img src="EMG.jpg" alt="Configuración empleada" width="300"/>

Después de haber guardado y procesado la señal, en python se muestra la gráfica capturada con todas sus características, tales como, frecuencia de muestreo, tiempo de muestreo, longitud de la señal, cantidad de contracciones y músculo medido, como se muestra en la siguiente imagen. 

## FILTRADO DE LA SEÑAL 
## APLICACIÓN DE VENTANAS 
## ANÁLISIS ESPECTRAL
## ANÁLISIS DE RESULTADOS
## APLICACIÓN BIOMÉDICA
El presente laboratorio tiene variedad de aplicaciones para la ingeniería biomédica, ya que contribuye al entendimiento de la función muscular y puede ser útil en varias áreas de la salud. Por ejemplo, la fatiga muscular es un fenómeno clave en la rehabilitación de pacientes con lesiones o en proceso de recuperación tras una cirugía,a modo que, los terapeutas pueden ajustar las sesiones de ejercicio de acuerdo con el estado muscular de cada paciente, evitando el sobreesfuerzo. También,  es una herramienta poderosa para diagnosticar enfermedades neuromusculares, como en el caso de la esclerosis lateral amiotrófica o la fatiga crónica (miopatías). 
