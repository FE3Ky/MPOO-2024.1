class Endereco:
    def __init__(self, cidade, estado, rua, bairro, cep, numero):
        self.__cidade = cidade
        self.__estado = estado
        self.__rua = rua
        self.__bairro = bairro
        self.__cep = cep
        self.__numero = numero

    def __str__(self) -> str:
        return f"Cidade {self.__cidade} Estado {self.__estado} CEP {self.__cep}\nRua {self.__rua} Bairro {self.__bairro} Numero {self.__numero}"