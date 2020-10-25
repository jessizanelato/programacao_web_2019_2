import sys

def minhaFuncao(x, y, z):
    return (x + y) / z


a = float(sys.argv[1])  # este é um comentário de linha
b = float(sys.argv[2])
c = float(sys.argv[3])

# Python não possui uma definição para comentário de bloco,
# logo utilizam-se vários comentários de linha

result = minhaFuncao(a, b, c)
print(result)

array = [2, 13, 22, None, 8, 1, 14, None, 17]
pivot = 10
esquerda = []
direita = []

for valor in array:
    if valor is None:
        continue    
    elif valor < pivot:
        esquerda.append(valor)
    else:
        direita.append(valor)

print("Direita = " + str(direita))
print("Esquerda = " + str(esquerda))

print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2)))

for i in range(5):
    print("{} {}".format("Item", i))

j = 5
while j > 0:
    print("j = {}".format(j))
    j -= 1

msg = "j é maior que i" if j > i else "i é maior que j"
print(msg)

try:
    x = 1/0
except ZeroDivisionError as err:
    print("Mensagem customizada de erro: {}".format(err))
except:
    print("Erro desconhecido")
    raise
