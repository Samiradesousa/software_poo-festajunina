from Modelo.nota import Nota

class Jurado:
    # Lista para armazenar todos os jurados 
    jurados = []

    # Método construtor
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
        
    # Método para listar todos os jurados 
    @classmethod
    def listar_jurados(cls):
        return cls.jurados

    # Método para adicionar um novo jurado à lista de jurados
    @classmethod
    def adicionar_jurado(cls, jurado):
        cls.jurados.append(jurado)

    # Método para dar notas
    def atribuir_nota(self, aluno,elegancia, desenvoltura, simpatia, item):
        avaliacao = Nota(elegancia, desenvoltura, simpatia, item)
        aluno.nota.append(avaliacao)

    def dar_notas(self, elegancia, desenvoltura, simpatia, item):
        jurado = Jurado(elegancia, desenvoltura, simpatia, item)
        jurado.dar_nota(jurado)