from rich.console import Console
from rich.panel import Panel
import questionary as qs
from DRE import DREData

console = Console()


def validar_valor(texto):
    try:
        valor = float(texto) if texto else 0.0
        if valor < 0:
            return "O valor nao pode ser negativo."
        return True
    except ValueError:
        return "Por favor, digite um numero valido."


def validar_nome(texto):
    if not texto.strip():
        return "O nome nao pode ser vazio."
    return True


def obter_ativo():
    nome = qs.text("Digite o nome do ativo: ", validate=validar_nome).ask()
    if nome is None:
        return None

    valor_txt = qs.text("Digite o valor do ativo: ", validate=validar_valor).ask()
    if valor_txt is None:
        return None

    tipo = qs.select("Selecione o tipo do ativo:", choices=["Ativo Circulante", "Ativo Nao Circulante"]).ask()
    if tipo is None:
        return None

    valor = float(valor_txt) if valor_txt else 0.0
    return {"nome": nome, "valor": valor, "tipo": tipo}


def obter_passivo():
    nome = qs.text("Digite o nome do passivo: ", validate=validar_nome).ask()
    if nome is None:
        return None

    valor_txt = qs.text("Digite o valor do passivo: ", validate=validar_valor).ask()
    if valor_txt is None:
        return None

    tipo = qs.select("Selecione o tipo do passivo:", choices=["Passivo Circulante", "Passivo Nao Circulante"]).ask()
    if tipo is None:
        return None

    valor = float(valor_txt) if valor_txt else 0.0
    return {"nome": nome, "valor": valor, "tipo": tipo}


def calcular_total(lista):
    return sum(item["valor"] for item in lista)


class BPData:
    def __init__(self, dre_data: DREData) -> None:
        self.dre_data = dre_data
        self.lista_ativos = []
        self.lista_passivos = []

        opcao = None
        while opcao != "Sair e Calcular":
            opcao = qs.select(
                "Escolha uma opção:",
                choices=["Adicionar Ativo", "Adicionar Passivo", "Sair e Calcular"],
            ).ask()

            if opcao is None:
                break

            if opcao == "Adicionar Ativo":
                ativo = obter_ativo()
                if ativo is None:
                    break
                self.lista_ativos.append(ativo)
                console.print(
                    Panel.fit(
                        f"[bold green]Ativo Adicionado:[/bold green]\nNome: {ativo['nome']}\nValor: {ativo['valor']}\nTipo: {ativo['tipo']}"
                    )
                )

            elif opcao == "Adicionar Passivo":
                passivo = obter_passivo()
                if passivo is None:
                    break
                self.lista_passivos.append(passivo)
                console.print(
                    Panel.fit(
                        f"[bold red]Passivo Adicionado:[/bold red]\nNome: {passivo['nome']}\nValor: {passivo['valor']}\nTipo: {passivo['tipo']}"
                    )
                )

        self.total_ativos = calcular_total(self.lista_ativos)
        self.total_passivos = calcular_total(self.lista_passivos)
        self.balanco = self.total_ativos - (self.total_passivos + self.dre_data.capital_social + self.dre_data.lucro_liquido_apos_ir)

        if self.balanco == 0:
            self.status = "Balanco Perfeito"
        elif self.balanco > 0:
            self.status = f"Ativos {self.balanco:.2f} Superiores a Passivos + Capital Social"
        else:
            self.status = f"Passivos + Capital Social {abs(self.balanco):.2f} Superiores a Ativos"