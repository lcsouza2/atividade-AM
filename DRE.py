import questionary as qs


def validar_valor(texto):
    try:
        valor = float(texto) if texto else 0.0
        if valor < 0:
            return "O valor nao pode ser negativo."
        return True
    except ValueError:
        return "Por favor, digite um numero valido."


def ler_valor(pergunta: str) -> float:
    resposta = qs.text(pergunta, validate=validar_valor).ask()
    if resposta is None or resposta == "":
        return 0.0
    return float(resposta)


class DREData:
    def __init__(self) -> None:
        self.receita_operacional_bruta = ler_valor("Digite a Receita Operacional Bruta:")
        self.vendas_canceladas = ler_valor("Digite o valor de Vendas Canceladas:")
        self.descontos_concedidos = ler_valor("Digite o valor de Descontos Concedidos:")
        self.custo_mercadorias_vendidas = ler_valor("Digite o valor do Custo das Mercadorias Vendidas (CMV):")
        self.despesas_vendas = ler_valor("Digite o valor de Despesas de Vendas:")
        self.despesas_administrativas = ler_valor("Digite o valor de Despesas Administrativas:")
        self.despesas_financeiras = ler_valor("Digite o valor de Despesas Financeiras:")
        self.imposto_renda = ler_valor("Digite o valor do Imposto de Renda (IR):")
        self.capital_social = ler_valor("Digite o valor do Capital Social:")

        self.receita_operacional_liquida = (
            self.receita_operacional_bruta - self.vendas_canceladas - self.descontos_concedidos
        )
        self.lucro_bruto = self.receita_operacional_liquida - self.custo_mercadorias_vendidas
        self.lucro_operacional = self.lucro_bruto - self.despesas_vendas - self.despesas_administrativas
        self.lucro_liquido_antes_ir = self.lucro_operacional - self.despesas_financeiras
        self.lucro_liquido_apos_ir = self.lucro_liquido_antes_ir - self.imposto_renda
