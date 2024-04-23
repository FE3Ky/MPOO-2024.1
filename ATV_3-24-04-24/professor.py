from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, cpf, titulacao, cidade, estado, rua, bairro, cep, numero):
        super().__init__(nome, cpf, cidade, estado, rua, bairro, cep, numero)
        self.__titulacao = titulacao

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    def __str__(self) -> str:
        return f"Nome: {self._nome}\nCpf: {self._cpf}\nTitulação: {self.__titulacao}\nEndereço: {self._endereco}"