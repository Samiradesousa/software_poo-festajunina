from Modelo.alunos import Aluno  # Importa a classe Aluno do módulo aluno
from Modelo.jurados import Jurado  # Importa a classe Jurado do módulo jurado
from Modelo.nota import Nota  # Importa a classe Nota do módulo nota

# Função para cadastrar alunos no sistema.
def cadastrar_alunos():

    while True:
        nome = input("Digite o nome do aluno: ")
        turma = input("Digite a sala do aluno: ")
        categoria = input("Digite a categoria do aluno (Miss ou Mister): ")
        
        aluno = Aluno(nome, turma, categoria)  # Cria um objeto Aluno
        Aluno.adicionar_aluno(aluno)  # Adiciona o aluno à lista de alunos

        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break
# Função para cadastrar jurados no sistema.
def cadastrar_jurados():

    while True:
        nome = input("Digite o nome do jurado: ")
        curso = input("Digite o curso do jurado: ")
        
        jurado = Jurado(nome, curso)  # Cria um objeto Jurado
        Jurado.adicionar_jurado(jurado)  # Adiciona o jurado à lista de jurados

        continuar = input("Deseja cadastrar outro jurado? (s/n): ").lower()
        if continuar != 's':
            break

# Função para que os jurados atribuam notas aos alunos.
def dar_notas():
    
    jurados = Jurado.listar_jurados()  # Lista de jurados cadastrados
    alunos = Aluno.listar_alunos()  # Lista de alunos cadastrados

    if not jurados or not alunos:
        print("É necessário cadastrar ao menos um jurado e um aluno antes de dar notas.")
        return

    for jurado in jurados:
        print(f"\nJurado: {jurado.nome}, Curso: {jurado.curso}")
        for aluno in alunos:
            print(f"\nAluno: {aluno.nome}, Categoria: {aluno.categoria}")
            elegancia = float(input("Nota para Elegância: "))
            desenvoltura = float(input("Nota para Desenvoltura: "))
            simpatia = float(input("Nota para Simpatia: "))
            item = float(input("Nota para Item: "))
            
            jurado.dar_nota(elegancia, desenvoltura, simpatia, item)  # Atribui notas ao aluno pelo jurado

            break

# Função para listar todos os jurados cadastrados junto com as notas que deram.
def listar_jurados_e_notas():
    
    print("\nJurados e as Notas que Deram:")
    for jurado in Jurado.listar_jurados():
        print(jurado)  # Imprime os dados do jurado
        for aluno_nome, nota in jurado.notas_dadas:
            print(f"  Aluno: {aluno_nome}")  # Imprime o nome do aluno
            print(f"    {nota}")  # Imprime as notas dadas pelo jurado
            print(f"    Média das notas: {nota.media()}")  # Imprime a média das notas

# Função principal que controla o menu do sistema.
def main():
    
    while True:
        print("\n*** Bem-vindo ao Concurso de Festa Junina ***\n")
        print("1 - Cadastrar Alunos")
        print("2 - Cadastrar Jurados")
        print("3 - Dar Notas")
        print("4 - Listar Jurados e suas Notas")
        print("5 - Sair\n")

        opcao = input("\nDigite o número referente à sua opção: ")

        if opcao == '1':
            cadastrar_alunos()
        elif opcao == '2':
            cadastrar_jurados()
        elif opcao == '3':
            dar_notas()
        elif opcao == '4':
            listar_jurados_e_notas()
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()