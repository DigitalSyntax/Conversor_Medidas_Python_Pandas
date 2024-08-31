import pandas as pd



def Cm_a_Pulgadas(cm):
    
    return cm / 2.54




# Leer el archivo excel

df = pd.read_excel("Muebles_Medidas.xlsx")


# Añadir una columna al Dataframe que sea de pulgadas y que se rellene con el calculo de 'cm / 2.54'


df["Pulgadas"] = df["Centimetros"].apply(Cm_a_Pulgadas)



df.to_excel("Nuevas_Medidas.xlsx", index=False)


print("Conversion realizada Exitosamente en un archivo llamadado 'Nuevas_Medidas.xlsx' ")






