# Caixa de diálogo FRX Cursor Browser (Report Builder)

Permite navegar pelos registros na tabela FRX subjacente ao layout do relatório. Esta caixa de diálogo modal está disponível na opção Browse FRX… no menu de contexto de qualquer caixa de diálogo do Report Builder.

# Opções da caixa de diálogo

As opções da caixa de diálogo a seguir fornecem maneiras de personalizar a exibição da caixa de diálogo.
 **Grid**
Exibe os registros no cursor FRX subjacente ao layout de relatório atual. Você pode rolar verticalmente pelos registros e horizontalmente pelas colunas.
**Name**
Exibe o conteúdo da coluna NAME do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**Expr**
Exibe o conteúdo da coluna EXPR do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**Style**
Exibe o conteúdo da coluna STYLE do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**Picture**
Exibe o conteúdo da coluna PICTURE do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**Order**
Exibe o conteúdo da coluna ORDER do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**Comment**
Exibe o conteúdo da coluna COMMENT do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**Tag**
Exibe o conteúdo da coluna TAG do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**Tag2**
Exibe o conteúdo da coluna TAG2 do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**Fontface**
Exibe o conteúdo da coluna FONTFACE do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**SupExpr**
Exibe o conteúdo da coluna SUPEXPR do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**User**
Exibe o conteúdo da coluna USER do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**CURPOS=.T. (Object selected in layout)**
Exibe o valor da coluna CURPOS do registro atual do cursor FRX. O valor é atualizado conforme você rola pela grade.
**OK**
Fecha a caixa de diálogo Browse FRX.

# Exibindo o FRX Cursor Browser usando parâmetros de linha de comando

Você pode usar os parâmetros de linha de comando do report builder para exibir a caixa de diálogo FRX Cursor Browser diretamente da janela Command:

 Para exibir o navegador FRX Cursor
 - Abra a janela Command.
- Digite o seguinte comando:

`DO (_REPORTBUILDER) WITH 2 [, cFileName ]`

Se o segundo parâmetro for omitido, você será solicitado a selecionar um arquivo de relatório com a caixa de diálogo Open File.
