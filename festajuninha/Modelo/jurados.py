from Modelo.nota import Nota

class Jurado:
    # Lista para armazenar todos os jurados 
    lista_jurados = []

    # Método construtor
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
        self.notas_dadas = {}  # Dicionário para armazenar as notas atribuídas aos alunos

    # Método para adicionar um novo jurado à lista de jurados
    @classmethod
    def adicionar_jurado(cls, jurado):
        cls.lista_jurados.append(jurado)

    # Método para listar todos os jurados 
    @classmethod
    def listar_jurados(cls):
        return cls.lista_jurados

    # Método para dar notas
    def dar_nota(self, aluno, elegancia, desenvoltura, simpatia, item):
        avaliacao = Nota(elegancia, desenvoltura, simpatia, item)
        aluno.adicionar_nota(avaliacao)  # Adiciona a nota ao aluno
        self.notas_dadas[aluno.nome] = avaliacao  # Armazena a nota atribuída ao aluno