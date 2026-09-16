# Propriedade QuietMode

Especifica se o ReportListener pode fornecer qualquer feedback ou interface ao usuário.

```foxpro
ReportListener.QuietMode [= lExpr]
```

# Valor de retorno

Tipo de dados lógico.

O valor padrão de QuietMode difere dependendo de como a sessão do Visual FoxPro foi iniciada, conforme determinado pelo valor da propriedade _VFP.StartMode . Consulte a propriedade StartMode para obter mais informações.
 **True, (.T.)**
O feedback ao usuário é permitido. Este valor é o padrão para um objeto ReportListener instanciado em uma sessão interativa do Visual FoxPro ou em um aplicativo distribuível (.app ou .exe).
**False, (.F.)**
O feedback ao usuário não é permitido. Este valor é o padrão para um objeto ReportListener instanciado em um servidor de automação.

# Observações

Aplica-se a: objeto ReportListener .

Se você usar NODIALOG em um comando LABEL ou REPORT FORM e o valor de QuietMode for `.F.`, a palavra-chave NODIALOG tem precedência para esta execução de relatório. O ReportListener define QuietMode como .T. temporariamente durante a execução do relatório.

Para obter informações sobre quando os componentes nativos do sistema de relatórios atribuem este valor em relação a outros eventos de relatório no início e no fim de uma execução de relatório, consulte Compreendendo relatórios assistidos por objetos no Visual FoxPro.

QuietMode tem precedência sobre a configuração de AllowModalMessages e afeta o comportamento dos métodos DoStatus e DoMessage . Para obter mais informações sobre os mecanismos de feedback ao usuário do ReportListener, consulte a propriedade AllowModalMessages .
