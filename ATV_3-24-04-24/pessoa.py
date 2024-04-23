from endereco import Endereco

class Pessoa:
    def __init__(self, nome, cpf, cidade, estado, rua, bairro, cep, numero):
        self._nome = nome
        self._cpf = cpf
        self._endereco = Endereco(cidade, estado, rua, bairro, cep, numero)