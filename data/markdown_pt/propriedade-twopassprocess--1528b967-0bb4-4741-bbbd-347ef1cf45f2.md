# Propriedade TwoPassProcess

Especifica se esta execução de relatório exige várias passagens pelo escopo de dados para produzir a saída.

```foxpro
ReportListener.TwoPassProcess
```

# Valor de retorno

Tipo de dados Logical.

O valor padrão é False (.F.).

# Observações

Aplica-se a: objeto ReportListener.

Quando TwoPassProcess é `.T.`, o relatório é executado em duas passagens. A pré-passagem adicional permite que Engine e ReportListener determinem o valor de _PAGETOTAL para exibição em expressões do relatório durante a passagem de saída subsequente.

Os componentes do sistema de relatórios do Visual FoxPro optam por duas passagens quando encontram no relatório uma expressão que usa _PAGETOTAL ou quando você define explicitamente esta propriedade como `.T.`. Se TwoPassProcess for `.F.`, mas o mecanismo encontrar uma expressão _PAGETOTAL, ele definirá a propriedade como `.T.` durante o relatório.

> **Dica:** Ao definir TwoPassProcess como .T. antes da execução, você força o relatório a usar duas passagens mesmo que _PAGETOTAL não apareça em nenhuma expressão. Não é necessário adicionar ao layout uma expressão oculta contendo _PAGETOTAL, como nas versões anteriores do Visual FoxPro.

TwoPassProcess funciona em conjunto com CurrentPass para fornecer informações sobre o status de uma execução enquanto ela ocorre. O valor de CurrentPass muda conforme TwoPassProcess. Consulte Propriedade CurrentPass para obter mais informações. Para saber como os componentes nativos do sistema de relatórios tratam essas e outras opções no início e no fim da execução, consulte Noções básicas sobre relatórios assistidos por objetos do Visual FoxPro.
