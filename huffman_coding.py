from heapq import *

class Nodo:
    def __init__(self, valor, izquierda = None, derecha = None):
        self.valor = valor
        self.izquierda: Nodo = izquierda
        self.derecha: Nodo = derecha

    def __lt__(self, other):
        return self.valor[0] < other.valor[0]


def huffman_coding(string):

    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    freq_sort = [Nodo((item[1], item[0])) for item in freq.items()] 
    heapify(freq_sort)

    while len(freq_sort) > 1:
        peque1 = heappop(freq_sort)
        peque2 = heappop(freq_sort)

        raiz = Nodo((peque1.valor[0] + peque2.valor[0], "*"), izquierda=peque1, derecha=peque2)

        heappush(freq_sort, raiz)
        print(f"PADRE: {raiz.valor} H IZQ: {raiz.izquierda.valor} H DER {raiz.derecha.valor}")
    
    return raiz


def DFS(nodo, acumulado = "", tabla_valores = None):
    if tabla_valores is None:
        tabla_valores = {}

    if nodo is None:
        return tabla_valores

    if nodo.izquierda is None and nodo.derecha is None:
        tabla_valores[nodo.valor[1]] = acumulado
        return tabla_valores

    
    DFS(nodo.izquierda, acumulado + "0", tabla_valores)
    DFS(nodo.derecha, acumulado + "1", tabla_valores)

    return tabla_valores


def codificar(mensaje, tabla):
    codigo = ""

    for caracter in mensaje:
        codigo += tabla[caracter]

    return codigo

def decodificar(codigo, raiz):
    resultado = ""
    nodo_actual = raiz

    for bin in codigo:
        if bin == "0":
            nodo_actual = nodo_actual.izquierda

        else:
            nodo_actual = nodo_actual.derecha

        if nodo_actual.izquierda is None and nodo_actual.derecha is None:
            resultado += nodo_actual.valor[1]
            nodo_actual = raiz

    return resultado


string = "BCAADDDCCACACAC"
print("string original:",string)
arbol = huffman_coding(string)
tabla = DFS(arbol)
codigo = codificar(string, tabla)
print("codigo caracter:", tabla)
print("string codificado:", codigo)
str_decode = decodificar(codigo, arbol)
print("decodificado:", str_decode)
