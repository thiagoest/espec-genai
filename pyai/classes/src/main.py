from universidade.professor_adjunto import ProfessorAdjunto
from universidade.professor_substituto import ProfessorSubstituto
from universidade.pessoa import Pessoa
from universidade.disciplina import Disciplina
#from universidade.conteudo_ministrado import ConteudoMinistrado
#from universidade.professor import Professor


try:
    ps = ProfessorSubstituto("João", 11111111111)
    pa = ProfessorAdjunto("Maria", 22222222222)
    p1 = Pessoa("Thiago", 11111111111)
    #prof1 = Professor("Paulo", 11111111111)
    d1 = Disciplina("Orientação a Objetos", 60, pa)
    d2 = Disciplina("Algoritmos", 60, ps)

    ps.anos_trabalho = 2
    ps.qtde_proj_presquisa = 3

    #print(p1.cpf)
    #print(p1.nome)

    #print(prof1.nome)
    #print(prof1.cpf)
    #print(prof1.salario)
    
    print(d1.nome)
    print(d1.professor.nome)
    print(d1.professor._calcular_bonus())

    print(d2.nome)
    print(d2.professor.nome)
    print(d2.professor._calcular_bonus())

    #d1.adicionar_conteudo_ministrado("Getters e Setters", 1)
    #d1.adicionar_conteudo_ministrado("Classes", 2)
    #d1.adicionar_conteudo_ministrado("Modificadores de Acesso", 1)

except ValueError as e:    
    print("Erro de valor:", e)
except TypeError as e:
    print("Erro de tipo:", e)
except Exception as e:
    print ("Erro genẽrico:", e)


