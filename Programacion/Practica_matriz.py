def matri_transpuest(A):#Ejercicio 2
    C=[]
    for i in range (len(A)):
        C.append([])
    print(C)

    nuevo_val=0
    for i in range (len(A)):
        for j in range (len(A)):
            nuevo_val=A[j][i] #Si se cambia estos indices se obtierne la matriz transpuesta
            C[i].append(nuevo_val)
    print(C)

matri_transpuest([[1,2,3],[4,5,6],[7,8,9]])

print("_"*20)

def identi(A): #Ejercicio 5
    for i in range(len(A)):
         for j in range (len(A)):
             if i==j and A[i][j]!=1: #Esto indica que si el elemento de la diagonal no es 1, entonces no es una matriz identidad
                 return False
             elif i!=j and A[i][j]!=0:#Esto indica que si el elemento fuera de la diagonal no es 0, entonces no es una matriz identidad
                 return False
    return True
print(identi([[1,0,0],[0,1,0],[0,0,1]]))
print(identi([[1,1,10],[0,1,0],[0,0,1]]))

print("_"*20)

def suma_bords(A):#Ejercicio 6
    suma=0
    for i in range(len(A)):
        for j in range(len(A)):
            if i==j:
              continue
            elif i!=j:
                suma+=A[i][j]
    return suma
print(suma_bords([[1,2,3],[4,5,6],[7,8,9]]))

print("_"*20)

def may_prom(A):#Ejercicio 7
    mayor=A[0][0]
    menor=A[0][0]
    for i in range(len(A)):
        for j in range (len(A)):
            if A[i][j]>mayor:
                mayor=A[i][j]
            if A[i][j]<menor:
                menor=A[i][j]
    print("El numero mas grande en la matriz" , A , "es:",mayor ,"y el menor fue:",menor)

may_prom([[1,2,3],[4,5,6],[7,8,20]])

print("_"*20)

def sum_fila(A): #Ejercicio 3
    suma_fila_max=0
    for i in range(len(A)):
        suma_fils=0
        for j in range(len(A[0])):
            suma_fils+=A[i][j]
    if suma_fils>suma_fila_max:
        suma_fila_max=suma_fils
    suma_max_col=0
    for j in range(len(A[0])):
        suma_col=0
        for i in range(len(A)):
            suma_col=A[i][j]
    if suma_col>suma_max_col:
        suma_max_col=suma_col
    C=[suma_fila_max,suma_max_col]
    return C
A=[[1,2,3],[4,5,6],[7,8,20]]
print(f"La suma maxima de la fila fue: {sum_fila(A)[0]} y la suma maxima de la columna fue: {sum_fila(A)[1]}")

print("_"*20)

def busqueda_elem(matriz,valor): #Ejercicio 4
    valor_encontrado=0
    for i in range(len(matriz)):
       for j in range (len(A[0])):
           if matriz[i][j]==valor:
                valor_encontrado+=1
    return  valor_encontrado
A=[[1,2,3],[4,5,6],[7,5,20]]
print(f"El valor 5 aparece {busqueda_elem(A,5)} veces en la matriz.")

print("_"*20)

def triangu_sup(A):#Ejercicio 9
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]!=0 and i>j: #Si el elemento es diferente de 0 y esta debajo de la diagonal, entonces no es una matriz triangular superior
                return False
    return True
            
A=[[4,2,3],[0,2,6],[0,0,1]]
print(triangu_sup(A))


def busqueda_tesor(A,valor):#Ejercicio 10
    C=[]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==valor:
                C.append((i,j))
    return C

valor=int(input("Ingrese el valor que quiere buscar en la matriz:"))
A=[[4,2,3],[0,2,6],[0,0,1]]
print(f"El valor {valor} se encuentra en las siguientes posiciones: {busqueda_tesor(A,valor)}")

def multiplicacion_matriz(A,B):#Ejercicio 1
    for i in range(len(A)):
        for j in range(len(A[0])):
            if len(A[0])!=len(B):
                return "No se pueden multiplicar las matrices"