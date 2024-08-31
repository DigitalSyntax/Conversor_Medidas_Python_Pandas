import pandas as pd


# Dataframe : es la informacion basica con el nomnre de las piezas y centimetros para poder armar el excel


data = {
   
   "Piezas" : ["Pata", "Tablero", "Puerta", "Estante"],
   "Centimetros" : [40,120,60,75,]  
 }


df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel


df.to_excel("Muebles_Medidas.xlsx", index=False)



