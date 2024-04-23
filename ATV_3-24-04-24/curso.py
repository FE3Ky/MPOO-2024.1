from aluno import Aluno
from disciplina import Disciplina
from professor import Professor
from coordenador import Coordenador

class Curso:
    def __init__(self, nome, codigo, sigla, coordenador: Coordenador):
        self.__nome = nome
        self.__codigo = codigo
        self.__sigla = sigla
        self.__alunos = []
        self.__disciplinas = []
        self.__professores = []
        self.__coordenador = coordenador

    def matricular_aluno(self, aluno:Aluno):
        self.__alunos.append(aluno)

    def cadastrar_disciplina(self, disciplina:Disciplina):
        self.__disciplinas.append(disciplina)

    def cadastrar_professor(self, professor:Professor):
        self.__professores.append(professor)

    def listar_alunos(self):
        print("Alunos------------------------------------------")
        for aluno in self.__alunos:
            print(aluno)
            print("")

    def listar_professores(self):
        print("Professores-------------------------------------")
        for professor in self.__professores:
            print(professor)
            print("")

    def listar_disciplinas(self):
        print("Disciplinas-------------------------------------")
        for disciplina in self.__disciplinas:
            print(disciplina)
            print("")

    def __str__(self) -> str:
        return f"Nome: {self.__nome}\nCodigo: {self.__codigo}\nSigla: {self.__sigla}\nCordenador: {self.__coordenador.nome}\n"