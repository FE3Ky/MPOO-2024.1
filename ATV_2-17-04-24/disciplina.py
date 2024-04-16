from professor import Professor
from sala import Sala

class Disciplina:
    def __init__(self, nome, codigo, periodo, sigla,  professor:Professor, sala:Sala):
        self.__nome = nome
        self.__codigo = codigo
        self.__periodo = periodo
        self.__sigla = sigla
        self.__professor = professor
        self.__sala = sala

    def __str__(self) -> str:
        return f"Nome: {self.__nome}\nCodigo: {self.__codigo}\nPeriodo: {self.__periodo}\n"\
        f"Sigla: {self.__sigla}\nProfessor: {self.__professor.nome}\nSala {self.__sala}"