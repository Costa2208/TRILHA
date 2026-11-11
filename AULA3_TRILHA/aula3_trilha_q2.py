class Funcionario:

    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = float(salario_base)

    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):

    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = float(bonus_fixo)

    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo


class Vendedor(Funcionario):

    def __init__(self, nome, salario_base, total_vendas, taxa_comissao):
        super().__init__(nome, salario_base)
        self.total_vendas = float(total_vendas)
        self.taxa_comissao = float(
            taxa_comissao
        )  

    def calcular_salario(self):
        comissao = self.total_vendas * self.taxa_comissao
        return self.salario_base + comissao


if __name__ == "__main__":
    func = Funcionario("Carlos", 3000.0)

    gerente = Gerente("Ana", 5000.0, 1500.0)

    vendedor = Vendedor("Pedro", 2000.0, 50000.0, 0.05)

    print(f"Salário de {func.nome}: R$ {func.calcular_salario():.2f}")
    print(
        f"Salário da Gerente {gerente.nome}: R$ {gerente.calcular_salario():.2f}"
    )
    print(
        f"Salário do Vendedor {vendedor.nome}: R$ {vendedor.calcular_salario():.2f}"
    )