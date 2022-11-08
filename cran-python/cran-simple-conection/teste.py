class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade


pessoa1 = Pessoa('Albert', 23)


rows, cols = (5, 5) 
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

arr[0][1] = pessoa1
print(arr)

primeira_pessoa = arr[0][1]
Nome = primeira_pessoa.nome

print(Nome)
