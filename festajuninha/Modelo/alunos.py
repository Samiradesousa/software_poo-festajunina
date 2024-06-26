'''Este software permite que o usuário cadastre os dados de cada aluno participante do concurso de festa junina,
 além de registrar jurados e suas áreas de atuação. Cada jurado pode atribuir notas para as categorias: Elegância,
 Desenvoltura, Simpatia e Item Reciclável, com cada jurado podendo fornecer apenas um voto por aluno. O software
 retorna uma lista que inclui o nome do jurado, os nomes dos alunos que ele avaliou, as notas atribuídas por ele
 para cada aluno e a média das notas dadas pelo jurado '''

class Aluno:
    # Lista para armazenar todos os alunos 
    alunos = []

    # Método construtor
    def __init__(self, nome, turma, categoria):
        self.nome = nome
        self.turma = turma
        self.categoria = categoria
        self.notas = []

    # Método de classe para adicionar um novo aluno à lista de alunos
    @classmethod
    def adicionar_aluno(cls, aluno):
        cls.alunos.append(aluno)

    # Método para adicionar uma nota ao aluno
    def adicionar_nota(self, nota):
        self.notas.append(nota)

    # Método de classe para listar todos os alunos 
    @classmethod
    def listar_alunos(cls):
        return cls.alunos