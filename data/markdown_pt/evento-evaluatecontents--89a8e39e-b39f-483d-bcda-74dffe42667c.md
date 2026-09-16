# Evento EvaluateContents

Ocorre imediatamente antes do ReportListener começar a renderizar objetos para uma banda, para cada elemento de layout do tipo Expression, fornecendo uma oportunidade de alterar seus atributos.

```foxpro
PROCEDURE Object.EvaluateContents
LPARAMETERS nFRXRecno, oObjProperties
```

#### Parâmetros

O Visual FoxPro passa os parâmetros do evento EvaluateContents na seguinte ordem:
 **nFRXRecno**
Tipo de dados inteiro, especificando o número do registro no arquivo de definição de relatório ou etiqueta (frx ou lbx) descrevendo o elemento de layout sendo renderizado.
**oObjProperties**
Um objeto da classe Empty, com membros fornecendo valores relevantes para ajustar os atributos de um elemento de layout Expression. Membro Type Uso do oObjProperties reload Lógico, padrão .F. Flag para alertar o ReportListener se você fizer alterações. Defina este valor como True ( .T. ) para notificar o ReportListener de alterações em quaisquer membros de leitura/gravação de oObjProperties . text Caractere, padrão conteúdo avaliado do elemento de layout Expression. Você pode alterar este valor para alterar o conteúdo renderizado da Expression em tempo de execução. value Variant, somente leitura Este valor fornece os resultados avaliados de expressões de relatório, incluindo campos calculados, dos seguintes tipos de dados: Double (B) Date (D) Float (F) Integer (I) Logical (L) Numeric (N) DateTime (T) Currency (Y) Null (X) Para outros tipos de dados, seu conteúdo é uma cadeia nula ( "" ). Expressões concatenadas com os operadores especiais " ; " e " , " podem ter elementos de tipo misto e são consideradas cadeias de caracteres (tipo "C") neste contexto. Para obter mais informações, consulte Aparando e concatenando expressões . fontname Caractere, padrão a fonte armazenada na tabela de definição de relatório ou etiqueta para este elemento de layout. Você pode alterar este valor para alterar a fonte da Expression em tempo de execução. fontstyle, fontsize Inteiro, padrão aos valores numéricos de estilo e tamanho armazenados na tabela de definição de relatório ou etiqueta para este elemento de layout. Você pode alterar estes valores para alterar o tamanho e o estilo da fonte usada para renderizar esta Expression em tempo de execução. Os valores numéricos reconhecidos para oObjProperties.fontstyle estão documentados na tabela 60FRX.DBF no diretório FILESPEC. Para obter mais informações sobre 60FRX, consulte Estruturas de tabela de arquivos de tabela (.dbc, .frx, .lbx, .mnx, .pjx, .scx, .vcx) . fillred, fillblue, fillgreen, penred, penblue, pengreen Inteiro, valores válidos de 0 a 255 , padrão 255 , padrão aos valores armazenados na tabela de definição de relatório ou etiqueta, a menos que o valor da tabela fosse -1 para indicar "usar padrão". Se o valor da tabela fosse - 1 , o ReportListener substitui o valor real que pretende usar. Você pode alterar estes valores para alterar os componentes Vermelho, Azul e Verde das cores Fill e Pen para um elemento Expression. Para obter mais informações, consulte Como: alterar cores em controles de relatório . Se um valor inválido ou não numérico for passado para qualquer uma das propriedades de cor, elas revertem para os valores padrão armazenados na tabela de definição de relatório. Nenhum erro ocorre. fillalpha Inteiro, valores válidos de 0 a 255 , padrão 0 quando backstyle é transparente e 255 quando backstyle é opaco. Consulte Observações abaixo para informações sobre o uso dos valores alpha de elementos de layout de relatório. Se um valor inválido ou não numérico for passado para este valor, ele reverte para o valor padrão conforme mostrado neste gráfico. Para informações sobre configurações de backstyle de relatório (transparente e opaco), consulte Como: alterar opacidade de controles de relatório . penalpha Inteiro, valores válidos de 0 a 255 , padrão 255 (opaco). Consulte Observações abaixo para informações sobre o uso dos valores alpha de elementos de layout de relatório. Se um valor inválido ou não numérico for passado para este valor, ele reverte para o valor padrão conforme mostrado neste gráfico. Observação A Microsoft reserva o direito de invocar EvaluateContents para elementos de layout de relatório e etiqueta adicionais, conforme necessário, e adicionar aos membros de oObjProperties apropriadamente para esses tipos adicionais de elementos de layout. Você pode usar nFRXRecno para testar o tipo de elemento de layout, conforme mostrado no código de exemplo no método Render .

