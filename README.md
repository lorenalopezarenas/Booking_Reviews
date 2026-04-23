# PROYECTO BOOKING-REVIEWS

## Objetivo del proyecto 🎯

Este proyecto tiene como objetivo analizar el comportamiento de las reservas y cancelaciones hoteleras en Europa y su relación con la satisfacción del cliente, integrando información operativa (reservas) con datos de experiencia (reviews).

A través de un análisis exploratorio de datos (EDA) y visualizaciones en Power BI, se busca:

- Identificar patrones de comportamiento en las reservas (duración, anticipación, tipo de cliente).
- Analizar los factores que influyen en la satisfacción del cliente.
- Estudiar diferencias por tipo de hotel, canal de reserva y segmento de cliente.
- Detectar insights útiles para la optimización de ingresos y experiencia del huésped.

El propósito final es comprender qué variables explican mejor el comportamiento del cliente y la percepción del servicio en el sector hotelero.

---------------------------------------------------------------------------------------------------------

## Fuentes de datos 📂

Para la realización de este proyecto se han utilizado dos conjuntos de datos relacionados con las reservas y cancelaciones de hoteles y reseñas que han dejado los huéspedes en hoteles europeos:

### Dataset 1: Hotel bookings (hotel_booking.csv)

Contiene información sobre reservas hoteleras, incluyendo:

- Tipo de habitación
- Lead time
- Cancelaciones
- Duración de la estancia
- Tipo de cliente y canal de reserva

### Dataset 2: Hotel reviews (hotel_reviews.csv)

Contiene información sobre la experiencia del cliente:

- Puntuaciones de satisfacción
- Comentarios de los huéspedes
- Metadatos del reviewer

---------------------------------------------------------------------------------------------------------

## Metodología 🧪

El proyecto se ha desarrollado en varias fases:

### 1.Análisis preliminar

### 2. Limpieza y preprocesamiento de datos

- Tratamiento de valores nulos
- Eliminación de variables sin variabilidad
- Unificación de datasets

### 3. Análisis exploratorio (EDA)

- Distribución de variables numéricas y categóricas
- Análisis de outliers y sesgos
- Estudio de correlaciones
- Análisis de comportamiento
- Segmentación por tipo de cliente
- Estudio de duración de estancia y lead time
- Relación entre precio y satisfacción

### 4. Visualización en Power BI

- Dashboard interactivo para exploración de insights
- Análisis de tendencias temporales y operativas

---------------------------------------------------------------------------------------------------------

## Estructura del Proyecto 🗂️

├── data/ # Datos crudos y procesados

├── notebooks/ # Notebooks de Jupyter con el análisis

├── src/ # Archivo de soporte

├── README.md # Descripción del proyecto

├── requirements.txt # Librerías del proyecto

---------------------------------------------------------------------------------------------------------

## Instalación y requisitos 🛠️

Este proyecto usa Python Python 3.14.0 y requiere las siguientes bibliotecas:

pandas
numpy
matplotlib
seaborn

---------------------------------------------------------------------------------------------------------

## Resultados y conclusiones 📊

El análisis muestra que el negocio hotelero está principalmente impulsado por clientes no fidelizados (Transient), captados mayoritariamente a través de agencias de viajes online, lo que genera una alta dependencia de intermediarios y una demanda relativamente volátil. Las estancias se concentran en viajes cortos de 2 a 4 noches y en un perfil muy homogéneo de clientes (principalmente parejas de dos adultos). En términos económicos, el precio medio (ADR) presenta variaciones moderadas, pero sin diferencias estructurales claras, mientras que la satisfacción del cliente se mantiene alta y muy estable, sin relación significativa con el precio ni con la antelación de la reserva. En conjunto, los resultados indican un modelo de negocio rentable pero poco fidelizado, donde el segmento más lucrativo también es el más inestable, lo que sugiere la necesidad de reforzar estrategias de retención y reducir la dependencia de canales externos.

---------------------------------------------------------------------------------------------------------

### Autor ✒️

Lorena López Arenas
