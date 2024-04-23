from curso import Curso
from aluno import Aluno
from disciplina import Disciplina
from professor import Professor
from sala import Sala
from coordenador import Coordenador
from diretor import Diretor
from servidor import Servidor
from unidade_academica import UnidadeAcademica

diretor = Diretor(
    "José Augusto Rodriges", "222.222.222-22", "Diretoria",
    "Recife", "PE", "Rua da Concordia", "Santo Antonio", 
    "50010-520", "352"
)

unidadeAcademica = UnidadeAcademica(
    "Unidade Academica de PythonLandia", "UAPY", diretor, 
    "Serra Talhada", "PE", "Av. Gregório Ferraz Nogueira",
    "Jose Tome de Souza Ramos", "56909-535", "345"
)

coordenadorBsi  = Coordenador(
    "Felipe Xavier Carvalho", "444.444.444-44", "Doutor em Filosofia",
    "Recife", "PE", "Abadia dos Dourados", "Imbiribeira", "51180-360",
    "123"
)

bsi = Curso(
    "Bacharelado em Sistemas de Informação",
    "BSI1234", "BSI", coordenadorBsi
)

pfs1 = Professor(
    "Carlos Silva", "111.111.111-11", "Professor Mestre",
    "Santa Cruz da Baixa Verde", "PE", "Padre Cícero",
    "Centro", "56895-970", "141"
)

aluno = Aluno(
    "João José Carvalho",
    "000.000.000-00", "123456",
    "Triunfo", "PE", "Joaquim Antas Florentino", 
    "Liberdade", "56870-000", "195"
)

sala1B2 = Sala(
    "2", "1", "30"
)

ip = Disciplina(
    "Introdução a Programação", "IP12", "1 Periodo",
    "IP", pfs1, sala1B2 
)

servidor = Servidor(
    "Analice Pereira Santos", "333.333.333-33", "Administrativo", 
    "Serra Talhada", "PE", "Avenida Luíz Cosme de Magalhães",
    "Tancredo Neves", "56909-302", "899"
)

unidadeAcademica.cadastrar_servidor(servidor)
bsi.matricular_aluno(aluno=aluno)
bsi.cadastrar_professor(professor=pfs1)
bsi.cadastrar_disciplina(disciplina=ip)
unidadeAcademica.cadastrar_curso(bsi)
print(unidadeAcademica)
unidadeAcademica.listar_cursos()
bsi.listar_alunos()
bsi.listar_disciplinas()
bsi.listar_professores()
unidadeAcademica.listar_servidores()