# Observações

Aplica-se a: Objeto ReportListener.

O Visual FoxPro chama EvaluateContents no início do processamento da banda, uma vez para cada elemento Expression. Não é garantido que seja chamado exatamente uma vez; pode ser chamado várias vezes para expressões avaliadas que abrangem bandas ou páginas se o Sistema de Relatórios considerar necessário (por exemplo, se a expressão incluir _PAGENO).

> **Observação:** Se você escrever código para tentar prever quando EvaluateContents pode ser chamado várias vezes, considere que nem todos os tipos de banda suportam abrangência de páginas. Consulte Report Bands para obter mais informações.

> **Dica:** Para aprimorar o desempenho, o Visual FoxPro não chama AdjustObjectSize nem EvaluateContents se determinar que não há código no ReportListener para o evento. Se você geralmente inclui código de espaço reservado ou código generalizado em cada evento, considere omitir tal código para esses dois eventos, especialmente se o nível da classe é abstrato (nunca instanciado diretamente). Inclua código apenas nos níveis de classe que realmente usam esta funcionalidade. O custo de desempenho para EvaluateContents aumenta com a quantidade de texto que o ReportListener nativo fornece na propriedade de membro oObjProperties.text, portanto pode variar com cada chamada.

Você pode usar este método para alterar várias características de elementos de layout Expression. No entanto, você não pode alterar a largura do elemento de layout, portanto deve ajustar as características de fonte e o conteúdo da Expression com esta limitação em mente. Se o elemento de layout foi marcado para esticar, segue as mesmas regras que elementos Shape e Picture aos quais você faz ajustes de altura no evento AdjustObjectSize. Para obter mais informações, consulte Evento AdjustObjectSize.

EvaluateContents fornece os meios para alterar o valor Alpha (transparência) dos valores Pen e Fill para uma Expression. Arquivos de definição de relatório e etiqueta armazenam apenas componentes RGB (Vermelho, Verde, Azul) de valores de cor, com uma única configuração para "opaco" ou "transparente". Usando EvaluateContents, você pode fornecer efeitos de cor mais sutis por manipulação direta do valor Alpha.

> **Dica:** A capacidade de usar valores de cor Alpha ao renderizar é um recurso fornecido pelo Microsoft Windows GDI+. Para obter mais informações, consulte Usando GDI+ em relatórios .

# Exemplo

O exemplo a seguir alterna entre diferentes combinações de cores baseadas nas instâncias ímpares e pares de quaisquer Expressions da banda Detail de um relatório, fornecendo um efeito de saída "greenbar". Também aplica alguns atributos de estilo a elementos que não estão em bandas Detail. Observe que esses efeitos são aplicados apenas a Expressions (por exemplo, labels em uma banda Page Header não são afetados).

```foxpro
oReportListener = CREATEOBJECT("greenBar")
oReportListener.ListenerType = 1
REPORT FORM (GETFILE("frx")) PREVIEW OBJECT oReportListener
#DEFINE DETAIL_BAND 4
#DEFINE BOLD_UNDERLINE_ITALIC 1+4+2
DEFINE CLASS greenBar AS ReportListener
   detailInstance = 0
   isDetail = .F.
   PROC BeforeBand(nBandObjCode, nFRXRecno)
     IF nBandObjCode = DETAIL_BAND
        THIS.detailInstance = THIS.detailInstance + 1
        THIS.isDetail = .T.
     ELSE
        THIS.isDetail = .F.
     ENDIF
   ENDPROC
   PROC EvaluateContents(nFRXRecno, oProps)
       oProps.Reload = .T.
       * re-load every time, in this example,
       * since we want to change every Expression
       IF THIS.isDetail
          IF THIS.detailInstance % 2 = 0
             oProps.penRed = 0
             oProps.penBlue = 125
             oProps.penGreen = 0
          ELSE
             oProps.penRed = 0
             oProps.penBlue = 0
             oProps.penGreen = 0
             oProps.fillRed = 0
             oProps.FillBlue = 0
             oProps.FillGreen = 255
             oProps.FillAlpha = 125
              *half-transparent background color
          ENDIF
       ELSE
          oProps.FontStyle = BOLD_UNDERLINE_ITALIC
       ENDIF
   ENDPROC
ENDDEFINE
```
