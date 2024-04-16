from endereco import Endereco

class Aluno:
    def __init__(self, nome, cpf, matricula, cidade, estado, rua, bairro, cep, numero):
        self.__nome = nome
        self.__cpf = cpf
        self.__matricula = matricula
        self.__endereco = Endereco(cidade, estado, rua, bairro, cep, numero)

    def __str__(self) -> str:
        return f"Nome: {self.__nome}\nCpf: {self.__cpf}\nMatricula: {self.__matricula}\nEndereço: {self.__endereco}"