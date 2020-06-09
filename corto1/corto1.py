import os 
file= open("collatz.txt","a")


for i in  range(2,512):
    respuesta=[]
    respuesta.append(i)
    j=i
    while j!=1:
        if j%2==0:
            j=j/2
            respuesta.append(j)
        else:
            j=(j*3)+1
            respuesta.append(j)

        if j==1:
            respuesta.append(j)  
    print(respuesta)        

file.close()