from servidor import Servidor

class Diretor(Servidor):
    def __init__(self, nome, cpf, setor, cidade, estado, rua, bairro, cep, numero):
        super().__init__(nome, cpf, setor, cidade, estado, rua, bairro, cep, numero)

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    def __str__(self) -> str:
        return f"Nome: {self._nome}\nCpf: {self._cpf}\nSetor: {self._setor}\nEndereço: {self._endereco}"