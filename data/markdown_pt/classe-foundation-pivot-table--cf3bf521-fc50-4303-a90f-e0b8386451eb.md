# Classe Foundation Pivot Table

Esta classe Custom usa o mecanismo do Assistente PivotTable para gerar uma tabela dinâmica do Excel a partir de dados FoxPro.

| Categoria | Automation |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Automation |
| Class | pivottable |
| Base Class | Custom |
| Class Library | pivtable.vcx |
| Parent Class | automation |
| Sample | ...\Samples\Solution\Ffc\Automate.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário em um ambiente de dados, o Visual FoxPro abre um construtor para que você possa especificar os valores cPivFldCol, cPivFldRow, cPivFldPage, cPivFldData, lHasColumnTotals e lHasRowTotals. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar classes Foundation do Visual FoxPro para mais informações sobre o uso de classes foundation.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade CheckState | Especifica se deve testar o estado do Microsoft Excel por meio de uma rotina de erro. Padrão: .F. |
| Propriedade cOutfile | Especifica o nome do arquivo de saída. Padrão: "" |
| Propriedade cPivFldCol | Especifica o nome do campo que identifica cada coluna da tabela dinâmica. Padrão: "" |
| Propriedade cPivFldData | Especifica o nome do campo relatado como dados da tabela dinâmica. Padrão: "" |
| Propriedade cPivFldPage | Especifica o nome do campo que determina as páginas da tabela dinâmica. Padrão: "" |
| Propriedade cPivFldRow | Especifica o nome do campo cujos valores identificam cada linha da tabela dinâmica. Padrão: "" |
| Propriedade lHasColumnTotals | Especifica se deve totalizar colunas. Padrão: .F. |
| Propriedade lHasRowTotals | Especifica se deve totalizar linhas. Padrão: .F. |
| Propriedade nAction | Especifica a ação de saída a executar. Ação de saída: 1 = planilha Microsoft Excel Padrão: 1 |
| Método GetXLPath | Consulta o registro para a existência do Microsoft Excel. Sintaxe: GetXLPath( ) Retorno: nenhum Argumentos: nenhum |
| Método MSQueryCheck | Consulta o registro para a existência do MS Query. Sintaxe: MSQueryCheck( ) Retorno: nenhum Argumentos: nenhum |
| Método PivotOutput | Cria uma saída de tabela dinâmica do Microsoft Excel. Sintaxe: PivotOutput( ) Retorno: nenhum Argumentos: nenhum |
| Propriedade aFldList[1,1] | Interna à classe. |
| Propriedade cFormName | Interna à classe. |
| Propriedade cFormSCX | Interna à classe. |
| Método CheckFldLen | Interno à classe. |
| Método GetDOSName | Interno à classe. |
| Propriedade lHasMSQry32 | Interna à classe. |
| Propriedade lHasNoTask | Interna à classe. |
| Propriedade lIsNumeric | Interna à classe. |
| Propriedade SkipError | Interna à classe. |
