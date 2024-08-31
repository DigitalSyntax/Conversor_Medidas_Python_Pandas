# 📏 Conversión de Medidas: Centímetros a Pulgadas
Este repositorio contiene un script en Python que convierte medidas de centímetros a pulgadas utilizando un archivo Excel como fuente de datos. El script lee un archivo Excel con una columna de medidas en centímetros, realiza la conversión a pulgadas y guarda los resultados en un nuevo archivo Excel.

# 🛠️ Funcionalidades
1. Lectura de archivos Excel: El script lee un archivo Excel llamado Muebles_Medidas.xlsx, que contiene una columna de medidas en centímetros.
2. Conversión a pulgadas: Utiliza una función personalizada para convertir las medidas de centímetros a pulgadas (cm / 2.54).
3. Generación de un nuevo archivo Excel: Después de la conversión, se añade una nueva columna con las medidas en pulgadas y se guarda en un archivo llamado Nuevas_Medidas.xlsx.

# ▶️ Ejecución
Para ejecutar el script, asegúrate de tener instalado pandas y de que el archivo Muebles_Medidas.xlsx esté en el mismo directorio que el script. Luego, simplemente ejecuta:

Conversor.Py

El script generará un nuevo archivo Excel llamado Nuevas_Medidas.xlsx con una columna adicional que muestra las medidas en pulgadas.

# 💡 Requisitos
- Python 3.x
- Pandas
- OpenPyXL
  
Instala pandas y OPenPyXL utilizando el archivo Requirements.txt si aún no tienes nada de lo anterior instalado, simplemente ejecuta el siguiente comando en la terminal:


pip install -r requirements.txt 



# 📝 Nota
Este script es útil para cualquier situación en la que necesites convertir medidas de centímetros a pulgadas y trabajar con datos almacenados en un archivo Excel.
