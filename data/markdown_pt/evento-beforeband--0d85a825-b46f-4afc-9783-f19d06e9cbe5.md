# Evento BeforeBand

Ocorre imediatamente antes de o Sistema de Relatórios começar a processar uma banda de relatório.

```foxpro
PROCEDURE Object.BeforeBand
LPARAMETERS nBandObjCode, nFRXRecNo
```

#### Parâmetros

O Visual FoxPro passa os parâmetros do evento BeforeBand na seguinte ordem:
 **nBandObjCode**
Tipo de dados Integer que especifica o tipo de banda, conforme armazenado no campo ObjCode do arquivo de definição de relatório ou etiqueta (frx ou lbx). Os valores numéricos reconhecidos para nBandObjCode estão documentados na tabela 60FRX.DBF do diretório FILESPEC, da seguinte forma: 0 Título 1 Cabeçalho de página 2 Cabeçalho de coluna 3 Cabeçalho de grupo 4 Detalhe 5 Rodapé de grupo 6 Rodapé de coluna 7 Rodapé de página 8 Resumo 9 Cabeçalho de detalhe 10 Rodapé de detalhe. Para obter mais informações sobre 60FRX, consulte Estruturas de tabelas de arquivos de tabela (.dbc, .frx, .lbx, .mnx, .pjx, .scx, .vcx).
**nFRXRecno**
Tipo de dados Integer que especifica o número do registro no arquivo de definição de relatório ou etiqueta (frx ou lbx) que descreve o elemento de layout sendo renderizado.

# Observações

Aplica-se a: objeto ReportListener.

Para cada banda do relatório, ReportListener dispara o evento BeforeBand antes que o Mecanismo de Relatórios execute qualquer código na expressão OnEntry. Ele dispara o evento AfterBand depois que qualquer código OnExit é executado.

> **Observação:** Para obter informações sobre a ordem dos eventos durante a execução de um relatório, consulte Noções básicas sobre relatórios do Visual FoxPro assistidos por objetos.
