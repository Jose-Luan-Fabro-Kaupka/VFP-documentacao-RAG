# Propriedade OLELCID

Contém um valor numérico que indica o Locale ID de um controle OLE Bound ou de um controle OLE Container. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Control.OLELCID
```

# Observações

Aplica-se a: OLE Bound Control | OLE Container Control

O valor do Locale ID é determinado pelo valor da propriedade DefOLELCID do formulário ou da janela principal do Visual FoxPro quando um controle OLE Bound ou um controle OLE Container é colocado no formulário ou na janela principal do Visual FoxPro.

Se a propriedade DefOLELCID do formulário ou da janela principal do Visual FoxPro for zero quando o controle OLE Bound ou o controle OLE Container for colocado no formulário ou na janela principal do Visual FoxPro, o controle usa o Locale ID (LCID) atual do Visual FoxPro. Use SYS(3004) para determinar o Locale ID atual do Visual FoxPro. Use a propriedade DefOLELCID para especificar um Locale ID para um formulário.

Consulte SYS(3005) para obter uma listagem de Locale IDs.

> **Observação:** A propriedade OLELCID afeta apenas o idioma da interface do usuário exibida pelos controles OLE, e não o idioma dos comandos Automation. O idioma dos comandos Automation é afetado apenas pelo Global LocaleID, definido com SYS(3005) .
