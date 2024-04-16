from endereco import Endereco

class Professor:
    def __init__(self, nome, cpf, titulacao, cidade, estado, rua, bairro, cep, numero):
        self.__nome = nome
        self.__cpf = cpf
        self.__titulacao = titulacao
        self.__endereco = Endereco(cidade, estado, rua, bairro, cep, numero)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def __str__(self) -> str:
        return f"Nome: {self.__nome}\nCpf: {self.__cpf}\nTitulação: {self.__titulacao}\nEndereço: {self.__endereco}"