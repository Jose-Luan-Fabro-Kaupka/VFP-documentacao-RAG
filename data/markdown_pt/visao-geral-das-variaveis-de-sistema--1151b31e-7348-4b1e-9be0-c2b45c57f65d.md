# Visão geral das variáveis de sistema

Variáveis de sistema são variáveis internas que o Visual FoxPro cria e mantém automaticamente. Elas são designadas como PUBLIC por padrão, mas você pode declará-las como PRIVATE.

> **Observação:** Recursos recentes do Visual FoxPro substituíram a funcionalidade de muitas variáveis de sistema. Para obter mais informações, consulte a descrição de cada variável de sistema e Elementos de linguagem compatíveis com versões anteriores.

A tabela a seguir lista os tipos de variáveis de sistema do Visual FoxPro e sua designação em expressões.

| Tipo de variável | Descrição | Expressão |
| --- | --- | --- |
| C | Caractere | cExpression |
| D | Data | dExpression |
| L | Lógico | lExpression |
| N | Numérico | nExpression |
| O | Objeto | oExpression |

A tabela a seguir lista todas as variáveis de sistema, seus tipos e valores padrão.

| Variável | Tipo | Valor padrão |
| --- | --- | --- |
| _ALIGNMENT | C | LEFT |
| _ASCIICOLS | N | 80 |
| _ASCIIROWS | N | 63 |
| _ASSIST | C | Cadeia de caracteres vazia |
| _BEAUTIFY | C | Cadeia de caracteres vazia |
| _BOX | L | .T. |
| _BROWSER | C | Browser.app |
| _BUILDER | C | Builder.app |
| _CALCMEM | N | 0.0 |
| _CALCVALUE | N | 0.0 |
| _CLIPTEXT | C | Cadeia de caracteres vazia |
| _CONVERTER | C | Cadeia de caracteres vazia |
| _COVERAGE | C | Coverage.app |
| _CUROBJ | N | -1 |
| _DBLCLICK | N | 0.5 |
| _DIARYDATE | D | Data atual |
| _DOS | L | .T. no FoxPro para MS-DOS |
| _FOXDOC | C | Cadeia de caracteres vazia |
| _FOXREF | C | FoxRef.app |
| _GALLERY | C | Gallery.app |
| _GENGRAPH | C | Cadeia de caracteres vazia |
| _GENHTML | C | Genhtml.prg |
| _GENMENU | C | Genmenu.prg |
| _GENPD | C | Cadeia de caracteres vazia |
| _GENSCRN | C | Genscrn.prg |
| _GENXTAB | C | Cadeia de caracteres vazia |
| _GETEXPR | C | Cadeia de caracteres vazia |
| _INCLUDE | C | Cadeia de caracteres vazia |
| _INCSEEK | N | .5 |
| _INDENT | N | 0 |
| _LMARGIN | N | 0 |
| _MAC | L | .T. no Visual FoxPro para Macintosh |
| _MENUDESIGNER | C | Cadeia de caracteres vazia |
| _MLINE | N | 0 |
| _PADVANCE | C | FORMFEED |
| _PAGENO | N | 1 |
| _PAGETOTAL | N | 0 |
| _PBPAGE | N | 1 |
| _PCOLNO | N | Coluna atual |
| _PCOPIES | N | 1 |
| _PDRIVER | C | Cadeia de caracteres vazia |
| _PDSETUP | C | Cadeia de caracteres vazia |
| _PECODE | C | Cadeia de caracteres vazia |
| _PEJECT | C | NONE |
| _PEPAGE | N | 32767 |
| _PLENGTH | N | 66 |
| _PLINENO | N | 0 |
| _PLOFFSET | N | 0 |
| _PPITCH | C | DEFAULT |
| _PQUALITY | L | .F. |
| _PRETEXT | C | Cadeia de caracteres vazia |
| _PSCODE | C | Cadeia de caracteres vazia |
| _PSPACING | N | 1 |
| _PWAIT | L | .F. |
| _RMARGIN | N | 80 |
| _REPORTBUILDER | C | HOME() + "REPORTBUILDER.APP" |
| _REPORTOUTPUT | C | HOME() + "REPORTOUTPUT.APP" |
| _REPORTPREVIEW | C | HOME() + "REPORTPREVIEW.APP" |
| _SAMPLES | C | HOME() + "SAMPLES" |
| _SCCTEXT | C | Scctext.prg |
| _SCREEN | O | FORM |
| _SHELL | C | Cadeia de caracteres vazia |
| _SPELLCHK | C | Spellchk.app |
| _STARTUP | C | Cadeia de caracteres vazia |
| _TABS | C | Cadeia de caracteres vazia |
| _TALLY | N | 0 |
| _TASKPANE | C | Taskpane.app |
| _TEXT | C | –1 |
| _THROTTLE | N | 0 |
| _TOOLBOX | C | Toolbox.app |
| _TOOLTIPTIMEOUT | N | -1 |
| _TRANSPORT | C | Cadeia de caracteres vazia |
| _TRIGGERLEVEL | N | 0 |
| _UNIX | L | .T. no FoxPro para UNIX |
| _VFP | O | Microsoft Visual FoxPro |
| _WINDOWS | L | .T. no Visual FoxPro para Windows |
| _WIZARD | C | Wizard.app |
| _WRAP | L | .F. |
