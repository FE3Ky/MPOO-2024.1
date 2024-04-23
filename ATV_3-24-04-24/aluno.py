from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, cidade, estado, rua, bairro, cep, numero):
        super().__init__(nome, cpf, cidade, estado, rua, bairro, cep, numero)
        self.__matricula = matricula

    def __str__(self) -> str:
        return f"Nome: {self._nome}\nCpf: {self._cpf}\nMatricula: {self.__matricula}\nEndereço: {self._endereco}"