# Método IncludePageInOutput

Permite que ReportListener especifique intervalos de páginas de saída.

```foxpro
? oReportListener.IncludePageInOutput(iPage)
```

#### Parâmetros
 **iPage**
Especifica o número da página para a qual o ReportListener indica que a renderização ocorrerá ou não.

# Valor de retorno

Tipo de dados Logical.

Retorna True (`.T.`) se o parâmetro que você passa identifica uma página no conjunto atual de páginas a serem renderizadas.

# Observações

Aplica-se a: Objeto ReportListener.

A classe nativa ReportListener usa os dois argumentos RANGE do comando REPORT FORM para retornar um valor para este método. Esses dois argumentos são representados em seu objeto membro CommandClauses como CommandClauses.RangeFrom e CommandClauses.RangeTo.

No entanto, classes derivadas podem suportar intervalos mais refinados, como `1-10,16,20`, e retornar valores diferentes de IncludePageInOutput.

> **Importante:** A classe nativa ReportListener usa este método para avaliar quais páginas são renderizadas para resultados de saída, mas não quais registros ou páginas são realmente processados. Durante uma execução de relatório, todos os registros e páginas apropriados para suas cláusulas de escopo são sempre processados, mesmo quando não todas as páginas são incluídas na saída. Esta regra garante que, mesmo se você especificar um intervalo de páginas limitado para saída, suas expressões calculadas, como números de página e totais de resumo, estejam corretas.

Como o Sistema de Relatórios precisa avaliar o escopo completo para fornecer os resultados corretos, o ReportListener não invoca este método em sua passagem preliminar se estiver executando uma execução de relatório de múltiplas passagens. No entanto, sua classe derivada pode invocar este método a qualquer momento, para avaliar a necessidade de suas próprias ações durante a passagem preliminar. Para obter mais informações, consulte a propriedade TwoPassProcess.

Se o usuário invocar impressão a partir de uma visualização de relatório, usando o método OnPreviewClose do ReportListener, as páginas que imprimem não correspondem necessariamente aos resultados de IncludePageInOutput. As páginas impressas podem ser determinadas pelas alterações do usuário no intervalo de impressão usando a caixa de diálogo PROMPT do comando REPORT FORM ou por uma alteração dinâmica nos membros CommandClauses do ReportListener fornecidos para este propósito: PrintPageCurrent, PrintRangeFrom e PrintRangeTo. As páginas impressas podem ser qualquer subconjunto do intervalo completo de páginas de saída. Para obter mais informações, consulte a propriedade CommandClauses.

# Exemplo

O exemplo a seguir mostra um objeto derivado de ReportListener avaliando se deve incluir uma página na saída usando critérios específicos de sua classe.

```foxpro
PROC IncludePageInOutput(nPageNo)
   LOCAL lInclude
      FOR EACH oRangeObject in THIS.MyRangeCollection
            IF oRangeObject.Includes(nPageNo)
                lInclude = .T.
                EXIT
           ENDIF
      END FOR
   RETURN lInclude
ENDPROC
```
