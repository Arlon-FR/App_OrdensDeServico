#Lista de ordens de serviço
ordens_de_servico = [
    {"id": 1, "cliente": "João", "status": "Aberta"},
    {"id": 2, "cliente": "Maria", "status": "Fechada"},
    {"id": 3, "cliente": "Carlos",  "status": "Em andamento"}
]

def buscar_ordem_de_servico(id_busca):
    for ordem in ordens_de_servico:
        if ordem["id"] == id_busca:
            return ordem
    return None

def adicionar_ordem_de_servico(): 
    #Gera um novo ID para a ordem
    novo_id = len(ordens_de_servico) + 1
    nome_cliente = input("Digite o nome do cliente: ")
    status_ordem = input("Digite o status da ordem (Aberta, Fechada, etc.): ")

    # Criar uma nova ordem de serviço (dicionário)
    nova_ordem = {"id": novo_id, "cliente": nome_cliente, "status": status_ordem}

    #Adiionar a lista
    ordens_de_servico.append(nova_ordem)
    print(f"Nova ordem de serviço adicionada: {nova_ordem}")


def atualizar_status_ordem():
    id_busca = int(input("Digite o ID da ordem de serviço que você quer atualizar: "))

    ordem_encontrada = buscar_ordem_de_servico(id_busca)

    if ordem_encontrada:
        novo_status = input(f"Digite um novo status para a ordem {id_busca}: ")
        ordem_encontrada["status"] = novo_status
    
        print(f"Status atualizado: {ordem_encontrada}")
    else:
        print("Ordem de serviço não encontrada")


def main():
    while True:
        print("\nMenu:")
        print("1. Buscar ordem de serviço")
        print("2. Adicionar nova ordem de serviço")
        print("3. Atualizar status de uma ordem de serviço")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            id_busca = int(input("Digite o ID da ordem de serviço que você quer buscar: "))
            ordem_encontrada = buscar_ordem_de_servico(id_busca)
            if ordem_encontrada:
                print(f"Ordem de Serviço encontrada: {ordem_encontrada}")
            else:
                print("Ordem de Serviço não encontrada.")
        
        elif escolha == "2":
            adicionar_ordem_de_servico()
        
        elif escolha == "3":
            atualizar_status_ordem()
        
        elif escolha == "4":
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Chamar a função principal
main()

