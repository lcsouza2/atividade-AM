from BP import BPData

class Indicadores:
    def __init__(self, bp_data: BPData):

        total_ativos_circulantes = sum([i["valor"] for i in bp_data.lista_ativos if i["tipo"] == "Ativo Circulante"])
        total_passivo_circulante = sum([i["valor"] for i in bp_data.lista_passivos if i["tipo"] == "Passivo Circulante"])
        self.liquidez_corrente = total_ativos_circulantes / total_passivo_circulante if total_passivo_circulante != 0 else 0
        self.liquidez_seca = (total_ativos_circulantes - bp_data.estoques) / total_passivo_circulante if total_passivo_circulante != 0 else 0
        self.endividamento_geral = bp_data.total_passivos / bp_data.total_ativos if bp_data.total_ativos != 0 else 0
        self.margem_bruta = bp_data.dre_data.lucro_bruto / bp_data.dre_data.receita_operacional_liquida if bp_data.dre_data.receita_operacional_liquida != 0 else 0
        self.margem_operacional = bp_data.dre_data.lucro_operacional / bp_data.dre_data.receita_operacional_liquida if bp_data.dre_data.receita_operacional_liquida != 0 else 0
        self.margem_liquida = bp_data.dre_data.lucro_liquido_apos_ir / bp_data.dre_data.receita_operacional_liquida if bp_data.dre_data.receita_operacional_liquida != 0 else 0
        self.giro_ativo_total = bp_data.dre_data.receita_operacional_liquida / bp_data.total_ativos if bp_data.total_ativos != 0 else 0
