# Caixa de diálogo Data Grouping

Permite especificar regiões aninhadas do layout de relatório ou etiqueta que são renderizadas somente quando uma expressão altera seu valor.

> **Observação:** Dependendo da configuração da variável de sistema _REPORTBUILDER, esta caixa de diálogo pode ser substituída por uma interface de usuário alternativa. Para mais informações, consulte a variável de sistema _REPORTBUILDER .

How to: Add Data Groups to Reports

# Group expressions

Lista as expressões que determinam quebras entre grupos de dados. O botão mover permite alterar a ordem de aninhamento das expressões de grupo.

Você pode digitar a expressão diretamente ou criar uma expressão clicando no botão de reticências (…). Expressões vazias não são válidas. Para mais informações, consulte a caixa de diálogo Expression Builder.

# Group properties

Especifica opções de saída para grupos de dados.
 **Start group on new column**
Especifica que a alteração da expressão de grupo forçará as informações a serem renderizadas como uma nova coluna. Disponível somente quando o layout da página contém mais de uma coluna.
**Start each group on a new page**
Especifica que a alteração da expressão de grupo forçará as informações a serem renderizadas como uma nova página.
**Reset page number to 1 for each group**
Inicia uma nova página e reinicia a numeração de páginas sempre que o valor da expressão do grupo de dados mudar.
**Reprint group header on each page**
Especifica que o cabeçalho do grupo seguirá o cabeçalho da página em todas as páginas do grupo de dados quando o grupo de dados ocupar mais de uma página.
**Start group on new page when less than**
Especifica a distância mínima da parte inferior da página que determina quando iniciar o cabeçalho do grupo na próxima página. Dica Use esta opção para evitar um cabeçalho de grupo "órfão" e dados potencialmente inadequados no final de uma página sem informações de detalhe correspondentes. Um cabeçalho de grupo órfão pode exibir dados de um registro não mostrado em outro lugar na página, pois o rodapé da página exibirá informações adequadas ao grupo anterior.
**Insert**
Insere uma caixa de texto em branco na caixa Group expressions para que você possa digitar uma nova expressão de grupo.
**Delete**
Exclui a expressão de grupo selecionada da caixa Group expressions.
