# Caixa de diálogo Expression Builder

Permite criar e editar expressões. O Expression Builder fornece listas de opções apropriadas e pode ser aberto a partir de vários designers, janelas, builders e assistentes.

Para criar uma expressão, digite-a na caixa Expression ou selecione itens das listas Functions. Uma expressão pode ser simples, como um nome de campo, ou complexa, como um cálculo envolvendo funções IIF( ), concatenações e conversões de tipo de dados.
 **Expression**
Exibe a expressão que você está criando ou editando. Dica Você pode inserir mais de 255 caracteres, bem como caracteres estendidos, como CHR(13) (retorno de carro) e CHR(10) (avanço de linha), para expressões no Expression Builder. A caixa Expression no Expression Builder suporta sintaxe colorida e compilação em segundo plano quando ativada. Para obter mais informações, consulte Como: exibir e imprimir código-fonte em cores . Cuidado Valores de propriedade que excedem 255 caracteres ou incluem caracteres estendidos contêm preenchimento com caracteres CHR(1). No entanto, classes em arquivos de biblioteca de classes visuais (.vcx) que contêm propriedades com esses valores não podem ser usadas em versões anteriores ao Visual FoxPro 9.0. Se você tentar modificar essas classes em uma versão anterior, ocorre um erro. Você ainda pode usar outras classes nos mesmos arquivos de biblioteca de classes visuais (.vcx) com versões anteriores do Visual FoxPro, desde que não contenham valores de propriedade que excedam 255 caracteres ou incluam caracteres estendidos.
**Functions**
Exibe listas de tipos de função. Quando você seleciona uma função de um dos quatro tipos, o Visual FoxPro a cola automaticamente na caixa de expressão. Ao construir expressões para views remotas, o Visual FoxPro lista somente as funções específicas do back-end de dados de destino. String Lista as funções de cadeia de caracteres disponíveis. Logical Lista as funções lógicas disponíveis. Math Lista as funções matemáticas disponíveis. Date Lista as funções de data e hora disponíveis.
**Fields**
Lista os campos na tabela ou view atual. Para colar um campo na caixa Expression, clique duas vezes no campo ou selecione o campo e pressione ENTER. Para exibir campos de uma tabela diferente, selecione uma tabela diferente na caixa From Table.
**From Table**
Lista tabelas e views que estão abertas. Selecione uma tabela ou view para atualizar a caixa Fields.
**Variables**
Lista variáveis de memória do sistema, matrizes e variáveis de memória que você criou. Para colar uma variável na caixa Expression, clique duas vezes na variável ou selecione a variável e pressione ENTER.
**Verify**
Valida a sintaxe da expressão na caixa de expressão se a tabela correspondente estiver aberta. Se a expressão for válida, "Expression is valid" é exibido na barra de status. Se não for válida ou se a tabela correspondente não estiver aberta, o Visual FoxPro exibe uma mensagem de erro. Esta opção não está habilitada para views remotas. Cuidado Se você incluir uma chamada de função definida pelo usuário na expressão, um erro é indicado; no entanto, um erro não necessariamente ocorre quando a expressão é avaliada em tempo de execução.
**Options**
Exibe a caixa de diálogo Expression Builder Options, que você pode usar para definir preferências para o Expression Builder. Para obter mais informações, consulte a caixa de diálogo Expression Builder Options .

A tabela a seguir descreve algumas funções úteis para manipular cadeias de caracteres em expressões.

| Se você deseja | Use esta função |
| --- | --- |
| Remover espaços em branco à esquerda e à direita de expressões de caracteres | Função ALLTRIM( ) |
| Remover espaços em branco à esquerda | Função LTRIM( ) |
| Remover espaços em branco à direita | Função RTRIM( ) |
| Adicionar caracteres especificados à esquerda, à direita ou em ambos os lados de uma cadeia de caracteres | Funções PADL( ) | PADR( ) | PADC( ) |
| Trabalhar com partes de uma cadeia de caracteres para comparações | Função SUBSTR( ) |
| Usar um número especificado de caracteres começando pela esquerda de uma cadeia de caracteres | Função LEFT( ) |
| Usar um número especificado de caracteres começando pela direita de uma cadeia de caracteres | Função RIGHT( ) |
| Alterar maiúsculas para minúsculas ou minúsculas para maiúsculas | Função UPPER( ) , Função LOWER( ) |
| Converter uma cadeia de caracteres para iniciais maiúsculas | Função PROPER( ) |
| Ter um campo numérico interpretado como uma cadeia de caracteres | Função STR( ) |
