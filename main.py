from rich.console import Console
from rich.panel import Panel
from DRE import DREData
from BP import BPData

console = Console()


def main() -> None:
    console.print(Panel.fit("[bold blue]Calculadora DRE e BP[/bold blue]"))

    dre_data = DREData()
    bp_data = BPData(dre_data)

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
    [bold yellow]Receita Operacional Bruta:[/bold yellow] {dre_data.receita_operacional_bruta}
        [green](-) Vendas Canceladas:[/green] {dre_data.vendas_canceladas}
        [green](-) Descontos Concedidos:[/green] {dre_data.descontos_concedidos}
    [bold yellow]Receita Operacional Liquida:[/bold yellow] {dre_data.receita_operacional_liquida}
        [green](-) Custo das Mercadorias Vendidas (CMV):[/green] {dre_data.custo_mercadorias_vendidas}
    [bold yellow]Lucro Bruto:[/bold yellow] {dre_data.lucro_bruto}
        [green](-) Despesas de Vendas:[/green] {dre_data.despesas_vendas}
        [green](-) Despesas Administrativas:[/green] {dre_data.despesas_administrativas}
        [green](-) Despesas Financeiras:[/green] {dre_data.despesas_financeiras}
    [bold yellow]Lucro Operacional:[/bold yellow] {dre_data.lucro_operacional}
    [bold yellow]Lucro Liquido Antes do IR:[/bold yellow] {dre_data.lucro_liquido_antes_ir}
        [green](-) Imposto de Renda (IR):[/green] {dre_data.imposto_renda}
    [bold green]Total (Lucro Liquido):[/bold green] {dre_data.lucro_liquido_apos_ir}
    [bold green]Total de Deducoes:[/bold green] {total_deducoes}
    """
        )
    )

    console.print(
        Panel.fit(
            f"""[bold green]Balanco Patrimonial[/bold green]
    [yellow]Total de Ativos:[/yellow] {bp_data.total_ativos}
    [yellow]Total de Passivos:[/yellow] {bp_data.total_passivos}
    [yellow]Total de Passivos + Capital Social:[/yellow] {bp_data.total_passivos + dre_data.capital_social}
    [bold blue]Balanco (Ativos - (Passivos + Capital Social + Lucro da DRE)):[/bold blue] {bp_data.balanco}
    [bold green]{bp_data.status}[/bold green]"""
        )
    )


if __name__ == "__main__":
    main()
