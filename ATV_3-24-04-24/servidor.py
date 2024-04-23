from pessoa import Pessoa

class Servidor(Pessoa):
    def __init__(self, nome, cpf, setor, cidade, estado, rua, bairro, cep, numero):
        super().__init__(nome, cpf, cidade, estado, rua, bairro, cep, numero)
        self._setor = setor
    
    def __str__(self) -> str:
        return f"Nome: {self._nome}\nCpf: {self._cpf}\nSetor: {self._setor}\nEndereço: {self._endereco}"