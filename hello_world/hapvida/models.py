# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AbsAuditDdl(models.Model):
    data = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    objeto = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=60, blank=True, null=True)
    comando = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abs_audit_ddl'


class AuAcessoTela(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    nm_operador = models.CharField(max_length=8, blank=True, null=True)
    cd_tela = models.CharField(max_length=10, blank=True, null=True)
    cd_dia_semana = models.NullBooleanField()
    qt_hora_inicial = models.IntegerField(blank=True, null=True)
    qt_hora_final = models.IntegerField(blank=True, null=True)
    qt_dias_atras = models.IntegerField(blank=True, null=True)
    qt_hora_limite = models.IntegerField(blank=True, null=True)
    cd_classe = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cod_grupo = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_acesso_tela'


class AuAgendOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    qtd_mat_med_estoq = models.FloatField(blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    prc_mat_med_estoq = models.FloatField(blank=True, null=True)
    cd_agenda = models.FloatField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ordem_prescricao_plano = models.FloatField(blank=True, null=True)
    dt_agenda = models.DateField(blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_dosagem = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_paciente = models.FloatField(blank=True, null=True)
    cd_pessoa_hosp = models.FloatField(blank=True, null=True)
    cd_pessoa_hap = models.FloatField(blank=True, null=True)
    nm_pessoa = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_agend_onco_hist'


class AuAltaAtendimento(models.Model):
    cd_acao = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_causa_obito = models.IntegerField(blank=True, null=True)
    dt_internacao = models.DateField(blank=True, null=True)
    hr_internacao = models.IntegerField(blank=True, null=True)
    dt_alta = models.DateField(blank=True, null=True)
    hr_alta = models.IntegerField(blank=True, null=True)
    cd_alta = models.IntegerField(blank=True, null=True)
    ds_observacoes_medicas = models.CharField(max_length=2000, blank=True, null=True)
    fl_cobrado = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_procedimento_sus = models.CharField(max_length=8, blank=True, null=True)
    cd_grupo_proced_sus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_alta_atendimento'


class AuAlteracaoLaudo(models.Model):
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_alteracao_laudo = models.FloatField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_ordem_alt = models.IntegerField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_profissional_alt = models.IntegerField(blank=True, null=True)
    cd_especialidade = models.FloatField(blank=True, null=True)
    cd_natureza_alt_laudo = models.FloatField(blank=True, null=True)
    ds_motivo_alt_laudo = models.CharField(max_length=100, blank=True, null=True)
    dt_alteracao = models.DateField(blank=True, null=True)
    ds_laudo_ant = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'au_alteracao_laudo'


class AuAmostraRast(models.Model):
    cd_lote = models.FloatField(blank=True, null=True)
    cd_amostra_coleta = models.IntegerField(blank=True, null=True)
    dt_amostra_coleta = models.DateField(blank=True, null=True)
    cd_amostra_lab = models.IntegerField(blank=True, null=True)
    dt_amostra_lab = models.DateField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_amostra_rast'


class AuAnestProcedRealizado(models.Model):
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_ocorrencia = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_profissional = models.FloatField(blank=True, null=True)
    cd_tipo_ato_profissional = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=20, blank=True, null=True)
    cd_senha_autorizacao = models.CharField(max_length=30, blank=True, null=True)
    cd_grupo_produto = models.FloatField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_anest_proced_realizado'


class AuAnoMesPlantao(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    ano_referencia = models.IntegerField(blank=True, null=True)
    mes_referencia = models.IntegerField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_ano_mes_plantao'


class AuAtendimento(models.Model):
    dt_coleta_digital = models.DateField(blank=True, null=True)
    cd_atendimento_origem = models.FloatField(blank=True, null=True)
    fl_gerado_auto = models.CharField(max_length=1, blank=True, null=True)
    fl_diferenca_acomodacao = models.CharField(max_length=1, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    vl_glosa = models.FloatField(blank=True, null=True)
    vl_glosa_analisar = models.FloatField(blank=True, null=True)
    dt_canc_atend = models.DateField(blank=True, null=True)
    cd_diagnostico = models.CharField(max_length=6, blank=True, null=True)
    dt_ent_controladoria = models.DateField(blank=True, null=True)
    dt_ent_faturamento = models.DateField(blank=True, null=True)
    fl_bloqueio = models.CharField(max_length=1, blank=True, null=True)
    dt_bloqueio = models.DateField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_paciente = models.IntegerField(blank=True, null=True)
    cd_motivo_atendimento = models.IntegerField(blank=True, null=True)
    fl_nivel = models.IntegerField(blank=True, null=True)
    dt_atendimento = models.DateField(blank=True, null=True)
    hr_atendimento = models.IntegerField(blank=True, null=True)
    cd_atendimento_mae = models.IntegerField(blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    cd_clinica = models.IntegerField(blank=True, null=True)
    cd_medico_atendente = models.IntegerField(blank=True, null=True)
    cd_medico_acompanha = models.IntegerField(blank=True, null=True)
    cd_encaminha = models.IntegerField(blank=True, null=True)
    cd_tipo_atendimento = models.IntegerField(blank=True, null=True)
    cd_grupo_atendimento = models.IntegerField(blank=True, null=True)
    cd_matricula = models.CharField(max_length=30, blank=True, null=True)
    cd_tipo_documento = models.NullBooleanField()
    cd_condicao_social = models.NullBooleanField()
    cd_estado_paciente = models.NullBooleanField()
    cd_aspecto = models.NullBooleanField()
    cd_procedencia = models.IntegerField(blank=True, null=True)
    cd_natureza_consulta = models.NullBooleanField()
    nm_queixa_principal = models.CharField(max_length=1000, blank=True, null=True)
    fl_toma_antibiotico = models.CharField(max_length=1, blank=True, null=True)
    fl_internacao = models.CharField(max_length=1, blank=True, null=True)
    dt_fim_atendimento = models.DateField(blank=True, null=True)
    hr_fim_atendimento = models.IntegerField(blank=True, null=True)
    qt_peso = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    qt_tamanho = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ds_observacao = models.CharField(max_length=100, blank=True, null=True)
    cd_usuario_digitador = models.CharField(max_length=8, blank=True, null=True)
    nu_pedido_posto = models.IntegerField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_coleta_digital_exame = models.DateField(blank=True, null=True)
    ds_just_cons_retorno = models.CharField(max_length=1000, blank=True, null=True)
    cd_usu_liberou_retorno = models.CharField(max_length=10, blank=True, null=True)
    dt_ent_pront_auditoria = models.DateField(blank=True, null=True)
    dt_dev_pront_pendencia = models.DateField(blank=True, null=True)
    dt_ent_nsala_auditoria = models.DateField(blank=True, null=True)
    cd_usuario_cancelou = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_atendimento'


class AuAtendimentoMovDoc(models.Model):
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_atendimento_mov_doc = models.FloatField(blank=True, null=True)
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_senha_autoriza = models.CharField(max_length=20, blank=True, null=True)
    cd_tipo_documento_escaneavel = models.FloatField(blank=True, null=True)
    nu_documento = models.FloatField(blank=True, null=True)
    ds_arquivo = models.CharField(max_length=30, blank=True, null=True)
    cd_setor_origem = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_destino = models.CharField(max_length=6, blank=True, null=True)
    fl_tipo_envio = models.NullBooleanField()
    fl_obrigatorio = models.NullBooleanField()
    fl_status = models.NullBooleanField()
    dt_instancia = models.DateField(blank=True, null=True)
    cd_processo_doc_atend = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_atendimento_mov_doc'


class AuAutorOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_autorizacao_senha = models.FloatField(blank=True, null=True)
    dt_autorizacao_tratamento = models.DateField(blank=True, null=True)
    nu_item_tratamento = models.FloatField(blank=True, null=True)
    dt_autorizacao = models.DateField(blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_dosagem = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_paciente = models.FloatField(blank=True, null=True)
    cd_pessoa_hosp = models.FloatField(blank=True, null=True)
    cd_pessoa_hap = models.FloatField(blank=True, null=True)
    nm_pessoa = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_estoq = models.FloatField(blank=True, null=True)
    prc_mat_med_estoq = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_autor_onco_hist'


class AuAvaliacaoCid10(models.Model):
    cd_acao = models.NullBooleanField()
    cd_avaliacao = models.IntegerField(blank=True, null=True)
    cd_cid10 = models.CharField(max_length=4, blank=True, null=True)
    cd_formulario_protocolo = models.CharField(max_length=30, blank=True, null=True)
    cd_avaliacao_cid10 = models.FloatField(blank=True, null=True)
    cd_macrodiag_cid10 = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_avaliacao_cid10'


class AuBemPessoa(models.Model):
    cd_pessoa = models.FloatField()
    nu_ordem_bem = models.FloatField()
    cd_acao = models.FloatField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=14, blank=True, null=True)
    ds_bem = models.CharField(max_length=60, blank=True, null=True)
    vl_mercado_bem = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_bem_pessoa'


class AuCertificacaoUnidade(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    dt_operacao = models.DateField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    dt_inicio_certifica = models.DateField(blank=True, null=True)
    nm_operador_audit = models.CharField(max_length=10, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nu_dias = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_certificacao_unidade'


class AuChefiaPlantaoMedicoEspec(models.Model):
    cd_acao = models.NullBooleanField()
    cd_operador_medico = models.CharField(max_length=10, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_local_atendimento = models.IntegerField(blank=True, null=True)
    cd_grupo_atendimento = models.IntegerField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_chefia_plantao_medico_espec'


class AuChequeCaucao(models.Model):
    cd_acao = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_ordem_caucao = models.IntegerField(blank=True, null=True)
    cd_convenio_pagador = models.NullBooleanField()
    dt_paga_caucao = models.DateField(blank=True, null=True)
    cd_caucao = models.IntegerField(blank=True, null=True)
    cd_cobranca = models.CharField(max_length=15, blank=True, null=True)
    fl_cheque = models.CharField(max_length=1, blank=True, null=True)
    cd_banco = models.CharField(max_length=10, blank=True, null=True)
    cd_agencia = models.CharField(max_length=10, blank=True, null=True)
    nu_cheque = models.CharField(max_length=10, blank=True, null=True)
    vl_caucao = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ds_observacao = models.CharField(max_length=200, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_recibo = models.DateField(blank=True, null=True)
    nu_parcelas = models.FloatField(blank=True, null=True)
    cd_bandeira_cartao = models.FloatField(blank=True, null=True)
    cd_forma_pagamento = models.FloatField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_cheque_caucao'


class AuCid10Hosp(models.Model):
    cd_acao = models.NullBooleanField()
    cid10 = models.CharField(max_length=4, blank=True, null=True)
    opc = models.CharField(max_length=1, blank=True, null=True)
    cat = models.CharField(max_length=1, blank=True, null=True)
    subcat = models.CharField(max_length=1, blank=True, null=True)
    descr = models.CharField(max_length=50, blank=True, null=True)
    restrsexo = models.CharField(max_length=1, blank=True, null=True)
    cd_grupo_cid10 = models.CharField(max_length=5, blank=True, null=True)
    cd_subgrupo_cid10 = models.IntegerField(blank=True, null=True)
    cd_categoria_cid10 = models.CharField(max_length=4, blank=True, null=True)
    nm_cid10 = models.CharField(max_length=400, blank=True, null=True)
    fl_uso = models.CharField(max_length=1, blank=True, null=True)
    obs = models.CharField(max_length=4000, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_cid10_hosp'


class AuClasseAcomodacaoConvenio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_plano_convenio = models.IntegerField(blank=True, null=True)
    cd_classe_acomodacao = models.IntegerField(blank=True, null=True)
    fl_pagamento = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_classe_acomodacao_convenio'


class AuClassiPrioridadeExame(models.Model):
    cd_prioridade = models.FloatField(blank=True, null=True)
    ds_prioridade = models.CharField(max_length=300, blank=True, null=True)
    tempo_processo = models.FloatField(blank=True, null=True)
    cd_color = models.CharField(max_length=50, blank=True, null=True)
    cd_risco_associado_emg = models.CharField(max_length=50, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_classi_prioridade_exame'


class AuCobrancaPaciente(models.Model):
    cd_acao = models.NullBooleanField()
    cd_cobranca = models.CharField(max_length=15, blank=True, null=True)
    nu_guia = models.CharField(max_length=15, blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_plano_convenio = models.IntegerField(blank=True, null=True)
    dt_cobranca = models.DateField(blank=True, null=True)
    dt_competencia = models.DateField(blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_final = models.DateField(blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    vl_cobranca = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pc_taxa_servico = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    vl_taxa_servico = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vl_saldo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ds_observacao = models.CharField(max_length=260, blank=True, null=True)
    vl_diaria = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nu_capa_processo = models.FloatField(blank=True, null=True)
    cd_pessoa = models.FloatField(blank=True, null=True)
    nu_remessa = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_sequencia = models.FloatField(blank=True, null=True)
    vl_pacote = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_cobranca_paciente'


class AuComanda(models.Model):
    cd_acao = models.NullBooleanField()
    nu_comanda = models.CharField(max_length=8, blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_ordem_cmd = models.IntegerField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    dt_comanda = models.DateField(blank=True, null=True)
    cd_setor_origem = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_destino = models.CharField(max_length=6, blank=True, null=True)
    fl_requisicao_devolucao = models.NullBooleanField()
    ds_observacao = models.CharField(max_length=2000, blank=True, null=True)
    fl_gera_comanda = models.CharField(max_length=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_ocorrencia_pacote = models.IntegerField(blank=True, null=True)
    cd_profissional = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_comanda'


class AuComandaMatMed(models.Model):
    cd_acao = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_ordem_cmd = models.IntegerField(blank=True, null=True)
    cd_ordem_m = models.IntegerField(blank=True, null=True)
    cd_cobranca = models.CharField(max_length=15, blank=True, null=True)
    cd_mat_med = models.IntegerField(blank=True, null=True)
    cd_convenio_pagador = models.NullBooleanField()
    hr_comanda = models.IntegerField(blank=True, null=True)
    qt_material = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    vl_material = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    qt_entregue = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    vl_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    qt_devolvido = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    fl_sinal = models.CharField(max_length=1, blank=True, null=True)
    qt_material_paga = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    vl_total_pago = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ds_observacao = models.CharField(max_length=120, blank=True, null=True)
    fl_status_pago = models.CharField(max_length=3, blank=True, null=True)
    qt_entregue_real = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cd_natureza_glosa = models.CharField(max_length=2, blank=True, null=True)
    cd_fornecedor = models.BigIntegerField(blank=True, null=True)
    nu_nota_fornecedor = models.BigIntegerField(blank=True, null=True)
    qt_requisicao = models.FloatField(blank=True, null=True)
    cd_item_hapvida = models.CharField(max_length=12, blank=True, null=True)
    vl_item_hap = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fl_tipo_classificacao = models.NullBooleanField()
    cd_ocorrencia_pacote = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_comanda_mat_med'


class AuComandaRestaurante(models.Model):
    cd_acao = models.NullBooleanField()
    nu_comanda_restaurante = models.CharField(max_length=8, blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_tipo_comanda = models.IntegerField(blank=True, null=True)
    dt_comanda = models.DateField(blank=True, null=True)
    hr_comanda = models.IntegerField(blank=True, null=True)
    vl_comanda = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_funcionario = models.IntegerField(blank=True, null=True)
    cd_garcon = models.IntegerField(blank=True, null=True)
    qt_comanda = models.IntegerField(blank=True, null=True)
    cd_setor_atendimento = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_resp_cortesia = models.CharField(max_length=6, blank=True, null=True)
    cd_cobranca = models.CharField(max_length=15, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_comanda_restaurante'


class AuComandaTaxa(models.Model):
    cd_acao = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_ordem_cmd = models.IntegerField(blank=True, null=True)
    cd_ordem_tx = models.IntegerField(blank=True, null=True)
    cd_taxas = models.CharField(max_length=8, blank=True, null=True)
    cd_cobranca = models.CharField(max_length=15, blank=True, null=True)
    cd_convenio_pagador = models.NullBooleanField()
    hr_comanda = models.IntegerField(blank=True, null=True)
    qt_taxa = models.IntegerField(blank=True, null=True)
    vl_taxa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vl_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fl_sinal = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    qt_taxa_paga = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    vl_total_pago = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ds_observacao = models.CharField(max_length=120, blank=True, null=True)
    fl_status_pago = models.CharField(max_length=3, blank=True, null=True)
    cd_natureza_glosa = models.CharField(max_length=2, blank=True, null=True)
    cd_item_hapvida = models.CharField(max_length=12, blank=True, null=True)
    vl_item_hap = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_ocorrencia_pacote = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_comanda_taxa'


class AuComprOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_nota = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    id_ordem_compra = models.FloatField(blank=True, null=True)
    id_pedido_compra = models.FloatField(blank=True, null=True)
    dt_nota = models.DateField(blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_unit = models.FloatField(blank=True, null=True)
    prc_mat_med_unit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_compr_onco_hist'


class AuConfirmaRecebimentoTransf(models.Model):
    cd_confirma_rec = models.IntegerField(blank=True, null=True)
    cd_transferencia_ori = models.IntegerField(blank=True, null=True)
    cd_setor_controle_ori = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_destino_ori = models.CharField(max_length=6, blank=True, null=True)
    dt_emissao_ori = models.DateField(blank=True, null=True)
    cd_transferencia_nova = models.IntegerField(blank=True, null=True)
    cd_setor_controle_nova = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_destino_nova = models.CharField(max_length=6, blank=True, null=True)
    dt_emissao_nova = models.DateField(blank=True, null=True)
    cd_usuario_recebedor_nova = models.CharField(max_length=10, blank=True, null=True)
    cd_usuario_entregador_nova = models.CharField(max_length=10, blank=True, null=True)
    fl_liberado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_confirma_recebimento_transf'


class AuConsigSolicitaItem(models.Model):
    cd_acao = models.NullBooleanField()
    cd_solicitacao = models.IntegerField(blank=True, null=True)
    cd_material = models.IntegerField(blank=True, null=True)
    sequencial = models.IntegerField(blank=True, null=True)
    qt_solicitada = models.IntegerField(blank=True, null=True)
    qt_autorizada = models.IntegerField(blank=True, null=True)
    fl_consig = models.CharField(max_length=1, blank=True, null=True)
    cd_fornec_solicit = models.IntegerField(blank=True, null=True)
    cd_fornec_autoriz = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_consig_solicita_item'


class AuConsigSolicitacao(models.Model):
    cd_acao = models.NullBooleanField()
    cd_solicitacao = models.IntegerField(blank=True, null=True)
    cd_setor_solicitante = models.CharField(max_length=6, blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_profissional = models.IntegerField(blank=True, null=True)
    cd_paciente = models.IntegerField(blank=True, null=True)
    cd_agenda = models.IntegerField(blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    dt_cirurgia = models.DateField(blank=True, null=True)
    hr_cirurgia = models.IntegerField(blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)
    nm_paciente = models.CharField(max_length=45, blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    fl_transferido = models.CharField(max_length=1, blank=True, null=True)
    ds_autorizacao = models.CharField(max_length=25, blank=True, null=True)
    ds_observacao = models.CharField(max_length=240, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_consig_solicitacao'


class AuContaCorrente(models.Model):
    dt_lancamento = models.DateField(blank=True, null=True)
    cd_usuario = models.FloatField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    cd_conta_bancaria = models.FloatField(blank=True, null=True)
    cd_banco = models.CharField(max_length=10, blank=True, null=True)
    cd_agencia = models.CharField(max_length=10, blank=True, null=True)
    cd_conta_corrente = models.CharField(max_length=20, blank=True, null=True)
    cd_tipo_conta_corrente = models.FloatField(blank=True, null=True)
    cd_um_inicial = models.IntegerField(blank=True, null=True)
    dt_saldo_inicial = models.DateField(blank=True, null=True)
    vl_saldo_inicial = models.FloatField(blank=True, null=True)
    cd_um_saldo = models.IntegerField(blank=True, null=True)
    dt_saldo = models.DateField(blank=True, null=True)
    vl_saldo = models.FloatField(blank=True, null=True)
    vl_saldo_inicial_cheque = models.FloatField(blank=True, null=True)
    vl_saldo_cheque = models.FloatField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    fl_financeiro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_conta_corrente'


class AuContaCorrenteCl(models.Model):
    cd_acao = models.NullBooleanField()
    cd_cobranca = models.CharField(max_length=15, blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    dt_movimento = models.DateField(blank=True, null=True)
    cd_tipo_movimento = models.IntegerField(blank=True, null=True)
    vl_movimento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vl_saldo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_conta_corrente_cl'


class AuContatoPessoa(models.Model):
    cd_pessoa = models.FloatField(blank=True, null=True)
    nm_contato_pessoa = models.CharField(max_length=45, blank=True, null=True)
    nr_cargo_contato = models.CharField(max_length=25, blank=True, null=True)
    nu_telefone_contato = models.IntegerField(blank=True, null=True)
    dt_nascimento_contato = models.DateField(blank=True, null=True)
    ds_contato = models.CharField(max_length=25, blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_contato_pessoa'


class AuContribuicaoPrevidencia(models.Model):
    cd_acao = models.NullBooleanField()
    dt_vigencia = models.DateField(blank=True, null=True)
    qt_salarios = models.IntegerField(blank=True, null=True)
    nu_meses_classe = models.IntegerField(blank=True, null=True)
    vl_salario_base = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pc_aliquota = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    vl_contribuicao = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_contribuicao_previdencia'


class AuControlaProdutividade(models.Model):
    cd_produtividade = models.IntegerField(blank=True, null=True)
    mes_ano_referencia = models.DateField(blank=True, null=True)
    dt_processamento = models.DateField(blank=True, null=True)
    vl_total_bruto = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vl_total_desconto = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)
    terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_empresa = models.FloatField(blank=True, null=True)
    dt_ini_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    dt_vencimento_folha = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_controla_produtividade'


class AuControleAcessoVidaImagem(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=20, blank=True, null=True)
    tp_operador = models.FloatField(blank=True, null=True)
    cd_tela = models.CharField(max_length=20, blank=True, null=True)
    dt_registro = models.DateField(blank=True, null=True)
    cd_operador_cadastro = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_controle_acesso_vida_imagem'


class AuConvenio(models.Model):
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_pessoa = models.IntegerField(blank=True, null=True)
    cd_tipo_convenio = models.IntegerField(blank=True, null=True)
    fl_cobra_honorario = models.CharField(max_length=1, blank=True, null=True)
    fl_remessa = models.CharField(max_length=1, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    fl_tipo = models.CharField(max_length=1, blank=True, null=True)
    fl_enviar_titulo_finpac = models.CharField(max_length=1, blank=True, null=True)
    vl_lim_lib_mat_med = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pc_desconto_uco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fl_hr_exp_cons_emerg = models.CharField(max_length=1, blank=True, null=True)
    fl_cbhpm_convenio = models.CharField(max_length=1, blank=True, null=True)
    hr_encerra_atend_ambulat = models.DateField(blank=True, null=True)
    fl_inclui_exame_lab_cta = models.CharField(max_length=1, blank=True, null=True)
    cd_operadora_saude = models.FloatField(blank=True, null=True)
    fl_paga_honorario_esp = models.CharField(max_length=1, blank=True, null=True)
    qtd_max_dias_atend = models.IntegerField(blank=True, null=True)
    cd_mat_geral_tiss = models.FloatField(blank=True, null=True)
    cd_med_geral_tiss = models.FloatField(blank=True, null=True)
    cd_opme_geral_tiss = models.FloatField(blank=True, null=True)
    cd_taxa_geral_tiss = models.FloatField(blank=True, null=True)
    fl_inc_reg_tiss = models.CharField(max_length=1, blank=True, null=True)
    hr_inic_especial = models.IntegerField(blank=True, null=True)
    hr_fim_especial = models.IntegerField(blank=True, null=True)
    fl_dia_enc_especial = models.CharField(max_length=1, blank=True, null=True)
    qt_dias_cons_retorno = models.FloatField(blank=True, null=True)
    nm_path_logotipo = models.CharField(max_length=80, blank=True, null=True)
    ds_resumo_contrato = models.CharField(max_length=1000, blank=True, null=True)
    fl_convenio_pacote_atend = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    fl_realiza_cons_eletiva = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_convenio'


class AuConvenioPagador(models.Model):
    cd_acao = models.NullBooleanField()
    cd_convenio_pagador = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_convenio_base = models.IntegerField(blank=True, null=True)
    cd_plano_base = models.IntegerField(blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_plano = models.IntegerField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    dt_validade = models.DateField(blank=True, null=True)
    cd_tabela_proced = models.IntegerField(blank=True, null=True)
    pc_desconto_proced = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_tabela_taxa = models.IntegerField(blank=True, null=True)
    pc_desconto_taxa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_tabela_mat_med = models.IntegerField(blank=True, null=True)
    pc_desconto_mat_med = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pc_desconto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_tabela_medicamento = models.IntegerField(blank=True, null=True)
    pc_desconto_medicamento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_um_proced = models.IntegerField(blank=True, null=True)
    cd_um_taxa = models.IntegerField(blank=True, null=True)
    cd_um_mat_med = models.IntegerField(blank=True, null=True)
    cd_um_medicamento = models.IntegerField(blank=True, null=True)
    cd_categoria = models.CharField(max_length=1, blank=True, null=True)
    cd_franquia = models.CharField(max_length=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    pc_acrescimo_taxa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pc_acrescimo_mat_med = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pc_acrescimo_medicamento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_convenio_pagador'


class AuCotacao(models.Model):
    cd_acao = models.NullBooleanField()
    cd_cotacao = models.FloatField(blank=True, null=True)
    cd_fornecedor = models.FloatField(blank=True, null=True)
    nm_forma_pagamento = models.CharField(max_length=20, blank=True, null=True)
    cd_condicao_entrega = models.CharField(max_length=3, blank=True, null=True)
    qt_dias_validade = models.IntegerField(blank=True, null=True)
    qt_dias_entrega = models.IntegerField(blank=True, null=True)
    nm_observacao = models.CharField(max_length=60, blank=True, null=True)
    pc_icms = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_cotacao'


class AuDataCheckMedprev(models.Model):
    cd_id = models.FloatField(blank=True, null=True)
    cd_programa = models.FloatField(blank=True, null=True)
    fl_sexo = models.CharField(max_length=2, blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_metodo_realizado = models.FloatField(blank=True, null=True)
    cd_parametro_referencia = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    fl_tipo_valor = models.CharField(max_length=1, blank=True, null=True)
    cd_referencia = models.CharField(max_length=1, blank=True, null=True)
    ds_intervalo1 = models.CharField(max_length=50, blank=True, null=True)
    ds_intervalo2 = models.CharField(max_length=50, blank=True, null=True)
    nu_ig_inicio = models.FloatField(blank=True, null=True)
    nu_ig_fim = models.FloatField(blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_fim = models.DateField(blank=True, null=True)
    cd_ref = models.FloatField(blank=True, null=True)
    cd_proced_param_referencia = models.FloatField(blank=True, null=True)
    fl_ativo = models.CharField(max_length=1, blank=True, null=True)
    qt_idade_inicial = models.FloatField(blank=True, null=True)
    qt_idade_final = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    ds_alterado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_data_check_medprev'


class AuDataCheckUnidade(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    dt_operacao = models.DateField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_ultimo_processamento = models.DateField(blank=True, null=True)
    nu_dias = models.FloatField(blank=True, null=True)
    nm_operador_audit = models.CharField(max_length=10, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_data_check_unidade'


class AuDevolucaoProntuario(models.Model):
    cd_devolucao_prontuario = models.FloatField(blank=True, null=True)
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    dt_envio = models.DateField(blank=True, null=True)
    dt_recebimento = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_tipo_devolucao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_devolucao_prontuario'


class AuDiagnosticoExame(models.Model):
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    nu_seq_diagnostico = models.IntegerField(blank=True, null=True)
    cd_modelo_diagnostico = models.IntegerField(blank=True, null=True)
    ds_diagnostico_exame = models.CharField(max_length=2000, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_diagnostico_exame'


class AuDietaPaciente(models.Model):
    cd_atendimento = models.IntegerField()
    cd_ocorrencia_plano = models.IntegerField()
    cd_ordem_prescricao = models.IntegerField()
    cd_ordem_dieta = models.IntegerField()
    cd_dieta = models.IntegerField()
    dt_prescricao_dieta = models.DateField()
    dt_inicial = models.DateField()
    dt_final = models.DateField(blank=True, null=True)
    cd_medico = models.IntegerField(blank=True, null=True)
    cd_unidade_usual = models.CharField(max_length=2)
    nu_frequencia = models.IntegerField(blank=True, null=True)
    qt_dieta = models.IntegerField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=120, blank=True, null=True)
    cd_tipo_acesso = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    fl_status_uso = models.CharField(max_length=1, blank=True, null=True)
    hr_inicio_uso = models.IntegerField(blank=True, null=True)
    cd_profissional_prescreve = models.IntegerField(blank=True, null=True)
    cd_profissional_valida = models.IntegerField(blank=True, null=True)
    cd_profissional_cancela = models.IntegerField(blank=True, null=True)
    fl_validado = models.CharField(max_length=1, blank=True, null=True)
    fl_impresso = models.CharField(max_length=1, blank=True, null=True)
    fl_bomba_infusao = models.CharField(max_length=1, blank=True, null=True)
    qt_gotejamento = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cd_gotejamento = models.IntegerField(blank=True, null=True)
    qt_tempo_gotej = models.IntegerField(blank=True, null=True)
    cd_unidade_gotej = models.CharField(max_length=2, blank=True, null=True)
    fl_rotina_rg = models.CharField(max_length=1, blank=True, null=True)
    cd_ordem_impressao = models.IntegerField(blank=True, null=True)
    cd_ordem_impressao_item = models.IntegerField(blank=True, null=True)
    dt_impressao = models.DateField(blank=True, null=True)
    cd_profissional_imprime = models.IntegerField(blank=True, null=True)
    dt_hr_suspensao = models.DateField(blank=True, null=True)
    fl_enterofix = models.CharField(max_length=1, blank=True, null=True)
    fl_equipo_bomba = models.CharField(max_length=1, blank=True, null=True)
    id_session = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_acao = models.DateTimeField(blank=True, null=True)
    dt_validacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_dieta_paciente'


class AuDigitalMotivoAutoriza(models.Model):
    ds_motivo_autoriza = models.CharField(max_length=50, blank=True, null=True)
    dt_autoriza = models.DateField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    fl_digital_pendente = models.CharField(max_length=1, blank=True, null=True)
    ds_justificativa = models.CharField(max_length=256, blank=True, null=True)
    nm_autorizador = models.CharField(max_length=10, blank=True, null=True)
    nm_liberador = models.CharField(max_length=10, blank=True, null=True)
    dt_liberacao = models.DateField(blank=True, null=True)
    fl_face_pendente = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_digital_motivo_autoriza'


class AuEmprestimo(models.Model):
    cd_acao = models.NullBooleanField()
    cd_emprestimo = models.IntegerField(blank=True, null=True)
    cd_lancamento = models.IntegerField(blank=True, null=True)
    dt_lancamento = models.DateField(blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    qt_material = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    vl_material = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vl_material_um = models.FloatField(blank=True, null=True)
    nm_mensagem = models.CharField(max_length=60, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_emprestimo'


class AuEmprestimoTroca(models.Model):
    cd_acao = models.NullBooleanField()
    nu_protocolo = models.IntegerField()
    cd_setor_origem = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_destino = models.CharField(max_length=6, blank=True, null=True)
    cd_usuario_origem = models.CharField(max_length=10, blank=True, null=True)
    cd_usuario_destino = models.CharField(max_length=10, blank=True, null=True)
    nm_usuario_destino = models.CharField(max_length=35, blank=True, null=True)
    dt_emprestimo = models.DateField(blank=True, null=True)
    dt_devolucao = models.DateField(blank=True, null=True)
    dt_troca = models.DateField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    ds_observacao = models.CharField(max_length=200, blank=True, null=True)
    fl_situacao = models.CharField(max_length=1, blank=True, null=True)
    cd_fornec_origem = models.FloatField(blank=True, null=True)
    cd_fornec_destino = models.FloatField(blank=True, null=True)
    ds_observacao_dev = models.CharField(max_length=200, blank=True, null=True)
    ds_observacao_troca = models.CharField(max_length=200, blank=True, null=True)
    nm_usuario_origem = models.CharField(max_length=35, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    fl_tipo = models.CharField(max_length=1, blank=True, null=True)
    nu_protocolo_refer = models.IntegerField(blank=True, null=True)
    nm_usuario_autorizador = models.CharField(max_length=30, blank=True, null=True)
    dt_autorizacao = models.DateField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_emprestimo_troca'


class AuEnderecoPessoa(models.Model):
    cd_pessoa = models.FloatField(blank=True, null=True)
    nu_endereco = models.IntegerField(blank=True, null=True)
    cd_cep_endereco = models.CharField(max_length=8, blank=True, null=True)
    nm_cidade_endereco = models.CharField(max_length=60, blank=True, null=True)
    cd_uf_endereco = models.CharField(max_length=2, blank=True, null=True)
    cd_tipo_logradouro = models.CharField(max_length=10, blank=True, null=True)
    nm_rua_endereco = models.CharField(max_length=60, blank=True, null=True)
    nm_bairro_endereco = models.CharField(max_length=60, blank=True, null=True)
    ds_compl_enderero = models.CharField(max_length=60, blank=True, null=True)
    fl_tipo_endereco = models.CharField(max_length=1, blank=True, null=True)
    fl_ender_cobranca = models.CharField(max_length=1, blank=True, null=True)
    nu_telefone = models.CharField(max_length=10, blank=True, null=True)
    nu_ramal = models.CharField(max_length=4, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_endereco_pessoa'


class AuEnvioEmailAutorizacao(models.Model):
    cd_envio_email_autorizacao = models.FloatField(blank=True, null=True)
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_setor = models.FloatField(blank=True, null=True)
    ds_assunto = models.CharField(max_length=100, blank=True, null=True)
    dt_envio = models.DateField(blank=True, null=True)
    ds_corpo_envio = models.CharField(max_length=1000, blank=True, null=True)
    dt_recebimento = models.DateField(blank=True, null=True)
    ds_corpo_recebimento = models.CharField(max_length=1000, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_envio_email_autorizacao'


class AuEspecialidadeProfissional(models.Model):
    cd_profissional = models.IntegerField(blank=True, null=True)
    cd_especialidade = models.IntegerField(blank=True, null=True)
    fl_esp_principal = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_especialidade_profissional'


class AuEstoqFinOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_unid = models.FloatField(blank=True, null=True)
    prc_mat_med_unid = models.FloatField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_setor_controle = models.CharField(max_length=6, blank=True, null=True)
    anomes = models.CharField(max_length=6, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    nm_material = models.CharField(max_length=45, blank=True, null=True)
    qt_estoque_final = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_estoq_fin_onco_hist'


class AuEstoqIniOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_unid = models.FloatField(blank=True, null=True)
    prc_mat_med_unid = models.FloatField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_setor_controle = models.CharField(max_length=6, blank=True, null=True)
    anomes = models.CharField(max_length=6, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    nm_material = models.CharField(max_length=45, blank=True, null=True)
    qt_estoque_inicial = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_estoq_ini_onco_hist'


class AuExameLabApoio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_mnemonico_exame = models.CharField(max_length=20, blank=True, null=True)
    cd_laboratorio_apoio = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    ds_exame = models.CharField(max_length=100, blank=True, null=True)
    ds_origem_admissivel = models.CharField(max_length=60, blank=True, null=True)
    ds_inf_comple = models.CharField(max_length=100, blank=True, null=True)
    fl_em_uso = models.CharField(max_length=1, blank=True, null=True)
    cd_metodo_realizado = models.FloatField(blank=True, null=True)
    fl_libera_bioquimico = models.CharField(max_length=1, blank=True, null=True)
    fl_libera_automatico = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_grupo_alergeno = models.IntegerField(blank=True, null=True)
    cd_perfil = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_exame_lab_apoio'


class AuExameMaterialLabApoio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_laboratorio_apoio = models.IntegerField(blank=True, null=True)
    cd_mnemonico_exame = models.CharField(max_length=20, blank=True, null=True)
    cd_mnemonico_mat = models.CharField(max_length=20, blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    vl_exame = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_exame_material_lab_apoio'


class AuExameSolicitadoSa(models.Model):
    cd_usuario_autorizou = models.CharField(max_length=10, blank=True, null=True)
    ds_just_supervisor = models.CharField(max_length=2000, blank=True, null=True)
    fl_restricao = models.CharField(max_length=1, blank=True, null=True)
    fl_exame_cancelado = models.CharField(max_length=1, blank=True, null=True)
    nu_pedido = models.BigIntegerField(blank=True, null=True)
    dt_pedido = models.DateField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_senha = models.CharField(max_length=20, blank=True, null=True)
    cd_pessoa_solic = models.FloatField(blank=True, null=True)
    fl_exame_setor = models.CharField(max_length=1, blank=True, null=True)
    ds_justificativa = models.CharField(max_length=4000, blank=True, null=True)
    nu_atendimento_hapvida = models.CharField(max_length=14, blank=True, null=True)
    cd_usuario_coletou = models.CharField(max_length=10, blank=True, null=True)
    dt_usuario_coletou = models.DateField(blank=True, null=True)
    cd_restricao = models.FloatField(blank=True, null=True)
    dt_usuario_autorizou = models.DateField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=2000, blank=True, null=True)
    fl_lado_membro = models.CharField(max_length=1, blank=True, null=True)
    cd_senha_master = models.IntegerField(blank=True, null=True)
    cd_exame = models.IntegerField(blank=True, null=True)
    cd_paciente = models.IntegerField(blank=True, null=True)
    dt_atendimento = models.DateField(blank=True, null=True)
    cd_grupo_atendimento = models.IntegerField(blank=True, null=True)
    cd_local_atendimento = models.IntegerField(blank=True, null=True)
    cd_senha_atendimento = models.IntegerField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    qt_exames = models.IntegerField(blank=True, null=True)
    nu_guia = models.CharField(max_length=15, blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)
    dt_importacao = models.DateField(blank=True, null=True)
    fl_exame_impresso = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_prioridade = models.FloatField(blank=True, null=True)
    fl_solicitou_laudo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_exame_solicitado_sa'


class AuExcecaoProdmedProced(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_tipo_produtividade = models.NullBooleanField()
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_tabela_procedimento = models.IntegerField(blank=True, null=True)
    cd_um_proc = models.IntegerField(blank=True, null=True)
    dt_ini_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_op_solicitante = models.CharField(max_length=30, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_excecao_prodmed_proced'


class AuFatOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_estoq = models.FloatField(blank=True, null=True)
    prc_mat_med_estoq = models.FloatField(blank=True, null=True)
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_ocorrencia = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_ordem_cmd = models.FloatField(blank=True, null=True)
    cd_ordem_m = models.FloatField(blank=True, null=True)
    dt_comanda = models.DateField(blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_dosagem = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_paciente = models.FloatField(blank=True, null=True)
    cd_pessoa_hosp = models.FloatField(blank=True, null=True)
    cd_pessoa_hap = models.FloatField(blank=True, null=True)
    nm_pessoa = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_fat_onco_hist'


class AuFatura(models.Model):
    dt_lancamento = models.DateField(blank=True, null=True)
    cd_usuario = models.FloatField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    cd_fatura = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_fatura'


class AuFichaAnestParamAnest(models.Model):
    id_ficha_anest_param_anest_au = models.IntegerField(primary_key=True)
    cd_acao = models.IntegerField()
    dt_audit = models.DateField()
    cd_terminal = models.CharField(max_length=255)
    cd_operador = models.CharField(max_length=255)
    id_ficha_anest_param_anest = models.IntegerField()
    id_ficha_anestesica_app = models.IntegerField()
    nm_ult_operador = models.CharField(max_length=255)
    id_ficha_anestesica_asa = models.IntegerField(blank=True, null=True)
    id_ficha_anest_mallampati = models.IntegerField(blank=True, null=True)
    id_ficha_anest_tipo_anest = models.IntegerField(blank=True, null=True)
    nu_monitorizacao_hora = models.IntegerField(blank=True, null=True)
    nu_monitorizacao_minuto = models.IntegerField(blank=True, null=True)
    nu_monitorizacao_intervalo = models.IntegerField(blank=True, null=True)
    fl_emergencia_urgencia = models.CharField(max_length=1, blank=True, null=True)
    fl_via_aerea_dificil = models.CharField(max_length=1, blank=True, null=True)
    ds_ficha_anestesica = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_ficha_anest_param_anest'


class AuFichaAnestPreAdmissao(models.Model):
    id_ficha_anest_pre_admis_au = models.IntegerField(primary_key=True)
    cd_acao = models.IntegerField()
    dt_audit = models.DateField()
    cd_terminal = models.CharField(max_length=255)
    cd_operador = models.CharField(max_length=255)
    id_ficha_anest_pre_admissao = models.IntegerField()
    id_ficha_anestesica_app = models.IntegerField()
    nm_ult_operador = models.CharField(max_length=255)
    nu_peso = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    nu_altura = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    nu_pa_sistolica = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    nu_pa_diastolica = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    nu_freq_cardiaca = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    nu_freq_respiratoria = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    nu_temperatura = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_ficha_anest_pre_admissao'


class AuFormsReports(models.Model):
    nm_objeto = models.CharField(max_length=20, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    ip_maquina = models.CharField(max_length=60, blank=True, null=True)
    fl_web = models.CharField(max_length=1, blank=True, null=True)
    ds_so = models.CharField(max_length=512, blank=True, null=True)
    ds_username = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_forms_reports'


class AuFormularioAtendimento(models.Model):
    cd_formulario_atendimento = models.FloatField(blank=True, null=True)
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_formulario_t43j5_a = models.FloatField(blank=True, null=True)
    cd_formulario_vigencia = models.FloatField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    ds_observacao = models.CharField(max_length=300, blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)
    dt_formulario = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_tipo_devolucao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_formulario_atendimento'


class AuFormularioT43J5A(models.Model):
    cd_formulario_t43j5_a = models.FloatField(blank=True, null=True)
    ds_formulario_t43j5_a = models.CharField(max_length=300, blank=True, null=True)
    cd_formulario_vigencia = models.FloatField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_formulario_t43j5_a'


class AuFormularioVigencia(models.Model):
    cd_formulario_vigencia = models.FloatField(blank=True, null=True)
    dt_inicio_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_tipo_devolucao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_formulario_vigencia'


class AuGrupoAlergeno(models.Model):
    cd_acao = models.NullBooleanField()
    cd_grupo_alergeno = models.IntegerField(blank=True, null=True)
    nm_grupo_alergeno = models.CharField(max_length=45, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_grupo_alergeno'


class AuGrupoAtendAltoCusto(models.Model):
    cd_acao = models.NullBooleanField()
    cd_local_atendimento = models.IntegerField(blank=True, null=True)
    cd_grupo_atendimento = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_grupo_atend_alto_custo'


class AuGrupoAtendimentoSa(models.Model):
    cd_grupo_atendimento = models.IntegerField(blank=True, null=True)
    cd_local_atendimento = models.IntegerField(blank=True, null=True)
    ds_grupo_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_cor_atendimento = models.IntegerField(blank=True, null=True)
    dt_atualizacao = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=20, blank=True, null=True)
    cd_tipo_atendimento = models.IntegerField(blank=True, null=True)
    cd_clinica = models.IntegerField(blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    nu_idade_min = models.IntegerField(blank=True, null=True)
    nu_idade_max = models.IntegerField(blank=True, null=True)
    cd_grupo_procedimento = models.FloatField(blank=True, null=True)
    cd_setor_grupo = models.CharField(max_length=6, blank=True, null=True)
    qt_atend_hora = models.IntegerField(blank=True, null=True)
    fl_possui_triagem = models.CharField(max_length=1, blank=True, null=True)
    hr_inicio_triagem = models.IntegerField(blank=True, null=True)
    hr_fim_triagem = models.IntegerField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    fl_classe_grupo = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'au_grupo_atendimento_sa'


class AuGrupoFrasco(models.Model):
    cd_acao = models.NullBooleanField()
    cd_grupo_frasco = models.IntegerField(blank=True, null=True)
    nm_grupo_frasco = models.CharField(max_length=45, blank=True, null=True)
    qt_frasco = models.IntegerField(blank=True, null=True)
    qt_amostras = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_grupo_frasco'


class AuGrupoFrascoProcedimento(models.Model):
    cd_acao = models.NullBooleanField()
    cd_grupo_frasco = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    nm_operador = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_grupo_frasco_procedimento'


class AuGrupoProcSalaCtrl(models.Model):
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_grupo_proc_sala_ctrl = models.FloatField(blank=True, null=True)
    cd_grupo_procedimento = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_grupo_proc_sala_ctrl'


class AuGrupoProduto(models.Model):
    cd_acao = models.NullBooleanField()
    cd_grupo_produto = models.IntegerField(blank=True, null=True)
    nm_grupo_produto = models.CharField(max_length=45, blank=True, null=True)
    volume_frasco = models.CharField(max_length=15, blank=True, null=True)
    sigla_setor = models.CharField(max_length=3, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    empresa = models.CharField(max_length=30, blank=True, null=True)
    extensao = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_grupo_produto'


class AuGuia(models.Model):
    fl_tipo_exame = models.FloatField(blank=True, null=True)
    nu_gab = models.CharField(max_length=30, blank=True, null=True)
    fl_tipo_gab = models.CharField(max_length=1, blank=True, null=True)
    cd_restricao_cart_hapvida = models.FloatField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    nu_guia = models.CharField(max_length=15, blank=True, null=True)
    dt_autorizacao_guia = models.DateField(blank=True, null=True)
    qt_dias_autorizado = models.IntegerField(blank=True, null=True)
    cd_convenio_pagador = models.NullBooleanField()
    cd_cobranca = models.CharField(max_length=15, blank=True, null=True)
    cd_pessoa_realiza = models.FloatField(blank=True, null=True)
    cd_ocorrencia_ocupa = models.IntegerField(blank=True, null=True)
    cd_setor_origem = models.CharField(max_length=6, blank=True, null=True)
    cd_ocorrencia_pedido = models.IntegerField(blank=True, null=True)
    fl_realizar = models.CharField(max_length=1, blank=True, null=True)
    fl_day_clinic = models.CharField(max_length=1, blank=True, null=True)
    dt_prorrogacao_negada = models.DateField(blank=True, null=True)
    hr_prorrogacao_negada = models.IntegerField(blank=True, null=True)
    cd_auditor = models.FloatField(blank=True, null=True)
    hr_ini_autorizacao = models.IntegerField(blank=True, null=True)
    dt_registro_guia = models.DateField(blank=True, null=True)
    cd_clinica_citologia = models.FloatField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_guia'


class AuIndHospitalarUnidade(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_unidade = models.FloatField(blank=True, null=True)
    origem = models.FloatField(blank=True, null=True)
    fl_ativo = models.CharField(max_length=1, blank=True, null=True)
    dt_modificacao = models.DateField(blank=True, null=True)
    cd_usuario_modificacao = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_ind_hospitalar_unidade'


class AuIndicadorHospitalar(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nm_relatorio = models.CharField(max_length=20, blank=True, null=True)
    fl_qualiss = models.CharField(max_length=1, blank=True, null=True)
    cd_sigla_indicador = models.CharField(max_length=10, blank=True, null=True)
    cd_tela_inclusao = models.CharField(max_length=16, blank=True, null=True)
    cd_local_indicador = models.FloatField(blank=True, null=True)
    cd_indicador_hospitalar = models.FloatField(blank=True, null=True)
    ds_indicador_hospitalar = models.CharField(max_length=100, blank=True, null=True)
    cd_item_indicador_num = models.CharField(max_length=8, blank=True, null=True)
    cd_item_indicador_den = models.CharField(max_length=8, blank=True, null=True)
    fl_ccih = models.CharField(max_length=1, blank=True, null=True)
    nm_tela = models.CharField(max_length=20, blank=True, null=True)
    multiplicador = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_indicador_hospitalar'


class AuIndicadorHospitalarItem(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_indicador_hospitalar = models.FloatField(blank=True, null=True)
    cd_filial = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade = models.FloatField(blank=True, null=True)
    ano = models.FloatField(blank=True, null=True)
    mes = models.FloatField(blank=True, null=True)
    meta = models.FloatField(blank=True, null=True)
    variacao = models.FloatField(blank=True, null=True)
    dt_modificacao = models.DateField(blank=True, null=True)
    cd_usuario_modificacao = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_indicador_hospitalar_item'


class AuInstrumento(models.Model):
    cd_acao = models.NullBooleanField()
    instrumento = models.CharField(max_length=6, blank=True, null=True)
    nm_instrumento = models.CharField(max_length=40, blank=True, null=True)
    caminho = models.CharField(max_length=255, blank=True, null=True)
    formato_arquivo = models.CharField(max_length=8, blank=True, null=True)
    extensao = models.CharField(max_length=3, blank=True, null=True)
    ultimo_arquivo = models.IntegerField(blank=True, null=True)
    faixa = models.IntegerField(blank=True, null=True)
    diretorio_transferencia = models.CharField(max_length=255, blank=True, null=True)
    fl_libera_automatico = models.CharField(max_length=1, blank=True, null=True)
    ds_diretorio_geracao = models.CharField(max_length=255, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    directories_filial = models.CharField(max_length=30, blank=True, null=True)
    path_filial = models.CharField(max_length=255, blank=True, null=True)
    directories_backuplis = models.CharField(max_length=255, blank=True, null=True)
    fl_job = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    empresa = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_instrumento'


class AuItemAvaliacao(models.Model):
    cd_acao = models.IntegerField(blank=True, null=True)
    cd_avaliacao = models.IntegerField(blank=True, null=True)
    cd_nivel_avaliacao = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    nm_item_avaliacao = models.CharField(max_length=160, blank=True, null=True)
    cd_componente_avaliacao = models.IntegerField(blank=True, null=True)
    cd_avaliacao_referenciada = models.IntegerField(blank=True, null=True)
    ds_formula = models.CharField(max_length=2000, blank=True, null=True)
    fl_tipo_atributo = models.CharField(max_length=20, blank=True, null=True)
    ds_instrucao = models.CharField(max_length=2000, blank=True, null=True)
    nu_ordem_apresentacao = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    id_componente = models.CharField(max_length=2000, blank=True, null=True)
    cd_ordem_pai = models.IntegerField(blank=True, null=True)
    fl_formula = models.CharField(max_length=1, blank=True, null=True)
    fl_tipo_valor = models.CharField(max_length=20, blank=True, null=True)
    cd_tipo_informacao = models.IntegerField(blank=True, null=True)
    ds_item_avaliacao = models.CharField(max_length=240, blank=True, null=True)
    fl_tipo_formula = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_usual = models.CharField(max_length=2, blank=True, null=True)
    ds_valor_parametro = models.CharField(max_length=2000, blank=True, null=True)
    vl_parametro_minimo_h = models.IntegerField(blank=True, null=True)
    vl_parametro_maximo_h = models.IntegerField(blank=True, null=True)
    vl_parametro_minimo_m = models.IntegerField(blank=True, null=True)
    vl_parametro_maximo_m = models.IntegerField(blank=True, null=True)
    vl_parametro_minimo_a = models.IntegerField(blank=True, null=True)
    vl_parametro_maximo_a = models.IntegerField(blank=True, null=True)
    vl_parametro_minimo_c = models.IntegerField(blank=True, null=True)
    vl_parametro_maximo_c = models.IntegerField(blank=True, null=True)
    vl_parametro_minimo_rn = models.IntegerField(blank=True, null=True)
    vl_parametro_maximo_rn = models.IntegerField(blank=True, null=True)
    vl_parametro_minimo_lactente = models.IntegerField(blank=True, null=True)
    vl_parametro_maximo_lactente = models.IntegerField(blank=True, null=True)
    fl_unidade_tempo = models.CharField(max_length=1, blank=True, null=True)
    qt_idade_inicial = models.IntegerField(blank=True, null=True)
    qt_idade_final = models.IntegerField(blank=True, null=True)
    vl_formula = models.CharField(max_length=240, blank=True, null=True)
    qt_decimal = models.NullBooleanField()
    ds_valida_item = models.CharField(max_length=2000, blank=True, null=True)
    ds_query_item = models.CharField(max_length=2000, blank=True, null=True)
    ds_mensagem_item = models.CharField(max_length=500, blank=True, null=True)
    fl_formulario = models.CharField(max_length=1, blank=True, null=True)
    fl_mutiplo_valor = models.CharField(max_length=1, blank=True, null=True)
    cd_grupo_cid10 = models.CharField(max_length=4000, blank=True, null=True)
    cd_subgrupo_cid10 = models.CharField(max_length=4000, blank=True, null=True)
    cd_categoria_cid10 = models.CharField(max_length=4000, blank=True, null=True)
    fl_tipo_grafico = models.CharField(max_length=1, blank=True, null=True)
    cd_grupo_nanda = models.CharField(max_length=4000, blank=True, null=True)
    cd_nanda = models.CharField(max_length=4000, blank=True, null=True)
    fl_resultado_acumulado = models.CharField(max_length=1, blank=True, null=True)
    sinal_balanco = models.CharField(max_length=1, blank=True, null=True)
    nm_formulario = models.CharField(max_length=30, blank=True, null=True)
    ds_ref_retorno_formulario = models.CharField(max_length=60, blank=True, null=True)
    fl_obrigatorio = models.CharField(max_length=1, blank=True, null=True)
    cd_tipo_solicitacao = models.IntegerField(blank=True, null=True)
    cd_aval_referenciada = models.IntegerField(blank=True, null=True)
    fl_tipo_alerta_intervalo = models.NullBooleanField()
    fl_bloqueia_fora_intervalo = models.CharField(max_length=1, blank=True, null=True)
    ds_mensagem_fora_intervalo = models.CharField(max_length=2000, blank=True, null=True)
    fl_herda_valor = models.CharField(max_length=1, blank=True, null=True)
    fl_abrangencia_heranca = models.CharField(max_length=1, blank=True, null=True)
    fl_ocorrencia_heranca = models.CharField(max_length=1, blank=True, null=True)
    ds_sql_exec = models.CharField(max_length=4000, blank=True, null=True)
    fl_sql_exec_acao = models.CharField(max_length=1, blank=True, null=True)
    cd_index_nm = models.IntegerField(blank=True, null=True)
    fl_padrao = models.CharField(max_length=1, blank=True, null=True)
    fl_tipo_aprazamento_padrao = models.CharField(max_length=1, blank=True, null=True)
    qt_frequencia_padrao = models.IntegerField(blank=True, null=True)
    fl_expandir = models.CharField(max_length=1, blank=True, null=True)
    simbolo = models.CharField(max_length=3, blank=True, null=True)
    fl_mostra = models.CharField(max_length=1, blank=True, null=True)
    fl_sql_exec_acao_unit = models.CharField(max_length=1, blank=True, null=True)
    fl_copia = models.CharField(max_length=1, blank=True, null=True)
    fl_realca = models.CharField(max_length=50, blank=True, null=True)
    nm_itens_exclusivos = models.CharField(max_length=50, blank=True, null=True)
    fl_nao_mostrar_result_se_check = models.CharField(max_length=1, blank=True, null=True)
    fl_nao_imprime = models.CharField(max_length=1, blank=True, null=True)
    fl_coluna_matriz = models.CharField(max_length=1, blank=True, null=True)
    fl_obrigatorio_max = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_avaliacao'


class AuItemDevolucao(models.Model):
    cd_acao = models.NullBooleanField()
    cd_devolucao = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    dt_validade = models.DateField(blank=True, null=True)
    qt_material = models.FloatField(blank=True, null=True)
    vl_material = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vl_material_um = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_devolucao'


class AuItemGrupoProcedimento(models.Model):
    cd_acao = models.NullBooleanField()
    cd_grupo_produto = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    abreviatura = models.CharField(max_length=5, blank=True, null=True)
    fl_senha_coletor = models.CharField(max_length=1, blank=True, null=True)
    fl_libera_automatico = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_grupo_procedimento'


class AuItemGrupoProdutoUnid(models.Model):
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    cd_grupo_produto = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    dt_ini_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_grupo_produto_unid'


class AuItemKitAnestesiaLote(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    id_kit_anest = models.CharField(max_length=10, blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_material = models.IntegerField(blank=True, null=True)
    qt_material = models.FloatField(blank=True, null=True)
    cd_lote = models.CharField(max_length=20, blank=True, null=True)
    dt_validade_lote = models.DateField(blank=True, null=True)
    cd_codigo_barra = models.CharField(max_length=3000, blank=True, null=True)
    fl_material_devolvido = models.CharField(max_length=1, blank=True, null=True)
    qtd_material_devolvido = models.FloatField(blank=True, null=True)
    cd_setor_consignado = models.CharField(max_length=6, blank=True, null=True)
    cd_material_original = models.IntegerField(blank=True, null=True)
    qt_material_original = models.FloatField(blank=True, null=True)
    qtd_padrao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_kit_anestesia_lote'


class AuItemMatMed(models.Model):
    cd_mat_med = models.FloatField(blank=True, null=True)
    cd_item_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade = models.CharField(max_length=2, blank=True, null=True)
    qt_unidade = models.FloatField(blank=True, null=True)
    qt_frequencia_uso = models.IntegerField(blank=True, null=True)
    fl_periodo = models.CharField(max_length=1, blank=True, null=True)
    ds_referencia_regra = models.CharField(max_length=120, blank=True, null=True)
    qt_limite_por_prescricao = models.IntegerField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_mat_med'


class AuItemNota(models.Model):
    cd_acao = models.NullBooleanField()
    cd_nota = models.IntegerField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_setor_entrada = models.CharField(max_length=6, blank=True, null=True)
    dt_validade = models.DateField(blank=True, null=True)
    qt_material = models.FloatField(blank=True, null=True)
    vl_material = models.FloatField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    vl_ipi = models.FloatField(blank=True, null=True)
    vl_frete = models.FloatField(blank=True, null=True)
    vl_icms_retido = models.FloatField(blank=True, null=True)
    vl_diferenca_icms = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_nota'


class AuItemPedido(models.Model):
    cd_acao = models.NullBooleanField()
    cd_pedido = models.FloatField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    qt_de_embalagem = models.FloatField(blank=True, null=True)
    qt_por_embalagem = models.FloatField(blank=True, null=True)
    vl_por_embalagem = models.FloatField(blank=True, null=True)
    fl_pedido = models.NullBooleanField()
    qt_saldo_pedido = models.FloatField(blank=True, null=True)
    vl_ipi = models.FloatField(blank=True, null=True)
    qt_material = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_pedido'


class AuItemProdutividadeMedica(models.Model):
    cd_produtividade = models.IntegerField(blank=True, null=True)
    cd_medico = models.FloatField(blank=True, null=True)
    cd_ocorrencia = models.FloatField(blank=True, null=True)
    cd_tipo_produtividade = models.IntegerField(blank=True, null=True)
    cd_grupo = models.IntegerField(blank=True, null=True)
    cd_produto = models.CharField(max_length=8, blank=True, null=True)
    cd_tipo_valor_fixo = models.FloatField(blank=True, null=True)
    qt_exames = models.FloatField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=255, blank=True, null=True)
    vl_movimento = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vl_saldo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cd_setor_origem = models.CharField(max_length=6, blank=True, null=True)
    cd_atendimento_proced = models.IntegerField(blank=True, null=True)
    cd_ocorrencia_proced = models.IntegerField(blank=True, null=True)
    cd_ordem_proced = models.IntegerField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_produtividade_medica'


class AuItemRestaurante(models.Model):
    cd_acao = models.NullBooleanField()
    cd_comanda_restaurante = models.CharField(max_length=8, blank=True, null=True)
    nu_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    vl_comanda = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    qt_comanda = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_item_restaurante'


class AuKitAnestesiaLote(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    id_kit_anest = models.CharField(max_length=10, blank=True, null=True)
    id_kit_cirur = models.FloatField(blank=True, null=True)
    cd_requisicao = models.IntegerField(blank=True, null=True)
    tipo_kit = models.NullBooleanField()
    fl_kit_devolucao = models.CharField(max_length=1, blank=True, null=True)
    id_kit_anest_herdado = models.CharField(max_length=10, blank=True, null=True)
    fl_status = models.NullBooleanField()
    cd_setor_controle = models.CharField(max_length=6, blank=True, null=True)
    dt_menor_validade = models.DateField(blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    cd_agenda = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_pessoa_func_montou = models.FloatField(blank=True, null=True)
    cd_pessoa_func_recebeu_kit = models.FloatField(blank=True, null=True)
    fl_prenota_impressa = models.CharField(max_length=1, blank=True, null=True)
    fl_etiqueta_impressa = models.CharField(max_length=1, blank=True, null=True)
    cd_pessoa_func_devolveu_kit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_kit_anestesia_lote'


class AuLaboratorioApoio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_laboratorio_apoio = models.IntegerField(blank=True, null=True)
    nm_laboratorio_apoio = models.CharField(max_length=50, blank=True, null=True)
    nm_pessoa_contato = models.CharField(max_length=30, blank=True, null=True)
    nr_fone_contato = models.CharField(max_length=20, blank=True, null=True)
    ds_email_contato = models.CharField(max_length=20, blank=True, null=True)
    ds_versao_xml = models.CharField(max_length=1000, blank=True, null=True)
    cd_entidade = models.BigIntegerField(blank=True, null=True)
    ds_chave = models.CharField(max_length=16, blank=True, null=True)
    cd_laboratorio_convenio = models.CharField(max_length=20, blank=True, null=True)
    cd_protocolo_convenio = models.IntegerField(blank=True, null=True)
    ds_diretorio_envio = models.CharField(max_length=1000, blank=True, null=True)
    ds_diretorio_recepcao = models.CharField(max_length=1000, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    cd_profissional = models.IntegerField(blank=True, null=True)
    fl_ativo = models.CharField(max_length=1, blank=True, null=True)
    fl_tipolab = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    empresa = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_laboratorio_apoio'


class AuLaudoExameProcedimento(models.Model):
    cd_acao = models.NullBooleanField()
    cd_procedimento = models.CharField(max_length=8)
    cd_modelo_laudo = models.IntegerField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_laudo_exame_procedimento'


class AuLaudoPaciente(models.Model):
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_modelo_laudo = models.IntegerField(blank=True, null=True)
    ds_laudo_medico = models.TextField(blank=True, null=True)  # This field type is a guess.
    nm_exame = models.CharField(max_length=100, blank=True, null=True)
    cd_natureza_alt_laudo = models.FloatField(blank=True, null=True)
    ds_motivo_alt_laudo = models.CharField(max_length=100, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_medico_unidade = models.FloatField(blank=True, null=True)
    fl_queixa_principal = models.CharField(max_length=1, blank=True, null=True)
    dt_processamento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_laudo_paciente'


class AuLaudoPacienteLibera(models.Model):
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    dt_status = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_laudo_paciente_libera'


class AuLaudoParamFiltro(models.Model):
    fl_habilita_filtro = models.FloatField(blank=True, null=True)
    cd_profissional = models.IntegerField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    dt_inicial = models.DateField(blank=True, null=True)
    dt_final = models.DateField(blank=True, null=True)
    cd_tipo_atendimento = models.CharField(max_length=2, blank=True, null=True)
    fl_cr = models.FloatField(blank=True, null=True)
    fl_mg = models.FloatField(blank=True, null=True)
    fl_ct = models.FloatField(blank=True, null=True)
    fl_mr = models.FloatField(blank=True, null=True)
    fl_us = models.FloatField(blank=True, null=True)
    fl_es = models.FloatField(blank=True, null=True)
    fl_nm = models.FloatField(blank=True, null=True)
    fl_xa = models.FloatField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_laudo_param_filtro'


class AuLeitoAcomodacao(models.Model):
    cd_acao = models.NullBooleanField()
    cd_acomodacao = models.CharField(max_length=6, blank=True, null=True)
    cd_posto = models.CharField(max_length=6, blank=True, null=True)
    cd_classe_acomodacao = models.IntegerField(blank=True, null=True)
    nu_leito = models.IntegerField(blank=True, null=True)
    fl_ocupacao_acomodacao = models.CharField(max_length=1, blank=True, null=True)
    dt_ocupacao = models.DateField(blank=True, null=True)
    hr_ocupacao = models.IntegerField(blank=True, null=True)
    dt_prevista_liberacao = models.DateField(blank=True, null=True)
    hr_prevista_liberacao = models.IntegerField(blank=True, null=True)
    ds_observacoes_medicas = models.CharField(max_length=60, blank=True, null=True)
    cd_status = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_leito_acomodacao'


class AuLocalTotemSa(models.Model):
    ip_maquina = models.CharField(max_length=100, blank=True, null=True)
    cd_local_atendimento = models.FloatField(blank=True, null=True)
    nm_maquina = models.CharField(max_length=40, blank=True, null=True)
    user_totem = models.CharField(max_length=10, blank=True, null=True)
    fl_tipo_impressora = models.FloatField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_local_totem_sa'


class AuLoteLabFechamento(models.Model):
    cd_lote = models.FloatField()
    cd_laboratorio_apoio = models.IntegerField()
    dt_encerramento = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nm_operador_audit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_lote_lab_fechamento'


class AuLoteProtocolo(models.Model):
    cd_lote_protocolo = models.FloatField(blank=True, null=True)
    cd_lote = models.FloatField(blank=True, null=True)
    nu_pedido = models.FloatField(blank=True, null=True)
    dt_pedido = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_lote_protocolo'


class AuLoteRast(models.Model):
    cd_lote = models.FloatField(blank=True, null=True)
    cd_empresa_rast = models.IntegerField(blank=True, null=True)
    cd_funcionario = models.IntegerField(blank=True, null=True)
    nm_funcionario = models.CharField(max_length=45, blank=True, null=True)
    nu_cpf = models.CharField(max_length=20, blank=True, null=True)
    nr_fone_contato = models.CharField(max_length=20, blank=True, null=True)
    dt_saida_lote = models.DateField(blank=True, null=True)
    cd_oper_entrega = models.CharField(max_length=10, blank=True, null=True)
    cd_setor_coleta = models.CharField(max_length=6, blank=True, null=True)
    qt_amostra_entrega = models.IntegerField(blank=True, null=True)
    dt_chegada_lote = models.DateField(blank=True, null=True)
    cd_oper_recebe = models.CharField(max_length=10, blank=True, null=True)
    cd_setor_recebe = models.CharField(max_length=6, blank=True, null=True)
    qt_amostra_recebe = models.IntegerField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    ds_observacao = models.CharField(max_length=1000, blank=True, null=True)
    dt_cancelamento = models.DateField(blank=True, null=True)
    cd_oper_cancela = models.CharField(max_length=10, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_lote_rast'


class AuMacroCid10(models.Model):
    cd_acao = models.NullBooleanField()
    cd_macrodiag_cid10 = models.IntegerField(blank=True, null=True)
    cid10 = models.CharField(max_length=4, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_macro_cid10'


class AuMacrodiagCid10(models.Model):
    cd_acao = models.NullBooleanField()
    cd_macrodiag_cid10 = models.IntegerField(blank=True, null=True)
    nm_macrodiag_cid10 = models.CharField(max_length=100, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_macrodiag_cid10'


class AuManipOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_estoq = models.FloatField(blank=True, null=True)
    prc_mat_med_estoq = models.FloatField(blank=True, null=True)
    cd_requisicao = models.FloatField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_atendimento = models.FloatField(blank=True, null=True)
    nu_comanda = models.CharField(max_length=9, blank=True, null=True)
    dt_manipulacao = models.DateField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_dosagem = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_paciente = models.FloatField(blank=True, null=True)
    cd_pessoa_hosp = models.FloatField(blank=True, null=True)
    cd_pessoa_hap = models.FloatField(blank=True, null=True)
    nm_pessoa = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_manip_onco_hist'


class AuMatMed(models.Model):
    cd_acao = models.NullBooleanField()
    cd_mat_med = models.FloatField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    cd_apresentacao = models.CharField(max_length=4, blank=True, null=True)
    cd_classificacao = models.IntegerField(blank=True, null=True)
    cd_unidade = models.CharField(max_length=2, blank=True, null=True)
    qt_conteudo = models.FloatField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_mat_med'


class AuMatMedImcompGrupoProc(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    cd_param_grupo_proc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_mat_med_imcomp_grupo_proc'


class AuMatMedImcompProcedPed(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    cd_procedimento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_mat_med_imcomp_proced_ped'


class AuMaterialConvenio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_material = models.FloatField(blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_plano_convenio = models.IntegerField(blank=True, null=True)
    fl_pagamento = models.CharField(max_length=1, blank=True, null=True)
    cd_material_convenio = models.FloatField(blank=True, null=True)
    nm_material_convenio = models.CharField(max_length=55, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_material_convenio'


class AuMaterialGasto(models.Model):
    cd_material = models.FloatField(blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    fl_tipo_gasto = models.IntegerField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_material_gasto'


class AuMaterialLabApoio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_mnemonico_mat = models.CharField(max_length=20, blank=True, null=True)
    cd_laboratorio_apoio = models.IntegerField(blank=True, null=True)
    ds_material = models.CharField(max_length=20, blank=True, null=True)
    material_real = models.CharField(max_length=20, blank=True, null=True)
    conservante = models.CharField(max_length=20, blank=True, null=True)
    ds_inf_comple = models.CharField(max_length=60, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_mnemonico_exame = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_material_lab_apoio'


class AuMedicoFilial(models.Model):
    cd_empresa = models.FloatField(blank=True, null=True)
    cd_medico = models.FloatField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_medico_filial'


class AuMedicoFormaPagamento(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_medico_forma_pagamento = models.IntegerField(blank=True, null=True)
    cd_prestador_fisico = models.FloatField(blank=True, null=True)
    cd_prestador_juridico = models.FloatField(blank=True, null=True)
    cd_especialidade = models.IntegerField(blank=True, null=True)
    dt_inicio_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_forma_pagamento_medico = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_operacao = models.DateField(blank=True, null=True)
    id_pessoa_finpac = models.FloatField(blank=True, null=True)
    id_cc_finpac = models.FloatField(blank=True, null=True)
    id_pessoa_sap = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_medico_forma_pagamento'


class AuMetodoProcedimento(models.Model):
    cd_acao = models.NullBooleanField()
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_metodo_realizado = models.IntegerField(blank=True, null=True)
    cd_metodo_usual = models.CharField(max_length=1, blank=True, null=True)
    dt_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_laboratorio_apoio = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_metodo_procedimento'


class AuMetodoRealizadoFilial(models.Model):
    cd_acao = models.NullBooleanField()
    cd_metodo_realizado = models.IntegerField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    fl_ativo = models.CharField(max_length=1, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_modificacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_metodo_realizado_filial'


class AuModeloPlanoTratFilial(models.Model):
    cd_modelo = models.IntegerField()
    cd_ocorrencia_filial = models.IntegerField()
    cd_filial = models.CharField(max_length=3)
    cd_grupo_atendimento = models.IntegerField(blank=True, null=True)
    cd_local_atendimento = models.IntegerField(blank=True, null=True)
    cd_classe_acomodacao = models.IntegerField(blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    fl_visita_obrigatoria = models.CharField(max_length=1, blank=True, null=True)
    fl_obriga_biometria = models.CharField(max_length=1, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=64, blank=True, null=True)
    id_session = models.CharField(max_length=30, blank=True, null=True)
    fl_reconhecimento_facial = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_modelo_plano_trat_filial'


class AuModeloPlanoTratamento(models.Model):
    cd_modelo = models.IntegerField(blank=True, null=True)
    ds_modelo = models.CharField(max_length=1000)
    nu_tempo_estimado = models.IntegerField(blank=True, null=True)
    fl_unidade_tempo = models.CharField(max_length=1, blank=True, null=True)
    ds_tratamento = models.CharField(max_length=1000, blank=True, null=True)
    fl_local_tratamento = models.CharField(max_length=1, blank=True, null=True)
    cd_diagnostico = models.IntegerField(blank=True, null=True)
    dt_ultima_modificacao = models.DateField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=1000, blank=True, null=True)
    cd_cid = models.CharField(max_length=4, blank=True, null=True)
    cd_mnemonico_modelo = models.CharField(max_length=50, blank=True, null=True)
    fl_tipo_modelo = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=64, blank=True, null=True)
    id_session = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_modelo_plano_tratamento'


class AuMovDoc(models.Model):
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_mov_doc = models.FloatField(blank=True, null=True)
    cd_atendimento_mov_doc = models.FloatField(blank=True, null=True)
    cd_tipo_doc_movimentacao = models.FloatField(blank=True, null=True)
    dt_movimentacao = models.DateField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    ds_observacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_mov_doc'


class AuMovimentacaoAntiga(models.Model):
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    lote = models.IntegerField(blank=True, null=True)
    prontuario = models.CharField(max_length=8, blank=True, null=True)
    dt_operacao_ini = models.DateField(blank=True, null=True)
    dt_operacao_fim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_movimentacao_antiga'


class AuMovimentoConta(models.Model):
    dt_lancamento = models.DateField(blank=True, null=True)
    cd_usuario = models.FloatField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    cd_movimento_conta = models.FloatField(blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_um = models.IntegerField(blank=True, null=True)
    vl_movimento = models.FloatField(blank=True, null=True)
    fl_movimento_conta = models.NullBooleanField()
    cd_tipo_transacao_db = models.CharField(max_length=3, blank=True, null=True)
    cd_documento_debito = models.CharField(max_length=15, blank=True, null=True)
    cd_conta_corrente_debito = models.FloatField(blank=True, null=True)
    cd_tipo_transacao_cr = models.CharField(max_length=3, blank=True, null=True)
    cd_documento_credito = models.CharField(max_length=15, blank=True, null=True)
    cd_conta_corrente_credito = models.FloatField(blank=True, null=True)
    cd_autoriza_cheque = models.FloatField(blank=True, null=True)
    dt_estorno = models.DateField(blank=True, null=True)
    fl_status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'au_movimento_conta'


class AuMovimentoTransacao(models.Model):
    dt_lancamento = models.DateField(blank=True, null=True)
    cd_usuario = models.FloatField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    cd_movimento_conta = models.FloatField(blank=True, null=True)
    cd_ordem_transacao = models.FloatField(blank=True, null=True)
    cd_operacao = models.FloatField(blank=True, null=True)
    dt_emissao_documento = models.DateField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    vl_transacao = models.FloatField(blank=True, null=True)
    cd_um_transacao = models.IntegerField(blank=True, null=True)
    fl_lancamento = models.CharField(max_length=1, blank=True, null=True)
    cd_historico_padrao = models.FloatField(blank=True, null=True)
    nm_historico = models.CharField(max_length=120, blank=True, null=True)
    dt_estorno = models.DateField(blank=True, null=True)
    fl_financeiro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_movimento_transacao'


class AuNota(models.Model):
    cd_acao = models.NullBooleanField()
    cd_nota = models.FloatField(blank=True, null=True)
    fl_nivel_atualizacao = models.NullBooleanField()
    dt_saida = models.DateField(blank=True, null=True)
    dt_entrada = models.DateField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_fornecedor = models.FloatField(blank=True, null=True)
    cd_nota_fornecedor = models.FloatField(blank=True, null=True)
    nm_serie = models.CharField(max_length=8, blank=True, null=True)
    cd_especie_nota = models.CharField(max_length=5, blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    vl_total_nota = models.FloatField(blank=True, null=True)
    vl_total_material = models.FloatField(blank=True, null=True)
    vl_base_icms = models.FloatField(blank=True, null=True)
    pc_icms = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    vl_icms = models.FloatField(blank=True, null=True)
    pc_aliquota_estado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    vl_ipi = models.FloatField(blank=True, null=True)
    vl_despesas_acessorias = models.FloatField(blank=True, null=True)
    vl_icms_retido = models.FloatField(blank=True, null=True)
    vl_diferenca_icms = models.FloatField(blank=True, null=True)
    cd_setor_entrada = models.CharField(max_length=6, blank=True, null=True)
    cd_fatura = models.FloatField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=240, blank=True, null=True)
    cd_historico_padrao = models.FloatField(blank=True, null=True)
    nm_historico = models.CharField(max_length=120, blank=True, null=True)
    cd_operacao = models.FloatField(blank=True, null=True)
    vl_um = models.FloatField(blank=True, null=True)
    fl_estoque = models.CharField(max_length=1, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_nota'


class AuObrigacao(models.Model):
    dt_lancamento = models.DateField(blank=True, null=True)
    cd_usuario = models.FloatField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    cd_obrigacao = models.IntegerField(blank=True, null=True)
    cd_cedente_sacado = models.FloatField(blank=True, null=True)
    cd_tipo_obrigacao = models.FloatField(blank=True, null=True)
    cd_banco = models.CharField(max_length=10, blank=True, null=True)
    cd_agencia = models.CharField(max_length=10, blank=True, null=True)
    cd_carteira = models.IntegerField(blank=True, null=True)
    dt_emissao = models.DateField(blank=True, null=True)
    dt_vencimento = models.DateField(blank=True, null=True)
    dt_prevista_liquidacao = models.DateField(blank=True, null=True)
    fl_aceite = models.CharField(max_length=1, blank=True, null=True)
    cd_especie_titulo = models.FloatField(blank=True, null=True)
    fl_financeiro = models.CharField(max_length=1, blank=True, null=True)
    cd_status = models.IntegerField(blank=True, null=True)
    dt_status = models.DateField(blank=True, null=True)
    cd_um = models.IntegerField(blank=True, null=True)
    vl_obrigacao = models.FloatField(blank=True, null=True)
    vl_saldo_obrigacao = models.FloatField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    vl_saldo_pedido = models.FloatField(blank=True, null=True)
    vl_saldo_nota = models.FloatField(blank=True, null=True)
    cd_historico_padrao = models.FloatField(blank=True, null=True)
    nm_historico = models.CharField(max_length=120, blank=True, null=True)
    cd_documento_gerador = models.CharField(max_length=30, blank=True, null=True)
    cd_documento_controle = models.CharField(max_length=30, blank=True, null=True)
    dt_conversao_moeda = models.DateField(blank=True, null=True)
    dt_validade_documento = models.DateField(blank=True, null=True)
    pc_multa_atrazo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    vl_juro_dia = models.FloatField(blank=True, null=True)
    cd_um_correcao = models.IntegerField(blank=True, null=True)
    vl_desconto_antecipacao = models.FloatField(blank=True, null=True)
    dt_desconto_antecipacao = models.DateField(blank=True, null=True)
    cd_autoriza_cheque = models.FloatField(blank=True, null=True)
    vl_despesas_pendentes = models.FloatField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=240, blank=True, null=True)
    nu_remessa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_obrigacao'


class AuOcupacaoAcomodacao(models.Model):
    cd_posto = models.CharField(max_length=6, blank=True, null=True)
    cd_classe_acomodacao = models.IntegerField(blank=True, null=True)
    nu_leito = models.IntegerField(blank=True, null=True)
    dt_ocupacao = models.DateField(blank=True, null=True)
    hr_ocupacao = models.IntegerField(blank=True, null=True)
    dt_prevista_liberacao = models.DateField(blank=True, null=True)
    hr_prevista_liberacao = models.IntegerField(blank=True, null=True)
    dt_liberacao = models.DateField(blank=True, null=True)
    hr_liberacao = models.IntegerField(blank=True, null=True)
    ds_observacoes_medicas = models.CharField(max_length=240, blank=True, null=True)
    fl_atendimento_ocupa = models.CharField(max_length=1, blank=True, null=True)
    fl_diferenca_acomodacao = models.CharField(max_length=1, blank=True, null=True)
    cd_motivo_diferenca_acomod = models.CharField(max_length=1, blank=True, null=True)
    cd_usuario_digitador = models.CharField(max_length=10, blank=True, null=True)
    fl_procedimento = models.CharField(max_length=1, blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    fl_ocupacao = models.CharField(max_length=1, blank=True, null=True)
    cd_acomodacao = models.CharField(max_length=6, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_ocupacao_acomodacao'


class AuOperador(models.Model):
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_menu = models.CharField(max_length=5, blank=True, null=True)
    cd_classe = models.NullBooleanField()
    cd_nivel_tela = models.NullBooleanField()
    cd_senha = models.CharField(max_length=6, blank=True, null=True)
    fl_status = models.NullBooleanField()
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    ds_operador = models.CharField(max_length=45, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    cod_grupo = models.IntegerField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_posto_srv = models.IntegerField(blank=True, null=True)
    cd_pessoa = models.IntegerField(blank=True, null=True)
    fl_autoriza_digital = models.CharField(max_length=1, blank=True, null=True)
    fl_multiempresa = models.CharField(max_length=1, blank=True, null=True)
    fl_libera_setor_externo = models.CharField(max_length=1, blank=True, null=True)
    fl_audita_alta = models.CharField(max_length=1, blank=True, null=True)
    nu_conexao = models.FloatField(blank=True, null=True)
    ult_acesso = models.DateField(blank=True, null=True)
    ult_atualizacao = models.DateField(blank=True, null=True)
    cd_funcionario = models.IntegerField(blank=True, null=True)
    nu_matricula = models.IntegerField(blank=True, null=True)
    fl_inc_gasto_manual_pep = models.CharField(max_length=1, blank=True, null=True)
    fl_controla_permissao = models.CharField(max_length=1, blank=True, null=True)
    fl_autoriza_comanda_manual = models.CharField(max_length=1, blank=True, null=True)
    fl_autoriza_perda_outros = models.CharField(max_length=1, blank=True, null=True)
    fl_controla_validade = models.CharField(max_length=1, blank=True, null=True)
    fl_acesso_saida_urg = models.CharField(max_length=1, blank=True, null=True)
    fl_senha_padrao = models.CharField(max_length=1, blank=True, null=True)
    fl_auditoria_contas = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_operador'


class AuOperadorDevolucao(models.Model):
    cd_operador_devolucao = models.FloatField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_tipo_devolucao = models.NullBooleanField()
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_operador_devolucao'


class AuOperadorLocalAtendSa(models.Model):
    cd_operador = models.CharField(max_length=20, blank=True, null=True)
    cd_local_atendimento = models.IntegerField(blank=True, null=True)
    cd_status = models.NullBooleanField()
    fl_tipo = models.NullBooleanField()
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_operador_local_atend_sa'


class AuPaciente(models.Model):
    cd_acao = models.NullBooleanField()
    cd_paciente = models.IntegerField(blank=True, null=True)
    nm_paciente = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    nm_municipio = models.CharField(max_length=60, blank=True, null=True)
    cd_uf = models.CharField(max_length=2, blank=True, null=True)
    cd_estado_civil = models.IntegerField(blank=True, null=True)
    cd_cor = models.NullBooleanField()
    fl_tipo_sanguineo = models.CharField(max_length=2, blank=True, null=True)
    fl_fator_rh = models.CharField(max_length=1, blank=True, null=True)
    cd_profissao = models.CharField(max_length=8, blank=True, null=True)
    nm_pai = models.CharField(max_length=45, blank=True, null=True)
    nm_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_prof_pai = models.CharField(max_length=8, blank=True, null=True)
    cd_prof_mae = models.CharField(max_length=8, blank=True, null=True)
    cd_tipo_endereco = models.CharField(max_length=10, blank=True, null=True)
    nm_endereco = models.CharField(max_length=60, blank=True, null=True)
    nu_endereco = models.CharField(max_length=10, blank=True, null=True)
    nm_complemento_end = models.CharField(max_length=60, blank=True, null=True)
    nm_bairro = models.CharField(max_length=60, blank=True, null=True)
    nu_cep = models.CharField(max_length=8, blank=True, null=True)
    nu_telefone = models.CharField(max_length=20, blank=True, null=True)
    nu_ramal = models.CharField(max_length=4, blank=True, null=True)
    nm_ponto_referencia = models.CharField(max_length=60, blank=True, null=True)
    ds_local_trabalho_paciente = models.CharField(max_length=45, blank=True, null=True)
    nu_telefone_trabalho = models.CharField(max_length=10, blank=True, null=True)
    cd_nacionalidade = models.IntegerField(blank=True, null=True)
    nu_rg = models.BigIntegerField(blank=True, null=True)
    cd_orgao_expedidor = models.CharField(max_length=45, blank=True, null=True)
    cd_uf_orgao = models.CharField(max_length=2, blank=True, null=True)
    nu_cgc_cpf = models.BigIntegerField(blank=True, null=True)
    nu_carteira_prof = models.IntegerField(blank=True, null=True)
    nu_serie = models.IntegerField(blank=True, null=True)
    cd_religiao = models.IntegerField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_paciente'


class AuParamControlePermissao(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_setor = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_setor', blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_fim = models.DateField(blank=True, null=True)
    hr_inicio = models.IntegerField(blank=True, null=True)
    hr_fim = models.IntegerField(blank=True, null=True)
    nm_operador = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='nm_operador', blank=True, null=True)
    usuario_gravou = models.CharField(max_length=10, blank=True, null=True)
    dt_usuario_gravou = models.DateField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_controle_permissao'


class AuParamCurvaAbc(models.Model):
    cd_acao = models.NullBooleanField()
    cd_dia = models.NullBooleanField()
    nm_dia = models.CharField(max_length=15, blank=True, null=True)
    nm_setor = models.CharField(max_length=50, blank=True, null=True)
    nm_flag = models.CharField(max_length=50, blank=True, null=True)
    cd_mes = models.NullBooleanField()
    dt_transacao = models.DateField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_curva_abc'


class AuParamFilialSolicOpe(models.Model):
    cd_acao = models.NullBooleanField()
    id_seq_param = models.IntegerField()
    id_seq = models.IntegerField()
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_tipo_solicitacao = models.IntegerField(blank=True, null=True)
    cd_grupo_chamado = models.IntegerField(blank=True, null=True)
    nm_operador_chamado = models.CharField(max_length=30, blank=True, null=True)
    cd_setor_executante = models.CharField(max_length=6, blank=True, null=True)
    ds_executante_padrao = models.CharField(max_length=100, blank=True, null=True)
    fl_aviso_inicial = models.CharField(max_length=1, blank=True, null=True)
    fl_avisa_grupo_pai = models.CharField(max_length=1, blank=True, null=True)
    fl_bloqueada_abertura_central = models.CharField(max_length=1, blank=True, null=True)
    fl_conclui_realizado = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_solicitante = models.CharField(max_length=6, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_filial_solic_ope'


class AuParamFilialSolicitacao(models.Model):
    cd_acao = models.NullBooleanField()
    id_seq_param = models.IntegerField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_tipo_solicitacao = models.IntegerField(blank=True, null=True)
    cd_grupo_chamado = models.IntegerField(blank=True, null=True)
    nm_operador_chamado = models.CharField(max_length=30, blank=True, null=True)
    cd_setor_executante = models.CharField(max_length=6, blank=True, null=True)
    ds_executante_padrao = models.CharField(max_length=100, blank=True, null=True)
    fl_aviso_inicial = models.CharField(max_length=1, blank=True, null=True)
    fl_avisa_grupo_pai = models.CharField(max_length=1, blank=True, null=True)
    fl_bloqueada_abertura_central = models.CharField(max_length=1, blank=True, null=True)
    fl_conclui_realizado = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_solicitante = models.CharField(max_length=6, blank=True, null=True)
    nr_periodo_tempo_alerta = models.FloatField(blank=True, null=True)
    cd_unidade_tempo_alerta = models.CharField(max_length=2, blank=True, null=True)
    id_mnemonico_avaliacao = models.CharField(max_length=200, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_filial_solicitacao'


class AuParamMovProibicao(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_fim = models.DateField(blank=True, null=True)
    hr_inicio = models.IntegerField(blank=True, null=True)
    hr_fim = models.IntegerField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    usuario_gravou = models.CharField(max_length=10, blank=True, null=True)
    dt_usuario_gravou = models.DateField(blank=True, null=True)
    fl_liberado = models.CharField(max_length=1, blank=True, null=True)
    usuario_liberou = models.CharField(max_length=10, blank=True, null=True)
    dt_liberacao = models.DateField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_mov_proibicao'


class AuParamParametroReferencia(models.Model):
    cd_ref = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_metodo_realizado = models.IntegerField(blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    fl_unidade_tempo = models.CharField(max_length=1, blank=True, null=True)
    qt_idade_inicial = models.IntegerField(blank=True, null=True)
    qt_idade_final = models.IntegerField(blank=True, null=True)
    fl_datacheck = models.CharField(max_length=1, blank=True, null=True)
    dt_ini_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    nm_operador_audit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_parametro_referencia'


class AuParamPlantaoMedico(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    cd_um_vl = models.IntegerField(blank=True, null=True)
    vl_plantao = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_op_solicitante = models.CharField(max_length=30, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_plantao_medico'


class AuParamProdmedDesconto(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    fl_pessoa_fisica_juridica = models.CharField(max_length=1, blank=True, null=True)
    fl_cobra_ir = models.CharField(max_length=1, blank=True, null=True)
    pct_desconto_ir = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fl_cobra_iss = models.CharField(max_length=1, blank=True, null=True)
    pct_desconto_iss = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fl_isento = models.CharField(max_length=1, blank=True, null=True)
    cd_cedente_sacado = models.FloatField(blank=True, null=True)
    fl_tipo_ir = models.FloatField(blank=True, null=True)
    fl_cobra_cofins = models.CharField(max_length=1, blank=True, null=True)
    pct_desconto_cofins = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fl_cobra_pis = models.CharField(max_length=1, blank=True, null=True)
    pct_desconto_pis = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fl_cobra_csll = models.CharField(max_length=1, blank=True, null=True)
    pct_desconto_csll = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pct_desconto_base_iss = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_prodmed_desconto'


class AuParamProdmedGrupoProced(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    cd_grupo_procedimento = models.IntegerField(blank=True, null=True)
    cd_tipo_produtividade = models.NullBooleanField()
    cd_tabela_procedimento = models.IntegerField(blank=True, null=True)
    cd_um = models.IntegerField(blank=True, null=True)
    pct_fixo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vl_fixo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fl_filme = models.CharField(max_length=1, blank=True, null=True)
    cd_um_ac = models.IntegerField(blank=True, null=True)
    cd_tabela_ac = models.IntegerField(blank=True, null=True)
    pct_acrescimo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_op_solicitante = models.CharField(max_length=30, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_prodmed_grupo_proced'


class AuParamProdmedPlantaoVar(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    cd_grupo_procedimento = models.IntegerField(blank=True, null=True)
    cd_um_vl = models.IntegerField(blank=True, null=True)
    vl_plantao = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vl_procedimento_plantao = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_op_solicitante = models.CharField(max_length=30, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_prodmed_plantao_var'


class AuParamProdmedProcedimento(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_tipo_produtividade = models.NullBooleanField()
    cd_tabela_procedimento = models.IntegerField(blank=True, null=True)
    cd_um_proc = models.IntegerField(blank=True, null=True)
    pct_fixo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vl_fixo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fl_filme = models.CharField(max_length=1, blank=True, null=True)
    cd_um_ac = models.IntegerField(blank=True, null=True)
    cd_tabela_ac = models.IntegerField(blank=True, null=True)
    pct_acrescimo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vl_exame_plantao = models.FloatField(blank=True, null=True)
    pct_part_out_conv = models.FloatField(blank=True, null=True)
    pct_part_out_conv_plan = models.FloatField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_op_solicitante = models.CharField(max_length=30, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_prodmed_procedimento'


class AuParamProdmedSetGrProced(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    cd_grupo_procedimento = models.IntegerField(blank=True, null=True)
    cd_tipo_produtividade = models.NullBooleanField()
    cd_tabela_procedimento = models.IntegerField(blank=True, null=True)
    cd_um = models.IntegerField(blank=True, null=True)
    pct_fixo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vl_fixo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fl_filme = models.CharField(max_length=1, blank=True, null=True)
    cd_um_ac = models.IntegerField(blank=True, null=True)
    cd_tabela_ac = models.IntegerField(blank=True, null=True)
    pct_acrescimo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_op_solicitante = models.CharField(max_length=30, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_prodmed_set_gr_proced'


class AuParamProdmedSetProced(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_tipo_produtividade = models.NullBooleanField()
    cd_tabela_procedimento = models.IntegerField(blank=True, null=True)
    cd_um_proc = models.IntegerField(blank=True, null=True)
    pct_fixo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vl_fixo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fl_filme = models.CharField(max_length=1, blank=True, null=True)
    cd_um_ac = models.IntegerField(blank=True, null=True)
    cd_tabela_ac = models.IntegerField(blank=True, null=True)
    pct_acrescimo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_op_solicitante = models.CharField(max_length=30, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_prodmed_set_proced'


class AuParamProdmedValorFixo(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    cd_tipo_valor_fixo = models.FloatField(blank=True, null=True)
    cd_um_vl = models.IntegerField(blank=True, null=True)
    vl_fixo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_op_solicitante = models.CharField(max_length=30, blank=True, null=True)
    dt_solicitacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_prodmed_valor_fixo'


class AuParamRepasse(models.Model):
    cd_acao = models.NullBooleanField()
    dt_vigencia = models.DateField(blank=True, null=True)
    vl_max_cobra_percent = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vl_percentual = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    vl_percent_ir = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_repasse'


class AuParamSolicParecer(models.Model):
    id_param_solic_parecer = models.IntegerField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_especialidade = models.IntegerField(blank=True, null=True)
    cd_tipo_parecer = models.IntegerField(blank=True, null=True)
    cd_parecerista = models.IntegerField(blank=True, null=True)
    cd_especialidade_detalhe = models.IntegerField(blank=True, null=True)
    dt_criacao = models.DateField(blank=True, null=True)
    nm_operador_criacao = models.CharField(max_length=10, blank=True, null=True)
    dt_ult_atu = models.DateField(blank=True, null=True)
    nm_operador_atu = models.CharField(max_length=10, blank=True, null=True)
    fl_ativado = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'au_param_solic_parecer'


class AuParamUnidAtendOperador(models.Model):
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    fl_selecionado = models.CharField(max_length=1, blank=True, null=True)
    nu_tempo = models.FloatField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_param_unid_atend_operador'


class AuParametroConvenio(models.Model):
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_plano_convenio = models.IntegerField(blank=True, null=True)
    dt_vigencia_parametro = models.DateField(blank=True, null=True)
    cd_tabela_proced = models.IntegerField(blank=True, null=True)
    pc_desconto_proced = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_um_proced = models.IntegerField(blank=True, null=True)
    cd_tabela_taxa = models.IntegerField(blank=True, null=True)
    pc_desconto_taxa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_um_taxa = models.IntegerField(blank=True, null=True)
    cd_tabela_mat_med = models.IntegerField(blank=True, null=True)
    pc_desconto_mat_med = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_um_mat_med = models.IntegerField(blank=True, null=True)
    cd_tabela_medicamento = models.IntegerField(blank=True, null=True)
    pc_desconto_medicamento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_um_medicamento = models.IntegerField(blank=True, null=True)
    cd_um_proced_filme = models.IntegerField(blank=True, null=True)
    cd_material_tab_ref_ans = models.CharField(max_length=3, blank=True, null=True)
    cd_medicamento_tab_ref_ans = models.CharField(max_length=3, blank=True, null=True)
    cd_taxa_tab_ref_ans = models.CharField(max_length=3, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    pc_acrescimo_taxa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pc_acrescimo_mat_med = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pc_acrescimo_medicamento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_parametro_convenio'


class AuParametroGeraisFilial(models.Model):
    cd_filial = models.CharField(max_length=5, blank=True, null=True)
    cd_parametro = models.CharField(max_length=100, blank=True, null=True)
    fl_ativo = models.CharField(max_length=1, blank=True, null=True)
    dt_criacao = models.DateField(blank=True, null=True)
    dt_ativacao = models.DateField(blank=True, null=True)
    cd_user_ativou = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_parametro_gerais_filial'


class AuPedido(models.Model):
    dt_lancamento = models.DateField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    cd_pedido = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_pedido'


class AuPedidoCotacao(models.Model):
    cd_acao = models.NullBooleanField()
    cd_cotacao = models.IntegerField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_similar = models.CharField(max_length=4, blank=True, null=True)
    qt_cotada = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_pedido_cotacao'


class AuPedidoExame(models.Model):
    cd_acao = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    nu_pedido = models.FloatField(blank=True, null=True)
    dt_pedido = models.DateField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    nm_operador = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_pedido_exame'


class AuPedidoFornecedor(models.Model):
    cd_pedido = models.FloatField(blank=True, null=True)
    fl_pedido = models.NullBooleanField()
    cd_fornecedor = models.FloatField(blank=True, null=True)
    dt_pedido = models.DateField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_motivo_aceite_pedido = models.FloatField(blank=True, null=True)
    cd_condicao_entrega = models.CharField(max_length=3, blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    vl_pedido = models.FloatField(blank=True, null=True)
    vl_saldo_pedido = models.FloatField(blank=True, null=True)
    vl_saldo_nota = models.FloatField(blank=True, null=True)
    vl_saldo_obrigacao = models.FloatField(blank=True, null=True)
    dt_validade_pedido = models.DateField(blank=True, null=True)
    qt_dias_entrega = models.FloatField(blank=True, null=True)
    cd_cotacao = models.FloatField(blank=True, null=True)
    ds_forma_pagamento = models.CharField(max_length=20, blank=True, null=True)
    pc_icms = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ds_observacao = models.CharField(max_length=240, blank=True, null=True)
    dt_prevista_entraga = models.DateField(blank=True, null=True)
    dt_entrega = models.DateField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    cd_setor_controle = models.CharField(max_length=6, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'au_pedido_fornecedor'


class AuPendenciaCl(models.Model):
    cd_usuario_digitador = models.CharField(max_length=30, blank=True, null=True)
    nu_pendencia = models.FloatField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_convenio_pagador = models.NullBooleanField()
    cd_pessoa_cobra = models.FloatField(blank=True, null=True)
    dt_registro = models.DateField(blank=True, null=True)
    cd_motivo_pendencia = models.IntegerField(blank=True, null=True)
    fl_situacao = models.CharField(max_length=1, blank=True, null=True)
    ds_observacao = models.CharField(max_length=50, blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_ocorrencia_pedido = models.IntegerField(blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_senha_autoriza = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_pendencia_cl'


class AuPermissaoTrocarBio(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    nm_operador_permissao = models.CharField(max_length=10, blank=True, null=True)
    nm_operador_audit = models.CharField(max_length=10, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_permissao_trocar_bio'


class AuPessoa(models.Model):
    cd_acao = models.NullBooleanField()
    cd_pessoa = models.FloatField(blank=True, null=True)
    nu_cgc_cpf = models.FloatField(blank=True, null=True)
    nm_pessoa_razao_social = models.CharField(max_length=45, blank=True, null=True)
    nm_fantasia = models.CharField(max_length=20, blank=True, null=True)
    fl_tipo_pessoa = models.NullBooleanField()
    fl_empresa = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_nascimento_fundacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_pessoa'


class AuPessoaConvenio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_pessoa = models.FloatField(blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    fl_credenciado = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_pessoa_convenio'


class AuPlanOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_estoq = models.FloatField(blank=True, null=True)
    prc_mat_med_estoq = models.FloatField(blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    dt_inicial = models.DateField(blank=True, null=True)
    dt_final = models.DateField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    fl_estabilidade = models.CharField(max_length=1, blank=True, null=True)
    qt_estabilidade = models.FloatField(blank=True, null=True)
    dt_agenda = models.DateField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_paciente = models.FloatField(blank=True, null=True)
    dt_planejamento = models.DateField(blank=True, null=True)
    cd_agenda = models.FloatField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_dosagem = models.CharField(max_length=2, blank=True, null=True)
    cd_pessoa_hosp = models.FloatField(blank=True, null=True)
    cd_pessoa_hap = models.FloatField(blank=True, null=True)
    nm_pessoa = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_plan_onco_hist'


class AuPlanoConvenio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_plano_convenio = models.IntegerField(blank=True, null=True)
    ds_plano_convenio = models.CharField(max_length=45, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_plano_convenio'


class AuPlantoesMedico(models.Model):
    cd_medico = models.FloatField(blank=True, null=True)
    ano_referencia = models.IntegerField(blank=True, null=True)
    mes_referencia = models.IntegerField(blank=True, null=True)
    nu_plantoes = models.IntegerField(blank=True, null=True)
    dt_inicio_plantao = models.DateField(blank=True, null=True)
    hr_inicio_plantao = models.IntegerField(blank=True, null=True)
    dt_fim_plantao = models.DateField(blank=True, null=True)
    hr_fim_plantao = models.IntegerField(blank=True, null=True)
    dt_processamento = models.DateField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)
    terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_grupo_procedimento = models.IntegerField(blank=True, null=True)
    cd_empresa = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    tempo_considerado = models.FloatField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    fl_sobre_aviso = models.CharField(max_length=1, blank=True, null=True)
    dt_aprovacao = models.DateField(blank=True, null=True)
    cd_aprovador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_plantoes_medico'


class AuPontoOperadorAtendSa(models.Model):
    nm_maquina = models.CharField(max_length=40, blank=True, null=True)
    fl_imp_digital = models.CharField(max_length=1, blank=True, null=True)
    fl_imagem_foto = models.CharField(max_length=1, blank=True, null=True)
    cd_grupo_consultorio = models.IntegerField(blank=True, null=True)
    cd_ponto_atendimento = models.IntegerField(blank=True, null=True)
    cd_local_atendimento = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=20, blank=True, null=True)
    ds_ponto_atendimento = models.CharField(max_length=40, blank=True, null=True)
    fl_tipo = models.NullBooleanField()
    fl_imp_ativa = models.NullBooleanField()
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    ult_operador = models.CharField(max_length=20, blank=True, null=True)
    fl_novosam = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_ponto_operador_atend_sa'


class AuPreco(models.Model):
    cd_acao = models.NullBooleanField()
    cd_item = models.IntegerField(blank=True, null=True)
    vl_custo = models.FloatField(blank=True, null=True)
    vl_venda = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_preco'


class AuPrescricaoAlta(models.Model):
    cd_atendimento = models.IntegerField()
    cd_ocorrencia_plano = models.IntegerField()
    cd_ordem_prescricao = models.IntegerField()
    cd_ordem_alta = models.IntegerField()
    cd_tipo_alta = models.IntegerField()
    cd_posto_destino = models.CharField(max_length=6, blank=True, null=True)
    dt_alta_medica = models.DateField(blank=True, null=True)
    hr_alta_medica = models.IntegerField(blank=True, null=True)
    cd_profissional_alta = models.IntegerField(blank=True, null=True)
    cd_profissional_cancela = models.IntegerField(blank=True, null=True)
    fl_status_uso = models.CharField(max_length=1, blank=True, null=True)
    cd_ordem_impressao = models.IntegerField(blank=True, null=True)
    cd_ordem_impressao_item = models.IntegerField(blank=True, null=True)
    dt_impressao = models.DateField(blank=True, null=True)
    cd_profissional_imprime = models.IntegerField(blank=True, null=True)
    hr_alta_apartir = models.IntegerField(blank=True, null=True)
    ds_observacao_alta = models.CharField(max_length=2000, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    id_session = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_acao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_prescricao_alta'


class AuPrescricaoMedica(models.Model):
    cd_atendimento = models.IntegerField()
    cd_ocorrencia_plano = models.IntegerField()
    cd_ordem_prescricao = models.IntegerField()
    cd_ordem_prescricao_pai = models.IntegerField(blank=True, null=True)
    nu_prescricao_medica = models.IntegerField()
    dt_prescricao = models.DateField()
    hr_prescricao = models.IntegerField()
    fl_prescricao_medica = models.CharField(max_length=1)
    fl_status_prescricao = models.CharField(max_length=1)
    cd_avaliacao = models.IntegerField(blank=True, null=True)
    cd_profissional = models.IntegerField()
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    ds_observacao = models.TextField(blank=True, null=True)
    fl_assinatura = models.CharField(max_length=1, blank=True, null=True)
    fl_tipo_aprazamento = models.CharField(max_length=1, blank=True, null=True)
    qt_frequencia_uso = models.IntegerField(blank=True, null=True)
    dt_inicio_avaliacao = models.DateField(blank=True, null=True)
    hr_inicio_avaliacao = models.IntegerField(blank=True, null=True)
    qt_frequencia_totalizacao = models.IntegerField(blank=True, null=True)
    qt_peso_kg_registrado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    id_session = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_acao = models.DateTimeField(blank=True, null=True)
    nu_documento_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_prescricao_medica'


class AuPrescricaoMedicaHv(models.Model):
    cd_atendimento = models.IntegerField()
    cd_ocorrencia_plano = models.IntegerField()
    cd_ordem_prescricao = models.IntegerField()
    cd_ordem_hv = models.IntegerField()
    vig = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    volume_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qt_frequencia_uso = models.IntegerField(blank=True, null=True)
    fl_frequencia_uso = models.CharField(max_length=3, blank=True, null=True)
    qt_gotejamento = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cd_gotejamento = models.IntegerField(blank=True, null=True)
    fl_bomba_infusao = models.CharField(max_length=1, blank=True, null=True)
    qt_soro_s_glicose = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qt_soro_c_glicose = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fl_validado = models.CharField(max_length=1, blank=True, null=True)
    fl_status_uso = models.CharField(max_length=1, blank=True, null=True)
    fl_impresso = models.CharField(max_length=1, blank=True, null=True)
    cd_profissional_prescreve = models.IntegerField(blank=True, null=True)
    cd_profissional_valida = models.IntegerField(blank=True, null=True)
    cd_profissional_cancela = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_ordem_impressao = models.IntegerField(blank=True, null=True)
    cd_ordem_impressao_item = models.IntegerField(blank=True, null=True)
    dt_impressao = models.DateField(blank=True, null=True)
    cd_profissional_imprime = models.IntegerField(blank=True, null=True)
    cd_tipo_acesso_infusao = models.CharField(max_length=1, blank=True, null=True)
    cd_tipo_fase = models.CharField(max_length=1, blank=True, null=True)
    dt_hr_suspensao = models.DateField(blank=True, null=True)
    qt_tempo_fase_rapida = models.IntegerField(blank=True, null=True)
    cd_unid_tempo_fase_rapida = models.CharField(max_length=2, blank=True, null=True)
    fl_necessario = models.CharField(max_length=1, blank=True, null=True)
    fl_acm = models.CharField(max_length=1, blank=True, null=True)
    dt_libera_sn = models.DateField(blank=True, null=True)
    hr_libera_sn = models.IntegerField(blank=True, null=True)
    cd_profissional_libera_sn = models.IntegerField(blank=True, null=True)
    cd_tipo_hv = models.CharField(max_length=1, blank=True, null=True)
    qt_quota = models.FloatField(blank=True, null=True)
    id_session = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_acao = models.DateTimeField(blank=True, null=True)
    dt_validacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_prescricao_medica_hv'


class AuPrescricaoPlano(models.Model):
    cd_atendimento = models.IntegerField()
    cd_ocorrencia_plano = models.IntegerField()
    cd_ordem_prescricao = models.IntegerField()
    cd_ordem_prescricao_plano = models.IntegerField()
    cd_prescricao_plano_pai = models.IntegerField(blank=True, null=True)
    dt_inicio_uso = models.DateField()
    hr_inicio_uso = models.IntegerField(blank=True, null=True)
    dt_fim_uso = models.DateField(blank=True, null=True)
    hr_fim_uso = models.IntegerField(blank=True, null=True)
    cd_mat_med = models.IntegerField(blank=True, null=True)
    qt_frequencia_uso = models.IntegerField(blank=True, null=True)
    cd_unidade_usual = models.CharField(max_length=2, blank=True, null=True)
    cd_tipo_acesso = models.IntegerField()
    qt_dosagem = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qt_diluicao = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cd_gotejamento = models.IntegerField(blank=True, null=True)
    qt_gotejamento = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    dt_revisao_prescricao = models.DateField(blank=True, null=True)
    fl_status_uso = models.CharField(max_length=1, blank=True, null=True)
    fl_necessario = models.CharField(max_length=1, blank=True, null=True)
    fl_diluicao = models.CharField(max_length=1, blank=True, null=True)
    fl_alergia = models.CharField(max_length=1, blank=True, null=True)
    fl_periodo = models.CharField(max_length=1, blank=True, null=True)
    ds_observacao = models.CharField(max_length=500, blank=True, null=True)
    nu_produto = models.IntegerField()
    cd_principio_ativo = models.IntegerField(blank=True, null=True)
    cd_ocorrencia_diluicao = models.IntegerField(blank=True, null=True)
    cd_ordem_administracao = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_profissional_cancela = models.IntegerField(blank=True, null=True)
    qt_mat_med = models.IntegerField(blank=True, null=True)
    cd_apresentacao = models.CharField(max_length=4, blank=True, null=True)
    qt_tempo_gotej = models.IntegerField(blank=True, null=True)
    cd_unidade_gotej = models.CharField(max_length=2, blank=True, null=True)
    fl_acm = models.CharField(max_length=1, blank=True, null=True)
    cd_diluente = models.IntegerField(blank=True, null=True)
    qt_reconstituicao = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qt_dosagem_med = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cd_unidade_dosagem_med = models.CharField(max_length=2, blank=True, null=True)
    cd_apresentacao_diluente = models.CharField(max_length=4, blank=True, null=True)
    cd_ordem_proc_plano_uso = models.IntegerField(blank=True, null=True)
    cd_profissional_prescreve = models.IntegerField(blank=True, null=True)
    cd_profissional_valida = models.IntegerField(blank=True, null=True)
    fl_validado = models.CharField(max_length=1, blank=True, null=True)
    fl_impresso = models.CharField(max_length=1, blank=True, null=True)
    fl_bomba_infusao = models.CharField(max_length=1, blank=True, null=True)
    cd_reconstituir = models.IntegerField(blank=True, null=True)
    qt_reconstituir = models.FloatField(blank=True, null=True)
    cd_reconstituir2 = models.IntegerField(blank=True, null=True)
    qt_reconstituir2 = models.FloatField(blank=True, null=True)
    cd_apres_reconstituir = models.CharField(max_length=4, blank=True, null=True)
    cd_apres_reconstituir2 = models.CharField(max_length=4, blank=True, null=True)
    fl_frequencia_uso = models.CharField(max_length=3, blank=True, null=True)
    cd_tipo_prescricao_plano = models.IntegerField()
    qt_dosagem_hv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cd_unidade_hv = models.CharField(max_length=2, blank=True, null=True)
    cd_ordem_hv = models.IntegerField(blank=True, null=True)
    nu_ordem_apresentacao = models.IntegerField(blank=True, null=True)
    cd_ordem_impressao = models.IntegerField(blank=True, null=True)
    cd_ordem_impressao_item = models.IntegerField(blank=True, null=True)
    dt_libera_sn = models.DateField(blank=True, null=True)
    hr_libera_sn = models.IntegerField(blank=True, null=True)
    cd_profissional_libera_sn = models.IntegerField(blank=True, null=True)
    dt_impressao = models.DateField(blank=True, null=True)
    cd_profissional_imprime = models.IntegerField(blank=True, null=True)
    dt_hr_suspensao = models.DateField(blank=True, null=True)
    ds_apres_ud_fazer_retirar = models.CharField(max_length=4, blank=True, null=True)
    fl_bureta = models.CharField(max_length=1, blank=True, null=True)
    id_session = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_acao = models.DateTimeField(blank=True, null=True)
    dt_validacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_prescricao_plano'


class AuProcedParamReferencia(models.Model):
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_metodo_realizado = models.IntegerField(blank=True, null=True)
    cd_parametro_referencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_sexo = models.CharField(max_length=2, blank=True, null=True)
    qt_idade_inicial = models.IntegerField(blank=True, null=True)
    qt_idade_final = models.IntegerField(blank=True, null=True)
    fl_unidade_tempo = models.CharField(max_length=1, blank=True, null=True)
    vl_parametro_minimo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vl_parametro_maximo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vl_parametro_normal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    fl_valor_parametro = models.CharField(max_length=1, blank=True, null=True)
    ds_valor_parametro = models.CharField(max_length=2000, blank=True, null=True)
    cd_unidade_usual = models.CharField(max_length=2, blank=True, null=True)
    vl_formula = models.CharField(max_length=50, blank=True, null=True)
    qt_decimal = models.NullBooleanField()
    dt_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    fl_aparecer_laudo = models.CharField(max_length=1, blank=True, null=True)
    cd_referencia = models.CharField(max_length=2, blank=True, null=True)
    fl_tipo_valor = models.CharField(max_length=1, blank=True, null=True)
    ds_texto_resultado = models.CharField(max_length=60, blank=True, null=True)
    cd_ref = models.FloatField(blank=True, null=True)
    cd_proced_param_referencia = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_proced_param_referencia'


class AuProcedimento(models.Model):
    cd_acao = models.NullBooleanField()
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_subgrupo_procedimento = models.CharField(max_length=5, blank=True, null=True)
    cd_grupo_procedimento = models.CharField(max_length=3, blank=True, null=True)
    nm_procedimento = models.CharField(max_length=240, blank=True, null=True)
    qt_idade_inicial = models.IntegerField(blank=True, null=True)
    qt_idade_final = models.IntegerField(blank=True, null=True)
    cd_sexo = models.CharField(max_length=2, blank=True, null=True)
    nr_procedimento = models.CharField(max_length=45, blank=True, null=True)
    cd_clinica = models.NullBooleanField()
    cd_via_acesso = models.IntegerField(blank=True, null=True)
    fl_parto = models.NullBooleanField()
    fl_cirurgia = models.NullBooleanField()
    cd_porte_anestesia = models.NullBooleanField()
    cd_tipo_anestesia = models.NullBooleanField()
    qt_dias = models.IntegerField(blank=True, null=True)
    qt_aux = models.NullBooleanField()
    qt_incid_filme = models.IntegerField(blank=True, null=True)
    qt_filme_m2 = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    qt_custo_operacional = models.IntegerField(blank=True, null=True)
    qt_unidade_topografica = models.CharField(max_length=10, blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    fl_tipo_exame = models.NullBooleanField()
    qt_ch = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_procedimento_cbhpm = models.CharField(max_length=8, blank=True, null=True)
    cd_procedimento_amb = models.CharField(max_length=8, blank=True, null=True)
    fl_rol_ans = models.CharField(max_length=1, blank=True, null=True)
    fl_cbhpm = models.CharField(max_length=1, blank=True, null=True)
    fl_exige_result_antes_checar = models.CharField(max_length=1, blank=True, null=True)
    nu_prioridade_exame = models.BigIntegerField(blank=True, null=True)
    qt_hr_padrao_exame_eme = models.BigIntegerField(blank=True, null=True)
    fl_tuss = models.CharField(max_length=1, blank=True, null=True)
    cd_tipo_tabela = models.BigIntegerField(blank=True, null=True)
    qt_dias_terceirizados = models.BigIntegerField(blank=True, null=True)
    fl_nao_copia_prescricao = models.CharField(max_length=1, blank=True, null=True)
    cd_procedimento_tuss = models.CharField(max_length=8, blank=True, null=True)
    fl_continuo = models.CharField(max_length=1, blank=True, null=True)
    qt_frequencia_maxima = models.BigIntegerField(blank=True, null=True)
    nm_procedimento_alias_1 = models.CharField(max_length=240, blank=True, null=True)
    nm_procedimento_alias_2 = models.CharField(max_length=240, blank=True, null=True)
    cd_mnemonico = models.CharField(max_length=8, blank=True, null=True)
    nu_frascos_coleta = models.BigIntegerField(blank=True, null=True)
    cd_procedimento_pai = models.CharField(max_length=8, blank=True, null=True)
    fl_gas = models.CharField(max_length=1, blank=True, null=True)
    fl_gastos_gerais = models.CharField(max_length=1, blank=True, null=True)
    cd_referencia = models.CharField(max_length=15, blank=True, null=True)
    fl_aerosol = models.CharField(max_length=1, blank=True, null=True)
    cd_unidade_usual = models.CharField(max_length=2, blank=True, null=True)
    fl_exibe_result_anterior = models.CharField(max_length=1, blank=True, null=True)
    fl_urgencia = models.CharField(max_length=1, blank=True, null=True)
    fl_procedimento_ficticio = models.CharField(max_length=1, blank=True, null=True)
    fl_procedimento_vida_imagem = models.CharField(max_length=1, blank=True, null=True)
    cd_porte_cirurgia = models.BigIntegerField(blank=True, null=True)
    fl_laudo_observacao = models.CharField(max_length=1, blank=True, null=True)
    fl_entrega_material = models.CharField(max_length=1, blank=True, null=True)
    fl_fisioteraria = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento'


class AuProcedimentoAnaliseChefia(models.Model):
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)
    dt_inicio_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_analise_chefia'


class AuProcedimentoAnomalia(models.Model):
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_ocorrencia = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_procedimento = models.FloatField(blank=True, null=True)
    nu_pedido = models.FloatField(blank=True, null=True)
    dt_ocorrencia = models.DateField(blank=True, null=True)
    cd_operador_informante = models.CharField(max_length=30, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nm_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    ds_alterado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_anomalia'


class AuProcedimentoConvenio(models.Model):
    cd_operador = models.CharField(max_length=20, blank=True, null=True)
    dt_atualizacao = models.DateField(blank=True, null=True)
    fl_senha_auto_hapvida = models.CharField(max_length=1, blank=True, null=True)
    dt_fin_vigencia = models.DateField(blank=True, null=True)
    cd_procedimento_pagador = models.CharField(max_length=8, blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_plano_convenio = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    fl_pagamento = models.CharField(max_length=1, blank=True, null=True)
    cd_procedimento_convenio = models.CharField(max_length=8, blank=True, null=True)
    nm_procedimento_convenio = models.CharField(max_length=240, blank=True, null=True)
    qt_filme_m2 = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    vl_pacote = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    qt_dias_autorizado = models.IntegerField(blank=True, null=True)
    dt_ini_vigencia = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_convenio'


class AuProcedimentoMatMed(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_mat_med = models.IntegerField(blank=True, null=True)
    nm_procedimento_mat_med = models.CharField(max_length=255, blank=True, null=True)
    qt_mat_med = models.IntegerField(blank=True, null=True)
    fl_uso = models.CharField(max_length=1, blank=True, null=True)
    cd_agrupamento = models.CharField(max_length=20, blank=True, null=True)
    qt_frequencia_uso = models.IntegerField(blank=True, null=True)
    cd_unidade_frequencia = models.CharField(max_length=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_mat_med'


class AuProcedimentoModelo(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ocorrencia_procedimento = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    fl_status = models.FloatField(blank=True, null=True)
    fl_bipagem_isento = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'au_procedimento_modelo'


class AuProcedimentoModeloAnest(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ocorrencia_procedimento = models.FloatField(blank=True, null=True)
    cd_tipo_anestesia = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_modelo_anest'


class AuProcedimentoModeloConven(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ocorrencia_procedimento = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_convenio = models.FloatField(blank=True, null=True)
    qt_item = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_modelo_conven'


class AuProcedimentoModeloFilhos(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ocorrencia_procedimento = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_modelo_filhos'


class AuProcedimentoModeloFilial(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ocorrencia_procedimento = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    qt_item = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_modelo_filial'


class AuProcedimentoModeloItem(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ocorrencia_procedimento = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_exame = models.CharField(max_length=8, blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_tipo_item = models.FloatField(blank=True, null=True)
    qt_item = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_modelo_item'


class AuProcedimentoModeloTempo(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ocorrencia_procedimento = models.FloatField(blank=True, null=True)
    tp_sala_cirurgica = models.FloatField(blank=True, null=True)
    tp_permanencia = models.FloatField(blank=True, null=True)
    tp_uti = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_modelo_tempo'


class AuProcedimentoPlanoUso(models.Model):
    cd_atendimento = models.IntegerField()
    cd_ocorrencia_plano = models.IntegerField()
    cd_ordem_prescricao = models.IntegerField()
    cd_ordem_proc_plano_uso = models.IntegerField()
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    dt_inicio = models.DateField()
    hr_inicio = models.IntegerField()
    dt_fim = models.DateField(blank=True, null=True)
    hr_fim = models.IntegerField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=120, blank=True, null=True)
    fl_status_uso = models.CharField(max_length=1, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    qt_procedimento = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cd_unidade_usual = models.CharField(max_length=2, blank=True, null=True)
    qt_frequencia_uso = models.IntegerField(blank=True, null=True)
    cd_proc_plano_pai = models.IntegerField(blank=True, null=True)
    cd_cid10 = models.CharField(max_length=4, blank=True, null=True)
    fl_tipo_aprazamento = models.CharField(max_length=1, blank=True, null=True)
    cd_profissional_prescreve = models.IntegerField(blank=True, null=True)
    cd_profissional_valida = models.IntegerField(blank=True, null=True)
    fl_validado = models.CharField(max_length=1, blank=True, null=True)
    fl_impresso = models.CharField(max_length=1, blank=True, null=True)
    cd_profissional_cancela = models.IntegerField(blank=True, null=True)
    cd_ordem_impressao = models.IntegerField(blank=True, null=True)
    cd_ordem_impressao_item = models.IntegerField(blank=True, null=True)
    dt_impressao = models.DateField(blank=True, null=True)
    cd_profissional_imprime = models.IntegerField(blank=True, null=True)
    nm_procedimento = models.CharField(max_length=240, blank=True, null=True)
    cd_tipo_procedimento = models.IntegerField(blank=True, null=True)
    dt_hr_suspensao = models.DateField(blank=True, null=True)
    fl_necessario = models.CharField(max_length=1, blank=True, null=True)
    fl_acm = models.CharField(max_length=1, blank=True, null=True)
    dt_libera_sn = models.DateField(blank=True, null=True)
    hr_libera_sn = models.IntegerField(blank=True, null=True)
    cd_profissional_libera_sn = models.IntegerField(blank=True, null=True)
    id_session = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_acao = models.DateTimeField(blank=True, null=True)
    dt_validacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_plano_uso'


class AuProcedimentoRealizado(models.Model):
    cd_acao = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    dt_procedimento_realizado = models.DateField(blank=True, null=True)
    hr_procedimento_realizado = models.IntegerField(blank=True, null=True)
    qt_procedimento = models.IntegerField(blank=True, null=True)
    vl_procedimento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_modelo = models.IntegerField(blank=True, null=True)
    fl_bilat = models.CharField(max_length=1, blank=True, null=True)
    cd_via_acesso = models.IntegerField(blank=True, null=True)
    dt_resultado = models.DateField(blank=True, null=True)
    fl_emitiu_resultado = models.CharField(max_length=1, blank=True, null=True)
    fl_entregue_resultado = models.CharField(max_length=1, blank=True, null=True)
    cd_metodo_realizado = models.IntegerField(blank=True, null=True)
    fl_multipla = models.CharField(max_length=1, blank=True, null=True)
    cd_pessoa_cobra = models.FloatField(blank=True, null=True)
    cd_senha_autoriza = models.CharField(max_length=20, blank=True, null=True)
    cd_tipo_anestesia = models.IntegerField(blank=True, null=True)
    vl_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    ds_observacao = models.CharField(max_length=2000, blank=True, null=True)
    dt_libera_assina_digital = models.DateField(blank=True, null=True)
    cd_bioquimico_responsavel = models.FloatField(blank=True, null=True)
    dt_entregou_material = models.DateField(blank=True, null=True)
    dt_libera_laudo = models.DateField(blank=True, null=True)
    cd_oper_lib_laudo_vi = models.CharField(max_length=30, blank=True, null=True)
    fl_libera_assina_digital = models.CharField(max_length=1, blank=True, null=True)
    fl_libera_laudo = models.CharField(max_length=1, blank=True, null=True)
    fl_importa_interface = models.CharField(max_length=1, blank=True, null=True)
    fl_imprimiu_mapa = models.CharField(max_length=1, blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    cd_comite = models.BigIntegerField(blank=True, null=True)
    cd_ocorrencia_pacote = models.BigIntegerField(blank=True, null=True)
    qt_procedimento_paga = models.BigIntegerField(blank=True, null=True)
    vl_total_pago = models.BigIntegerField(blank=True, null=True)
    fl_status_pago = models.CharField(max_length=3, blank=True, null=True)
    fl_leito = models.CharField(max_length=1, blank=True, null=True)
    fl_entregou_material = models.CharField(max_length=1, blank=True, null=True)
    cd_natureza_glosa = models.CharField(max_length=2, blank=True, null=True)
    fl_imprimiu_assina_digital = models.CharField(max_length=1, blank=True, null=True)
    ds_observacao_procedimento = models.CharField(max_length=600, blank=True, null=True)
    fl_status_laudo = models.CharField(max_length=1, blank=True, null=True)
    dt_status_laudo = models.DateField(blank=True, null=True)
    cd_profissional_laudo = models.IntegerField(blank=True, null=True)
    ds_pendencia_laudo = models.CharField(max_length=1000, blank=True, null=True)
    fl_lado_membro = models.CharField(max_length=1, blank=True, null=True)
    cd_prof_resp = models.IntegerField(blank=True, null=True)
    ds_obs_dgn = models.CharField(max_length=2000, blank=True, null=True)
    cd_ocorrencia_plano = models.IntegerField(blank=True, null=True)
    cd_ordem_exa = models.IntegerField(blank=True, null=True)
    cd_ordem_item = models.IntegerField(blank=True, null=True)
    fl_liberado_auto = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_realizado'


class AuProcedimentoSemLaudoHap(models.Model):
    cd_atendimento = models.ForeignKey('TbProcedimentoRealizado', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_ocorrencia = models.ForeignKey('TbProcedimentoRealizado', models.DO_NOTHING, db_column='cd_ocorrencia')
    cd_ordem = models.ForeignKey('TbProcedimentoRealizado', models.DO_NOTHING, db_column='cd_ordem')
    cd_procedimento = models.CharField(max_length=8)
    fl_sol_laudo = models.CharField(max_length=1)
    cd_senha_autorizacao = models.CharField(max_length=20, blank=True, null=True)
    cd_item_pre_autorizacao = models.FloatField(blank=True, null=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)
    dt_cadastro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_sem_laudo_hap'
        unique_together = (('cd_atendimento', 'cd_ocorrencia', 'cd_ordem'),)


class AuProcedimentoTerceirizado(models.Model):
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_ocorrencia = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_laboratorio_apoio = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    qt_procedimento = models.IntegerField(blank=True, null=True)
    vl_procedimento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_mnemonico_exame = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nm_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    ds_alterado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_procedimento_terceirizado'


class AuProcessoDocAtend(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_processo_doc_atend = models.FloatField(blank=True, null=True)
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_senha_autoriza = models.CharField(max_length=20, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    fl_analise_divergencia = models.CharField(max_length=1, blank=True, null=True)
    dt_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_processo_doc_atend'


class AuProdutividadeMedica(models.Model):
    cd_produtividade = models.IntegerField(blank=True, null=True)
    cd_medico = models.FloatField(blank=True, null=True)
    mes_ano_referencia = models.DateField(blank=True, null=True)
    dt_geracao = models.DateField(blank=True, null=True)
    vl_faturado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vl_pago = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cd_obrigacao = models.IntegerField(blank=True, null=True)
    vl_irrf = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vl_iss = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    dt_obrigacao = models.DateField(blank=True, null=True)
    nu_nfiscal = models.CharField(max_length=10, blank=True, null=True)
    cd_cedente_sacado = models.FloatField(blank=True, null=True)
    fl_bloqueio = models.CharField(max_length=1, blank=True, null=True)
    fl_geracao = models.IntegerField(blank=True, null=True)
    vl_pis = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vl_cofins = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vl_csll = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_ini_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_produtividade_medica'


class AuProdutividadeVidaImagem(models.Model):
    cd_pessoa = models.FloatField(blank=True, null=True)
    data_entrada = models.DateField(blank=True, null=True)
    data_saida = models.DateField(blank=True, null=True)
    cd_escala_entrada = models.FloatField(blank=True, null=True)
    mes_ano_ref = models.DateField(blank=True, null=True)
    fl_tipo_reg = models.CharField(max_length=1, blank=True, null=True)
    grupo = models.FloatField(blank=True, null=True)
    cd_empresa = models.FloatField(blank=True, null=True)
    cd_user_geracao = models.CharField(max_length=30, blank=True, null=True)
    dt_geracao = models.DateField(blank=True, null=True)
    cd_user_liberacao = models.CharField(max_length=30, blank=True, null=True)
    dt_liberacao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    fl_sobre_aviso = models.CharField(max_length=1, blank=True, null=True)
    qt_horas_sobre_aviso = models.FloatField(blank=True, null=True)
    plantao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_produtividade_vida_imagem'


class AuProduto(models.Model):
    cd_acao = models.NullBooleanField()
    nu_produto = models.IntegerField(blank=True, null=True)
    nm_produto = models.CharField(max_length=240, blank=True, null=True)
    fl_uso = models.CharField(max_length=1, blank=True, null=True)
    fl_padronizado = models.CharField(max_length=1, blank=True, null=True)
    fl_diluente = models.CharField(max_length=1, blank=True, null=True)
    fl_hemoderivado = models.CharField(max_length=1, blank=True, null=True)
    fl_compoe_hv = models.CharField(max_length=1, blank=True, null=True)
    nr_produto = models.CharField(max_length=40, blank=True, null=True)
    nu_ordem_apresentacao = models.IntegerField(blank=True, null=True)
    cd_unidade_padrao = models.CharField(max_length=2, blank=True, null=True)
    cd_tipo_acesso = models.IntegerField(blank=True, null=True)
    fl_possui_glicose = models.CharField(max_length=1, blank=True, null=True)
    fl_soro = models.CharField(max_length=1, blank=True, null=True)
    fl_eletrolito = models.CharField(max_length=1, blank=True, null=True)
    fl_pode_diluente_inf_lenta = models.CharField(max_length=1, blank=True, null=True)
    fl_medic_programa_nacional = models.CharField(max_length=1, blank=True, null=True)
    qt_concentracao_max = models.FloatField(blank=True, null=True)
    cd_unid_conc_max = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_padrao_aerosol = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_padrao_produto = models.CharField(max_length=2, blank=True, null=True)
    fl_droga_vasoativa = models.CharField(max_length=1, blank=True, null=True)
    fl_compoe_hv_r = models.CharField(max_length=1, blank=True, null=True)
    fl_compoe_hv_c = models.CharField(max_length=1, blank=True, null=True)
    fl_profilaxia = models.CharField(max_length=1, blank=True, null=True)
    fl_terceira_comanda = models.CharField(max_length=1, blank=True, null=True)
    fl_eletrolito_excecao = models.CharField(max_length=1, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_produto'


class AuProfProcedRealizado(models.Model):
    cd_acao = models.NullBooleanField()
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_profissional = models.IntegerField(blank=True, null=True)
    cd_tipo_ato_profissional = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    qt_pontos_profissional = models.IntegerField(blank=True, null=True)
    fl_vincula = models.CharField(max_length=1, blank=True, null=True)
    vl_honorario_prof = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_paga_honorario = models.DateField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    fl_repasse_medico = models.CharField(max_length=1, blank=True, null=True)
    cd_natureza_glosa = models.CharField(max_length=2, blank=True, null=True)
    fl_honorario = models.CharField(max_length=1, blank=True, null=True)
    vl_paga_honorario = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pc_acres_honorario = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vl_honorario_franquia_prof = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_ocorrencia_pacote = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_prof_proced_realizado'


class AuProfissional(models.Model):
    cd_profissional = models.IntegerField(blank=True, null=True)
    cd_crm_profissional = models.CharField(max_length=8, blank=True, null=True)
    fl_auditor_sus = models.CharField(max_length=1, blank=True, null=True)
    fl_interno = models.CharField(max_length=1, blank=True, null=True)
    fl_cobra_fisica_juridica = models.CharField(max_length=1, blank=True, null=True)
    fl_funcionario = models.CharField(max_length=1, blank=True, null=True)
    qt_sal_pago = models.IntegerField(blank=True, null=True)
    senha_funcionario = models.CharField(max_length=10, blank=True, null=True)
    f_ativo = models.CharField(max_length=1, blank=True, null=True)
    cd_tipo_funcionario = models.CharField(max_length=2, blank=True, null=True)
    cd_grupo_garcon = models.CharField(max_length=2, blank=True, null=True)
    dt_ini_ferias_lic = models.DateField(blank=True, null=True)
    dt_fim_ferias_lic = models.DateField(blank=True, null=True)
    dt_demissao = models.DateField(blank=True, null=True)
    cd_uf_conselho = models.CharField(max_length=2, blank=True, null=True)
    cd_conselho = models.CharField(max_length=10, blank=True, null=True)
    cd_tipo_prof = models.CharField(max_length=8, blank=True, null=True)
    cd_funcionario = models.IntegerField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    cd_associado = models.IntegerField(blank=True, null=True)
    cd_cooperativa = models.CharField(max_length=1, blank=True, null=True)
    pc_acrescimo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pc_desconto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)
    dt_cadastro = models.DateField(blank=True, null=True)
    cd_classe_medico = models.IntegerField(blank=True, null=True)
    fone = models.FloatField(blank=True, null=True)
    ddd = models.FloatField(blank=True, null=True)
    cd_tipo_negociacao = models.CharField(max_length=2, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_profissional'


class AuPropriedade(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nm_propriedade = models.CharField(max_length=256, blank=True, null=True)
    vl_propriedade = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_propriedade'


class AuProrrogacaoGuia(models.Model):
    cd_acao = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    dt_ini_prorrogacao = models.DateField(blank=True, null=True)
    dt_fim_prorrogacao = models.DateField(blank=True, null=True)
    dt_autoriza_prorrogacao = models.DateField(blank=True, null=True)
    cd_auditor = models.FloatField(blank=True, null=True)
    cd_classe_auditor = models.NullBooleanField()
    hr_ini_prorrogacao = models.IntegerField(blank=True, null=True)
    hr_fim_prorrogacao = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_prorrogacao_guia'


class AuPublicacaoControle(models.Model):
    cd_sacti = models.CharField(max_length=10)
    fl_id = models.CharField(max_length=2)
    nm_descricao = models.CharField(max_length=200, blank=True, null=True)
    dt_ativacao = models.DateField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_acao = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nm_operador_audit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_publicacao_controle'


class AuQualificacaoPreLaudo(models.Model):
    cd_qualificacao_pre_laudo = models.FloatField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_profissional_laudo = models.IntegerField(blank=True, null=True)
    nu_qualificacao = models.IntegerField(blank=True, null=True)
    cd_profissional_qualificador = models.IntegerField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=128, blank=True, null=True)
    dt_qualificacao = models.DateField(blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_qualificacao_pre_laudo'


class AuRealizOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_estoq = models.FloatField(blank=True, null=True)
    prc_mat_med_estoq = models.FloatField(blank=True, null=True)
    cd_agenda = models.FloatField(blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    cd_ordem_prescricao_plano = models.FloatField(blank=True, null=True)
    dt_agenda = models.DateField(blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_dosagem = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_paciente = models.FloatField(blank=True, null=True)
    cd_pessoa_hosp = models.FloatField(blank=True, null=True)
    cd_pessoa_hap = models.FloatField(blank=True, null=True)
    nm_pessoa = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_realiz_onco_hist'


class AuRegistroCirurgia(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    id_registro = models.IntegerField(blank=True, null=True)
    cd_paciente = models.IntegerField(blank=True, null=True)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_tipo_anestesia = models.IntegerField(blank=True, null=True)
    dt_inicio_cirurgia = models.DateField(blank=True, null=True)
    dt_fim_cirurgia = models.DateField(blank=True, null=True)
    hr_inicio_cirurgia = models.IntegerField(blank=True, null=True)
    hr_fim_cirurgia = models.IntegerField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=500, blank=True, null=True)
    hr_anestesia = models.IntegerField(blank=True, null=True)
    fl_cancelado = models.CharField(max_length=1, blank=True, null=True)
    cd_motivo_cancel = models.IntegerField(blank=True, null=True)
    cd_sala_cirurgica = models.CharField(max_length=6, blank=True, null=True)
    id_kit = models.IntegerField(blank=True, null=True)
    fl_video = models.CharField(max_length=1, blank=True, null=True)
    hr_fim_anestesia = models.IntegerField(blank=True, null=True)
    cd_porte_cirurgia = models.IntegerField(blank=True, null=True)
    cd_procedimento2 = models.CharField(max_length=8, blank=True, null=True)
    cd_procedimento3 = models.CharField(max_length=8, blank=True, null=True)
    cd_procedimento4 = models.CharField(max_length=8, blank=True, null=True)
    fl_raiox = models.CharField(max_length=1, blank=True, null=True)
    cd_asa = models.FloatField(blank=True, null=True)
    cd_grau_contaminacao = models.CharField(max_length=1, blank=True, null=True)
    fl_convencional = models.CharField(max_length=1, blank=True, null=True)
    fl_envia_pelicula_plano = models.CharField(max_length=1, blank=True, null=True)
    fl_ch_antes_inducao_ane = models.CharField(max_length=1, blank=True, null=True)
    fl_ch_antes_incisao_cir = models.CharField(max_length=1, blank=True, null=True)
    fl_ch_antes_paciente_sair_sala = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_registro_cirurgia'


class AuRegistroCotacao(models.Model):
    cd_acao = models.NullBooleanField()
    cd_cotacao = models.IntegerField(blank=True, null=True)
    dt_regsitro = models.DateField(blank=True, null=True)
    fl_tipo_cotacao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_registro_cotacao'


class AuRegistroRes1(models.Model):
    ds_servico = models.CharField(max_length=3, blank=True, null=True)
    cd_registro = models.NullBooleanField()
    cd_origem = models.IntegerField(blank=True, null=True)
    nu_lote_pedido = models.IntegerField(blank=True, null=True)
    cd_pedido = models.CharField(max_length=20, blank=True, null=True)
    cd_exame = models.CharField(max_length=5, blank=True, null=True)
    ds_parametro = models.CharField(max_length=10, blank=True, null=True)
    ds_resultado = models.CharField(max_length=70, blank=True, null=True)
    ds_unidade = models.CharField(max_length=20, blank=True, null=True)
    fl_normalidade = models.NullBooleanField()
    ds_filler = models.CharField(max_length=6, blank=True, null=True)
    nu_registro = models.IntegerField(blank=True, null=True)
    dt_processamento = models.CharField(max_length=16, blank=True, null=True)
    dt_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_registro_res1'


class AuRemessaConvenio(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nu_remessa = models.FloatField(blank=True, null=True)
    cd_empresa_cobra = models.FloatField(blank=True, null=True)
    cd_convenio = models.FloatField(blank=True, null=True)
    dt_remessa = models.DateField(blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_fim = models.DateField(blank=True, null=True)
    dt_pagamento = models.DateField(blank=True, null=True)
    vl_total_honorario = models.FloatField(blank=True, null=True)
    vl_total_diaria = models.FloatField(blank=True, null=True)
    vl_total_taxa = models.FloatField(blank=True, null=True)
    vl_total_mat = models.FloatField(blank=True, null=True)
    vl_total_med = models.FloatField(blank=True, null=True)
    dt_processamento = models.DateField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)
    vl_total_outros = models.FloatField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    tl_recuperado = models.FloatField(blank=True, null=True)
    nu_seq_remessa = models.IntegerField(blank=True, null=True)
    nu_remessa_origem = models.FloatField(blank=True, null=True)
    fl_custo_operacional = models.CharField(max_length=1, blank=True, null=True)
    cd_classe_atendimento = models.NullBooleanField()
    fl_gerar_automaticamente = models.NullBooleanField()
    fl_remessa_sem_atendimento = models.NullBooleanField()
    fl_status_geracao_automatica = models.FloatField(blank=True, null=True)
    qt_caixa = models.FloatField(blank=True, null=True)
    dt_envio = models.DateField(blank=True, null=True)
    fl_status_envio = models.CharField(max_length=1, blank=True, null=True)
    dt_ent_same = models.DateField(blank=True, null=True)
    fl_conferida = models.CharField(max_length=1, blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    nm_operador_same = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_remessa_convenio'


class AuRepasseMedico(models.Model):
    cd_acao = models.NullBooleanField()
    cd_pessoa = models.IntegerField(blank=True, null=True)
    dt_pagamento = models.DateField(blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    nu_remessa = models.IntegerField(blank=True, null=True)
    dt_remessa = models.DateField(blank=True, null=True)
    vl_faturado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    vl_pago = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cd_obrigacao = models.IntegerField(blank=True, null=True)
    dt_obrigacao = models.DateField(blank=True, null=True)
    nu_nfiscal = models.CharField(max_length=10, blank=True, null=True)
    cd_cedente_sacado = models.BigIntegerField(blank=True, null=True)
    fl_bloqueio = models.CharField(max_length=1, blank=True, null=True)
    fl_isento = models.CharField(max_length=1, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    cd_associado = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_repasse_medico'


class AuRestricaoHapvida(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_restricao = models.FloatField(blank=True, null=True)
    ds_restricao = models.CharField(max_length=80, blank=True, null=True)
    fl_libera_urgencia = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_restricao_hapvida'


class AuResultadoProcedimento(models.Model):
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    sq_resultado = models.BigIntegerField(blank=True, null=True)
    cd_parametro_referencia = models.IntegerField(blank=True, null=True)
    vl_resultado_parametro = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ds_resultado_procedimento = models.CharField(max_length=50, blank=True, null=True)
    cd_unidade_usual = models.CharField(max_length=2, blank=True, null=True)
    vl_formula = models.CharField(max_length=50, blank=True, null=True)
    fl_valor_parametro = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    cd_perfil = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_resultado_procedimento'


class AuSenhaAtendimentoSa(models.Model):
    ds_obs_enfermagem = models.CharField(max_length=500, blank=True, null=True)
    dt_exame_importado = models.DateField(blank=True, null=True)
    cd_senha_master = models.IntegerField(blank=True, null=True)
    cd_grupo_atendimento = models.IntegerField(blank=True, null=True)
    cd_local_atendimento = models.IntegerField(blank=True, null=True)
    cd_senha_atendimento = models.IntegerField(blank=True, null=True)
    dt_geracao_senha = models.DateField(blank=True, null=True)
    fl_tipo_senha = models.NullBooleanField()
    cd_atendimento = models.IntegerField(blank=True, null=True)
    dt_inicio_cadastro = models.DateField(blank=True, null=True)
    dt_fim_cadastro = models.DateField(blank=True, null=True)
    cd_operador_cadastro = models.CharField(max_length=20, blank=True, null=True)
    cd_usuario = models.CharField(max_length=17, blank=True, null=True)
    cd_operador_inicio = models.CharField(max_length=20, blank=True, null=True)
    dt_inicio_atendimento = models.DateField(blank=True, null=True)
    cd_operador_fim = models.CharField(max_length=20, blank=True, null=True)
    dt_fim_atendimento = models.DateField(blank=True, null=True)
    fl_status = models.IntegerField(blank=True, null=True)
    cd_ponto_atendimento_cad = models.IntegerField(blank=True, null=True)
    cd_ponto_atendimento_ate = models.IntegerField(blank=True, null=True)
    fl_toca_som = models.NullBooleanField()
    nm_paciente = models.CharField(max_length=45, blank=True, null=True)
    vl_idade = models.IntegerField(blank=True, null=True)
    cd_paciente = models.IntegerField(blank=True, null=True)
    fl_prioridade = models.NullBooleanField()
    dt_fim_consulta_pac_obs = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_ordem = models.DateField(blank=True, null=True)
    cd_senha_master_uni = models.IntegerField(blank=True, null=True)
    nm_operador_obs_retorno = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    fl_status_anterior = models.IntegerField(blank=True, null=True)
    fl_principal = models.CharField(max_length=1, blank=True, null=True)
    cd_grupo_consultorio = models.IntegerField(blank=True, null=True)
    dt_cancela_chamada = models.DateField(blank=True, null=True)
    fl_triagem = models.CharField(max_length=1, blank=True, null=True)
    cd_nivel_classificacao_risco = models.IntegerField(blank=True, null=True)
    cd_operador_inicio_triagem = models.CharField(max_length=20, blank=True, null=True)
    dt_inicio_triagem = models.DateField(blank=True, null=True)
    dt_fim_triagem = models.DateField(blank=True, null=True)
    dt_ind_obs_eme = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_senha_atendimento_sa'


class AuSetor(models.Model):
    fl_imagem_digital = models.CharField(max_length=1, blank=True, null=True)
    fl_impressora_grafica = models.CharField(max_length=1, blank=True, null=True)
    fl_imprime_req_antes_lib = models.CharField(max_length=1, blank=True, null=True)
    fl_imprime_req_apos_lib = models.CharField(max_length=1, blank=True, null=True)
    fl_sala_recuperacao = models.CharField(max_length=1, blank=True, null=True)
    fl_gera_amostra_liberada = models.CharField(max_length=1, blank=True, null=True)
    fl_validacao_web = models.CharField(max_length=1, blank=True, null=True)
    fl_imp_face = models.CharField(max_length=1, blank=True, null=True)
    nu_tempo_validacao_web = models.IntegerField(blank=True, null=True)
    fl_almoxarifado = models.CharField(max_length=1, blank=True, null=True)
    fl_principal = models.CharField(max_length=1, blank=True, null=True)
    fl_cpd = models.CharField(max_length=1, blank=True, null=True)
    fl_faturamento = models.CharField(max_length=1, blank=True, null=True)
    fl_bercario = models.CharField(max_length=1, blank=True, null=True)
    fl_maternidade = models.CharField(max_length=1, blank=True, null=True)
    fl_centro_obstetrico = models.CharField(max_length=1, blank=True, null=True)
    fl_snd = models.CharField(max_length=1, blank=True, null=True)
    fl_restaurante = models.CharField(max_length=1, blank=True, null=True)
    cd_operacao_cr = models.FloatField(blank=True, null=True)
    cd_operacao_db = models.FloatField(blank=True, null=True)
    fl_laboratorio = models.CharField(max_length=1, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    fl_homecare = models.CharField(max_length=1, blank=True, null=True)
    fl_consulta_auto = models.CharField(max_length=1, blank=True, null=True)
    fl_uti = models.CharField(max_length=1, blank=True, null=True)
    fl_hapclinica = models.CharField(max_length=1, blank=True, null=True)
    fl_imp_digital = models.CharField(max_length=1, blank=True, null=True)
    fl_manutencao = models.CharField(max_length=1, blank=True, null=True)
    id_centro_custo_finpac = models.IntegerField(blank=True, null=True)
    fl_controla_lote = models.CharField(max_length=1, blank=True, null=True)
    cd_mapa = models.IntegerField(blank=True, null=True)
    fl_projeto_social = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_req = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_reposicao = models.CharField(max_length=6, blank=True, null=True)
    fl_produtividade_medica = models.CharField(max_length=1, blank=True, null=True)
    fl_comanda_automatica = models.CharField(max_length=1, blank=True, null=True)
    dt_comanda_aut_apartir = models.DateField(blank=True, null=True)
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    nm_setor = models.CharField(max_length=45, blank=True, null=True)
    fl_requisita = models.CharField(max_length=1, blank=True, null=True)
    fl_controla = models.CharField(max_length=1, blank=True, null=True)
    fl_transforma = models.CharField(max_length=1, blank=True, null=True)
    fl_aloca_pessoal = models.CharField(max_length=1, blank=True, null=True)
    fl_recebe = models.CharField(max_length=1, blank=True, null=True)
    fl_posto = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_sup = models.CharField(max_length=6, blank=True, null=True)
    ds_localizacao = models.CharField(max_length=45, blank=True, null=True)
    fl_interna = models.CharField(max_length=1, blank=True, null=True)
    fl_externo = models.CharField(max_length=1, blank=True, null=True)
    fl_alimentacao = models.CharField(max_length=1, blank=True, null=True)
    fl_estoque_proprio = models.CharField(max_length=1, blank=True, null=True)
    nu_telefone_principal = models.CharField(max_length=10, blank=True, null=True)
    nu_telefone_secundario = models.CharField(max_length=10, blank=True, null=True)
    ds_observacao = models.CharField(max_length=200, blank=True, null=True)
    fl_ped_exa_auto = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_emp = models.CharField(max_length=3, blank=True, null=True)
    cd_setor_grupo = models.CharField(max_length=6, blank=True, null=True)
    nu_pedido_inf = models.IntegerField(blank=True, null=True)
    nu_pedido_sup = models.IntegerField(blank=True, null=True)
    cd_setor_dev = models.CharField(max_length=6, blank=True, null=True)
    fl_recepcao = models.CharField(max_length=1, blank=True, null=True)
    fl_sadt = models.CharField(max_length=1, blank=True, null=True)
    fl_centro_cirurgico = models.CharField(max_length=1, blank=True, null=True)
    fl_emergencia = models.CharField(max_length=1, blank=True, null=True)
    fl_hemodinamica = models.CharField(max_length=1, blank=True, null=True)
    fl_farmacia_central = models.CharField(max_length=1, blank=True, null=True)
    fl_farmacia_apoio = models.CharField(max_length=1, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    fl_fornecedor = models.CharField(max_length=1, blank=True, null=True)
    fl_farmacia_consignados = models.CharField(max_length=1, blank=True, null=True)
    fl_trauma = models.CharField(max_length=1, blank=True, null=True)
    fl_ficha_atend_reduzida = models.CharField(max_length=1, blank=True, null=True)
    fl_pendencia_automatica = models.CharField(max_length=1, blank=True, null=True)
    id_almox = models.IntegerField(blank=True, null=True)
    fl_amb_externo_empresas = models.CharField(max_length=1, blank=True, null=True)
    hr_horario_solucao = models.CharField(max_length=5, blank=True, null=True)
    cd_setor_destino_padrao = models.CharField(max_length=6, blank=True, null=True)
    fl_sala_gesso = models.CharField(max_length=1, blank=True, null=True)
    fl_sala_peq_cirurgia = models.CharField(max_length=1, blank=True, null=True)
    fl_imp_digital_exame = models.CharField(max_length=1, blank=True, null=True)
    fl_validacao_web_exame = models.CharField(max_length=1, blank=True, null=True)
    fl_pediatria = models.CharField(max_length=1, blank=True, null=True)
    fl_log_imagem_digital = models.CharField(max_length=1, blank=True, null=True)
    fl_imagem_foto = models.CharField(max_length=1, blank=True, null=True)
    fl_controla_recebimento = models.CharField(max_length=1, blank=True, null=True)
    fl_imagens_pacs = models.CharField(max_length=1, blank=True, null=True)
    fl_densidade_codbar = models.CharField(max_length=4, blank=True, null=True)
    cd_setor_pacs = models.FloatField(blank=True, null=True)
    fl_estoque_rec_tra = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_coleta = models.CharField(max_length=6, blank=True, null=True)
    fl_orcamento_compra = models.CharField(max_length=1, blank=True, null=True)
    fl_tipo_coleta = models.FloatField(blank=True, null=True)
    fl_oncologia = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_frac = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_transacao_erp = models.CharField(max_length=6, blank=True, null=True)
    fl_matmed_redepropria = models.CharField(max_length=1, blank=True, null=True)
    fl_integra_estoque_erp = models.CharField(max_length=1, blank=True, null=True)
    fl_libera_emprestimo = models.CharField(max_length=1, blank=True, null=True)
    fl_exclui_do_ind_ocup = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_estoque = models.CharField(max_length=6, blank=True, null=True)
    fl_contagem_manual = models.CharField(max_length=1, blank=True, null=True)
    fl_implanta_pulseira = models.CharField(max_length=1, blank=True, null=True)
    fl_redepropria_almox = models.CharField(max_length=1, blank=True, null=True)
    fl_sala_observacao = models.CharField(max_length=1, blank=True, null=True)
    cd_mnemonico_setor = models.CharField(max_length=4, blank=True, null=True)
    fl_uso_restrito = models.CharField(max_length=1, blank=True, null=True)
    fl_exige_leitura_material_mob = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_setor'


class AuSimilar(models.Model):
    cd_acao = models.NullBooleanField()
    cd_similar = models.CharField(max_length=4, blank=True, null=True)
    nm_similar = models.CharField(max_length=45, blank=True, null=True)
    qt_estoque_minimo = models.FloatField(blank=True, null=True)
    qt_lote_reposicao = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_similar'


class AuSumarioOncoHist(models.Model):
    cd_acao = models.FloatField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    prc_estoque_fin_estoq = models.FloatField(blank=True, null=True)
    qtd_estoque_ini_unit = models.FloatField(blank=True, null=True)
    qtd_estoque_ini_man_unit = models.FloatField(blank=True, null=True)
    qtd_autorizado_estoq = models.FloatField(blank=True, null=True)
    qtd_agendado_estoq = models.FloatField(blank=True, null=True)
    qtd_comprado_unit = models.FloatField(blank=True, null=True)
    qtd_planejado_estoq = models.FloatField(blank=True, null=True)
    qtd_manipulado_estoq = models.FloatField(blank=True, null=True)
    qtd_administrado_estoq = models.FloatField(blank=True, null=True)
    qtd_perda_estab_estoq = models.FloatField(blank=True, null=True)
    qtd_faturado_estoq = models.FloatField(blank=True, null=True)
    qtd_estoque_fin_man_unit = models.FloatField(blank=True, null=True)
    qtd_estoque_fin_unit = models.FloatField(blank=True, null=True)
    prc_estoque_ini_unit = models.FloatField(blank=True, null=True)
    prc_estoque_ini_man_unit = models.FloatField(blank=True, null=True)
    prc_autorizado_estoq = models.FloatField(blank=True, null=True)
    prc_agendado_estoq = models.FloatField(blank=True, null=True)
    prc_comprado_unit = models.FloatField(blank=True, null=True)
    prc_planejado_estoq = models.FloatField(blank=True, null=True)
    prc_manipulado_estoq = models.FloatField(blank=True, null=True)
    prc_administrado_estoq = models.FloatField(blank=True, null=True)
    prc_perda_estab_estoq = models.FloatField(blank=True, null=True)
    prc_faturado_estoq = models.FloatField(blank=True, null=True)
    prc_estoque_fin_man_unit = models.FloatField(blank=True, null=True)
    prc_estoque_fin_unit = models.FloatField(blank=True, null=True)
    periodo = models.FloatField(blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_mat_med = models.FloatField(blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_estoque_ini = models.FloatField(blank=True, null=True)
    qtd_estoque_ini_man = models.FloatField(blank=True, null=True)
    qtd_autorizado = models.FloatField(blank=True, null=True)
    qtd_agendado = models.FloatField(blank=True, null=True)
    qtd_comprado = models.FloatField(blank=True, null=True)
    qtd_planejado = models.FloatField(blank=True, null=True)
    qtd_manipulado = models.FloatField(blank=True, null=True)
    qtd_administrado = models.FloatField(blank=True, null=True)
    qtd_perda_estab = models.FloatField(blank=True, null=True)
    qtd_faturado = models.FloatField(blank=True, null=True)
    qtd_estoque_fin_man = models.FloatField(blank=True, null=True)
    qtd_estoque_fin = models.FloatField(blank=True, null=True)
    prc_estoque_ini_estoq = models.FloatField(blank=True, null=True)
    prc_estoque_ini_man_estoq = models.FloatField(blank=True, null=True)
    prc_autorizado_unit = models.FloatField(blank=True, null=True)
    prc_agendado_unit = models.FloatField(blank=True, null=True)
    prc_comprado_estoq = models.FloatField(blank=True, null=True)
    prc_planejado_unit = models.FloatField(blank=True, null=True)
    prc_manipulado_unit = models.FloatField(blank=True, null=True)
    prc_administrado_unit = models.FloatField(blank=True, null=True)
    prc_perda_estab_unit = models.FloatField(blank=True, null=True)
    prc_faturado_unit = models.FloatField(blank=True, null=True)
    prc_estoque_fin_man_estoq = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_sumario_onco_hist'


class AuTaxas(models.Model):
    cd_acao = models.NullBooleanField()
    cd_taxas = models.CharField(max_length=8, blank=True, null=True)
    cd_grupo_taxas = models.CharField(max_length=2, blank=True, null=True)
    nm_taxas = models.CharField(max_length=240, blank=True, null=True)
    nr_taxas = models.CharField(max_length=60, blank=True, null=True)
    cd_classe_acomodacao = models.CharField(max_length=60, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_taxas'


class AuTaxasConvenio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_taxas = models.CharField(max_length=8, blank=True, null=True)
    cd_taxas_convenio = models.CharField(max_length=8, blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_plano_convenio = models.IntegerField(blank=True, null=True)
    fl_pagamento = models.CharField(max_length=1, blank=True, null=True)
    nm_taxas_convenio = models.CharField(max_length=240, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_taxas_convenio'


class AuTipoDevolucao(models.Model):
    cd_tipo_devolucao = models.NullBooleanField()
    ds_tipo_devolucao = models.CharField(max_length=50, blank=True, null=True)
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_tipo_devolucao'


class AuTipoDocumentoEscaneavel(models.Model):
    cd_acao = models.NullBooleanField()
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    fl_obrigatorio = models.NullBooleanField()
    fl_remocao_imediata = models.NullBooleanField()
    cd_tipo_documento_escaneavel = models.FloatField(blank=True, null=True)
    ds_tipo_documento_escaneavel = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_tipo_documento_escaneavel'


class AuTipoParecer(models.Model):
    cd_tipo_parecer = models.IntegerField(blank=True, null=True)
    nm_tipo_parecer = models.CharField(max_length=45, blank=True, null=True)
    qt_tempo_atendimento = models.IntegerField(blank=True, null=True)
    cd_unidade_tempo_atend = models.CharField(max_length=2, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    dt_criacao = models.DateField(blank=True, null=True)
    nm_operador_criacao = models.CharField(max_length=10, blank=True, null=True)
    dt_ult_atu = models.DateField(blank=True, null=True)
    nm_operador_atu = models.CharField(max_length=10, blank=True, null=True)
    cd_acao = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'au_tipo_parecer'


class AuTipoParecerDetalhe(models.Model):
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_especialidade_detalhe = models.IntegerField(blank=True, null=True)
    cd_tipo_parecer = models.IntegerField(blank=True, null=True)
    dt_criacao = models.DateField(blank=True, null=True)
    nm_operador_criacao = models.CharField(max_length=10, blank=True, null=True)
    dt_ult_atu = models.DateField(blank=True, null=True)
    nm_operador_atu = models.CharField(max_length=10, blank=True, null=True)
    cd_acao = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'au_tipo_parecer_detalhe'


class AuUltimaCompra(models.Model):
    cd_acao = models.NullBooleanField()
    cd_material = models.FloatField(blank=True, null=True)
    dt_ultima_compra = models.DateField(blank=True, null=True)
    vl_ultima_compra = models.FloatField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_ultima_compra'


class AuUnidadeAtendimento(models.Model):
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    nm_logotipo_unidade = models.CharField(max_length=10, blank=True, null=True)
    nu_cgc_cpf = models.FloatField(blank=True, null=True)
    nu_ins_est = models.CharField(max_length=20, blank=True, null=True)
    nu_ins_mun = models.CharField(max_length=20, blank=True, null=True)
    nm_municipio = models.CharField(max_length=45, blank=True, null=True)
    cd_uf = models.CharField(max_length=45, blank=True, null=True)
    nm_endereco = models.CharField(max_length=45, blank=True, null=True)
    nm_titular = models.CharField(max_length=45, blank=True, null=True)
    nu_serie = models.CharField(max_length=10, blank=True, null=True)
    cd_pessoa_cobra = models.FloatField(blank=True, null=True)
    nm_path_logotipo = models.CharField(max_length=80, blank=True, null=True)
    cd_vi_associado = models.FloatField(blank=True, null=True)
    qt_mult_conv_proprio = models.FloatField(blank=True, null=True)
    cd_acao = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_unidade_atendimento'


class AuUsuPreCadastroHapvida(models.Model):
    cd_acao_audit = models.FloatField(blank=True, null=True)
    cd_operador_audit = models.CharField(max_length=30, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    nu_cpf = models.FloatField(blank=True, null=True)
    nu_controle = models.FloatField(blank=True, null=True)
    nu_seq_doc = models.FloatField(blank=True, null=True)
    cd_doc_controle_boleto = models.CharField(max_length=30, blank=True, null=True)
    dt_pagamento = models.DateField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=400, blank=True, null=True)
    ds_arquivo = models.CharField(max_length=256, blank=True, null=True)
    dt_processamento = models.DateField(blank=True, null=True)
    dt_validade = models.DateField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_usu_pre_cadastro_hapvida'


class AuVlMatMedBrasindi(models.Model):
    cd_acao = models.NullBooleanField()
    cd_tabela_mat_med = models.IntegerField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    vl_mat_med = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_vigencia = models.DateField(blank=True, null=True)
    cd_unidade = models.CharField(max_length=2, blank=True, null=True)
    fl_tipo = models.CharField(max_length=1, blank=True, null=True)
    pc_alteracao = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_vl_mat_med_brasindi'


class AuVlMatMedConvenio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_tabela_mat_med = models.IntegerField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    vl_mat_med = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_vigencia = models.DateField(blank=True, null=True)
    cd_unidade = models.CharField(max_length=2, blank=True, null=True)
    fl_tipo = models.CharField(max_length=1, blank=True, null=True)
    pc_alteracao = models.IntegerField(blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_vl_mat_med_convenio'


class AuVlProcedimentoConvenio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_tabela_procedimento = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    vl_procedimento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_vigencia = models.DateField(blank=True, null=True)
    vl_particular = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fl_tipo = models.CharField(max_length=1, blank=True, null=True)
    pc_alteracao = models.IntegerField(blank=True, null=True)
    qt_filme_m2 = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    qt_um_custo = models.FloatField(blank=True, null=True)
    qt_auxiliares = models.FloatField(blank=True, null=True)
    nu_porte_anestesico = models.FloatField(blank=True, null=True)
    qt_incidencia = models.FloatField(blank=True, null=True)
    cd_porte_procedimento = models.CharField(max_length=5, blank=True, null=True)
    qt_porte_procedimento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_vl_procedimento_convenio'


class AuVlTaxasConvenio(models.Model):
    cd_acao = models.NullBooleanField()
    cd_tabela_taxa = models.IntegerField(blank=True, null=True)
    cd_taxas = models.CharField(max_length=8, blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    vl_taxas = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_vigencia = models.DateField(blank=True, null=True)
    fl_tipo = models.CharField(max_length=1, blank=True, null=True)
    pc_alteracao = models.IntegerField(blank=True, null=True)
    qt_ch = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dt_audit = models.DateField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_vl_taxas_convenio'


class BkpMetodoProcedimento(models.Model):
    cd_procedimento = models.CharField(max_length=8)
    cd_metodo_realizado = models.IntegerField()
    cd_metodo_usual = models.CharField(max_length=1, blank=True, null=True)
    dt_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_laboratorio_apoio = models.FloatField(blank=True, null=True)
    cd_laboratorio_ter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bkp_metodo_procedimento'


class BkpMetodoRealizado(models.Model):
    cd_metodo_realizado = models.IntegerField()
    ds_metodo_realizado = models.CharField(max_length=100, blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    dt_vigencia = models.DateField(blank=True, null=True)
    fl_filial = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bkp_metodo_realizado'


class BkpMetodoRealizadoFilial(models.Model):
    cd_metodo_realizado = models.IntegerField()
    cd_unidade_atendimento = models.CharField(max_length=3)
    fl_ativo = models.CharField(max_length=1)
    cd_operador = models.CharField(max_length=30)
    dt_modificacao = models.DateField()

    class Meta:
        managed = False
        db_table = 'bkp_metodo_realizado_filial'


class BkpParamParametroReferencia(models.Model):
    cd_ref = models.FloatField()
    cd_procedimento = models.CharField(max_length=8)
    cd_metodo_realizado = models.IntegerField()
    cd_sexo = models.CharField(max_length=1)
    fl_unidade_tempo = models.CharField(max_length=1)
    qt_idade_inicial = models.IntegerField()
    qt_idade_final = models.IntegerField()
    fl_datacheck = models.CharField(max_length=1, blank=True, null=True)
    dt_ini_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bkp_param_parametro_referencia'


class BkpProcTextoResultado(models.Model):
    cd_procedimento = models.CharField(max_length=8)
    cd_metodo_realizado = models.IntegerField()
    cd_parametro_referencia = models.IntegerField()
    cd_ordem = models.IntegerField()
    ds_texto_resultado = models.CharField(max_length=60)
    fl_referencia = models.CharField(max_length=1)
    cd_ref = models.FloatField()

    class Meta:
        managed = False
        db_table = 'bkp_proc_texto_resultado'


class BkpProcedParamReferencia(models.Model):
    cd_procedimento = models.CharField(max_length=8)
    cd_metodo_realizado = models.IntegerField()
    cd_parametro_referencia = models.IntegerField()
    cd_ordem = models.IntegerField()
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    qt_idade_inicial = models.IntegerField(blank=True, null=True)
    qt_idade_final = models.IntegerField(blank=True, null=True)
    fl_unidade_tempo = models.CharField(max_length=1, blank=True, null=True)
    vl_parametro_minimo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vl_parametro_maximo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vl_parametro_normal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    fl_valor_parametro = models.CharField(max_length=1, blank=True, null=True)
    ds_valor_parametro = models.CharField(max_length=2000, blank=True, null=True)
    cd_unidade_usual = models.CharField(max_length=2, blank=True, null=True)
    vl_formula = models.CharField(max_length=50, blank=True, null=True)
    qt_decimal = models.NullBooleanField()
    dt_vigencia = models.DateField(blank=True, null=True)
    dt_fim_vigencia = models.DateField(blank=True, null=True)
    cd_fator_conversao = models.FloatField(blank=True, null=True)
    fl_aparecer_laudo = models.CharField(max_length=1, blank=True, null=True)
    cd_referencia = models.CharField(max_length=2, blank=True, null=True)
    fl_tipo_valor = models.CharField(max_length=1, blank=True, null=True)
    ds_texto_resultado = models.CharField(max_length=60, blank=True, null=True)
    cd_ref = models.FloatField(blank=True, null=True)
    cd_proced_param_referencia = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bkp_proced_param_referencia'


class CpVlMatMedConvenio(models.Model):
    cd_tabela_mat_med = models.IntegerField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_um = models.FloatField(blank=True, null=True)
    vl_mat_med = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dt_vigencia = models.DateField(blank=True, null=True)
    cd_unidade = models.CharField(max_length=2, blank=True, null=True)
    fl_tipo = models.CharField(max_length=1, blank=True, null=True)
    pc_alteracao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cp_vl_mat_med_convenio'


class CreateJavaLobTable(models.Model):
    name = models.CharField(unique=True, max_length=700, blank=True, null=True)
    lob = models.BinaryField(blank=True, null=True)
    loadtime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'create$java$lob$table'


class DeptreeTemptab(models.Model):
    object_id = models.FloatField(blank=True, null=True)
    referenced_object_id = models.FloatField(blank=True, null=True)
    nest_level = models.FloatField(blank=True, null=True)
    seq_field = models.FloatField(db_column='seq#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'deptree_temptab'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True, null=True)
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Dummy(models.Model):
    dummy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dummy'


class GtParametroFormulario(models.Model):
    nm_parametro = models.CharField(primary_key=True, max_length=256)
    vl_parametro = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gt_parametro_formulario'


class MenuBAppl(models.Model):
    application_name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=15)
    file_name = models.CharField(max_length=30)
    creation_date = models.DateField()
    creator = models.CharField(max_length=30)
    version_release_nr = models.FloatField()
    last_release_date = models.DateField(blank=True, null=True)
    menu_directory = models.CharField(max_length=50, blank=True, null=True)
    identification = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'menu_b_appl'


class MenuBApplGrp(models.Model):
    application_name = models.CharField(max_length=30)
    group_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'menu_b_appl_grp'


class MenuBCircle(models.Model):
    seq_key = models.FloatField()
    menu_name = models.CharField(max_length=30)
    command_line = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = 'menu_b_circle'


class MenuBGroup(models.Model):
    group_name = models.CharField(max_length=30)
    debug_allowed = models.CharField(max_length=1)
    os_comm_allowed = models.CharField(max_length=1)
    bgm_allowed = models.CharField(max_length=1)
    object_text_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'menu_b_group'


class MenuBGrpPriv(models.Model):
    application_name = models.CharField(max_length=30)
    group_name = models.CharField(max_length=30)
    privilege_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'menu_b_grp_priv'


class MenuBInfo(models.Model):
    menu_name = models.CharField(max_length=30)
    application_name = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    sub_title = models.CharField(max_length=40)
    bottom_title = models.CharField(max_length=72, blank=True, null=True)
    object_text_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'menu_b_info'


class MenuBObjText(models.Model):
    application_name = models.CharField(max_length=30)
    object_text_id = models.FloatField()
    object_text_order = models.FloatField()
    object_text = models.CharField(max_length=78, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_b_obj_text'


class MenuBOption(models.Model):
    menu_name = models.CharField(max_length=30)
    application_name = models.CharField(max_length=30)
    option_number = models.FloatField()
    short_name = models.CharField(max_length=15)
    displayed = models.CharField(max_length=1)
    option_text = models.CharField(max_length=70)
    object_text_id = models.FloatField()
    command_type = models.FloatField()
    command_line = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = 'menu_b_option'


class MenuBParam(models.Model):
    substitution_string = models.CharField(max_length=2)
    application_name = models.CharField(max_length=30)
    par_size = models.FloatField()
    par_def = models.CharField(max_length=64, blank=True, null=True)
    echo = models.CharField(max_length=1)
    must_fill = models.CharField(max_length=1)
    response_required = models.CharField(max_length=1)
    upper_case = models.CharField(max_length=1)
    object_text_id = models.FloatField(blank=True, null=True)
    prompt = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_b_param'


class MenuBParmXref(models.Model):
    menu_name = models.CharField(max_length=30)
    application_name = models.CharField(max_length=30)
    substitution_string = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'menu_b_parm_xref'


class MenuBPriv(models.Model):
    privilege_id = models.FloatField()
    privilege_type = models.CharField(max_length=3)
    application_name = models.CharField(max_length=30)
    menu_name = models.CharField(max_length=30)
    option_number = models.FloatField()

    class Meta:
        managed = False
        db_table = 'menu_b_priv'


class MenuBProcedure(models.Model):
    application_name = models.CharField(max_length=30)
    procedure_name = models.CharField(max_length=30)
    object_text_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'menu_b_procedure'


class MenuBRef(models.Model):
    application_name = models.CharField(max_length=30)
    ref_type = models.FloatField()
    ref_app_name = models.CharField(max_length=30)
    ref_menu_name = models.CharField(max_length=30, blank=True, null=True)
    ref_opt_name = models.CharField(max_length=15, blank=True, null=True)
    ref_parm_name = models.CharField(max_length=2, blank=True, null=True)
    ref_proc_name = models.CharField(max_length=30, blank=True, null=True)
    new_menu_name = models.CharField(max_length=30, blank=True, null=True)
    new_opt_name = models.CharField(max_length=15, blank=True, null=True)
    new_parm_name = models.CharField(max_length=2, blank=True, null=True)
    new_proc_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_b_ref'


class MenuBUser(models.Model):
    group_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'menu_b_user'


class MvProtocolos(models.Model):
    id = models.FloatField(blank=True, null=True)
    url = models.CharField(max_length=4000, blank=True, null=True)
    codigo_atendimento = models.FloatField(blank=True, null=True)
    cd_protocolo = models.CharField(max_length=255, blank=True, null=True)
    nm_protocolo = models.CharField(max_length=1000, blank=True, null=True)
    cd_modelo = models.FloatField(blank=True, null=True)
    passo_corrente = models.CharField(max_length=4000, blank=True, null=True)
    finalizado = models.CharField(max_length=1, blank=True, null=True)
    abortado = models.CharField(max_length=1, blank=True, null=True)
    codigo_paciente = models.FloatField(blank=True, null=True)
    paciente = models.CharField(max_length=256, blank=True, null=True)
    profissional = models.CharField(max_length=256, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)
    data_conclusao = models.DateField(blank=True, null=True)
    tempo_execucao = models.FloatField(blank=True, null=True)
    justificativa = models.CharField(max_length=4000, blank=True, null=True)
    visual_attribute = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mv_protocolos'


class PixeonIntegExames(models.Model):
    na_accessionnumber = models.CharField(primary_key=True, max_length=16)
    na_datetimeperformed = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pixeon_integ_exames'


class PixeonIntegExamsN1(models.Model):
    na_accessionumber = models.CharField(max_length=16, blank=True, null=True)
    na_firstreceivetimestamp = models.BigIntegerField(blank=True, null=True)
    na_lastreceivetimestamp = models.BigIntegerField(blank=True, null=True)
    na_firstacqdatetime = models.CharField(max_length=15, blank=True, null=True)
    na_lastacqdatetime = models.CharField(max_length=15, blank=True, null=True)
    number_of_images = models.FloatField(blank=True, null=True)
    na_unit = models.CharField(max_length=255, blank=True, null=True)
    exam_available = models.CharField(max_length=1, blank=True, null=True)
    na_datetimeintegrated = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pixeon_integ_exams_n1'


class PixeonIntegExamsN2(models.Model):
    na_accessionumber = models.CharField(max_length=16, blank=True, null=True)
    na_firstreceivetimestamp = models.BigIntegerField(blank=True, null=True)
    na_lastreceivetimestamp = models.BigIntegerField(blank=True, null=True)
    number_of_images = models.FloatField(blank=True, null=True)
    na_unit = models.CharField(max_length=255, blank=True, null=True)
    na_datetimeintegrated = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pixeon_integ_exams_n2'


class PixeonIntegExamsN3(models.Model):
    na_accessionumber = models.CharField(max_length=16, blank=True, null=True)
    na_firstreceivetimestamp = models.BigIntegerField(blank=True, null=True)
    na_lastreceivetimestamp = models.BigIntegerField(blank=True, null=True)
    number_of_images = models.FloatField(blank=True, null=True)
    na_unit = models.CharField(max_length=255, blank=True, null=True)
    na_datetimeintegrated = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pixeon_integ_exams_n3'


class PixeonReport(models.Model):
    na_accessionumber = models.CharField(primary_key=True, max_length=50)
    nu_integrated = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pixeon_report'


class PixeonReportIntegrated(models.Model):
    na_accessionumber = models.CharField(primary_key=True, max_length=50)
    na_datetimeperformed = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pixeon_report_integrated'


class PlanTable(models.Model):
    statement_id = models.CharField(max_length=30, blank=True, null=True)
    plan_id = models.FloatField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=4000, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)
    object_node = models.CharField(max_length=128, blank=True, null=True)
    object_owner = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=30, blank=True, null=True)
    object_alias = models.CharField(max_length=65, blank=True, null=True)
    object_instance = models.BigIntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    optimizer = models.CharField(max_length=255, blank=True, null=True)
    search_columns = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    depth = models.BigIntegerField(blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)
    cost = models.BigIntegerField(blank=True, null=True)
    cardinality = models.BigIntegerField(blank=True, null=True)
    bytes = models.BigIntegerField(blank=True, null=True)
    other_tag = models.CharField(max_length=255, blank=True, null=True)
    partition_start = models.CharField(max_length=255, blank=True, null=True)
    partition_stop = models.CharField(max_length=255, blank=True, null=True)
    partition_id = models.BigIntegerField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)  # This field type is a guess.
    distribution = models.CharField(max_length=30, blank=True, null=True)
    cpu_cost = models.BigIntegerField(blank=True, null=True)
    io_cost = models.BigIntegerField(blank=True, null=True)
    temp_space = models.BigIntegerField(blank=True, null=True)
    access_predicates = models.CharField(max_length=4000, blank=True, null=True)
    filter_predicates = models.CharField(max_length=4000, blank=True, null=True)
    projection = models.CharField(max_length=4000, blank=True, null=True)
    time = models.BigIntegerField(blank=True, null=True)
    qblock_name = models.CharField(max_length=30, blank=True, null=True)
    other_xml = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan_table'


class Tb49PsSintetica(models.Model):
    nm_origem = models.CharField(max_length=1, blank=True, null=True)
    nm_cidade_endereco = models.CharField(max_length=60, blank=True, null=True)
    cd_unidade_atendimento = models.CharField(max_length=3, blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    nm_clinica = models.CharField(max_length=20, blank=True, null=True)
    dt_atendimento = models.DateField(blank=True, null=True)
    fl_consulta = models.FloatField(blank=True, null=True)
    fl_exame = models.FloatField(blank=True, null=True)
    fl_exame_ac_pln = models.FloatField(blank=True, null=True)
    fl_exame_ac_proc = models.FloatField(blank=True, null=True)
    vl_total_cons = models.FloatField(blank=True, null=True)
    vl_total_exa = models.FloatField(blank=True, null=True)
    vl_total_exa_ac = models.FloatField(blank=True, null=True)
    vl_total_matmed = models.FloatField(blank=True, null=True)
    vl_total_tx = models.FloatField(blank=True, null=True)
    vl_total_insumo_tipo9 = models.FloatField(blank=True, null=True)
    vl_total_hon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_49ps_sintetica'


class TbAcaoResolucaoParecerAud(models.Model):
    cd_reuniao = models.ForeignKey('TbAcaoResolucaoPendencia', models.DO_NOTHING, db_column='cd_reuniao', primary_key=True)
    cd_ordem_acao = models.ForeignKey('TbAcaoResolucaoPendencia', models.DO_NOTHING, db_column='cd_ordem_acao')
    cd_ordem_parecer_aud = models.IntegerField()
    dt_transacao = models.DateField()
    nm_operador = models.CharField(max_length=10)
    ds_parecer_auditoria = models.TextField()

    class Meta:
        managed = False
        db_table = 'tb_acao_resolucao_parecer_aud'
        unique_together = (('cd_reuniao', 'cd_ordem_acao', 'cd_ordem_parecer_aud'),)


class TbAcaoResolucaoPendencia(models.Model):
    cd_reuniao = models.ForeignKey('TbReuniaoAcompanhamento', models.DO_NOTHING, db_column='cd_reuniao', primary_key=True)
    cd_ordem_acao = models.IntegerField()
    cd_atendimento = models.ForeignKey('TbRegistroVisitaSatisfacao', models.DO_NOTHING, db_column='cd_atendimento', blank=True, null=True)
    cd_ocorrencia_plano = models.ForeignKey('TbRegistroVisitaSatisfacao', models.DO_NOTHING, db_column='cd_ocorrencia_plano', blank=True, null=True)
    cd_ordem_visita = models.ForeignKey('TbRegistroVisitaSatisfacao', models.DO_NOTHING, db_column='cd_ordem_visita', blank=True, null=True)
    ds_acao = models.CharField(max_length=1000, blank=True, null=True)
    dt_previsao_resolucao = models.DateField(blank=True, null=True)
    cd_responsavel = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='cd_responsavel', blank=True, null=True)
    cd_reuniao_vinculada = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_reuniao_vinculada', blank=True, null=True)
    cd_ordem_acao_vinculada = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_ordem_acao_vinculada', blank=True, null=True)
    cd_operador = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='cd_operador', blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_status = models.ForeignKey('TbStatusAcaoReuniao', models.DO_NOTHING, db_column='cd_status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acao_resolucao_pendencia'
        unique_together = (('cd_reuniao', 'cd_ordem_acao'),)


class TbAcessoApresentacao(models.Model):
    cd_tipo_acesso = models.ForeignKey('TbTipoAcesso', models.DO_NOTHING, db_column='cd_tipo_acesso', primary_key=True)
    cd_apresentacao = models.ForeignKey('TbApresentacao', models.DO_NOTHING, db_column='cd_apresentacao')

    class Meta:
        managed = False
        db_table = 'tb_acesso_apresentacao'
        unique_together = (('cd_tipo_acesso', 'cd_apresentacao'),)


class TbAcessoEmpresa(models.Model):
    nm_operador = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='nm_operador', primary_key=True)
    cd_unidade_atendimento = models.ForeignKey('TbUnidadeAtendimento', models.DO_NOTHING, db_column='cd_unidade_atendimento')
    cd_filial = models.ForeignKey('TbFilial', models.DO_NOTHING, db_column='cd_filial')
    cd_setor_operacao = models.CharField(max_length=6, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_ultimo_login = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acesso_empresa'
        unique_together = (('nm_operador', 'cd_unidade_atendimento', 'cd_filial'),)


class TbAcessoFinpac(models.Model):
    cod_usuario = models.CharField(max_length=50, blank=True, null=True)
    nm_operador = models.CharField(max_length=50, blank=True, null=True)
    cod_grupo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acesso_finpac'


class TbAcessoGrupo(models.Model):
    cod_grupo = models.IntegerField(primary_key=True)
    cod_op = models.CharField(max_length=20)
    cd_dia_semana = models.BooleanField()
    qt_hora_inicial = models.IntegerField(blank=True, null=True)
    qt_hora_final = models.IntegerField(blank=True, null=True)
    qt_dias_atras = models.IntegerField(blank=True, null=True)
    qt_hora_limite = models.IntegerField(blank=True, null=True)
    cd_classe = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'tb_acesso_grupo'
        unique_together = (('cod_grupo', 'cod_op', 'cd_dia_semana'),)


class TbAcessoSaidaUrgencia(models.Model):
    cd_setor = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_setor', primary_key=True)
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    hr_inicio = models.IntegerField()
    hr_fim = models.IntegerField()
    nm_operador = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='nm_operador')
    usuario_gravou = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='usuario_gravou', blank=True, null=True)
    dt_usuario_gravou = models.DateField(blank=True, null=True)
    fl_cancela = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acesso_saida_urgencia'
        unique_together = (('cd_setor', 'dt_inicio', 'dt_fim', 'hr_inicio', 'hr_fim', 'nm_operador'),)


class TbAcessoTela(models.Model):
    nm_operador = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='nm_operador', primary_key=True)
    cd_tela = models.CharField(max_length=10)
    cd_dia_semana = models.BooleanField()
    qt_hora_inicial = models.IntegerField()
    qt_hora_final = models.IntegerField()
    qt_dias_atras = models.IntegerField()
    qt_hora_limite = models.IntegerField()
    cd_classe = models.NullBooleanField()
    cod_grupo = models.IntegerField(blank=True, null=True)
    cd_ocorrencia = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tb_acesso_tela'
        unique_together = (('nm_operador', 'cd_tela', 'cd_dia_semana', 'cd_ocorrencia'),)


class TbAcessoUsuario(models.Model):
    cd_tela = models.CharField(primary_key=True, max_length=10)
    cod_usuario = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tb_acesso_usuario'
        unique_together = (('cd_tela', 'cod_usuario'),)


class TbAcoesAuditoria(models.Model):
    cd_acao = models.FloatField(primary_key=True)
    ds_acao = models.CharField(max_length=60, blank=True, null=True)
    cd_tipo_acao = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acoes_auditoria'


class TbAcompanhamentoAnestesia(models.Model):
    cd_atendimento = models.FloatField()
    cd_ocorrencia = models.FloatField()
    cd_ordem = models.FloatField()
    fl_doenca_previa = models.CharField(max_length=1, blank=True, null=True)
    fl_doenca_has = models.CharField(max_length=1, blank=True, null=True)
    fl_doenca_asma = models.CharField(max_length=1, blank=True, null=True)
    fl_doenca_dm = models.CharField(max_length=1, blank=True, null=True)
    fl_doenca_convulsoes = models.CharField(max_length=1, blank=True, null=True)
    fl_doenca_outro = models.CharField(max_length=1, blank=True, null=True)
    ds_doenca_outro = models.CharField(max_length=100, blank=True, null=True)
    fl_uso_medicacao = models.CharField(max_length=1, blank=True, null=True)
    ds_uso_medicacao = models.CharField(max_length=100, blank=True, null=True)
    fl_paciente_estavel = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_instavel = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_consciente = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_inconsciente = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_orientado = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_desorientado = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_eupneico = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_dispneico = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_cooperativo = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_nao_cooperativo = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_calmo = models.CharField(max_length=1, blank=True, null=True)
    fl_paciente_ansioso = models.CharField(max_length=1, blank=True, null=True)
    fl_asa = models.CharField(max_length=3, blank=True, null=True)
    fl_jejum = models.CharField(max_length=3, blank=True, null=True)
    fl_glasgow = models.CharField(max_length=2, blank=True, null=True)
    fl_anestesia_ant = models.CharField(max_length=1, blank=True, null=True)
    ds_anestesia_ant = models.CharField(max_length=100, blank=True, null=True)
    fl_inter_anestesia_ant = models.CharField(max_length=1, blank=True, null=True)
    ds_inter_anestesia_ant = models.CharField(max_length=100, blank=True, null=True)
    ds_exame_fisico = models.CharField(max_length=100, blank=True, null=True)
    ds_ap_respiratorio = models.CharField(max_length=100, blank=True, null=True)
    ds_ap_circulatorio = models.CharField(max_length=100, blank=True, null=True)
    ds_ap_digestivo = models.CharField(max_length=100, blank=True, null=True)
    ds_outro = models.CharField(max_length=100, blank=True, null=True)
    fl_alergias = models.CharField(max_length=1, blank=True, null=True)
    ds_alergias = models.CharField(max_length=100, blank=True, null=True)
    ds_admissao_pa = models.CharField(max_length=10, blank=True, null=True)
    ds_admissao_fc = models.CharField(max_length=5, blank=True, null=True)
    ds_admissao_o2 = models.CharField(max_length=3, blank=True, null=True)
    fl_checagem_material = models.CharField(max_length=1, blank=True, null=True)
    fl_anestesico_venoclise = models.CharField(max_length=1, blank=True, null=True)
    nu_jelco_anestesico = models.CharField(max_length=10, blank=True, null=True)
    fl_monitorizacao_sato2 = models.CharField(max_length=1, blank=True, null=True)
    fl_monitorizacao_pani = models.CharField(max_length=1, blank=True, null=True)
    fl_monitorizacao_cardioscopia = models.CharField(max_length=1, blank=True, null=True)
    fl_monitorizacao_outros = models.CharField(max_length=1, blank=True, null=True)
    ds_monitorizacao_outros = models.CharField(max_length=200, blank=True, null=True)
    ds_anestesica_fentanil = models.CharField(max_length=10, blank=True, null=True)
    hr_anestesica_fetanil = models.FloatField(blank=True, null=True)
    ds_anestesica_midazolam = models.CharField(max_length=10, blank=True, null=True)
    hr_anestesica_midazolam = models.FloatField(blank=True, null=True)
    ds_anestesica_propofol = models.CharField(max_length=10, blank=True, null=True)
    hr_anestesica_propofol = models.FloatField(blank=True, null=True)
    ds_anestesica_escopolamina = models.CharField(max_length=10, blank=True, null=True)
    hr_anestesica_escopolamina = models.FloatField(blank=True, null=True)
    ds_anestesica_outros = models.CharField(max_length=200, blank=True, null=True)
    fl_ventilacao_cateter_nasal = models.CharField(max_length=1, blank=True, null=True)
    ds_ventilacao_cateter_naasl = models.CharField(max_length=5, blank=True, null=True)
    fl_ventilacao_mascara_facial = models.CharField(max_length=1, blank=True, null=True)
    ds_ventilacao_mascara_facial = models.CharField(max_length=5, blank=True, null=True)
    fl_ventilacao_espontanea = models.CharField(max_length=1, blank=True, null=True)
    fl_ventilacao_iot = models.CharField(max_length=1, blank=True, null=True)
    fl_ventilacao_intercorrencias = models.CharField(max_length=1, blank=True, null=True)
    ds_ventilacao_intercorrencia = models.CharField(max_length=200, blank=True, null=True)
    fl_srpa_acordado = models.CharField(max_length=1, blank=True, null=True)
    fl_srpa_sonolento = models.CharField(max_length=1, blank=True, null=True)
    fl_srpa_eupneico = models.CharField(max_length=1, blank=True, null=True)
    fl_srpa_dispneico = models.CharField(max_length=1, blank=True, null=True)
    fl_srpa_estavel = models.CharField(max_length=1, blank=True, null=True)
    fl_srpa_instavel = models.CharField(max_length=1, blank=True, null=True)
    fl_posicao_decubito_esq = models.CharField(max_length=1, blank=True, null=True)
    fl_posicao_decubito_dir = models.CharField(max_length=1, blank=True, null=True)
    fl_posicao_decubito_dorsal = models.CharField(max_length=1, blank=True, null=True)
    fl_exame_colonoscopia = models.CharField(max_length=1, blank=True, null=True)
    fl_exame_tomografia = models.CharField(max_length=1, blank=True, null=True)
    fl_exame_ressonancia = models.CharField(max_length=1, blank=True, null=True)
    fl_exame_rx_contrastado = models.CharField(max_length=1, blank=True, null=True)
    fl_exame_outros = models.CharField(max_length=1, blank=True, null=True)
    ds_exame_outros = models.CharField(max_length=200, blank=True, null=True)
    fl_anestesia_sedacao = models.CharField(max_length=1, blank=True, null=True)
    fl_anestesia_geral = models.CharField(max_length=1, blank=True, null=True)
    fl_anestesia_raquianestesia = models.CharField(max_length=1, blank=True, null=True)
    fl_anestesia_outros = models.CharField(max_length=1, blank=True, null=True)
    ds_anestesia_outros = models.CharField(max_length=100, blank=True, null=True)
    cd_medico_acompanhante = models.FloatField(blank=True, null=True)
    fl_admitido_acordado = models.CharField(max_length=1, blank=True, null=True)
    fl_admitido_sonolento = models.CharField(max_length=1, blank=True, null=True)
    fl_admitido_eupneico = models.CharField(max_length=1, blank=True, null=True)
    fl_admitido_dispneico = models.CharField(max_length=1, blank=True, null=True)
    fl_admitido_estavel = models.CharField(max_length=1, blank=True, null=True)
    fl_admitido_instavel = models.CharField(max_length=1, blank=True, null=True)
    hr_admitido_spra = models.FloatField(blank=True, null=True)
    fl_moni_spra_sato2 = models.CharField(max_length=1, blank=True, null=True)
    fl_moni_spra_pani = models.CharField(max_length=1, blank=True, null=True)
    fl_moni_spra_cardioscopia = models.CharField(max_length=1, blank=True, null=True)
    fl_moni_spra_outros = models.CharField(max_length=1, blank=True, null=True)
    ds_moni_spra_outros = models.CharField(max_length=100, blank=True, null=True)
    ds_admissao_spra_pa = models.CharField(max_length=20, blank=True, null=True)
    ds_admissao_spra_fc = models.CharField(max_length=5, blank=True, null=True)
    ds_admissao_spra_sat02 = models.CharField(max_length=5, blank=True, null=True)
    hr_admissao_spra = models.FloatField(blank=True, null=True)
    fl_liberado_acordado = models.CharField(max_length=1, blank=True, null=True)
    fl_liberado_sonolento = models.CharField(max_length=1, blank=True, null=True)
    fl_liberado_eupneico = models.CharField(max_length=1, blank=True, null=True)
    fl_liberado_dispneico = models.CharField(max_length=1, blank=True, null=True)
    fl_liberado_estavel = models.CharField(max_length=1, blank=True, null=True)
    fl_liberado_instavel = models.CharField(max_length=1, blank=True, null=True)
    hr_liberado_spra = models.FloatField(blank=True, null=True)
    ds_liberado_spra_pa = models.CharField(max_length=20, blank=True, null=True)
    ds_liberado_spra_fc = models.CharField(max_length=5, blank=True, null=True)
    ds_liberado_spra_sat02 = models.CharField(max_length=5, blank=True, null=True)
    fl_liberado_ar = models.CharField(max_length=1, blank=True, null=True)
    fl_liberado_queixas = models.CharField(max_length=1, blank=True, null=True)
    ds_liberado_queixas = models.CharField(max_length=200, blank=True, null=True)
    fl_liberado_intercorrencia = models.CharField(max_length=1, blank=True, null=True)
    ds_liberado_intercorrencia = models.CharField(max_length=200, blank=True, null=True)
    fl_liberado_acompanhante = models.CharField(max_length=1, blank=True, null=True)
    fl_liberado_deambulando = models.CharField(max_length=1, blank=True, null=True)
    fl_liberado_eva = models.CharField(max_length=2, blank=True, null=True)
    cd_operador = models.CharField(max_length=10)
    dt_cadastro = models.DateField()
    nu_intervalo = models.FloatField(blank=True, null=True)
    hr_anestesia_ini = models.FloatField(blank=True, null=True)
    hr_anestesia_fim = models.FloatField(blank=True, null=True)
    hr_cirurgia_ini = models.FloatField(blank=True, null=True)
    hr_cirurgia_fim = models.FloatField(blank=True, null=True)
    cd_enfermeiro_acompanhante = models.FloatField(blank=True, null=True)
    ds_evolucao_medica = models.CharField(max_length=4000, blank=True, null=True)
    ds_evolucao_enfermagem = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acompanhamento_anestesia'
        unique_together = (('cd_atendimento', 'cd_ocorrencia', 'cd_ordem'),)


class TbAcompanhamentoContraste(models.Model):
    cd_atendimento = models.FloatField()
    cd_ocorrencia = models.FloatField()
    cd_ordem = models.FloatField()
    fl_hipertensao_arterial = models.CharField(max_length=1, blank=True, null=True)
    fl_tabagismo = models.CharField(max_length=1, blank=True, null=True)
    fl_neoplasias = models.CharField(max_length=1, blank=True, null=True)
    fl_doenca_cardiovascular = models.CharField(max_length=1, blank=True, null=True)
    fl_diabetes = models.CharField(max_length=1, blank=True, null=True)
    fl_doenca_renal = models.CharField(max_length=1, blank=True, null=True)
    fl_realizou_cirurgias = models.CharField(max_length=1, blank=True, null=True)
    ds_realizou_cirurgia = models.CharField(max_length=300, blank=True, null=True)
    fl_outro_problema = models.CharField(max_length=1, blank=True, null=True)
    ds_outro_problema = models.CharField(max_length=300, blank=True, null=True)
    fl_alergia_constraste = models.CharField(max_length=1, blank=True, null=True)
    ds_alergia_constraste = models.CharField(max_length=300, blank=True, null=True)
    fl_alergia_medicamentos = models.CharField(max_length=1, blank=True, null=True)
    ds_alergia_medicamentos = models.CharField(max_length=300, blank=True, null=True)
    fl_alergia_frutos_mar = models.CharField(max_length=1, blank=True, null=True)
    ds_alergia_frutos_mar = models.CharField(max_length=300, blank=True, null=True)
    fl_alergia_outros = models.CharField(max_length=1, blank=True, null=True)
    ds_alergia_outros = models.CharField(max_length=300, blank=True, null=True)
    fl_med_sivastatina = models.CharField(max_length=1, blank=True, null=True)
    fl_med_metformina = models.CharField(max_length=1, blank=True, null=True)
    fl_med_hidralazina = models.CharField(max_length=1, blank=True, null=True)
    fl_med_enalapril = models.CharField(max_length=1, blank=True, null=True)
    fl_med_aas = models.CharField(max_length=1, blank=True, null=True)
    fl_med_metropolol = models.CharField(max_length=1, blank=True, null=True)
    fl_med_furosemida = models.CharField(max_length=1, blank=True, null=True)
    fl_med_nifedipina = models.CharField(max_length=1, blank=True, null=True)
    fl_med_caverdilol = models.CharField(max_length=1, blank=True, null=True)
    fl_med_atenolol = models.CharField(max_length=1, blank=True, null=True)
    fl_uso_dentaria = models.CharField(max_length=1, blank=True, null=True)
    fl_uso_ortodontico = models.CharField(max_length=1, blank=True, null=True)
    fl_uso_ortopedicos = models.CharField(max_length=1, blank=True, null=True)
    fl_uso_marcapasso = models.CharField(max_length=1, blank=True, null=True)
    fl_uso_outros = models.CharField(max_length=1, blank=True, null=True)
    ds_uso_outros = models.CharField(max_length=300, blank=True, null=True)
    fl_check_orientado = models.CharField(max_length=1, blank=True, null=True)
    fl_check_pre_medicacao = models.CharField(max_length=1, blank=True, null=True)
    hr_check_pre_inicio = models.FloatField(blank=True, null=True)
    hr_check_pre_fim = models.FloatField(blank=True, null=True)
    fl_check_adornos = models.CharField(max_length=1, blank=True, null=True)
    fl_check_jejum = models.CharField(max_length=1, blank=True, null=True)
    hr_check_sinais_inicio = models.FloatField(blank=True, null=True)
    hr_check_sinais_fim = models.FloatField(blank=True, null=True)
    ds_check_temperatura = models.CharField(max_length=5, blank=True, null=True)
    ds_check_pulso = models.CharField(max_length=5, blank=True, null=True)
    ds_check_fc = models.CharField(max_length=5, blank=True, null=True)
    ds_check_pa = models.CharField(max_length=10, blank=True, null=True)
    ds_check_o2 = models.CharField(max_length=10, blank=True, null=True)
    fl_check_ureia = models.CharField(max_length=1, blank=True, null=True)
    fl_check_creatinina = models.CharField(max_length=1, blank=True, null=True)
    ds_check_peso = models.CharField(max_length=10, blank=True, null=True)
    ds_check_altura = models.CharField(max_length=10, blank=True, null=True)
    fl_puncao_mebro_dir = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_mebro_esq = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_infiltracao = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_flebite = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_esclerose = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_celulite = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_queimaduras = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_edema = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_infeccao = models.CharField(max_length=1, blank=True, null=True)
    fl_puncao_extravazamento = models.CharField(max_length=1, blank=True, null=True)
    ds_puncao_complemento = models.CharField(max_length=300, blank=True, null=True)
    fl_escala_dor = models.CharField(max_length=2, blank=True, null=True)
    ds_observacao = models.CharField(max_length=300, blank=True, null=True)
    hr_saida = models.FloatField(blank=True, null=True)
    cd_medico_acompanhante = models.FloatField(blank=True, null=True)
    dt_cadastro = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)
    fl_med_henetix = models.CharField(max_length=1, blank=True, null=True)
    fl_med_soro = models.CharField(max_length=1, blank=True, null=True)
    fl_med_hidrocortisona = models.CharField(max_length=1, blank=True, null=True)
    fl_med_outros = models.CharField(max_length=1, blank=True, null=True)
    ds_med_outros = models.CharField(max_length=100, blank=True, null=True)
    fl_via_venosa = models.CharField(max_length=1, blank=True, null=True)
    fl_via_oral = models.CharField(max_length=1, blank=True, null=True)
    fl_via_retal = models.CharField(max_length=1, blank=True, null=True)
    dt_validade = models.CharField(max_length=50, blank=True, null=True)
    nu_lote = models.CharField(max_length=50, blank=True, null=True)
    nu_quantidade = models.CharField(max_length=50, blank=True, null=True)
    cd_enfermeiro_acompanhante = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acompanhamento_contraste'
        unique_together = (('cd_atendimento', 'cd_ocorrencia', 'cd_ordem'),)


class TbAcompanhamentoEndoscopia(models.Model):
    cd_atendimento = models.FloatField()
    cd_ocorrencia = models.FloatField()
    cd_ordem = models.FloatField()
    nm_equipamento = models.CharField(max_length=100, blank=True, null=True)
    dt_inicio_cidex = models.FloatField(blank=True, null=True)
    dt_fim_cidex = models.FloatField(blank=True, null=True)
    fl_jejum = models.CharField(max_length=1, blank=True, null=True)
    fl_preparo_realizado = models.CharField(max_length=1, blank=True, null=True)
    fl_patologia_previa = models.CharField(max_length=1, blank=True, null=True)
    ds_patologia_previa = models.CharField(max_length=100, blank=True, null=True)
    fl_uso_medicamento = models.CharField(max_length=1, blank=True, null=True)
    ds_uso_medicamento = models.CharField(max_length=100, blank=True, null=True)
    fl_protese_dentaria = models.CharField(max_length=1, blank=True, null=True)
    ds_protese_dentaria = models.CharField(max_length=100, blank=True, null=True)
    fl_anti_coagulante = models.CharField(max_length=1, blank=True, null=True)
    ds_anti_coagulante = models.CharField(max_length=100, blank=True, null=True)
    fl_anti_convulsivante = models.CharField(max_length=1, blank=True, null=True)
    ds_anti_convulsivante = models.CharField(max_length=100, blank=True, null=True)
    fl_puncao_venosa = models.CharField(max_length=1, blank=True, null=True)
    ds_puncao_venosa = models.CharField(max_length=100, blank=True, null=True)
    fl_sintoma_hipoglicemia = models.CharField(max_length=1, blank=True, null=True)
    ds_sintoma_hipoglicemia = models.CharField(max_length=100, blank=True, null=True)
    fl_alergia = models.CharField(max_length=1, blank=True, null=True)
    ds_alergia = models.CharField(max_length=100, blank=True, null=True)
    dt_inicio_intra = models.FloatField(blank=True, null=True)
    dt_fim_intra = models.FloatField(blank=True, null=True)
    ds_ta_intra = models.CharField(max_length=10, blank=True, null=True)
    ds_fc_intra = models.CharField(max_length=10, blank=True, null=True)
    ds_fr_intra = models.CharField(max_length=10, blank=True, null=True)
    ds_so2_intra = models.CharField(max_length=10, blank=True, null=True)
    fl_o2_intra = models.CharField(max_length=1, blank=True, null=True)
    fl_inter_intra = models.CharField(max_length=1, blank=True, null=True)
    dt_inicio_pos = models.FloatField(blank=True, null=True)
    dt_fim_pos = models.FloatField(blank=True, null=True)
    ds_ta_pos = models.CharField(max_length=10, blank=True, null=True)
    ds_fc_pos = models.CharField(max_length=10, blank=True, null=True)
    ds_fr_pos = models.CharField(max_length=10, blank=True, null=True)
    ds_so2_pos = models.CharField(max_length=10, blank=True, null=True)
    fl_inter_pos = models.CharField(max_length=1, blank=True, null=True)
    fl_bocal_retirado = models.CharField(max_length=1, blank=True, null=True)
    fl_aux_poltrona = models.CharField(max_length=1, blank=True, null=True)
    fl_anatomia_patologica = models.CharField(max_length=1, blank=True, null=True)
    ds_qtd_frasco = models.CharField(max_length=3, blank=True, null=True)
    fl_urease = models.CharField(max_length=1, blank=True, null=True)
    ds_urease = models.CharField(max_length=100, blank=True, null=True)
    fl_pinca_biopsia = models.CharField(max_length=1, blank=True, null=True)
    fl_alca_polipectomia = models.CharField(max_length=1, blank=True, null=True)
    fl_cateter_injetor = models.CharField(max_length=1, blank=True, null=True)
    fl_ligadura_elastica = models.CharField(max_length=1, blank=True, null=True)
    fl_hemoclip = models.CharField(max_length=1, blank=True, null=True)
    fl_pinca_corpo_estranho = models.CharField(max_length=1, blank=True, null=True)
    ds_outro_material = models.CharField(max_length=100, blank=True, null=True)
    ds_nao_material_utilizado = models.CharField(max_length=100, blank=True, null=True)
    ds_evolucao_paciente = models.CharField(max_length=500, blank=True, null=True)
    fl_alta = models.CharField(max_length=1, blank=True, null=True)
    cd_alta_medico = models.FloatField(blank=True, null=True)
    fl_entregue_acomp = models.CharField(max_length=1, blank=True, null=True)
    fl_entregue_func = models.CharField(max_length=1, blank=True, null=True)
    fl_orientacao_alta = models.CharField(max_length=1, blank=True, null=True)
    cd_operador = models.CharField(max_length=10)
    dt_cadastro = models.DateField()

    class Meta:
        managed = False
        db_table = 'tb_acompanhamento_endoscopia'
        unique_together = (('cd_atendimento', 'cd_ocorrencia', 'cd_ordem'),)


class TbAcompanhante(models.Model):
    cd_acompanhante = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_acompanhante', primary_key=True)
    nu_telefone_contato = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acompanhante'


class TbAcreditacaoFilial(models.Model):
    cd_unidade_atendimento = models.CharField(primary_key=True, max_length=3)
    fl_ativa = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_acreditacao_filial'


class TbAdesaoVisita(models.Model):
    cd_adesao_visita = models.FloatField(primary_key=True)
    cd_setor = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_setor')
    dt_inicio_adesao = models.DateField()
    hr_inicio_adesao = models.IntegerField()
    dt_fim_adesao = models.DateField(blank=True, null=True)
    hr_fim_adesao = models.IntegerField(blank=True, null=True)
    cd_tipo_visita = models.ForeignKey('TbTipoVisitaAco', models.DO_NOTHING, db_column='cd_tipo_visita')
    dt_transacao = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    nm_terminal = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_adesao_visita'


class TbAdministracao(models.Model):
    cd_sistema = models.CharField(primary_key=True, max_length=30)
    nu_dias_implantacao = models.FloatField()
    qt_nivel_prioridade = models.FloatField(blank=True, null=True)
    dt_inicial_implantacao = models.DateField(blank=True, null=True)
    dt_final_implantacao = models.DateField(blank=True, null=True)
    cd_implantador = models.FloatField(blank=True, null=True)
    cd_ocorrencia = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_administracao'


class TbAdministracaoDiluicao(models.Model):
    cd_principio_ativo = models.ForeignKey('TbApresentacaoDiluicao', models.DO_NOTHING, db_column='cd_principio_ativo', primary_key=True)
    cd_ocorrencia_diluicao = models.ForeignKey('TbApresentacaoDiluicao', models.DO_NOTHING, db_column='cd_ocorrencia_diluicao')
    cd_ordem_administracao = models.IntegerField()
    cd_tipo_acesso = models.ForeignKey('TbTipoAcesso', models.DO_NOTHING, db_column='cd_tipo_acesso')
    ds_administracao_diluicao = models.CharField(max_length=120)
    cd_reconstituir = models.ForeignKey('TbProduto', models.DO_NOTHING, db_column='cd_reconstituir', blank=True, null=True)
    qt_reconstituir = models.FloatField(blank=True, null=True)
    cd_diluente = models.ForeignKey('TbProduto', models.DO_NOTHING, db_column='cd_diluente', blank=True, null=True)
    qt_diluente = models.FloatField(blank=True, null=True)
    nu_tempo_inicial = models.FloatField(blank=True, null=True)
    fl_tempo_inicio = models.CharField(max_length=2, blank=True, null=True)
    nu_tempo_final = models.FloatField(blank=True, null=True)
    fl_tempo_final = models.CharField(max_length=2, blank=True, null=True)
    ds_tempo = models.CharField(max_length=120, blank=True, null=True)
    cd_reconstituir2 = models.ForeignKey('TbProduto', models.DO_NOTHING, db_column='cd_reconstituir2', blank=True, null=True)
    qt_reconstituir2 = models.FloatField(blank=True, null=True)
    qt_retirar_reconst1 = models.FloatField(blank=True, null=True)
    fl_tipo_administracao = models.CharField(max_length=1, blank=True, null=True)
    qt_retirar_medic = models.FloatField(blank=True, null=True)
    qt_concentracao_diluicao = models.FloatField(blank=True, null=True)
    fl_administracao_padrao = models.CharField(max_length=1, blank=True, null=True)
    cd_unidade_conc_diluicao = models.ForeignKey('TbUnidadeUsual', models.DO_NOTHING, db_column='cd_unidade_conc_diluicao', blank=True, null=True)
    qt_dosagem_padrao = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    cd_unidade_dosagem_padrao = models.ForeignKey('TbUnidadeUsual', models.DO_NOTHING, db_column='cd_unidade_dosagem_padrao', blank=True, null=True)
    cd_apresentacao_diluente = models.ForeignKey('TbApresentacao', models.DO_NOTHING, db_column='cd_apresentacao_diluente', blank=True, null=True)
    qt_frequencia_padrao = models.IntegerField(blank=True, null=True)
    fl_unid_freq_padrao = models.CharField(max_length=2, blank=True, null=True)
    fl_sn_padrao = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_administracao_diluicao'
        unique_together = (('cd_principio_ativo', 'cd_ocorrencia_diluicao', 'cd_ordem_administracao'),)


class TbAgenciaBancaria(models.Model):
    cd_banco = models.CharField(primary_key=True, max_length=10)
    cd_agencia = models.CharField(max_length=10)
    cd_pessoa = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_pessoa')
    nm_agencia = models.CharField(max_length=45)
    nu_dv_agencia = models.CharField(max_length=1, blank=True, null=True)
    cd_compensacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agencia_bancaria'
        unique_together = (('cd_banco', 'cd_agencia'),)


class TbAgendOncoHist(models.Model):
    cd_agenda = models.ForeignKey('TbPrescricaoPlanoAgd', models.DO_NOTHING, db_column='cd_agenda', primary_key=True)
    cd_modelo = models.ForeignKey('TbPrescricaoPlanoAgd', models.DO_NOTHING, db_column='cd_modelo')
    cd_ordem_prescricao_plano = models.ForeignKey('TbPrescricaoPlanoAgd', models.DO_NOTHING, db_column='cd_ordem_prescricao_plano')
    dt_agenda = models.DateField(blank=True, null=True)
    cd_mat_med = models.ForeignKey('TbMatMed', models.DO_NOTHING, db_column='cd_mat_med', blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_dosagem = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_atendimento = models.ForeignKey('TbFilial', models.DO_NOTHING, db_column='cd_unidade_atendimento', blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_paciente = models.ForeignKey('TbPaciente', models.DO_NOTHING, db_column='cd_paciente', blank=True, null=True)
    cd_pessoa_hosp = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_pessoa_hosp', blank=True, null=True)
    cd_pessoa_hap = models.FloatField(blank=True, null=True)
    nm_pessoa = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)
    qtd_mat_med_estoq = models.FloatField(blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    prc_mat_med_estoq = models.FloatField(blank=True, null=True)
    cd_setor = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_setor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agend_onco_hist'
        unique_together = (('cd_agenda', 'cd_modelo', 'cd_ordem_prescricao_plano'),)


class TbAgendaInternProcedimento(models.Model):
    cd_agenda = models.ForeignKey('TmAgendaInternacao', models.DO_NOTHING, db_column='cd_agenda', primary_key=True)
    cd_procedimento = models.ForeignKey('TbProcedimento', models.DO_NOTHING, db_column='cd_procedimento')
    cd_via_acesso = models.IntegerField(blank=True, null=True)
    fl_bilat = models.CharField(max_length=1, blank=True, null=True)
    cd_tipo_anestesia = models.ForeignKey('TbTipoAnestesia', models.DO_NOTHING, db_column='cd_tipo_anestesia', blank=True, null=True)
    cd_param_grupo_proc = models.ForeignKey('TbParamGrupoProc', models.DO_NOTHING, db_column='cd_param_grupo_proc', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_intern_procedimento'
        unique_together = (('cd_agenda', 'cd_procedimento'),)


class TbAgendaInternacaoProf(models.Model):
    cd_agenda = models.ForeignKey('TmAgendaInternacao', models.DO_NOTHING, db_column='cd_agenda', primary_key=True)
    cd_procedimento = models.ForeignKey('TbProcedimento', models.DO_NOTHING, db_column='cd_procedimento')
    cd_profissional = models.ForeignKey('TbProfissional', models.DO_NOTHING, db_column='cd_profissional')
    cd_tipo_ato_profissional = models.ForeignKey('TbTipoAtoProfissional', models.DO_NOTHING, db_column='cd_tipo_ato_profissional', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_internacao_prof'
        unique_together = (('cd_agenda', 'cd_procedimento', 'cd_profissional'),)


class TbAgendaOncologia(models.Model):
    cd_agenda = models.IntegerField(primary_key=True)
    dt_agenda = models.DateField()
    hr_agenda = models.IntegerField(blank=True, null=True)
    cd_paciente = models.IntegerField(blank=True, null=True)
    cd_posto = models.CharField(max_length=6, blank=True, null=True)
    cd_medico = models.IntegerField(blank=True, null=True)
    cd_status = models.CharField(max_length=1, blank=True, null=True)
    nm_paciente = models.CharField(max_length=45, blank=True, null=True)
    dt_criacao = models.DateField(blank=True, null=True)
    nu_carteira_cpf = models.CharField(max_length=30, blank=True, null=True)
    cd_classificacao_oncologia = models.IntegerField(blank=True, null=True)
    cd_user_agendamento = models.CharField(max_length=10, blank=True, null=True)
    cd_senha_vinculada = models.CharField(max_length=9, blank=True, null=True)
    fl_inclusao = models.CharField(max_length=1, blank=True, null=True)
    fl_agenda_fechada = models.CharField(max_length=1, blank=True, null=True)
    fl_agenda_associada = models.CharField(max_length=1, blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    fl_biometria = models.CharField(max_length=1, blank=True, null=True)
    dt_biometria = models.DateField(blank=True, null=True)
    cd_user_biometria = models.CharField(max_length=10, blank=True, null=True)
    ds_motivo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_oncologia'


class TbAgendaOncologiaJust(models.Model):
    cd_agenda = models.IntegerField(primary_key=True)
    cd_ordem = models.IntegerField()
    cd_status = models.CharField(max_length=1, blank=True, null=True)
    cd_user = models.CharField(max_length=10, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    ds_justificativa = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_oncologia_just'
        unique_together = (('cd_agenda', 'cd_ordem'),)


class TbAgendaOncologiaObs(models.Model):
    cd_agenda = models.IntegerField(primary_key=True)
    cd_ordem = models.IntegerField()
    cd_posto = models.CharField(max_length=6, blank=True, null=True)
    cd_user = models.CharField(max_length=10, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda_oncologia_obs'
        unique_together = (('cd_agenda', 'cd_ordem'),)


class TbAgendaOperador(models.Model):
    nm_operador = models.CharField(primary_key=True, max_length=8)
    dt_agenda = models.DateField()
    hr_agenda = models.IntegerField()
    fl_agenda = models.CharField(max_length=1, blank=True, null=True)
    ds_agenda = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tb_agenda_operador'
        unique_together = (('nm_operador', 'dt_agenda', 'hr_agenda'),)


class TbAgrupamentoMedsuporteProc(models.Model):
    cd_grupo = models.ForeignKey('TbGrupoMedSuporteProc', models.DO_NOTHING, db_column='cd_grupo', primary_key=True)
    cd_procedimento = models.ForeignKey('TbProcedimento', models.DO_NOTHING, db_column='cd_procedimento')

    class Meta:
        managed = False
        db_table = 'tb_agrupamento_medsuporte_proc'
        unique_together = (('cd_grupo', 'cd_procedimento'),)


class TbAjusteBalanco(models.Model):
    cd_balanco = models.IntegerField(primary_key=True)
    cd_material = models.FloatField()
    cd_setor_controle = models.CharField(max_length=6)
    cd_ordem = models.IntegerField()
    qt_material = models.FloatField()
    qt_contada = models.FloatField(blank=True, null=True)
    dt_ajuste = models.DateField(blank=True, null=True)
    observacao = models.CharField(max_length=120, blank=True, null=True)
    cd_usuario = models.CharField(max_length=15, blank=True, null=True)
    dt_validade = models.DateField(blank=True, null=True)
    fl_ajustou = models.CharField(max_length=1, blank=True, null=True)
    qt_diferenca = models.FloatField(blank=True, null=True)
    fl_curva = models.CharField(max_length=1, blank=True, null=True)
    cd_ajuste = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ajuste_balanco'
        unique_together = (('cd_balanco', 'cd_material', 'cd_setor_controle', 'cd_ordem'),)


class TbAjusteBalancoLote(models.Model):
    cd_balanco = models.IntegerField(primary_key=True)
    cd_lote = models.CharField(max_length=20)
    qt_lote = models.FloatField()
    dt_validade = models.DateField()
    cd_ordem = models.IntegerField()
    dt_ajuste = models.DateField()

    class Meta:
        managed = False
        db_table = 'tb_ajuste_balanco_lote'
        unique_together = (('cd_balanco', 'cd_lote', 'dt_validade', 'cd_ordem'),)


class TbAjusteEstoqueLote(models.Model):
    cd_ajuste = models.BigIntegerField()
    cd_lote = models.CharField(max_length=20)
    qt_lote = models.FloatField()
    dt_validade = models.DateField()
    dt_validade_lote = models.DateField()
    dt_ajuste = models.DateField()
    cd_setor_controle = models.CharField(primary_key=True, max_length=10)
    cd_material = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tb_ajuste_estoque_lote'
        unique_together = (('cd_setor_controle', 'cd_material', 'cd_lote', 'cd_ajuste'),)


class TbAjusteLote(models.Model):
    cd_material = models.FloatField(primary_key=True)
    cd_setor_controle = models.CharField(max_length=6)
    cd_lote = models.CharField(max_length=20)
    dt_validade = models.DateField()
    qt_estoque = models.FloatField()
    cd_unidade_atendimento = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'tb_ajuste_lote'
        unique_together = (('cd_material', 'cd_setor_controle', 'cd_lote', 'dt_validade'),)


class TbAjusteRotativo(models.Model):
    cd_ajuste = models.BigIntegerField(primary_key=True)
    cd_material = models.FloatField()
    cd_setor_controle = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_setor_controle')
    qt_material = models.FloatField()
    qt_contada = models.FloatField(blank=True, null=True)
    dt_ajuste = models.DateField(blank=True, null=True)
    observacao = models.CharField(max_length=120, blank=True, null=True)
    cd_unidade_atendimento = models.ForeignKey('TbUnidadeAtendimento', models.DO_NOTHING, db_column='cd_unidade_atendimento', blank=True, null=True)
    cd_usuario = models.CharField(max_length=15, blank=True, null=True)
    dt_validade = models.DateField(blank=True, null=True)
    qt_segunda_contagem = models.FloatField(blank=True, null=True)
    fl_ajustou = models.CharField(max_length=1, blank=True, null=True)
    qt_diferenca = models.FloatField(blank=True, null=True)
    fl_controle_lote = models.CharField(max_length=1, blank=True, null=True)
    qt_kit = models.FloatField(blank=True, null=True)
    fl_curva = models.CharField(max_length=1, blank=True, null=True)
    fl_tipo_invent = models.CharField(max_length=20, blank=True, null=True)
    cd_ordem_tipo = models.IntegerField(blank=True, null=True)
    nu_inventario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ajuste_rotativo'


class TbAjusteRotativoLote(models.Model):
    cd_ajuste = models.ForeignKey(TbAjusteRotativo, models.DO_NOTHING, db_column='cd_ajuste', primary_key=True)
    cd_lote = models.CharField(max_length=20)
    qt_lote = models.FloatField()
    dt_validade = models.DateField()
    dt_ajuste = models.DateField()

    class Meta:
        managed = False
        db_table = 'tb_ajuste_rotativo_lote'
        unique_together = (('cd_ajuste', 'cd_lote', 'dt_validade'),)


class TbAltaAtendimento(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_ocorrencia = models.IntegerField()
    cd_causa_obito = models.ForeignKey('TbCausaObito', models.DO_NOTHING, db_column='cd_causa_obito', blank=True, null=True)
    dt_internacao = models.DateField()
    hr_internacao = models.IntegerField()
    dt_alta = models.DateField(blank=True, null=True)
    hr_alta = models.IntegerField(blank=True, null=True)
    cd_alta = models.ForeignKey('TbTipoAlta', models.DO_NOTHING, db_column='cd_alta', blank=True, null=True)
    ds_observacoes_medicas = models.CharField(max_length=2000, blank=True, null=True)
    fl_cobrado = models.CharField(max_length=1, blank=True, null=True)
    cd_procedimento_sus = models.CharField(max_length=8, blank=True, null=True)
    cd_grupo_proced_sus = models.IntegerField(blank=True, null=True)
    fl_int_rn = models.CharField(max_length=1, blank=True, null=True)
    fl_int_mae = models.CharField(max_length=1, blank=True, null=True)
    fl_alta_auditada = models.CharField(max_length=1, blank=True, null=True)
    cd_auditor_alta = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='cd_auditor_alta', blank=True, null=True)
    ds_obs_alta_franquia = models.CharField(max_length=500, blank=True, null=True)
    cd_usu_alta_franquia = models.CharField(max_length=30, blank=True, null=True)
    fl_valida_alta_paciente = models.CharField(max_length=1, blank=True, null=True)
    ds_justificativa_nao_coleta = models.CharField(max_length=500, blank=True, null=True)
    nm_operador_libera_bio = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alta_atendimento'
        unique_together = (('dt_alta', 'hr_alta', 'cd_atendimento'), ('dt_internacao', 'hr_internacao', 'cd_atendimento'), ('cd_atendimento', 'cd_ocorrencia'),)


class TbAltaAtendimentoLog(models.Model):
    cd_atendimento = models.IntegerField()
    cd_operador = models.CharField(max_length=30)
    dt_transacao = models.DateField(blank=True, null=True)
    dt_alta_ant = models.DateField(blank=True, null=True)
    hr_alta_ant = models.IntegerField(blank=True, null=True)
    cd_motivo_alta_ant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alta_atendimento_log'


class TbAltaNotificacaoCcih(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_notificacao = models.ForeignKey('TbNotificacaoCcih', models.DO_NOTHING, db_column='cd_notificacao')

    class Meta:
        managed = False
        db_table = 'tb_alta_notificacao_ccih'
        unique_together = (('cd_atendimento', 'cd_notificacao'),)


class TbAlteracaoAtendimento(models.Model):
    cd_alteracao = models.FloatField(primary_key=True)
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento')
    dt_atendimento = models.DateField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_cancelamento = models.DateField(blank=True, null=True)
    cd_tipo_atendimento = models.IntegerField(blank=True, null=True)
    cd_natureza_internacao = models.IntegerField(blank=True, null=True)
    cd_motivo_atendimento = models.IntegerField(blank=True, null=True)
    cd_clinica = models.ForeignKey('TbClinica', models.DO_NOTHING, db_column='cd_clinica', blank=True, null=True)
    hr_atendimento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alteracao_atendimento'


class TbAlteracaoConvenio(models.Model):
    cd_alteracao = models.FloatField(primary_key=True)
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento')
    cd_convenio_pagador = models.BooleanField()
    cd_convenio = models.ForeignKey('TmConvenio', models.DO_NOTHING, db_column='cd_convenio')
    cd_plano_convenio = models.ForeignKey('TbPlanoConvenio', models.DO_NOTHING, db_column='cd_plano_convenio')
    cd_usuario = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_alteracao = models.DateField(blank=True, null=True)
    cd_convenio_atual = models.ForeignKey('TmConvenio', models.DO_NOTHING, db_column='cd_convenio_atual', blank=True, null=True)
    cd_plano_atual = models.IntegerField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    cd_sup_alt_carteira = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alteracao_convenio'


class TbAlteracaoLaudo(models.Model):
    cd_alteracao_laudo = models.FloatField(primary_key=True)
    cd_atendimento = models.IntegerField()
    cd_ocorrencia = models.IntegerField()
    cd_ordem = models.IntegerField()
    cd_ordem_alt = models.IntegerField()
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_profissional_alt = models.ForeignKey('TbProfissional', models.DO_NOTHING, db_column='cd_profissional_alt', blank=True, null=True)
    cd_especialidade = models.FloatField(blank=True, null=True)
    cd_natureza_alt_laudo = models.FloatField(blank=True, null=True)
    ds_motivo_alt_laudo = models.CharField(max_length=100, blank=True, null=True)
    dt_alteracao = models.DateField(blank=True, null=True)
    ds_laudo_ant = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tb_alteracao_laudo'
        unique_together = (('cd_atendimento', 'cd_ocorrencia', 'cd_ordem', 'cd_ordem_alt'),)


class TbAlteracaoValorObrigacao(models.Model):
    cd_alteracao_valor_obrigacao = models.IntegerField(primary_key=True)
    ds_alteracao_valor_obrigacao = models.CharField(max_length=20)
    cd_operacao_pag = models.ForeignKey('TbOperacao', models.DO_NOTHING, db_column='cd_operacao_pag', blank=True, null=True)
    cd_operacao_rec = models.ForeignKey('TbOperacao', models.DO_NOTHING, db_column='cd_operacao_rec', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alteracao_valor_obrigacao'


class TbAlvaroDestino(models.Model):
    mn_alvaro = models.CharField(max_length=30, blank=True, null=True)
    mn_mat_alvaro = models.CharField(max_length=30, blank=True, null=True)
    ds_mat_alvaro = models.CharField(max_length=100, blank=True, null=True)
    ds_destino = models.CharField(max_length=10, blank=True, null=True)
    dt_importacao = models.CharField(max_length=10, blank=True, null=True)
    cd_entidade = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alvaro_destino'


class TbAlvaroMigracao(models.Model):
    fl_negociacao = models.CharField(max_length=3, blank=True, null=True)
    mn_pardini = models.CharField(max_length=30, blank=True, null=True)
    ds_pardini = models.CharField(max_length=100, blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    mn_alvaro = models.CharField(max_length=30, blank=True, null=True)
    ds_alvaro = models.CharField(max_length=100, blank=True, null=True)
    mn_mat_alvaro = models.CharField(max_length=30, blank=True, null=True)
    ds_mat_alvaro = models.CharField(max_length=100, blank=True, null=True)
    ds_dados_obrigatorios = models.CharField(max_length=100, blank=True, null=True)
    fl_curva = models.CharField(max_length=10, blank=True, null=True)
    ds_metodo_alvaro = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alvaro_migracao'


class TbAlvaroMigracaoRet(models.Model):
    mn_alvaro = models.CharField(max_length=30, blank=True, null=True)
    ds_interface = models.CharField(max_length=10, blank=True, null=True)
    ds_item_referencia = models.CharField(max_length=100, blank=True, null=True)
    ds_unid_med = models.CharField(max_length=50, blank=True, null=True)
    qt_decimal = models.CharField(max_length=10, blank=True, null=True)
    fl_tipo_valor = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alvaro_migracao_ret'


class TbAlvaroPardini(models.Model):
    mne_alvaro = models.CharField(max_length=30, blank=True, null=True)
    mne_pardini = models.CharField(max_length=30, blank=True, null=True)
    dsc_exame = models.CharField(max_length=100, blank=True, null=True)
    ds_metodo_realizado = models.CharField(max_length=100, blank=True, null=True)
    qt_decimal = models.NullBooleanField()
    ds_parametro_referencia = models.CharField(max_length=100, blank=True, null=True)
    valor_referencia = models.CharField(max_length=4000, blank=True, null=True)
    cd_metodo_realizado = models.IntegerField(blank=True, null=True)
    cd_parametro_referencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alvaro_pardini'


class TbAlvaroReferencia(models.Model):
    mn_alvaro = models.CharField(max_length=30, blank=True, null=True)
    ds_valor_referencia = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_alvaro_referencia'


class TbAmostraArquivo(models.Model):
    cd_amostra = models.CharField(max_length=18, blank=True, null=True)
    sq_arquivo = models.FloatField()
    sq_linha = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tb_amostra_arquivo'


class TbAmostraCapacidade(models.Model):
    cd_amostra = models.FloatField(primary_key=True)
    cd_atendimento = models.FloatField()
    nu_pedido = models.FloatField()
    cd_ocorrencia = models.FloatField()
    mn_mat_sao_marcos = models.CharField(max_length=20)
    mn_meio_codigo = models.CharField(max_length=20)
    mn_area_descricao = models.CharField(max_length=20)
    cd_regiao_produtiva = models.CharField(max_length=3)
    cd_unidade_produtiva = models.CharField(max_length=3)
    nu_volume_tubo = models.DecimalField(max_digits=10, decimal_places=3)
    nu_volume_reservado = models.DecimalField(max_digits=10, decimal_places=3)
    nu_volume = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cd_id_tubo_lab = models.CharField(max_length=12, blank=True, null=True)
    cd_laboratorio_ter = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tb_amostra_capacidade'


class TbAmostraCategorizacao(models.Model):
    cd_lote = models.ForeignKey('TbAmostraRast', models.DO_NOTHING, db_column='cd_lote')
    cd_amostra_coleta = models.ForeignKey('TbAmostraRast', models.DO_NOTHING, db_column='cd_amostra_coleta')
    cd_tubo_coleta = models.ForeignKey('TbAmostraRast', models.DO_NOTHING, db_column='cd_tubo_coleta')
    fl_classificacao = models.CharField(max_length=1)
    cd_categ_amostra = models.FloatField(blank=True, null=True)
    dt_classificacao = models.DateField()

    class Meta:
        managed = False
        db_table = 'tb_amostra_categorizacao'


class TbAmostraExame(models.Model):
    cd_amostra = models.IntegerField(primary_key=True)
    cd_atendimento = models.ForeignKey('TbPedidoExame', models.DO_NOTHING, db_column='cd_atendimento')
    cd_ocorrencia = models.ForeignKey('TbPedidoExame', models.DO_NOTHING, db_column='cd_ocorrencia')
    nu_pedido = models.FloatField()
    dt_pedido = models.DateField()
    nu_amostra_exame = models.IntegerField()
    cd_grupo_frasco = models.IntegerField()
    cd_grupo_produto = models.IntegerField()
    fl_libera_interface = models.CharField(max_length=1, blank=True, null=True)
    cd_grupo = models.CharField(max_length=10, blank=True, null=True)
    nm_material = models.CharField(max_length=240, blank=True, null=True)
    nm_condicao = models.CharField(max_length=50, blank=True, null=True)
    cd_regiao_produtiva = models.CharField(max_length=3, blank=True, null=True)
    cd_unidade_produtiva = models.CharField(max_length=3, blank=True, null=True)
    nm_conservante = models.CharField(max_length=50, blank=True, null=True)
    cd_id_tubo_lab = models.CharField(max_length=12, blank=True, null=True)
    dt_confirmacao = models.DateField(blank=True, null=True)
    cd_operador_confirma = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_amostra_exame'


class TbAmostraExame2(models.Model):
    cd_amostra = models.IntegerField()
    cd_atendimento = models.IntegerField()
    cd_ocorrencia = models.IntegerField()
    nu_pedido = models.FloatField()
    dt_pedido = models.DateField()
    nu_amostra_exame = models.IntegerField()
    cd_grupo_frasco = models.IntegerField()
    cd_grupo_produto = models.IntegerField()
    fl_libera_interface = models.CharField(max_length=1, blank=True, null=True)
    cd_grupo = models.CharField(max_length=10, blank=True, null=True)
    nm_material = models.CharField(max_length=240, blank=True, null=True)
    nm_condicao = models.CharField(max_length=50, blank=True, null=True)
    cd_regiao_produtiva = models.CharField(max_length=3, blank=True, null=True)
    cd_unidade_produtiva = models.CharField(max_length=3, blank=True, null=True)
    nm_conservante = models.CharField(max_length=50, blank=True, null=True)
    cd_id_tubo_lab = models.CharField(max_length=12, blank=True, null=True)
    dt_confirmacao = models.DateField(blank=True, null=True)
    cd_operador_confirma = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_amostra_exame2'


class TbAmostraFotoUnidade(models.Model):
    cd_unidade_atendimento = models.CharField(max_length=3)
    dt_operacao = models.DateField()
    nm_operador = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tb_amostra_foto_unidade'


class TbAmostraProcedimento(models.Model):
    cd_atendimento = models.IntegerField()
    cd_ocorrencia = models.IntegerField()
    cd_ordem = models.IntegerField()
    cd_procedimento = models.CharField(max_length=8)
    cd_amostra = models.IntegerField()
    fl_interfaceado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_amostra_procedimento'


class TbAmostraProcedimento2(models.Model):
    cd_atendimento = models.IntegerField()
    cd_ocorrencia = models.IntegerField()
    cd_ordem = models.IntegerField()
    cd_procedimento = models.CharField(max_length=8)
    cd_amostra = models.IntegerField()
    fl_interfaceado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_amostra_procedimento2'


class TbAmostraRast(models.Model):
    cd_lote = models.ForeignKey('TbLoteRast', models.DO_NOTHING, db_column='cd_lote', primary_key=True)
    cd_amostra_coleta = models.ForeignKey(TbAmostraExame, models.DO_NOTHING, db_column='cd_amostra_coleta')
    cd_tubo_coleta = models.IntegerField()
    dt_amostra_coleta = models.DateField()
    cd_amostra_lab = models.ForeignKey(TbAmostraExame, models.DO_NOTHING, db_column='cd_amostra_lab', blank=True, null=True)
    cd_tubo_lab = models.IntegerField(blank=True, null=True)
    dt_amostra_lab = models.DateField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_amostra_rast'
        unique_together = (('cd_lote', 'cd_amostra_coleta', 'cd_tubo_coleta'),)


class TbAnaliseGlosa(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_cobranca = models.ForeignKey('TbCobrancaPaciente', models.DO_NOTHING, db_column='cd_cobranca')
    cd_produto = models.CharField(max_length=8)
    fl_tipo_produto = models.CharField(max_length=1, blank=True, null=True)
    dt_analise = models.DateField()
    qt_paga = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    vl_total_pago = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_analise_glosa'
        unique_together = (('cd_atendimento', 'cd_cobranca', 'cd_produto', 'dt_analise'),)


class TbAnaliseGnnutriTemp(models.Model):
    nm_operador = models.CharField(max_length=20, blank=True, null=True)
    dt_registro = models.DateField(blank=True, null=True)
    fl_tipo = models.CharField(max_length=1, blank=True, null=True)
    cd_autorizacao_senha = models.FloatField(blank=True, null=True)
    cd_requisicao = models.FloatField(blank=True, null=True)
    nu_comanda = models.CharField(max_length=10, blank=True, null=True)
    cd_senha = models.CharField(max_length=30, blank=True, null=True)
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_material = models.FloatField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    qt_material = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_analise_gnnutri_temp'


class TbAnaliseInterface(models.Model):
    cd_amostra = models.IntegerField()
    cd_tipo = models.BooleanField()
    nu_pedido = models.IntegerField()
    nm_paciente = models.CharField(max_length=45)
    dt_amostra = models.DateField()
    nm_arquivo = models.CharField(max_length=30)
    nm_operador = models.CharField(max_length=20)
    nm_tela = models.CharField(max_length=10)
    nu_lote = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_analise_interface'


class TbAnaliseOncologiaTemp(models.Model):
    nm_operador = models.CharField(max_length=15, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    dt_referencia = models.DateField(blank=True, null=True)
    fl_referencia = models.CharField(max_length=1, blank=True, null=True)
    cd_material = models.IntegerField(blank=True, null=True)
    cd_atendimento = models.BigIntegerField(blank=True, null=True)
    nu_comanda = models.CharField(max_length=9, blank=True, null=True)
    qt_faturado = models.FloatField(blank=True, null=True)
    vl_faturado = models.FloatField(blank=True, null=True)
    cd_senha = models.CharField(max_length=20, blank=True, null=True)
    cd_brasindice = models.IntegerField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    qt_autorizado = models.FloatField(blank=True, null=True)
    vl_autorizado = models.FloatField(blank=True, null=True)
    cd_brasindice2 = models.IntegerField(blank=True, null=True)
    cd_complemento_brasindice2 = models.CharField(max_length=4, blank=True, null=True)
    qt_autorizado2 = models.FloatField(blank=True, null=True)
    vl_autorizado2 = models.FloatField(blank=True, null=True)
    cd_brasindice3 = models.IntegerField(blank=True, null=True)
    cd_complemento_brasindice3 = models.CharField(max_length=4, blank=True, null=True)
    qt_autorizado3 = models.FloatField(blank=True, null=True)
    vl_autorizado3 = models.FloatField(blank=True, null=True)
    cd_requisicao = models.BigIntegerField(blank=True, null=True)
    qt_requisicao = models.FloatField(blank=True, null=True)
    vl_requisicao = models.FloatField(blank=True, null=True)
    qt_dosagem_req = models.FloatField(blank=True, null=True)
    cd_unidade_usual_req = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_analise_oncologia_temp'


class TbAnaliseTempoTmp(models.Model):
    cd_filial = models.CharField(max_length=3)
    nm_fantasia = models.CharField(max_length=20)
    nm_paciente = models.CharField(max_length=45)
    cd_atendimento = models.IntegerField()
    dt_atendimento = models.DateField(blank=True, null=True)
    hr_atendimento = models.CharField(max_length=5, blank=True, null=True)
    dt_fim_atendimento = models.DateField(blank=True, null=True)
    hr_fim_atendimento = models.CharField(max_length=5, blank=True, null=True)
    qt_horas = models.CharField(max_length=10, blank=True, null=True)
    ds_diagnostico = models.CharField(max_length=4000, blank=True, null=True)
    cd_atendimento_ant = models.FloatField(blank=True, null=True)
    dt_atendimento_ant = models.DateField(blank=True, null=True)
    hr_atendimento_ant = models.CharField(max_length=5, blank=True, null=True)
    dt_fim_atendimento_ant = models.DateField(blank=True, null=True)
    hr_fim_atendimento_ant = models.CharField(max_length=5, blank=True, null=True)
    ds_diagnostico_ant = models.CharField(max_length=4000, blank=True, null=True)
    cd_usuario = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_analise_tempo_tmp'


class TbAnaliseVisitaEnfermagem(models.Model):
    cd_operador = models.CharField(max_length=20, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    nm_filial = models.CharField(max_length=100, blank=True, null=True)
    cd_posto = models.CharField(max_length=6, blank=True, null=True)
    nm_posto = models.CharField(max_length=100, blank=True, null=True)
    cd_acomodacao = models.CharField(max_length=6, blank=True, null=True)
    nu_leito = models.IntegerField(blank=True, null=True)
    cd_carteira_usuario = models.CharField(max_length=20, blank=True, null=True)
    nm_paciente = models.CharField(max_length=100, blank=True, null=True)
    cd_atendimento = models.BigIntegerField(blank=True, null=True)
    cd_cid10 = models.CharField(max_length=10, blank=True, null=True)
    nm_cid10 = models.CharField(max_length=1000, blank=True, null=True)
    cd_perfil = models.IntegerField(blank=True, null=True)
    nm_perfil = models.CharField(max_length=100, blank=True, null=True)
    dt_hr_visita_ini_ant = models.DateField(blank=True, null=True)
    qt_tolerancia = models.CharField(max_length=50, blank=True, null=True)
    dt_hr_visita_realizada = models.DateField(blank=True, null=True)
    ds_atraso = models.CharField(max_length=300, blank=True, null=True)
    nm_usuario = models.CharField(max_length=20, blank=True, null=True)
    ds_usuario = models.CharField(max_length=100, blank=True, null=True)
    vl_fr = models.CharField(max_length=40, blank=True, null=True)
    vl_pa = models.CharField(max_length=40, blank=True, null=True)
    vl_dor_toracica = models.CharField(max_length=40, blank=True, null=True)
    vl_snc = models.CharField(max_length=40, blank=True, null=True)
    vl_temp = models.CharField(max_length=40, blank=True, null=True)
    vl_fc = models.CharField(max_length=40, blank=True, null=True)
    vl_vomito = models.CharField(max_length=40, blank=True, null=True)
    vl_padrao_resp = models.CharField(max_length=40, blank=True, null=True)
    cd_ordem_analise = models.IntegerField(blank=True, null=True)
    dt_classificacao = models.DateField(blank=True, null=True)
    cd_profissional = models.IntegerField(blank=True, null=True)
    fl_biometria_obrigatoria = models.CharField(max_length=1, blank=True, null=True)
    fl_digital_capturada_pac = models.CharField(max_length=1, blank=True, null=True)
    ds_justificativa_nao_captura = models.CharField(max_length=300, blank=True, null=True)
    vl_pressao_arterial = models.CharField(max_length=40, blank=True, null=True)
    fl_bio_face_obrigatoria = models.CharField(max_length=1, blank=True, null=True)
    fl_bio_face_validada = models.CharField(max_length=1, blank=True, null=True)
    nu_tentativas_bio_face = models.IntegerField(blank=True, null=True)
    ds_jus_bio_face_negativa = models.CharField(max_length=240, blank=True, null=True)
    fl_class_pos_cirurgica = models.CharField(max_length=1, blank=True, null=True)
    nu_vigencia_pos = models.IntegerField(blank=True, null=True)
    fl_isolamento_contato = models.CharField(max_length=1, blank=True, null=True)
    vl_sinais_vitais = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_analise_visita_enfermagem'


class TbAnamnese(models.Model):
    ds_anamnese = models.CharField(primary_key=True, max_length=18)

    class Meta:
        managed = False
        db_table = 'tb_anamnese'


class TbAnamneseMamografia(models.Model):
    cd_atendimento = models.ForeignKey('TbProcedimentoRealizado', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_ocorrencia = models.ForeignKey('TbProcedimentoRealizado', models.DO_NOTHING, db_column='cd_ocorrencia')
    cd_ordem = models.ForeignKey('TbProcedimentoRealizado', models.DO_NOTHING, db_column='cd_ordem')
    ds_indicacao_queixa = models.CharField(max_length=255, blank=True, null=True)
    ds_evolucao = models.CharField(max_length=255, blank=True, null=True)
    ds_um = models.CharField(max_length=60, blank=True, null=True)
    ds_menarca = models.CharField(max_length=60, blank=True, null=True)
    ds_menopausa = models.CharField(max_length=60, blank=True, null=True)
    nu_gestacao = models.FloatField(blank=True, null=True)
    nu_gestacao_para = models.FloatField(blank=True, null=True)
    nu_gestacao_aborto = models.FloatField(blank=True, null=True)
    fl_aleitamento = models.CharField(max_length=1, blank=True, null=True)
    nu_aleitamento_duracao = models.FloatField(blank=True, null=True)
    fl_ca_mama_mae = models.CharField(max_length=1, blank=True, null=True)
    fl_ca_mama_irma = models.CharField(max_length=1, blank=True, null=True)
    fl_ca_mama_avo = models.CharField(max_length=1, blank=True, null=True)
    fl_ca_mama_tia = models.CharField(max_length=1, blank=True, null=True)
    fl_biopsia_md = models.CharField(max_length=1, blank=True, null=True)
    dt_biopsia_md = models.DateField(blank=True, null=True)
    fl_biopsia_me = models.CharField(max_length=1, blank=True, null=True)
    dt_biopsia_me = models.DateField(blank=True, null=True)
    fl_quadrantectomia_md = models.CharField(max_length=1, blank=True, null=True)
    dt_quadrantectomia_md = models.DateField(blank=True, null=True)
    fl_quadrantectomia_me = models.CharField(max_length=1, blank=True, null=True)
    dt_quadrantectomia_me = models.DateField(blank=True, null=True)
    fl_mastectomia_md = models.CharField(max_length=1, blank=True, null=True)
    dt_mastectomia_md = models.DateField(blank=True, null=True)
    fl_mastectomia_me = models.CharField(max_length=1, blank=True, null=True)
    dt_mastectomia_me = models.DateField(blank=True, null=True)
    fl_plastica_md = models.CharField(max_length=1, blank=True, null=True)
    dt_plastica_md = models.DateField(blank=True, null=True)
    fl_plastica_me = models.CharField(max_length=1, blank=True, null=True)
    dt_plastica_me = models.DateField(blank=True, null=True)
    fl_exame_anterior = models.CharField(max_length=1, blank=True, null=True)
    ds_exame_mama_d = models.CharField(max_length=255, blank=True, null=True)
    ds_exame_mama_e = models.CharField(max_length=255, blank=True, null=True)
    fl_tecnica = models.CharField(max_length=1, blank=True, null=True)
    ds_cc_mama_d_milo = models.CharField(max_length=255, blank=True, null=True)
    ds_cc_mama_e_milo = models.CharField(max_length=255, blank=True, null=True)
    nu_filmes_desp = models.FloatField(blank=True, null=True)
    nu_filmes_util = models.FloatField(blank=True, null=True)
    nm_profissional = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_anamnese_mamografia'
        unique_together = (('cd_atendimento', 'cd_ocorrencia', 'cd_ordem'),)


class TbAnamnesePaciente(models.Model):
    cd_paciente = models.ForeignKey('TbItensAnamnese', models.DO_NOTHING, db_column='cd_paciente', primary_key=True)
    ds_anamnese = models.ForeignKey('TbItensAnamnese', models.DO_NOTHING, db_column='ds_anamnese')
    dt_anamnese = models.DateField()
    ds_descricao = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_anamnese_paciente'
        unique_together = (('cd_paciente', 'dt_anamnese', 'ds_anamnese'),)


class TbAnestProcedRealizado(models.Model):
    cd_atendimento = models.FloatField(blank=True, null=True)
    cd_ocorrencia = models.FloatField(blank=True, null=True)
    cd_ordem = models.FloatField(blank=True, null=True)
    cd_profissional = models.FloatField()
    cd_tipo_ato_profissional = models.FloatField()
    cd_procedimento = models.CharField(max_length=20)
    cd_senha_autorizacao = models.CharField(max_length=30)
    cd_grupo_produto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_anest_proced_realizado'


class TbAnoMesPlantao(models.Model):
    cd_medico = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_medico', primary_key=True)
    ano_referencia = models.IntegerField()
    mes_referencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_ano_mes_plantao'
        unique_together = (('cd_medico', 'ano_referencia', 'mes_referencia'),)


class TbAntimicrobianoObservacao(models.Model):
    cd_material = models.FloatField(primary_key=True)
    ds_observacao = models.CharField(max_length=500, blank=True, null=True)
    fl_uso_restrito = models.CharField(max_length=1, blank=True, null=True)
    fl_ativo = models.CharField(max_length=1, blank=True, null=True)
    ds_historico_clinico = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_antimicrobiano_observacao'


class TbAntimicrobianoUsoRestrito(models.Model):
    cd_material = models.FloatField(primary_key=True)
    cd_indicacao = models.FloatField()
    ds_indicacao = models.CharField(max_length=500, blank=True, null=True)
    fl_grava = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_antimicrobiano_uso_restrito'
        unique_together = (('cd_material', 'cd_indicacao'),)


class TbAparelhosGasesTaxas(models.Model):
    cd_item = models.IntegerField(primary_key=True)
    ds_item = models.CharField(max_length=40)
    fl_mostrar_na_ns = models.CharField(max_length=1, blank=True, null=True)
    nu_ordem_impressao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_aparelhos_gases_taxas'


class TbAparelhosProcedimentos(models.Model):
    cd_item = models.FloatField(primary_key=True)
    cd_procedimento = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'tb_aparelhos_procedimentos'
        unique_together = (('cd_item', 'cd_procedimento'),)


class TbApexLog(models.Model):
    cd_apex_log = models.FloatField(primary_key=True)
    cd_operador = models.CharField(max_length=30)
    nm_sistema = models.CharField(max_length=100)
    dt_transacao = models.DateField()
    hr_transacao = models.CharField(max_length=5)
    cd_unidade_atendimento = models.ForeignKey('TbUnidadeAtendimento', models.DO_NOTHING, db_column='cd_unidade_atendimento', blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_posto = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_posto', blank=True, null=True)
    fl_login = models.CharField(max_length=1)
    nr_session_id = models.CharField(max_length=50, blank=True, null=True)
    nr_ip = models.CharField(max_length=50, blank=True, null=True)
    ds_log = models.CharField(max_length=2000, blank=True, null=True)
    fl_tipo_local = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_apex_log'


class TbAprazaPrescMatMed(models.Model):
    cd_atendimento = models.ForeignKey('TbProcedimentoPlanoUso', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_ocorrencia_plano = models.ForeignKey('TbProcedimentoPlanoUso', models.DO_NOTHING, db_column='cd_ocorrencia_plano')
    cd_ordem_prescricao = models.ForeignKey('TbProcedimentoPlanoUso', models.DO_NOTHING, db_column='cd_ordem_prescricao')
    cd_ordem_prescricao_plano = models.ForeignKey('TbPrescricaoPlano', models.DO_NOTHING, db_column='cd_ordem_prescricao_plano')
    cd_ordem = models.IntegerField()
    dt_aplicado = models.DateField(blank=True, null=True)
    hr_aplicado = models.IntegerField(blank=True, null=True)
    dt_aprazamento = models.DateField()
    hr_aprazamento = models.IntegerField()
    qt_aprazamento = models.IntegerField(blank=True, null=True)
    qt_aplicada = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    fl_status_uso = models.CharField(max_length=1, blank=True, null=True)
    cd_profissional_cancela = models.ForeignKey('TbProfissional', models.DO_NOTHING, db_column='cd_profissional_cancela', blank=True, null=True)
    cd_ordem_hv = models.ForeignKey('TbPrescricaoMedicaHv', models.DO_NOTHING, db_column='cd_ordem_hv', blank=True, null=True)
    cd_ordem_proc_plano_uso = models.ForeignKey('TbProcedimentoPlanoUso', models.DO_NOTHING, db_column='cd_ordem_proc_plano_uso', blank=True, null=True)
    ds_justificativa_nao_adm = models.CharField(max_length=300, blank=True, null=True)
    fl_gerado_gasto = models.CharField(max_length=1, blank=True, null=True)
    cd_status_administracao_med = models.ForeignKey('TbStatusAdministracaoMed', models.DO_NOTHING, db_column='cd_status_administracao_med', blank=True, null=True)
    cd_codigos_barra_lidos = models.CharField(max_length=2000, blank=True, null=True)
    fl_paciente_lido = models.CharField(max_length=1, blank=True, null=True)
    dt_preparo = models.DateField(blank=True, null=True)
    hr_preparo = models.IntegerField(blank=True, null=True)
    fl_bt_iniciar = models.CharField(max_length=1, blank=True, null=True)
    cd_terminal_status = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao_status = models.DateField(blank=True, null=True)
    cd_operador_status = models.CharField(max_length=30, blank=True, null=True)
    fl_carro_parada_c = models.CharField(max_length=1, blank=True, null=True)
    dt_hr_paciente_procedimento = models.DateField(blank=True, null=True)
    fl_bio_digital_obrigatoria = models.CharField(max_length=1, blank=True, null=True)
    fl_bio_digital_coletada = models.CharField(max_length=1, blank=True, null=True)
    ds_jus_digital_nao_coletada = models.CharField(max_length=1000, blank=True, null=True)
    fl_bio_face_obrigatoria = models.CharField(max_length=1, blank=True, null=True)
    fl_bio_face_validada = models.CharField(max_length=1, blank=True, null=True)
    ds_jus_bio_face_negativa = models.CharField(max_length=1000, blank=True, null=True)
    qt_dose_adm = models.IntegerField(blank=True, null=True)
    cd_unid_usual_dose_adm = models.ForeignKey('TbUnidadeUsual', models.DO_NOTHING, db_column='cd_unid_usual_dose_adm', blank=True, null=True)
    cd_supervisor_lib_mav = models.CharField(max_length=10, blank=True, null=True)
    dt_liberacao_mav = models.DateField(blank=True, null=True)
    cd_supervisor_lib_codbar = models.CharField(max_length=10, blank=True, null=True)
    ds_justifica_mudanca_horario = models.CharField(max_length=1000, blank=True, null=True)
    dt_mudanca_horario = models.DateField(blank=True, null=True)
    cd_user_mudanca = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_apraza_presc_mat_med'
        unique_together = (('cd_atendimento', 'cd_ocorrencia_plano', 'cd_ordem_prescricao', 'cd_ordem_prescricao_plano', 'cd_ordem'),)


class TbAprazamentoDieta(models.Model):
    cd_atendimento = models.ForeignKey('TbDietaPaciente', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_ocorrencia_plano = models.ForeignKey('TbDietaPaciente', models.DO_NOTHING, db_column='cd_ocorrencia_plano')
    cd_ordem_prescricao = models.ForeignKey('TbDietaPaciente', models.DO_NOTHING, db_column='cd_ordem_prescricao')
    cd_ordem_dieta = models.ForeignKey('TbDietaPaciente', models.DO_NOTHING, db_column='cd_ordem_dieta')
    cd_ordem = models.IntegerField()
    dt_aprazamento = models.DateField()
    hr_aprazamento = models.IntegerField()
    dt_aplicacao = models.DateField(blank=True, null=True)
    hr_aplicacao = models.IntegerField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    cd_tipo_cardapio = models.IntegerField()
    nu_refeicao = models.IntegerField(unique=True)
    fl_status_uso = models.CharField(max_length=1, blank=True, null=True)
    cd_profissional_cancela = models.ForeignKey('TbProfissional', models.DO_NOTHING, db_column='cd_profissional_cancela', blank=True, null=True)
    ds_justificativa_nao_adm = models.CharField(max_length=300, blank=True, null=True)
    fl_paciente_lido = models.CharField(max_length=1, blank=True, null=True)
    dt_preparo = models.DateField(blank=True, null=True)
    hr_preparo = models.IntegerField(blank=True, null=True)
    fl_bio_digital_obrigatoria = models.CharField(max_length=1, blank=True, null=True)
    fl_bio_digital_coletada = models.CharField(max_length=1, blank=True, null=True)
    ds_jus_digital_nao_coletada = models.CharField(max_length=1000, blank=True, null=True)
    fl_bio_face_obrigatoria = models.CharField(max_length=1, blank=True, null=True)
    fl_bio_face_validada = models.CharField(max_length=1, blank=True, null=True)
    ds_jus_bio_face_negativa = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_aprazamento_dieta'
        unique_together = (('cd_atendimento', 'cd_ocorrencia_plano', 'cd_ordem_prescricao', 'cd_ordem_dieta', 'cd_ordem'),)


class TbAprazamentoPrescAvaliacao(models.Model):
    cd_atendimento = models.ForeignKey('TbPrescricaoAvaliacao', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_ocorrencia_plano = models.ForeignKey('TbPrescricaoAvaliacao', models.DO_NOTHING, db_column='cd_ocorrencia_plano')
    cd_ordem_prescricao = models.ForeignKey('TbPrescricaoAvaliacao', models.DO_NOTHING, db_column='cd_ordem_prescricao')
    cd_ordem_avaliacao = models.ForeignKey('TbPrescricaoAvaliacao', models.DO_NOTHING, db_column='cd_ordem_avaliacao')
    cd_ordem_aprazamento = models.IntegerField()
    dt_aprazamento = models.DateField()
    hr_aprazamento = models.IntegerField(blank=True, null=True)
    dt_aplicado = models.DateField(blank=True, null=True)
    hr_aplicado = models.IntegerField(blank=True, null=True)
    ds_texto = models.CharField(max_length=4000, blank=True, null=True)
    ds_texto_livre = models.TextField(blank=True, null=True)
    ds_data = models.DateField(blank=True, null=True)
    ds_numero = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ds_lista = models.CharField(max_length=4000, blank=True, null=True)
    ds_check = models.CharField(max_length=1, blank=True, null=True)
    ds_imagem = models.BinaryField(blank=True, null=True)
    ds_som = models.TextField(blank=True, null=True)  # This field type is a guess.
    ds_video = models.BinaryField(blank=True, null=True)
    ds_formula = models.CharField(max_length=2000, blank=True, null=True)
    fl_formula = models.CharField(max_length=1, blank=True, null=True)
    fl_tipo_atributo = models.CharField(max_length=20)
    fl_tipo_valor = models.CharField(max_length=20)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    dt_transacao = models.DateField(blank=True, null=True)
    ds_resultado = models.CharField(max_length=2000, blank=True, null=True)
    fl_turno = models.CharField(max_length=1, blank=True, null=True)
    fl_mantido = models.CharField(max_length=1, blank=True, null=True)
    fl_status_uso = models.CharField(max_length=1, blank=True, null=True)
    cd_profissional_cancela = models.ForeignKey('TbProfissional', models.DO_NOTHING, db_column='cd_profissional_cancela', blank=True, null=True)
    cd_unidade_usual = models.ForeignKey('TbUnidadeUsual', models.DO_NOTHING, db_column='cd_unidade_usual', blank=True, null=True)
    vl_formula = models.CharField(max_length=240, blank=True, null=True)
    ds_mutiplo_valor = models.TextField(blank=True, null=True)
    fl_resultado_acumulado = models.CharField(max_length=1, blank=True, null=True)
    ds_numero_acumulado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ds_justificativa_nao_adm = models.CharField(max_length=30, blank=True, null=True)
    sinal_balanco = models.CharField(max_length=1, blank=True, null=True)
    cd_avaliacao = models.IntegerField(blank=True, null=True)
    cd_nivel_avaliacao = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    cd_componente_avaliacao = models.IntegerField(blank=True, null=True)
    cd_avaliacao_referenciada = models.IntegerField(blank=True, null=True)
    id_componente = models.CharField(max_length=2000, blank=True, null=True)
    cd_papel = models.ForeignKey('TbPapel', models.DO_NOTHING, db_column='cd_papel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_aprazamento_presc_avaliacao'
        unique_together = (('cd_atendimento', 'cd_ocorrencia_plano', 'cd_ordem_prescricao', 'cd_ordem_avaliacao', 'cd_ordem_aprazamento'),)


class TbApresentacao(models.Model):
    cd_apresentacao = models.CharField(primary_key=True, max_length=4)
    nm_apresentacao = models.CharField(max_length=45)
    cd_termo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_apresentacao'


class TbApresentacaoDiluicao(models.Model):
    cd_principio_ativo = models.ForeignKey('TbPrincipioAtivo', models.DO_NOTHING, db_column='cd_principio_ativo', primary_key=True)
    cd_ocorrencia_diluicao = models.IntegerField()
    cd_apresentacao = models.ForeignKey(TbApresentacao, models.DO_NOTHING, db_column='cd_apresentacao')
    cd_estado_fisico = models.ForeignKey('TbEstadoFisico', models.DO_NOTHING, db_column='cd_estado_fisico')
    qt_volume = models.FloatField(blank=True, null=True)
    qt_dosagem = models.FloatField()
    cd_unidade_dosagem = models.ForeignKey('TbUnidadeUsual', models.DO_NOTHING, db_column='cd_unidade_dosagem')
    ds_recomendacoes = models.CharField(max_length=240, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_apresentacao_diluicao'
        unique_together = (('cd_principio_ativo', 'cd_ocorrencia_diluicao'),)


class TbApresentacaoGasto(models.Model):
    cd_apresentacao = models.ForeignKey(TbApresentacao, models.DO_NOTHING, db_column='cd_apresentacao', primary_key=True)
    cd_mat_med = models.ForeignKey('TbMatMed', models.DO_NOTHING, db_column='cd_mat_med')

    class Meta:
        managed = False
        db_table = 'tb_apresentacao_gasto'
        unique_together = (('cd_apresentacao', 'cd_mat_med'),)


class TbApuracaoLeitosPostos(models.Model):
    cd_posto = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_posto', primary_key=True)
    qt_apuracao = models.FloatField(blank=True, null=True)
    dt_apuracao = models.DateField()
    qt_leitos_ocupados = models.FloatField(blank=True, null=True)
    qt_leitos_ocup_inst = models.FloatField(blank=True, null=True)
    qt_leitos_dayclinic = models.FloatField(blank=True, null=True)
    qt_leitos_bloqueados = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_apuracao_leitos_postos'
        unique_together = (('cd_posto', 'dt_apuracao'),)


class TbApuracaoVisAcoEme(models.Model):
    dt_apuracao = models.DateField(primary_key=True)
    cd_posto = models.CharField(max_length=6)
    cd_atendimento = models.IntegerField()
    cd_acomodacao = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_apuracao_vis_aco_eme'
        unique_together = (('dt_apuracao', 'cd_posto', 'cd_atendimento'),)


class TbArqFisicoAtend(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_setor_arquivo = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_setor_arquivo', blank=True, null=True)
    cd_estante = models.CharField(max_length=10, blank=True, null=True)
    cd_prateleira = models.CharField(max_length=10, blank=True, null=True)
    cd_arquivo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_arq_fisico_atend'


class TbArquivoBfile(models.Model):
    cd_id = models.FloatField(primary_key=True)
    ds_bfile = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tb_arquivo_bfile'


class TbAsa(models.Model):
    cd_asa = models.FloatField(primary_key=True)
    ds_asa = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_asa'


class TbAspectoPaciente(models.Model):
    cd_aspecto = models.BooleanField(primary_key=True)
    nm_aspecto = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_aspecto_paciente'


class TbAssinaturaMedico(models.Model):
    cd_medico = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_medico', primary_key=True)
    assinatura = models.TextField(blank=True, null=True)  # This field type is a guess.
    dt_inclusao = models.DateField(blank=True, null=True)
    ds_terminal = models.CharField(max_length=40, blank=True, null=True)
    nm_usuario = models.CharField(max_length=30, blank=True, null=True)
    cd_senha = models.CharField(unique=True, max_length=6, blank=True, null=True)
    cd_dedo = models.IntegerField(blank=True, null=True)
    template_digital = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_assinatura_medico'


class TbAssociacaoCcSetor(models.Model):
    cd_setor = models.CharField(primary_key=True, max_length=6)
    id_centro_custo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_associacao_cc_setor'
        unique_together = (('cd_setor', 'id_centro_custo'),)


class TbAtendRecebimentos(models.Model):
    dt_mes_base = models.CharField(max_length=20, blank=True, null=True)
    cd_convenio = models.FloatField(blank=True, null=True)
    dt_atendimento = models.DateField(blank=True, null=True)
    dt_fim_atendimento = models.DateField(blank=True, null=True)
    cd_atendimento = models.FloatField(unique=True, blank=True, null=True)
    cd_plano = models.FloatField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    cd_paciente = models.FloatField(blank=True, null=True)
    nm_paciente = models.CharField(max_length=45, blank=True, null=True)
    nu_cgc_cpf = models.FloatField(blank=True, null=True)
    nu_rg_paciente = models.BigIntegerField(blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    cd_senha_hap_vida = models.CharField(max_length=40, blank=True, null=True)
    tipo_atendimento = models.CharField(max_length=45, blank=True, null=True)
    tipo_conta = models.CharField(max_length=45, blank=True, null=True)
    cd_obrigacao = models.FloatField(blank=True, null=True)
    vl_adiantamento = models.FloatField(blank=True, null=True)
    vl_conta_hosp = models.FloatField(blank=True, null=True)
    vl_desconto = models.FloatField(blank=True, null=True)
    vl_pago = models.FloatField(blank=True, null=True)
    vl_saldo = models.FloatField(blank=True, null=True)
    cd_cobranca = models.FloatField(blank=True, null=True)
    dt_cobranca = models.DateField(blank=True, null=True)
    cd_pessoa = models.FloatField(blank=True, null=True)
    ds_operador = models.CharField(max_length=45, blank=True, null=True)
    ds_situacao = models.CharField(max_length=45, blank=True, null=True)
    cd_unidade_atendimento = models.FloatField(blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_status_obrigacao = models.FloatField(blank=True, null=True)
    ds_status = models.CharField(max_length=45, blank=True, null=True)
    dt_inclusao = models.DateField(blank=True, null=True)
    dt_alteracao = models.DateField(blank=True, null=True)
    vl_sld_cob_jur = models.FloatField(blank=True, null=True)
    vl_pg_cob_jur = models.FloatField(blank=True, null=True)
    fl_auditoria = models.FloatField(blank=True, null=True)
    ds_auditoria = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atend_recebimentos'


class TbAtendSam(models.Model):
    cd_atendimento = models.IntegerField(primary_key=True)
    dt_coleta = models.DateField()
    hr_coleta = models.IntegerField()
    vl_temp = models.IntegerField(blank=True, null=True)
    vl_fc = models.IntegerField(blank=True, null=True)
    vl_fr = models.IntegerField(blank=True, null=True)
    vl_pas = models.IntegerField(blank=True, null=True)
    vl_avsd = models.IntegerField(blank=True, null=True)
    vl_mews = models.IntegerField(blank=True, null=True)
    cd_usuario_recebe = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atend_sam'
        unique_together = (('cd_atendimento', 'dt_coleta', 'hr_coleta'),)


class TbAtendimentoCaucao(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    cd_usu_liberou_caucao = models.CharField(max_length=30, blank=True, null=True)
    ds_just_liberou_caucao = models.CharField(max_length=1000, blank=True, null=True)
    vl_devolucao_caucao = models.FloatField(blank=True, null=True)
    cd_usu_devolucao_caucao = models.CharField(max_length=30, blank=True, null=True)
    dt_devolucao_caucao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_caucao'


class TbAtendimentoCirurgicoImp(models.Model):
    cd_atendimento = models.FloatField(primary_key=True)
    cd_ocorrencia = models.FloatField()
    cd_ordem = models.FloatField()
    cd_procedimento = models.FloatField()
    cd_paciente = models.FloatField()
    dt_impresso = models.DateField(blank=True, null=True)
    fl_impresso = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_cirurgico_imp'
        unique_together = (('cd_atendimento', 'cd_ocorrencia', 'cd_ordem'),)


class TbAtendimentoDeclaracao(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    nm_acompanhante = models.CharField(max_length=45, blank=True, null=True)
    dt_inicial = models.DateField()
    dt_final = models.DateField()
    dt_operacao = models.DateField(blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_declaracao'


class TbAtendimentoDocDigit(models.Model):
    cd_ocorrencia = models.FloatField(primary_key=True)
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento')
    dt_digitalizacao = models.DateField(blank=True, null=True)
    ds_ocorrencia = models.CharField(max_length=100, blank=True, null=True)
    hr_digitalizacao = models.IntegerField(blank=True, null=True)
    cd_tipo_doc_digit = models.ForeignKey('TbTipoDocDigit', models.DO_NOTHING, db_column='cd_tipo_doc_digit', blank=True, null=True)
    dt_transacao = models.DateTimeField(blank=True, null=True)
    im_digitalizacao = models.BinaryField(blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    terminal = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_doc_digit'


class TbAtendimentoEncAuto(models.Model):
    cd_senha_master = models.ForeignKey('TbSenhaAtendimentoSa', models.DO_NOTHING, db_column='cd_senha_master', primary_key=True)
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', blank=True, null=True)
    fl_status_ant = models.FloatField(blank=True, null=True)
    dt_encerramento = models.DateField()
    fl_consolidado = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_enc_auto'
        unique_together = (('cd_senha_master', 'dt_encerramento'),)


class TbAtendimentoFluxo(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', blank=True, null=True)
    cd_ocorrencia = models.FloatField(blank=True, null=True)
    cd_fluxo_local = models.ForeignKey('TbFluxoLocal', models.DO_NOTHING, db_column='cd_fluxo_local', blank=True, null=True)
    dt_operecao = models.DateField(blank=True, null=True)
    cd_usuario_registro = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_fluxo'
        unique_together = (('cd_atendimento', 'cd_ocorrencia', 'cd_fluxo_local'),)


class TbAtendimentoLicenca(models.Model):
    cd_atendimento = models.FloatField(primary_key=True)
    dt_inicial = models.DateField()
    nu_periodo = models.FloatField()
    nu_ctps = models.FloatField()
    nu_serie_ctps = models.CharField(max_length=10)
    cd_uf_ctps = models.CharField(max_length=2)
    dt_operacao = models.DateField()
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    nu_documento_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_licenca'
        unique_together = (('cd_atendimento', 'dt_operacao'),)


class TbAtendimentoMovDoc(models.Model):
    cd_atendimento_mov_doc = models.FloatField(primary_key=True)
    cd_atendimento = models.FloatField()
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    cd_senha_autoriza = models.CharField(max_length=20, blank=True, null=True)
    cd_tipo_documento_escaneavel = models.FloatField()
    nu_documento = models.FloatField()
    ds_arquivo = models.CharField(max_length=30, blank=True, null=True)
    cd_setor_origem = models.CharField(max_length=6, blank=True, null=True)
    cd_setor_destino = models.CharField(max_length=6, blank=True, null=True)
    fl_tipo_envio = models.NullBooleanField()
    fl_obrigatorio = models.NullBooleanField()
    fl_status = models.NullBooleanField()
    dt_instancia = models.DateField(blank=True, null=True)
    cd_processo_doc_atend = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_mov_doc'
        unique_together = (('cd_atendimento', 'cd_tipo_documento_escaneavel', 'nu_documento', 'cd_procedimento', 'cd_senha_autoriza'),)


class TbAtendimentoQuestionario(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', blank=True, null=True)
    fl_cirurgia = models.CharField(max_length=1)
    ds_cirurgia = models.CharField(max_length=500, blank=True, null=True)
    fl_acidente = models.CharField(max_length=1)
    ds_acidente = models.CharField(max_length=500, blank=True, null=True)
    fl_habito = models.CharField(max_length=1)
    ds_habito = models.CharField(max_length=500, blank=True, null=True)
    fl_doenca = models.CharField(max_length=1)
    ds_doenca = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atendimento_questionario'


class TbAtestadoMedico(models.Model):
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento', primary_key=True)
    dt_emissao = models.DateField()
    hr_emissao = models.IntegerField(blank=True, null=True)
    qt_dias = models.IntegerField()
    cid10 = models.CharField(max_length=6, blank=True, null=True)
    nm_operador = models.CharField(max_length=10, blank=True, null=True)
    cd_medico_atendente = models.ForeignKey('TbProfissional', models.DO_NOTHING, db_column='cd_medico_atendente', blank=True, null=True)
    nu_documento = models.ForeignKey('TbDocumentoProntuario', models.DO_NOTHING, blank=True, null=True)
    fl_coacao = models.CharField(max_length=1, blank=True, null=True)
    ds_senha = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atestado_medico'
        unique_together = (('cd_atendimento', 'dt_emissao'),)


class TbAtivaDesativaItem(models.Model):
    cd_filial = models.CharField(max_length=3)
    qt_meses = models.IntegerField()
    dt_atu = models.DateField()
    cd_usuario = models.CharField(max_length=10, blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_ativa_desativa_item'


class TbAtividade(models.Model):
    cd_atividade = models.IntegerField(primary_key=True)
    nm_atividade = models.CharField(max_length=60)
    cd_atividade_pai = models.IntegerField(blank=True, null=True)
    nm_icone = models.CharField(max_length=40, blank=True, null=True)
    nm_bloco_entrada = models.CharField(max_length=60, blank=True, null=True)
    fl_query = models.CharField(max_length=1, blank=True, null=True)
    fl_insert = models.CharField(max_length=1, blank=True, null=True)
    fl_update = models.CharField(max_length=1, blank=True, null=True)
    fl_delete = models.CharField(max_length=1, blank=True, null=True)
    fl_status = models.CharField(max_length=1)
    nm_fomulario = models.CharField(max_length=50, blank=True, null=True)
    nm_relatorio = models.CharField(max_length=240, blank=True, null=True)
    nm_item = models.CharField(max_length=50, blank=True, null=True)
    nu_ordem_apresentacao = models.IntegerField(blank=True, null=True)
    cd_menu = models.CharField(unique=True, max_length=10, blank=True, null=True)
    fl_menu = models.CharField(max_length=3, blank=True, null=True)
    nm_formulario_pep_eme = models.CharField(max_length=50, blank=True, null=True)
    nm_icone_pep = models.CharField(max_length=40, blank=True, null=True)
    nm_parameter = models.CharField(max_length=240, blank=True, null=True)
    fl_emergencia = models.CharField(max_length=1, blank=True, null=True)
    fl_internacao = models.CharField(max_length=1, blank=True, null=True)
    fl_cirurgico = models.CharField(max_length=1, blank=True, null=True)
    fl_tipo_grupo = models.ForeignKey('TbTipoGrupoAvaliacao', models.DO_NOTHING, db_column='fl_tipo_grupo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atividade'


class TbAtividadeOcorrenciaAdm(models.Model):
    cd_sistema = models.ForeignKey('TbOcorrenciaAdministrativa', models.DO_NOTHING, db_column='cd_sistema', primary_key=True)
    cd_ocorrencia = models.ForeignKey('TbOcorrenciaAdministrativa', models.DO_NOTHING, db_column='cd_ocorrencia')
    dt_inicio_atividade = models.DateField()
    dt_final_atividade = models.DateField(blank=True, null=True)
    cd_consultor = models.FloatField()
    ds_atividade = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atividade_ocorrencia_adm'
        unique_together = (('cd_sistema', 'cd_ocorrencia', 'dt_inicio_atividade'),)


class TbAtualizarCadastro(models.Model):
    vendedor = models.CharField(max_length=45, blank=True, null=True)
    empresa = models.CharField(max_length=51, blank=True, null=True)
    endereco_empresa = models.CharField(max_length=307, blank=True, null=True)
    endereco_tit = models.CharField(max_length=307, blank=True, null=True)
    cpf_tit = models.FloatField(blank=True, null=True)
    titular = models.CharField(max_length=45, blank=True, null=True)
    cd_usuario = models.CharField(max_length=14, blank=True, null=True)
    cd_pessoa = models.FloatField(blank=True, null=True)
    beneficiario = models.CharField(max_length=70, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    ind = models.CharField(max_length=4000, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    senha = models.CharField(max_length=6, blank=True, null=True)
    nu_cpf = models.FloatField(blank=True, null=True)
    nm_mae = models.CharField(max_length=60, blank=True, null=True)
    nu_celular1 = models.CharField(max_length=10, blank=True, null=True)
    nu_celular2 = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_atualizar_cadastro'


class TbAudioConferenciaPep(models.Model):
    cd_atendimento = models.IntegerField(primary_key=True)
    cd_ordem = models.IntegerField()
    cd_setor = models.CharField(max_length=6, blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    hr_inicio = models.IntegerField(blank=True, null=True)
    dt_fim = models.DateField(blank=True, null=True)
    hr_fim = models.IntegerField(blank=True, null=True)
    cd_medico_origem = models.IntegerField(blank=True, null=True)
    cd_medico_destino = models.IntegerField(blank=True, null=True)
    ds_observacoes_origem = models.CharField(max_length=1000, blank=True, null=True)
    ds_observacoes_destino = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_audio_conferencia_pep'
        unique_together = (('cd_atendimento', 'cd_ordem'),)


class TbAuditAcoes(models.Model):
    id_session = models.CharField(max_length=20, blank=True, null=True)
    cd_acao = models.FloatField()
    cd_tipo_acesso = models.NullBooleanField()
    cd_papel = models.IntegerField(blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    cd_operador2 = models.CharField(max_length=30, blank=True, null=True)
    ds_operador2 = models.CharField(max_length=45, blank=True, null=True)
    cd_atividade = models.IntegerField(blank=True, null=True)
    nm_atividade = models.CharField(max_length=60, blank=True, null=True)
    dt_acao = models.DateTimeField(blank=True, null=True)
    cd_terminal = models.CharField(max_length=30, blank=True, null=True)
    cd_tela = models.CharField(max_length=60, blank=True, null=True)
    nu_tentativa = models.IntegerField(blank=True, null=True)
    ds_acao = models.CharField(max_length=500, blank=True, null=True)
    ds_obs = models.CharField(max_length=2000, blank=True, null=True)
    ds_filial = models.CharField(max_length=20, blank=True, null=True)
    ds_papel = models.CharField(max_length=60, blank=True, null=True)
    cd_campo = models.CharField(max_length=60, blank=True, null=True)
    cd_valor_old = models.CharField(max_length=2000, blank=True, null=True)
    cd_valor_new = models.CharField(max_length=2000, blank=True, null=True)
    cd_tabela = models.CharField(max_length=60, blank=True, null=True)
    id_transacao = models.FloatField(blank=True, null=True)
    ds_ip = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_audit_acoes'


class TbAuditRequisicaoPerdas(models.Model):
    cd_requisicao = models.IntegerField()
    cd_setor_controle = models.CharField(max_length=6)
    cd_setor_requisitante = models.CharField(max_length=6)
    cd_material = models.IntegerField(blank=True, null=True)
    cd_ordem = models.IntegerField(blank=True, null=True)
    qt_material = models.FloatField(blank=True, null=True)
    cd_audit_hospital = models.CharField(max_length=10, blank=True, null=True)
    ds_observ_hospital = models.CharField(max_length=200, blank=True, null=True)
    dt_audit_hospital = models.DateField(blank=True, null=True)
    cd_audit_logistica = models.CharField(max_length=10, blank=True, null=True)
    ds_observ_logistica = models.CharField(max_length=200, blank=True, null=True)
    dt_audit_logistica = models.DateField(blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    fl_audit = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_audit_requisicao_perdas'


class TbAuditarIp(models.Model):
    ds_ip = models.CharField(max_length=30)
    cd_operador = models.CharField(max_length=30)
    dt_audit = models.DateField()

    class Meta:
        managed = False
        db_table = 'tb_auditar_ip'


class TbAuditoriaObito(models.Model):
    id_auditoria_obito = models.FloatField(primary_key=True)
    dt_obito = models.DateField(blank=True, null=True)
    hr_obito = models.CharField(max_length=15, blank=True, null=True)
    dt_limite_audit = models.DateField(blank=True, null=True)
    cd_atendimento = models.ForeignKey('TbPrescricaoAlta', models.DO_NOTHING, db_column='cd_atendimento', blank=True, null=True)
    cd_ocorrencia_plano = models.ForeignKey('TbPrescricaoAlta', models.DO_NOTHING, db_column='cd_ocorrencia_plano', blank=True, null=True)
    cd_ordem_prescricao = models.ForeignKey('TbPrescricaoAlta', models.DO_NOTHING, db_column='cd_ordem_prescricao', blank=True, null=True)
    cd_ordem_alta = models.ForeignKey('TbPrescricaoAlta', models.DO_NOTHING, db_column='cd_ordem_alta', blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    cd_filial = models.CharField(max_length=3, blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)
    dt_alta_medica = models.DateField(blank=True, null=True)
    hr_alta_medica = models.IntegerField(blank=True, null=True)
    dt_alta_adm = models.DateField(blank=True, null=True)
    hr_alta_adm = models.IntegerField(blank=True, null=True)
    nm_paciente = models.CharField(max_length=45, blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_auditoria_obito'


class TbAuditoriaObitoItem(models.Model):
    id_auditoria_obito = models.FloatField(primary_key=True)
    cd_ordem = models.FloatField()
    cd_medico_auditor = models.FloatField(blank=True, null=True)
    dt_auditoria = models.DateField(blank=True, null=True)
    cd_cid_contribuicao = models.CharField(max_length=4, blank=True, null=True)
    ds_auditoria = models.CharField(max_length=3000, blank=True, null=True)
    fl_status = models.CharField(max_length=1, blank=True, null=True)
    cd_usuario_cancelou = models.CharField(max_length=10, blank=True, null=True)
    cd_cid_contribuicao2 = models.CharField(max_length=4, blank=True, null=True)
    cd_cid_contribuicao3 = models.CharField(max_length=4, blank=True, null=True)
    cd_cid_principal = models.CharField(max_length=4, blank=True, null=True)
    fl_obito_oncologia = models.CharField(max_length=1, blank=True, null=True)
    fl_obito_elucidativo = models.CharField(max_length=1, blank=True, null=True)
    cd_ordem_original = models.FloatField(blank=True, null=True)
    cd_cid_contribuicao4 = models.CharField(max_length=4, blank=True, null=True)
    cd_cid_contribuicao5 = models.CharField(max_length=4, blank=True, null=True)
    ds_observacao_auditor = models.CharField(max_length=3000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_auditoria_obito_item'
        unique_together = (('id_auditoria_obito', 'cd_ordem'),)


class TbAuditoriaProcedimentoKit(models.Model):
    cd_atendimento = models.IntegerField(blank=True, null=True)
    cd_procedimento = models.CharField(max_length=8, blank=True, null=True)
    fl_auditoria = models.CharField(max_length=1, blank=True, null=True)
    dt_auditoria = models.DateField(blank=True, null=True)
    cd_operador = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_auditoria_procedimento_kit'


class TbAutorOncoHist(models.Model):
    cd_autorizacao_senha = models.FloatField(primary_key=True)
    dt_autorizacao_tratamento = models.DateField()
    nu_item_tratamento = models.FloatField()
    dt_autorizacao = models.DateField(blank=True, null=True)
    cd_mat_med = models.ForeignKey('TbMatMed', models.DO_NOTHING, db_column='cd_mat_med', blank=True, null=True)
    nm_mat_med = models.CharField(max_length=55, blank=True, null=True)
    qtd_mat_med = models.FloatField(blank=True, null=True)
    cd_unidade_dosagem = models.CharField(max_length=2, blank=True, null=True)
    cd_unidade_atendimento = models.ForeignKey('TbFilial', models.DO_NOTHING, db_column='cd_unidade_atendimento', blank=True, null=True)
    nm_unidade_atendimento = models.CharField(max_length=45, blank=True, null=True)
    cd_paciente = models.ForeignKey('TbPaciente', models.DO_NOTHING, db_column='cd_paciente', blank=True, null=True)
    cd_pessoa_hosp = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_pessoa_hosp', blank=True, null=True)
    cd_pessoa_hap = models.FloatField(blank=True, null=True)
    nm_pessoa = models.CharField(max_length=45, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=45, blank=True, null=True)
    cd_sexo = models.CharField(max_length=1, blank=True, null=True)
    cd_brasindice = models.FloatField(blank=True, null=True)
    cd_complemento_brasindice = models.CharField(max_length=4, blank=True, null=True)
    ds_produto = models.CharField(max_length=100, blank=True, null=True)
    ds_embalagem = models.CharField(max_length=60, blank=True, null=True)
    prc_mat_med = models.FloatField(blank=True, null=True)
    qtd_mat_med_estoq = models.FloatField(blank=True, null=True)
    prc_mat_med_estoq = models.FloatField(blank=True, null=True)
    cd_setor = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_setor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_autor_onco_hist'
        unique_together = (('cd_autorizacao_senha', 'dt_autorizacao_tratamento', 'nu_item_tratamento'),)


class TbAutorizaCheque(models.Model):
    cd_pessoa = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_pessoa', primary_key=True)
    dt_validade = models.DateField()

    class Meta:
        managed = False
        db_table = 'tb_autoriza_cheque'


class TbAutorizacaoAcesso(models.Model):
    cd_papel = models.ForeignKey('TbPapel', models.DO_NOTHING, db_column='cd_papel', primary_key=True)
    cd_menu = models.ForeignKey(TbAtividade, models.DO_NOTHING, db_column='cd_menu')
    tp_privilegio = models.CharField(max_length=1)
    ds_privilegio = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tb_autorizacao_acesso'
        unique_together = (('cd_papel', 'cd_menu', 'tp_privilegio', 'ds_privilegio'),)


class TbAutorizacaoPepPosto(models.Model):
    cd_setor = models.CharField(primary_key=True, max_length=6)
    cd_atendimento = models.FloatField()
    dt_gravacao = models.DateField()
    hr_gravacao = models.IntegerField(blank=True, null=True)
    cd_usuario = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_autorizacao_pep_posto'
        unique_together = (('cd_setor', 'cd_atendimento', 'dt_gravacao'),)


class TbAutorizacaoProcedimentoSa(models.Model):
    cd_atendimento = models.FloatField(primary_key=True)
    cd_senha_master = models.FloatField()
    cd_exame = models.FloatField()
    cd_procedimento = models.CharField(max_length=20)
    cd_restricao = models.CharField(max_length=1000, blank=True, null=True)
    cd_senha_autoriza = models.CharField(max_length=30, blank=True, null=True)
    cd_pre_autorizacao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_autorizacao_procedimento_sa'
        unique_together = (('cd_atendimento', 'cd_senha_master', 'cd_exame', 'cd_procedimento'),)


class TbAuxExameTemp(models.Model):
    cd_atendimento = models.FloatField(primary_key=True)
    cd_grupo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tb_aux_exame_temp'
        unique_together = (('cd_atendimento', 'cd_grupo'),)


class TbAuxGrupoTemp(models.Model):
    usuario = models.CharField(primary_key=True, max_length=100)
    cd_grupo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tb_aux_grupo_temp'
        unique_together = (('usuario', 'cd_grupo'),)


class TbAvaliacao(models.Model):
    cd_avaliacao = models.IntegerField(primary_key=True)
    nm_avaliacao = models.CharField(max_length=255)
    cd_subgrupo_avaliacao = models.ForeignKey('TbSubgrupoAvaliacao', models.DO_NOTHING, db_column='cd_subgrupo_avaliacao')
    fl_uso = models.CharField(max_length=1)
    nm_documento = models.CharField(max_length=80, blank=True, null=True)
    fl_tipo_grupo = models.ForeignKey('TbTipoGrupoAvaliacao', models.DO_NOTHING, db_column='fl_tipo_grupo', blank=True, null=True)
    cd_tipo_solicitacao = models.ForeignKey('TbTipoSolicServicos', models.DO_NOTHING, db_column='cd_tipo_solicitacao', blank=True, null=True)
    cd_especie_avaliacao = models.CharField(max_length=100, blank=True, null=True)
    id_mnemonico_avaliacao = models.CharField(max_length=200, blank=True, null=True)
    cd_tipo_documento_prontuario = models.ForeignKey('TbTipoDocumentoProntuario', models.DO_NOTHING, db_column='cd_tipo_documento_prontuario', blank=True, null=True)
    fl_expandir = models.CharField(max_length=1, blank=True, null=True)
    fl_imp_sem_resultado = models.CharField(max_length=1, blank=True, null=True)
    fl_importa_dados_novos_itens = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao'


class TbAvaliacaoAtalho(models.Model):
    chave = models.CharField(primary_key=True, max_length=200)
    ordem = models.CharField(max_length=200)
    cd_avaliacao = models.ForeignKey(TbAvaliacao, models.DO_NOTHING, db_column='cd_avaliacao', blank=True, null=True)
    nome = models.CharField(max_length=300)
    nome_item = models.CharField(max_length=500)
    id_componente = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_atalho'
        unique_together = (('chave', 'ordem', 'nome'),)


class TbAvaliacaoCid10(models.Model):
    cd_avaliacao = models.IntegerField()
    cd_cid10 = models.CharField(max_length=4, blank=True, null=True)
    cd_formulario_protocolo = models.CharField(max_length=30, blank=True, null=True)
    cd_avaliacao_cid10 = models.FloatField(primary_key=True)
    cd_macrodiag_cid10 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_cid10'


class TbAvaliacaoExcecaoItem(models.Model):
    cd_avaliacao = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_avaliacao', primary_key=True)
    cd_nivel_avaliacao = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_nivel_avaliacao')
    cd_ordem = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_ordem')
    cd_avaliacao_ref_exceto = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_avaliacao_ref_exceto')
    cd_nivel_avaliacao_ref_exceto = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_nivel_avaliacao_ref_exceto')
    cd_ordem_ref_exceto = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_ordem_ref_exceto')

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_excecao_item'
        unique_together = (('cd_avaliacao', 'cd_nivel_avaliacao', 'cd_ordem', 'cd_avaliacao_ref_exceto', 'cd_nivel_avaliacao_ref_exceto', 'cd_ordem_ref_exceto'),)


class TbAvaliacaoObjeto(models.Model):
    cd_avaliacao = models.ForeignKey(TbAvaliacao, models.DO_NOTHING, db_column='cd_avaliacao', primary_key=True)
    cd_ordem = models.IntegerField()
    nm_botao = models.CharField(max_length=30, blank=True, null=True)
    cd_tipo_objeto = models.NullBooleanField()
    nm_objeto = models.CharField(max_length=50, blank=True, null=True)
    cd_ordem_apresentacao = models.IntegerField(blank=True, null=True)
    fl_habilitado = models.CharField(max_length=1, blank=True, null=True)
    cd_operador_cadastrou = models.CharField(max_length=10, blank=True, null=True)
    dt_cadastro = models.DateField(blank=True, null=True)
    cd_tipo_documento_prontuario = models.ForeignKey('TbTipoDocumentoProntuario', models.DO_NOTHING, db_column='cd_tipo_documento_prontuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_objeto'
        unique_together = (('cd_avaliacao', 'cd_ordem'),)


class TbAvaliacaoRegra(models.Model):
    cd_avaliacao = models.ForeignKey(TbAvaliacao, models.DO_NOTHING, db_column='cd_avaliacao', primary_key=True)
    cd_regra = models.IntegerField()
    nm_regra = models.CharField(max_length=240, blank=True, null=True)
    vl_conclusao_regra = models.CharField(max_length=240, blank=True, null=True)
    cd_mnemonico_modelo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_regra'
        unique_together = (('cd_avaliacao', 'cd_regra'),)


class TbAvaliacaoRegraCondicao(models.Model):
    cd_avaliacao = models.ForeignKey(TbAvaliacaoRegra, models.DO_NOTHING, db_column='cd_avaliacao', primary_key=True)
    cd_regra = models.ForeignKey(TbAvaliacaoRegra, models.DO_NOTHING, db_column='cd_regra')
    nu_ordem_regra = models.IntegerField()
    cd_nivel_avaliacao = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_nivel_avaliacao')
    cd_ordem = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_ordem')
    cd_predicado = models.CharField(max_length=2)
    vl_valor_condicao = models.CharField(max_length=240)
    cd_operador_logico = models.CharField(max_length=3, blank=True, null=True)
    qt_peso_condicao = models.IntegerField(blank=True, null=True)
    identificador_item = models.CharField(max_length=2000, blank=True, null=True)
    campo_sam = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_regra_condicao'
        unique_together = (('cd_avaliacao', 'cd_regra', 'nu_ordem_regra'),)


class TbAvaliacaoSolicAtividade(models.Model):
    cd_avaliacao = models.ForeignKey(TbAvaliacao, models.DO_NOTHING, db_column='cd_avaliacao', primary_key=True)
    cd_tipo_solicitacao = models.ForeignKey('TbTipoSolicServicos', models.DO_NOTHING, db_column='cd_tipo_solicitacao')
    cd_componente_avaliacao = models.ForeignKey('TbComponenteAvaliacao', models.DO_NOTHING, db_column='cd_componente_avaliacao')
    fl_obrigatorio = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_solic_atividade'
        unique_together = (('cd_avaliacao', 'cd_tipo_solicitacao', 'cd_componente_avaliacao'),)


class TbAvaliacaoStatusTempo(models.Model):
    cd_avaliacao = models.ForeignKey(TbAvaliacao, models.DO_NOTHING, db_column='cd_avaliacao', primary_key=True)
    cd_tipo_solicitacao = models.ForeignKey('TbTipoSolicServicos', models.DO_NOTHING, db_column='cd_tipo_solicitacao')
    fl_status_solicitacao = models.IntegerField()
    qt_tempo_limite = models.IntegerField(blank=True, null=True)
    cd_unidade_tempo_limite = models.ForeignKey('TbUnidadeUsual', models.DO_NOTHING, db_column='cd_unidade_tempo_limite', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_status_tempo'
        unique_together = (('cd_avaliacao', 'cd_tipo_solicitacao', 'fl_status_solicitacao'),)


class TbAvaliacaoTipoModelo(models.Model):
    cd_avaliacao = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_avaliacao', primary_key=True)
    cd_nivel_avaliacao = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_nivel_avaliacao')
    cd_ordem = models.ForeignKey('TbItemAvaliacao', models.DO_NOTHING, db_column='cd_ordem')
    cd_tipo = models.IntegerField()
    cd_seq = models.IntegerField()
    ds_texto = models.CharField(max_length=4000, blank=True, null=True)
    ds_texto_livre = models.TextField(blank=True, null=True)
    ds_data = models.DateField(blank=True, null=True)
    ds_numero = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ds_imagem = models.BinaryField(blank=True, null=True)
    ds_som = models.TextField(blank=True, null=True)  # This field type is a guess.
    ds_video = models.BinaryField(blank=True, null=True)
    cd_profissional = models.IntegerField(blank=True, null=True)
    cid10 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_tipo_modelo'
        unique_together = (('cd_avaliacao', 'cd_nivel_avaliacao', 'cd_ordem', 'cd_tipo', 'cd_seq'),)


class TbAvaliacaoTipoModeloItem(models.Model):
    cd_tipo = models.FloatField(primary_key=True)
    nm_tipo = models.CharField(max_length=200, blank=True, null=True)
    cd_profissional = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_avaliacao_tipo_modelo_item'


class TbAvisoAlta(models.Model):
    cd_recepcao = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_recepcao', blank=True, null=True)
    nm_usuar_emi = models.CharField(max_length=8)
    cd_posto = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_posto')
    cd_acomodacao = models.ForeignKey('TmSetor', models.DO_NOTHING, db_column='cd_acomodacao')
    cd_atendimento = models.ForeignKey('TmAtendimento', models.DO_NOTHING, db_column='cd_atendimento')
    dt_emissao = models.DateField(primary_key=True)
    hr_emissao = models.IntegerField()
    nm_usuar_rec = models.CharField(max_length=8, blank=True, null=True)
    dt_recebeu = models.DateField(blank=True, null=True)
    hr_recebeu = models.IntegerField(blank=True, null=True)
    nm_mensagem = models.CharField(max_length=60, blank=True, null=True)
    nm_usuar_central = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='nm_usuar_central', blank=True, null=True)
    dt_recebeu_central = models.DateField(blank=True, null=True)
    hr_recebeu_central = models.IntegerField(blank=True, null=True)
    nm_usuar_far = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='nm_usuar_far', blank=True, null=True)
    dt_recebeu_far = models.DateField(blank=True, null=True)
    hr_recebeu_far = models.IntegerField(blank=True, null=True)
    tp_aviso = models.IntegerField(blank=True, null=True)
    nm_usuar_day = models.ForeignKey('TbOperador', models.DO_NOTHING, db_column='nm_usuar_day', blank=True, null=True)
    dt_recebeu_day = models.DateField(blank=True, null=True)
    hr_recebeu_day = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_aviso_alta'
        unique_together = (('dt_emissao', 'hr_emissao', 'cd_atendimento'),)


class TbAvisoAux(models.Model):
    cd_recepcao = models.CharField(max_length=6, blank=True, null=True)
    nm_usuar_emi = models.CharField(max_length=8)
    cd_posto = models.CharField(max_length=6)
    cd_acomodacao = models.CharField(max_length=6)
    cd_atendimento = models.IntegerField(blank=True, null=True)
    dt_emissao = models.DateField(blank=True, null=True)
    hr_emissao = models.IntegerField(blank=True, null=True)
    nm_usuar_rec = models.CharField(max_length=8, blank=True, null=True)
    dt_recebeu = models.DateField(blank=True, null=True)
    hr_recebeu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_aviso_aux'


class TbB2BErro(models.Model):
    cd_laboratorio_apoio = models.IntegerField(primary_key=True)
    cd_lote = models.FloatField()
    dt_importacao = models.DateField()
    sq_erro = models.FloatField()
    fl_tipo = models.FloatField(blank=True, null=True)
    ds_erro = models.CharField(max_length=1000, blank=True, null=True)
    nm_arquivo = models.CharField(max_length=100, blank=True, null=True)
    nm_paciente = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_b2b_erro'
        unique_together = (('cd_laboratorio_apoio', 'cd_lote', 'dt_importacao', 'sq_erro'),)


class TbB2BXml(models.Model):
    cd_laboratorio_apoio = models.FloatField(primary_key=True)
    dt_registro = models.DateField()
    fl_tipo = models.FloatField(blank=True, null=True)
    ds_conteudo = models.TextField(blank=True, null=True)
    nm_arquivo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_b2b_xml'
        unique_together = (('cd_laboratorio_apoio', 'dt_registro'),)


class TbBaixaMatHemo(models.Model):
    cd_baixa = models.CharField(primary_key=True, max_length=10)
    cd_material = models.FloatField()
    qtd_baixa = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tb_baixa_mat_hemo'
        unique_together = (('cd_baixa', 'cd_material'),)


class TbBandeiraCartao(models.Model):
    cd_bandeira_cartao = models.IntegerField(primary_key=True)
    ds_bandeira_cartao = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bandeira_cartao'


class TbBemPessoa(models.Model):
    cd_pessoa = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_pessoa', primary_key=True)
    nu_ordem_bem = models.CharField(max_length=1)
    ds_bem = models.CharField(max_length=60)
    vl_mercado_bem = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bem_pessoa'
        unique_together = (('cd_pessoa', 'nu_ordem_bem'),)


class TbBioquimicoSenha(models.Model):
    nm_operador = models.CharField(max_length=10)
    ds_senha = models.CharField(max_length=6)
    fl_ativo = models.CharField(max_length=1)
    dt_senha = models.DateField()
    cd_operador_audit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bioquimico_senha'


class TbBlobTemp(models.Model):
    cd_blob = models.IntegerField(primary_key=True)
    im_blob = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_blob_temp'


class TbCabBaixaMatHemo(models.Model):
    cd_baixa = models.CharField(primary_key=True, max_length=10)
    dt_baixa = models.DateField()

    class Meta:
        managed = False
        db_table = 'tb_cab_baixa_mat_hemo'


class TbCalendarioEscalaHotelaria(models.Model):
    cd_escala_hotelaria = models.FloatField(primary_key=True)
    nm_operador = models.CharField(max_length=30)
    cd_ordem = models.FloatField()
    cd_ordem_calendario = models.FloatField()
    nr_dia = models.FloatField()
    cd_operador = models.CharField(max_length=30, blank=True, null=True)
    dt_inclusao = models.DateField(blank=True, null=True)
    dt_ult_alteracao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_calendario_escala_hotelaria'
        unique_together = (('cd_escala_hotelaria', 'nm_operador', 'cd_ordem', 'cd_ordem_calendario'),)


class TbCallCenterProd(models.Model):
    id = models.FloatField(primary_key=True)
    data = models.DateField()
    dia_semana = models.FloatField()
    qt_chamadas_recebidas = models.FloatField()
    perc_perda = models.FloatField()
    tme = models.FloatField()
    nivel_servico = models.FloatField()
    tma = models.FloatField()
    dt_ini_vigencia = models.DateField()
    dt_fin_vigencia = models.DateField(blank=True, null=True)
    user_ini = models.CharField(max_length=10)
    user_fin = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_call_center_prod'


class TbCaracteristicaFisica(models.Model):
    cd_pessoa = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_pessoa', primary_key=True)
    nm_conjuge = models.CharField(max_length=45, blank=True, null=True)
    nm_naturalidade = models.CharField(max_length=45, blank=True, null=True)
    nr_nacionalidade = models.CharField(max_length=20, blank=True, null=True)
    cd_cbo = models.ForeignKey('TbCbo', models.DO_NOTHING, db_column='cd_cbo', blank=True, null=True)
    cd_religiao = models.ForeignKey('TbReligiao', models.DO_NOTHING, db_column='cd_religiao', blank=True, null=True)
    cd_estado_civil = models.ForeignKey('TbEstadoCivil', models.DO_NOTHING, db_column='cd_estado_civil', blank=True, null=True)
    cd_vinculo_empregaticio = models.ForeignKey('TbVinculoEmpregaticio', models.DO_NOTHING, db_column='cd_vinculo_empregaticio', blank=True, null=True)
    cd_escolaridade = models.ForeignKey('TbEscolaridade', models.DO_NOTHING, db_column='cd_escolaridade', blank=True, null=True)
    cd_cor = models.ForeignKey('TbCor', models.DO_NOTHING, db_column='cd_cor', blank=True, null=True)
    cd_grupo_sanguineo = models.CharField(max_length=2, blank=True, null=True)
    cd_fator_rh = models.CharField(max_length=1, blank=True, null=True)
    nu_cart_trab = models.FloatField(blank=True, null=True)
    nu_serie_cart_trab = models.FloatField(blank=True, null=True)
    nu_tit_eleit = models.FloatField(blank=True, null=True)
    cd_uf_tit_eleit = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='cd_uf_tit_eleit', blank=True, null=True)
    nu_zona_tit_eleit = models.FloatField(blank=True, null=True)
    nu_secao_tit_eleit = models.FloatField(blank=True, null=True)
    nu_certidao_reservista = models.FloatField(blank=True, null=True)
    nu_cart_nac_habilit = models.FloatField(blank=True, null=True)
    fl_tipo_cart_nac_habilit = models.CharField(max_length=1, blank=True, null=True)
    vl_salario_mensal = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    vl_renda_familiar = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_caracteristica_fisica'


class TbCaracteristicaJuridica(models.Model):
    cd_pessoa = models.ForeignKey('TbPessoa', models.DO_NOTHING, db_column='cd_pessoa', primary_key=True)
    nu_insc_inss = models.CharField(max_length=15, blank=True, null=True)
    nu_alvara = models.CharField(max_length=15, blank=True, null=True)
    nu_contrato_social = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_caracteristica_juridica'
