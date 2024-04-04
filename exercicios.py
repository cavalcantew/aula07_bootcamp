from typing import List

lista = ([1.8, 2.5, 3.0 ])
def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

resultado = calcular_media(lista)
print(resultado)