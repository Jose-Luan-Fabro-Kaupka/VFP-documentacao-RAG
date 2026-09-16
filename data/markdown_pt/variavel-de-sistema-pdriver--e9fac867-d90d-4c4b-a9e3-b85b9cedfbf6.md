# Variável de sistema _PDRIVER

Incluída para compatibilidade com versões anteriores. Use o argumento TO FILE ASCII no REPORT FORM Command.

Especifica um programa de driver de impressora para relatórios baseados em caracteres.

```foxpro
_PDRIVER = expC
```

# Observações

Você pode especificar um programa de driver de impressora para relatórios baseados em caracteres armazenando o nome do programa em _PDRIVER. Relatórios baseados em caracteres são criados no FoxPro for MS-DOS e podem ser executados no FoxPro for Windows e no FoxPro for Macintosh. No FoxPro for Macintosh, um programa de driver de impressora não é necessário para imprimir relatórios baseados em caracteres criados no FoxPro for MS-DOS.

Armazenar o nome de um programa de driver de impressora em _PDRIVER descarrega o programa de driver de impressora atual, se houver um carregado. Quando você armazena um nome de programa de driver de impressora em _PDRIVER, a procedure PDONUNLOAD no programa de driver de impressora atualmente carregado é executada (se tiver uma procedure PDONUNLOAD). O driver de impressora que você armazena em _PDRIVER então é carregado e sua procedure PDONLOAD é executada (se tiver uma procedure PDONLOAD).

Quando você armazena um programa de driver de impressora em _PDRIVER, a mensagem "Printer driver installed" aparece. Para suprimir esta mensagem, emita SET NOTIFY OFF antes de armazenar um nome de programa de driver de impressora em _PDRIVER.
