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
