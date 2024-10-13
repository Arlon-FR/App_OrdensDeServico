#Lista de ordens de serviço
ordens_de_servico = []

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
    #Atualiza a Ordem de Serviço pelo ID
    id_busca = int(input("Digite o ID da ordem de serviço que você quer atualizar: "))
    #Encontra a Ordem de Serviço
    ordem_encontrada = buscar_ordem_de_servico(id_busca)

    if ordem_encontrada:
        novo_status = input(f"Digite um novo status para a ordem {id_busca}: ")
        ordem_encontrada["status"] = novo_status
    
        print(f"Status atualizado: {ordem_encontrada}")
    else:
        print("Ordem de serviço não encontrada")

def excluir_ordem_de_Servico():
    id_busca = int(input("Digite o ID da Ordem de Serviço que deseja excluir: "))
    ordem_encontrada = buscar_ordem_de_servico(id_busca)

    if ordem_encontrada: 
        ordens_de_servico.remove(ordem_encontrada)
        print(f"Ordem de serviço {id_busca} excluída com sucesso.")
    else:
        print("Ordem de serviço não encontrada.")


#Direciona para a função escolhida
def main():
    while True:
        print("\nMenu:")
        print("1. Buscar ordem de serviço")
        print("2. Adicionar nova ordem de serviço")
        print("3. Atualizar status de uma ordem de serviço")
        print("4. Excluir ordem de serviço")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            
            case "1":
                id_busca = int(input("Digite o ID da ordem de serviço que você quer buscar: "))
                ordem_encontrada = buscar_ordem_de_servico(id_busca)
                if ordem_encontrada:
                    print(f"Ordem de Serviço encontrada: {ordem_encontrada}")
                else:
                    print("Ordem de Serviço não encontrada.")
            
            case "2":
                adicionar_ordem_de_servico()
            
            case "3":
                atualizar_status_ordem()

            case "4":
                excluir_ordem_de_Servico()
            
            case "5":
                print("Saindo do sistema.")
                break
            
            case _:
                print("Opção inválida. Tente novamente.")


# Chamar a função principal
main()

