#Crear un split()
def mysplit(strng):
    lista=[]
    palabra=""
    for letra in strng+" ":
        
        if letra !=' ':
            palabra +=letra
        
        
        elif palabra != "": # Solo añade si hay contenido
            lista.append(palabra)
            palabra = ""
    
    return lista        

print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
