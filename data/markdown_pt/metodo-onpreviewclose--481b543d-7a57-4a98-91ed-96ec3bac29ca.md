# Método OnPreviewClose

Ocorre quando o usuário fecha uma visualização de relatório ou opta por imprimir a partir de uma visualização de relatório.

```foxpro
oReportListener.OnPreviewClose([lPrint])
```

#### Parâmetros
 **lPrint**
Especifica se o usuário indicou desejo de imprimir as páginas no conjunto de páginas de saída atual após fechar a visualização de relatório.

# Valor de retorno

None.

# Observações

Aplica-se a: ReportListener Object.

A PreviewContainer API especifica que, quando o usuário fecha um formulário de visualização de relatório, o PreviewContainer deve chamar o método OnPreviewClose do ReportListener. Quando o usuário escolhe imprimir a partir da Visualização, Preview chama OnPreviewClose com um argumento True (`.T.`).

> **Observação:** O ReportListener invoca o método SetReport do PreviewContainer em OnPreviewClose com um argumento NULL ( .NULL. ). Neste momento, o ReportListener pode escolher definir sua referência PreviewContainer como NULL ( .NULL. ) ou mantê-la. No entanto, de acordo com as convenções da PreviewContainer API, é responsabilidade do PreviewContainer remover sua referência de retorno ao ReportListener neste momento. Para obter mais informações, consulte The Preview Container API e PreviewContainer Property .

Se o usuário optou por imprimir a partir da visualização, a execução de impressão começa após este método terminar. A execução de impressão usa páginas em cache preparadas para visualização neste ponto, de modo que a saída disponível corresponde exatamente ao que o usuário viu na visualização, incluindo quaisquer especificações RANGE ou de escopo incluídas no comando REPORT FORM que invocou a visualização.

Se o valor CommandClauses.Prompt do ReportListener é True (`.T.`) neste ponto, a caixa de diálogo de configuração da impressora aparece antes da execução de impressão. O usuário pode alterar as especificações com as quais o relatório imprime. Este valor pode ser True por um dos seguintes motivos:
 - Você usou a cláusula PROMPT no comando REPORT FORM original.
- O PreviewContainer ou ReportListener ajusta o valor CommandClauses.Prompt dinamicamente.

As páginas que imprimem nem sempre são o intervalo completo de páginas de saída disponíveis; podem ser algum subconjunto deste intervalo. Menos que o número total de páginas de saída pode imprimir por um dos seguintes motivos:
 - O usuário ajusta o intervalo de páginas na caixa de diálogo PROMPT.
- O PreviewContainer ou ReportListener ajusta os membros CommandClauses do ReportListener fornecidos para limitar a saída impressa a partir do método OnPreviewClose. Esses membros são PrintPageCurrent, PrintRangeFrom e PrintRangeTo. Para obter mais informações, consulte CommandClauses Property .

Se você usar NOPAGEEJECT para combinar vários relatórios em uma única execução de relatório, o valor de CommandClauses.Prompt é significativo apenas no momento em que o PreviewContainer invoca a execução de impressão. Se você não ajustou seu valor dinamicamente, o valor de CommandClauses.Prompt foi determinado por se o comando REPORT FORM final na execução de relatório incluiu a cláusula PROMPT.

> **Importante:** Como a caixa de diálogo de configuração da impressora aparece após o relatório ter sido renderizado, em resposta a CommandClauses.Prompt, e como o relatório foi renderizado com informações obtidas da impressora definida anteriormente, há algum potencial de incompatibilidade entre o relatório renderizado anteriormente e as instruções definidas pelo usuário na caixa de diálogo. Por exemplo, a impressora escolhida na caixa de diálogo pode ter um tamanho de página imprimível diferente da impressora original. Os resultados impressos neste cenário são determinados pela forma como o driver da impressora escolhida escolhe lidar com esta instrução de tamanho de página.

# Exemplo

Você pode alterar os vários membros dinâmicos de CommandClauses durante o método OnPreviewClose, para imprimir intervalos de páginas complexos. No esboço de código a seguir, um ReportListener derivado fornece uma caixa de diálogo personalizada para obter um intervalo de páginas complexo de um usuário e, em seguida, invoca o comportamento nativo várias vezes para imprimir os vários intervalos de páginas solicitados pelo usuário.

```foxpro
PROCEDURE OnPreviewClose(lPrint)
   LOCAL liRange
   IF lPrint
      NODEFAULT
      IF NOT EMPTY(THIS.CommandClauses.PrintPageCurrent
         *user chose "print current page" option from PreviewContainer.
         *Print only that page:
         THIS.CommandClauses.PrintRangeFrom = ;
           THIS.CommandClauses.PrintPageCurrent
         THIS.CommandClauses.PrintRangeTo = ;
           THIS.CommandClauses.PrintPageCurrent
         DODEFAULT(.T.)
      ELSE
         THIS.ShowCustomPageSetupDialog()
         THIS.CommandClauses.Prompt = .F.
         IF EMPTY(THIS.PageRangeArray[1])
            * no printing is requested
            DODEFAULT(.F.)
         ELSE
            * user chose at least one range;
            * go through the array set up by
            * the dialog and print the range(s)
            FOR liRange = 1 TO (ALEN(THIS.PageRangeArray,1))
               THIS.CommandClauses.PrintRangeFrom = ;
                 THIS.PageRangeArray[liRange,1]
               THIS.CommandClauses.PrintRangeTo = ;
                 THIS.PageRangeArray[liRange,2]
               DODEFAULT(.T.)
            ENDFOR
         ENDIF
      ENDIF
   ENDIF
ENDPROC
```
