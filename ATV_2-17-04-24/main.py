from curso import Curso
from aluno import Aluno
from disciplina import Disciplina
from professor import Professor
from sala import Sala

bsi = Curso(
    "Bacharelado em Sistemas de Informação",
    "BSI1234", "BSI"
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

bsi.matricular_aluno(aluno=aluno)
bsi.cadastrar_professor(professor=pfs1)
bsi.cadastrar_disciplina(disciplina=ip)
bsi.listar_alunos()
bsi.listar_disciplinas()
bsi.listar_professores()