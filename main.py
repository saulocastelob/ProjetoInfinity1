repositorio = [
    {
        "matricula": 1,
        "nome": "Jonas",
        "idade": 29,
        "nota": 8.7
    }
]
matriculaAtual = 1
# menu de navegação
while True:
    print('--- BEM VINDO AO MENU ---')
    print('1 - Cadastrar aluno')
    print('2 - Listar todos')
    print('3 - Pesquisar aluno')
    print('4 - Editar aluno')
    print('5 - Excluir aluno')
    print('6 - Sair')
    opcao = input('Selecione uma opção: ')

    if opcao == "6":
        print("Voce saiu do sistema...")
        break
    elif opcao == "1":
        print("... CADASTRE ALUNO...")
        matriculaAtual += 1
        nome = input("digite nome do aluno: ") 
        idade = int(input("digite a idade do aluno: "))
        nota = float(input("digite a nota do aluno: "))
        aluno = {
            "matricula": matriculaAtual,
            "nome": nome,
            "idade": idade,
            "nota": nota
        }   
        repositorio.append(aluno)
        print("Aluno cadastrado com sucesso")
    elif opcao == "2":
        print("...ALUNOS MATRICULADOS...")
        for aluno in repositorio:
            print(f"matricula: {aluno['matricula']}")
            print(f"nome: {aluno['nome']}")
            print(f"idade: {aluno['idade']}")
            print(f"nota: {aluno['nota']}")
            print("-"*50)
    elif opcao == "3":
        matricula = int(input("digite a matricula do aluno: "))
        print("-"*50)
        for aluno in repositorio:
            if aluno["matricula"] == matricula:
                print(f"matricula: {aluno['matricula']}")
                print(f"nome: {aluno['nome']}")
                print(f"idade: {aluno['idade']}")
                print(f"nota: {aluno['nota']}")
                break
        else:
            print("aluno nao encontrado")           
    elif opcao == '4':
        matricula = int(input('Digite a matricula: '))
        print('-'*50)
        for aluno in repositorio:
            if aluno['matricula'] == matricula:
                aluno['nome'] = input('Digite o novo nome do aluno: ')
                aluno['idade'] = int(input('Digite a nova idade: '))
                aluno['nota'] = float(input('Digite a nova nota do aluno: '))
                print('Dados alterados com sucesso!')
                break
        else:
            print('Aluno não encontrado!')
    elif opcao == '5':
        matricula = int(input('Digite a matricula do aluno: '))
        print('-'*50)
        for aluno in repositorio:
            if aluno['matricula'] == matricula:
                repositorio.remove(aluno)
                print('Aluno removido com sucesso')
                break
        else:
            print('Aluno não encontrado!')        