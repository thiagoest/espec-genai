from universidade.pessoa import Pessoa
from universidade.disciplina import Disciplina


p1 = Pessoa()
p2 = Pessoa("Maria Oliveira", 456)

p1.nome = "João Silva"
d1 = Disciplina("Orientação a Objetos", 60, p1)
d2 = Disciplina("Orientação a Objetos", 60)

d1.exibir_informacoes()
d2.exibir_informacoes()