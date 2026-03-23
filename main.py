from rich.console import Console
from rich.panel import Panel
from DRE import DREData
from BP import BPData
from indicadores import Indicadores

console = Console()


def main() -> None:
    console.print(Panel.fit("[bold blue]Calculadora DRE e BP[/bold blue]"))

    dre_data = DREData()
    bp_data = BPData(dre_data)
    indicadores = Indicadores(bp_data)

    total_deducoes = (
        dre_data.vendas_canceladas
        + dre_data.descontos_concedidos
        + dre_data.custo_mercadorias_vendidas
        + dre_data.despesas_vendas
        + dre_data.despesas_administrativas
        + dre_data.despesas_financeiras
        + dre_data.imposto_renda
    )

    console.print(
        Panel.fit(
            f"""[bold green]Demonstracao de Resultados do Exercicio (DRE)[/bold green]
    [bold yellow]Receita Operacional Bruta:[/bold yellow] {dre_data.receita_operacional_bruta:.2f}
        [green](-) Vendas Canceladas:[/green] {dre_data.vendas_canceladas:.2f}
        [green](-) Descontos Concedidos:[/green] {dre_data.descontos_concedidos:.2f}
    [bold yellow]Receita Operacional Liquida:[/bold yellow] {dre_data.receita_operacional_liquida:.2f}
        [green](-) Custo das Mercadorias Vendidas (CMV):[/green] {dre_data.custo_mercadorias_vendidas:.2f}
    [bold yellow]Lucro Bruto:[/bold yellow] {dre_data.lucro_bruto:.2f}
        [green](-) Despesas de Vendas:[/green] {dre_data.despesas_vendas:.2f}
        [green](-) Despesas Administrativas:[/green] {dre_data.despesas_administrativas:.2f}
        [green](-) Despesas Financeiras:[/green] {dre_data.despesas_financeiras:.2f}
    [bold yellow]Lucro Operacional:[/bold yellow] {dre_data.lucro_operacional:.2f}
    [bold yellow]Lucro Liquido Antes do IR:[/bold yellow] {dre_data.lucro_liquido_antes_ir:.2f}
        [green](-) Imposto de Renda (IR):[/green] {dre_data.imposto_renda:.2f}
    [bold green]Total (Lucro Liquido):[/bold green] {dre_data.lucro_liquido_apos_ir:.2f}
    [bold green]Total de Deducoes:[/bold green] {total_deducoes:.2f}
    """
        )
    )

    console.print(
        Panel.fit(
            f"""[bold green]Balanco Patrimonial[/bold green]
    [yellow]Total de Ativos:[/yellow] {bp_data.total_ativos:.2f}
    [yellow]Total de Passivos:[/yellow] {bp_data.total_passivos:.2f}
    [yellow]Total de Passivos + Capital Social:[/yellow] {(bp_data.total_passivos + dre_data.capital_social):.2f}
    [bold blue]Balanco (Ativos - (Passivos + Capital Social + Lucro da DRE)):[/bold blue] {bp_data.balanco:.2f}
    [bold green]{bp_data.status}[/bold green]"""
        )
    )

    console.print(
        Panel.fit(
            f"""[bold green]Indicadores Financeiros[/bold green]
    [yellow]Liquidez Corrente:[/yellow] {indicadores.liquidez_corrente:.2f}
    [yellow]Liquidez Seca:[/yellow] {indicadores.liquidez_seca:.2f}
    [yellow]Giro do Estoque:[/yellow] {indicadores.giro_estoque:.2f}
    [yellow]Endividamento Geral:[/yellow] {indicadores.endividamento_geral:.2f}
    [yellow]Margem Bruta:[/yellow] {indicadores.margem_bruta:.2f}
    [yellow]Margem Operacional:[/yellow] {indicadores.margem_operacional:.2f}
    [yellow]Margem Liquida:[/yellow] {indicadores.margem_liquida:.2f}
    [yellow]Giro do Ativo Total:[/yellow] {indicadores.giro_ativo_total:.2f}

    [yellow]Idade media do estoque (dias):[/yellow] {indicadores.idade_media_estoque:.2f}
    [yellow]Prazo medio de recebimento (dias):[/yellow] {indicadores.prazo_medio_recebimento:.2f}
    [yellow]Prazo medio de pagamento (dias):[/yellow] {indicadores.prazo_medio_pagamento:.2f}"""
        )
    )


if __name__ == "__main__":
    main()
