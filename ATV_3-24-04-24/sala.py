class Sala:
    def __init__(self, bloco, numero, capacidade):
        self.__bloco = bloco
        self.__numero = numero
        self.__capacidade = capacidade

    def __str__(self) -> str:
        return f"Bloco: {self.__bloco} Numero: {self.__numero} Capacidade: {self.__capacidade}"