# Comando CREATE REPORT - Relatório rápido

Cria um relatório sem abrir o Designer de Relatórios.

```foxpro
CREATE REPORT FileName | ? FROM Source [FORM | COLUMN]
 [FIELDS FieldList] [ALIAS] [NOOVERWRITE] [WIDTH nColumns]
```

#### Parâmetros
 **FileName | ?**
Especifica o nome do arquivo de relatório ou exibe a caixa de diálogo Criar para que você informe o nome. A extensão padrão é .frx.
**FROM Source**
Especifica o nome da tabela usada para criar o relatório, que não precisa estar aberta, ou o alias de uma tabela aberta. Por exemplo: LOCAL lcFile USE ? ALIAS temp lcFile = PUTFILE("Report name","myreport.frx") IF NOT EMPTY(lcFile) CREATE REPORT (lcFile) ; FROM (ALIAS()) ENDIF. Dica: esse código não verifica EMPTY(ALIAS()) antes de usar a sintaxe Relatório rápido. Se nenhuma tabela estiver aberta na área de trabalho atual, o Visual FoxPro exibirá a caixa de diálogo para abrir uma tabela.
**[FORM | COLUMN]**
Especifica a criação do relatório com os campos e seus nomes organizados de cima para baixo na faixa Detail ou com os campos da esquerda para a direita ao longo da página. Com COLUMN, os nomes dos campos ficam na faixa Page Header. Se FORM e COLUMN forem omitidos, o padrão será COLUMN.
**[FIELDS FieldList ]**
Especifica os campos da tabela que aparecem no relatório. Separe os campos de FieldList com vírgulas.
**[ALIAS]**
Especifica que o alias da tabela será adicionado aos nomes dos campos no relatório.
**[NOOVERWRITE]**
Especifica que um relatório existente não deve ser sobrescrito. Se já houver um relatório com o nome indicado por FileName1, o novo relatório não será criado.
**[WIDTH nColumns ]**
Especifica a largura da página do relatório em colunas.

# Observações

Você também pode criar relatórios no Designer de Relatórios usando outra versão de CREATE REPORT. Consulte o comando CREATE REPORT.

Também é possível usar um assistente. Consulte Como: criar relatórios (Visual FoxPro).

Dependendo da configuração da variável de sistema _REPORTBUILDER, este comando pode exibir caixas de diálogo adicionais enquanto o construtor amplia o processo de relatório rápido. Consulte a variável de sistema _REPORTBUILDER.
