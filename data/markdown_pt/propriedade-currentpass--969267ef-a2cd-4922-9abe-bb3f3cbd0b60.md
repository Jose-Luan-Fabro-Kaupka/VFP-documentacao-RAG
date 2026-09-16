# Propriedade CurrentPass

Especifica a passagem atual pelas funções de dados e renderização de um relatório, durante uma execução de relatório que requer várias passagens pelo escopo de dados para produzir saída, como um relatório com _PAGETOTAL.

```foxpro
ReportListener.CurrentPass
```

# Valor/retorno da propriedade

Tipo de dados inteiro.

# Observações

Aplica-se a: ReportListener Object.

O ReportListener avalia o valor da propriedade TwoPassProcess após o evento BeforeReport. Com base neste resultado, ele define a propriedade CurrentPass de acordo com os valores na tabela abaixo. Como resultado, o valor de ambas estas propriedades fornece informações úteis a partir do próximo evento ReportListener (BeforeBand).

CurrentPass também fornece informações quando um comando LABEL ou REPORT FORM é concluído. O valor desta propriedade não é limpo após uma execução de relatório, para que você possa verificá-lo após a execução, para descobrir se o relatório foi executado em uma ou duas passagens. Em contraste, TwoPassProcess é redefinido para `.F.` após uma execução de relatório, para que o ReportListener possa reconhecer um valor `.T.` na próxima execução como suas instruções explícitas.

Para obter informações sobre quando os componentes nativos do Report System atribuem este valor e outros atributos de relatório no início e no fim de uma execução de relatório, consulte Understanding Visual FoxPro Object-Assisted Reporting.

A tabela a seguir lista os possíveis valores da propriedade CurrentPass.

| Configuração | Descrição |
| --- | --- |
| 0 | Valor padrão quando a instância do objeto ReportListener é criada. Valor durante a passagem de cálculo, ou prepass , quando o ReportListener está executando um relatório que requer várias passagens pelo escopo de dados (TwoPassProcess = .T. ). Valor durante toda a execução do relatório e na conclusão da execução do relatório, quando TwoPassProcess é .F. . |
| 1 | Valor durante a segunda passagem de saída e valor na conclusão da execução do relatório, quando TwoPassProcess é .T. . |
