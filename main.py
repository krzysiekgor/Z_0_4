import numpy as np

#typ tablicowy iteracyjny
a = np.array([1,2,3])
# print(a)

#typ tablicowy generowany od do, krok. Krok może być float
a= np.arange(1,5,0.5)
# print(a)

#sprawdzenie typów
# print(a.dtype)
# print(type(a))

#kształt tablicy
# print(a.shape)

#wymiar tablicy
# print(a.ndim)

#tablica 2x2
b = np.array([np.arange(2),np.arange(2)])
# print(b)

# print(b.shape)
# print(b.ndim)

#nadajemy typ danych
a = np.array([1,2,3],dtype='float64')

# print(a)
# print(a.dtype)
# print(type(a))
# print(a.shape)
# print(a.ndim)

#domyslnie dtype='float64'
zera = np.zeros((5,5), dtype='int32')
print(zera)

jedynki = np.ones((5,5))
print(jedynki)

#nadaje losowe wartosci
pusta = np.empty((2,2))
print(pusta)

#odwolanie do elementu maciezy
pusta[1][1]=2
print(pusta)

#nadaje 50 wartosci od 1 do 2
a = np.linspace(1,2)
print(a)

#parametr trzeci to ilosc liczb, endpoint czy ma być odstatnia wartość 2
a = np.linspace(1,2,5,endpoint=False)
print(a)


#b = np.indices((5,5))
#print(b[0][1][1])
b,c = np.indices((5,5))
print(b[1][1])

d,e = np.mgrid[0:5,0:5]
print(d)
print(e)

f = np.diag([x for x in range(5)],k=-1)
print(f)


f = np.diag([x for x in range(5)],k=1)
print(f)

g = np.fromiter(range(5),dtype='int32')
print(g)

marcin = b'Marcin'
#lub 2,3. Jeżeli nie można podzielić ciągu na równe wyrazy wywala exception
mar = np.frombuffer(marcin,dtype='S1')
print(mar)

marcin = 'Marcin'
mar_1 = np.array(list(marcin))
print(mar_1)

mar_3 = np.fromiter(marcin,dtype='U1')
print(mar_3)

a = np.ones((2,2))
b= np.ones((2,2))
c = a+b
print(c)

a = np.arange(10)
print(a)

s = slice(2,7,2)
print(a[s])

s = range(2,7,2)
print(a[s])
print(a[2:7:2])
print(a[1:])
print(a[1:5])

a = np.arange(25)
mat = a.reshape((5,5))
print(mat)
print(mat[1:])
print(mat[1:,1:])
print(mat[:,1:2])
print(mat[2:5,1:3])

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
b = a[rows,cols]
print(b)

