from Modelo.alunos import Aluno  # Importa a classe Aluno do módulo aluno
from Modelo.jurados import Jurado  # Importa a classe Jurado do módulo jurado

# Função para cadastrar alunos no sistema.
def cadastrar_alunos():

    while True:
        nome = input("\nDigite o nome do aluno: ")
        turma = input("\nDigite a sala do aluno: ")
        categoria = input("\nDigite a categoria do aluno (1 para Miss ou 2 para Mister): ")

        # Validação da categoria
        while categoria not in ['1', '2']:
            print("\nCategoria inválida. Digite 1 para Miss ou 2 para Mister.")
            categoria = input("\nDigite a categoria do aluno (1 para Miss ou 2 para Mister): ")

        # Convertendo categoria de '1'/'2' para 'Miss'/'Mister'
        if categoria == '1':
            categoria = "Miss"
        elif categoria == '2':
            categoria = "Mister"

        aluno = Aluno(nome, turma, categoria)  # Cria um objeto Aluno
        Aluno.adicionar_aluno(aluno)  # Adiciona o aluno à lista de alunos

        continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

# Função para cadastrar jurados no sistema.
def cadastrar_jurados():
    while True:
        nome = input("\nDigite o nome do jurado: ")
        curso = input("\nDigite o curso do jurado: ")
        
        jurado = Jurado(nome, curso)  # Cria um objeto Jurado
        Jurado.lista_jurados.append(jurado)  # Adiciona o jurado à lista de jurados

        continuar = input("\nDeseja cadastrar outro jurado? (s/n): ").lower()
        if continuar != 's':
            break

# Função para que os jurados atribuam notas aos alunos.
def dar_notas():
    jurados = Jurado.listar_jurados()  # Lista de jurados cadastrados
    alunos = Aluno.listar_alunos()  # Lista de alunos cadastrados

    if not jurados or not alunos:
        print("\nÉ necessário cadastrar ao menos um jurado e um aluno antes de dar notas.")
        return

    for jurado in jurados:
        print(f"\nJurado: {jurado.nome}, Curso: {jurado.curso}")
        for aluno in alunos:
            print(f"\nAluno: {aluno.nome}, Categoria: {aluno.categoria}")
            elegancia = float(input("Nota para Elegância: "))
            desenvoltura = float(input("Nota para Desenvoltura: "))
            simpatia = float(input("Nota para Simpatia: "))
            item = float(input("Nota para Item: "))
            
            # Corrigindo a chamada do método dar_nota
            jurado.dar_nota(aluno, elegancia, desenvoltura, simpatia, item)  # Atribui notas ao aluno pelo jurado

# Função para listar todos os jurados cadastrados junto com as notas que deram.
def listar_jurados_e_notas():
    print("\nJurados e as Notas que Deram: ")
    print(f"{'Nome do Jurado:':<20} | {'Curso:':<20} | {'Aluno:':<20} | {'Elegância:':<10} | {'Desenvoltura:':<15} | {'Simpatia:':<10} | {'Item:':<10} | {'Média:':<10}")
    for jurado in Jurado.listar_jurados():
        for aluno_nome, nota in jurado.notas_dadas.items():
            media = nota.media()
            print(f"{jurado.nome:<20} | {jurado.curso:<20} | {aluno_nome:<20} | {nota.elegancia:<10.2f} | {nota.desenvoltura:<15.2f} | {nota.simpatia:<10.2f} | {nota.item:<10.2f} | {media:<10.2f}")

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
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()