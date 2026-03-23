from BP import BPData


class Indicadores:
    def __init__(self, bp_data: BPData):
        base_dias = 360

        total_ativos_circulantes = sum(
            [i["valor"] for i in bp_data.lista_ativos if i["tipo"] == "Ativo Circulante"]
        )
        total_passivo_circulante = sum(
            [i["valor"] for i in bp_data.lista_passivos if i["tipo"] == "Passivo Circulante"]
        )

        self.liquidez_corrente = (
            total_ativos_circulantes / total_passivo_circulante if total_passivo_circulante != 0 else 0
        )
        self.liquidez_seca = (
            (total_ativos_circulantes - bp_data.estoques) / total_passivo_circulante
            if total_passivo_circulante != 0
            else 0
        )
        self.giro_estoque = (
            bp_data.dre_data.custo_mercadorias_vendidas / bp_data.estoques if bp_data.estoques != 0 else 0
        )
        self.endividamento_geral = bp_data.total_passivos / bp_data.total_ativos if bp_data.total_ativos != 0 else 0
        self.margem_bruta = (
            bp_data.dre_data.lucro_bruto / bp_data.dre_data.receita_operacional_liquida
            if bp_data.dre_data.receita_operacional_liquida != 0
            else 0
        )
        self.margem_operacional = (
            bp_data.dre_data.lucro_operacional / bp_data.dre_data.receita_operacional_liquida
            if bp_data.dre_data.receita_operacional_liquida != 0
            else 0
        )
        self.margem_liquida = (
            bp_data.dre_data.lucro_liquido_apos_ir / bp_data.dre_data.receita_operacional_liquida
            if bp_data.dre_data.receita_operacional_liquida != 0
            else 0
        )
        self.giro_ativo_total = (
            bp_data.dre_data.receita_operacional_liquida / bp_data.total_ativos if bp_data.total_ativos != 0 else 0
        )

        cmv = bp_data.dre_data.custo_mercadorias_vendidas
        rol = bp_data.dre_data.receita_operacional_liquida

        self.idade_media_estoque = (bp_data.estoques / cmv) * base_dias if cmv != 0 else 0

        self.prazo_medio_recebimento = (bp_data.clientes / rol) * base_dias if rol != 0 else 0

        self.prazo_medio_pagamento = (bp_data.fornecedores / cmv) * base_dias if cmv != 0 else 0
