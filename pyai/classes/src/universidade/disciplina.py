class Disciplina:
    def __init__(self, nome, carga_horaria = 60, professor = None):
        self.__nome = nome
        if carga_horaria > 0:
            self.__carga_horaria = carga_horaria
        else:
            self.__carga_horaria = -1 #Carga inválida
        self.__professor = professor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        if carga_horaria > 0:
            self.__carga_horaria = carga_horaria
        else:
            self.__carga_horaria = -1 #Carga Inválida

    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    def exibir_informacoes(self):
        print("Disciplina:", self.__nome)
        print("Carga Horária:", self.__carga_horaria)
        if self.__professor is not None:
            print("Professor Responsável:", self.__professor.nome)
        else:
            print("Disciplina sem professor alocado")