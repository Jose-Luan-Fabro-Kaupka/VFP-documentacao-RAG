# Propriedade CurrentDataSession

Fornece ao ReportListener o ID da sessão de dados de um relatório durante a execução de um comando LABEL ou REPORT FORM. Essa sessão pode ser privada, aberta pelo Report Engine, ou compartilhada com o formulário ou aplicativo que emitiu o comando.

```foxpro
ReportListener.CurrentDataSession
```

# Valor de retorno

Tipo de dado Integer.

O valor padrão é `1` (o ID da sessão de dados padrão).

# Observações

Aplica-se a: objeto ReportListener.

Se o relatório abrir seus dados em uma sessão privada, o Report Engine criará a sessão após o evento LoadReport e antes de BeforeReport. Ela será fechada antes de UnloadReport.

Para informações sobre quando os componentes nativos do Report System atribuem este e outros atributos, consulte Entendendo relatórios assistidos por objeto no Visual FoxPro.
