from endereco import Endereco
from diretor import Diretor
from servidor import Servidor
from curso import Curso

class UnidadeAcademica:
    def __init__(self, nome, sigla, diretor: Diretor, cidade, estado, rua, bairro, cep, numero) -> None:
        self.__nome = nome
        self.__sigla = sigla
        self.__diretor = diretor
        self.__cursos = []
        self.__servidores = []
        self.__endereco = Endereco(cidade, estado, rua, bairro, cep, numero)

    def cadastrar_servidor(self, servidor: Servidor):
        self.__servidores.append(servidor)

    def cadastrar_curso(self, curso: Curso):
        self.__cursos.append(curso)
    
    def listar_servidores(self):
        print("Servidores------------------------------------------")
        for servidor in self.__servidores:
            print(servidor)
            print("")
    
    def listar_cursos(self):
        print("Cursos----------------------------------------------")
        for curso in self.__cursos:
            print(curso)
            print("")
    
    def __str__(self) -> str:
        return f"Nome: {self.__nome}\nSigla: {self.__sigla}\nDiretor: {self.__diretor._nome}\nEndereço: {self.__endereco}\n"