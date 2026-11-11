class Assinatura:
    def __init__(self, nome, preco, dia, mes, ano, categoria):
        self.nome = nome
        self.preco = float(preco)
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)
        self.categoria = categoria

    def __str__(self):
        data_formatada = f"{self.dia:02d}/{self.mes:02d}/{self.ano}"
        return f"{self.nome} [{self.categoria}] - R$ {self.preco:.2f} (Vence em {data_formatada})"


class GerenciadorAssinaturas:
    def __init__(self):
        self.assinaturas = []

    def adicionar(self, assinatura):
        self.assinaturas.append(assinatura)
        print(f"Assinatura de '{assinatura.nome}' adicionada com sucesso!")

    def listar_todas(self):
        if not self.assinaturas:
            print("Nenhuma assinatura cadastrada até o momento.")
            return

        print("\n SUAS ASSINATURAS ")
        for sub in self.assinaturas:
            print(f"- {sub}")

    def calcular_total(self):
        total = 0.0
        for sub in self.assinaturas:
            total += sub.preco
        return total

    def exibir_detalhes_gastos(self):
        if not self.assinaturas:
            print("Nenhuma assinatura cadastrada até o momento.")
            return

        print("\n DETALHAMENTO DE GASTOS MENSAIS ")
        for sub in self.assinaturas:
            print(f"- {sub.nome}: R$ {sub.preco:.2f}")

        total = self.calcular_total()
        print(f"\nGasto total mensal: R$ {total:.2f}")

    def filtrar_por_categoria(self, categoria):
        encontradas = []
        for sub in self.assinaturas:
            if sub.categoria.lower() == categoria.lower():
                encontradas.append(sub)
        return encontradas


def menu():
    gerenciador = GerenciadorAssinaturas()

    while True:
        print("\n GERENCIADOR DE ASSINATURAS ")
        print("1. Adicionar assinatura")
        print("2. Listar todas as assinaturas")
        print("3. Ver gasto total detalhado")
        print("4. Filtrar por categoria")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n Nova Assinatura ")
            nome = input("Nome do serviço: ")
            preco = input("Preço mensal: ex(20.39)")
            dia = input("Dia de vencimento: (1-31)")
            mes = input("Mês de vencimento: (1-12)")
            ano = input("Ano de vencimento: ")
            categoria = input("Categoria: ")

            nova_assinatura = Assinatura(nome, preco, dia, mes, ano, categoria)
            gerenciador.adicionar(nova_assinatura)

        elif opcao == "2":
            gerenciador.listar_todas()

        elif opcao == "3":
            gerenciador.exibir_detalhes_gastos()

        elif opcao == "4":
            cat = input("\nDigite a categoria que deseja buscar: ")
            encontradas = gerenciador.filtrar_por_categoria(cat)

            if not encontradas:
                print(f"Nenhuma assinatura encontrada na categoria '{cat}'.")
            else:
                print(f"\nAssinaturas na categoria '{cat}':")
                for sub in encontradas:
                    print(f"- {sub}")

        elif opcao == "0":
            print("\nEncerrando o Gerenciador de Assinaturas. Até logo!")
            break

        else:
            print("Opção inválida! Por favor, escolha um número do menu.")

menu()