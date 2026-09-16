# Guia Fields, Table Designer

A guia Fields exibe informações ligeiramente diferentes dependendo de você abrir uma tabela de banco de dados ou uma tabela livre. Se você estiver criando uma tabela de banco de dados, a guia Fields inclui opções para definir regras de validação. Se você estiver criando uma tabela livre, a guia Fields contém somente opções básicas de nome de campo, tipo e formatação.

A guia Fields exibe campos de tabela em uma grade rolável. Cada linha contém o nome do campo, tipo de dados, largura de caracteres, largura decimal e suporte a valores nulos. Clique em uma célula na grade para modificar um campo.
 **Mover Button**
Este é o botão de seta dupla na extremidade esquerda da linha. Depois de ter inserido duas ou mais linhas, use o botão mover para mover uma linha para cima ou para baixo na lista.
**Name**
Especifica o nome do campo. Espaços não são aceitos. Para tabelas de banco de dados, o comprimento do nome pode ter até 128 caracteres. Para obter mais informações, consulte Criando nomes do Visual FoxPro.
**Type**
Especifica o tipo de dados do campo. Clique na seta suspensa para selecionar um tipo de dados da lista.
**Width**
Especifica o número de caracteres ou dígitos que o campo pode armazenar.
**Decimal**
Especifica o número de dígitos à direita do ponto decimal. A coluna Decimal se aplica a tipos de dados numéricos e double.
**Index**
Especifica um índice regular no campo para ordenar os dados.
**NULL**
Quando marcado, especifica que o campo pode aceitar um valor nulo.
**Insert Button**
Insere um novo campo acima do campo selecionado.
**Delete Button**
Exclui o campo selecionado da tabela.
**Display**
Especifica as propriedades de formato para entrada e exibição do campo. Format Especifica a expressão para maiúsculas/minúsculas, tamanho e estilo para exibição do campo na janela Browse, formulários ou relatórios. Configurações de propriedade dentro do formulário e relatório podem substituir esta expressão. Input mask Especifica o formato para valores conforme são inseridos no campo. Por exemplo, números de telefone podem ter um formato de (999) 999-9999. Caption Especifica o rótulo que aparece para o campo na janela Browse, formulários ou relatórios. Configurações de propriedade dentro do formulário ou relatório podem substituir esta configuração. Para especificar uma expressão para um caption de campo, inclua um sinal de igual (=) precedendo a cadeia de caption. Expressões não podem exceder 254 caracteres. Se a expressão exceder 254 caracteres, o caption assume o nome do campo por padrão. Observação O suporte para usar expressões como captions de campo deve ser usado somente com tabelas DBC em aplicativos executados no Visual FoxPro 8.0 ou posterior. Em versões anteriores, a expressão aparece como um literal de cadeia de caracteres.
**Field validation**
Se você estiver modificando uma tabela de banco de dados, o grupo de opções Field Properties aparece abaixo da grade rolável. Configurações de propriedades para o campo selecionado são especificadas nesta área. Escolha o botão de diálogo à direita de cada configuração de propriedade para exibir a caixa de diálogo Expression Builder Dialog Box, ou simplesmente digite a expressão diretamente. Entradas para estas opções não são obrigatórias. Rule Especifica a regra de nível de campo para impor validação de dados. Message Especifica a mensagem de erro a ser exibida se uma entrada violar a regra de validação de nível de campo. Default value Especifica o valor padrão para o campo.
**Map field type to classes**
Para especificar uma classe de controle padrão, defina a biblioteca e a classe que deseja criar quando arrastar o campo para um formulário. Display library Especifica o caminho e o nome do arquivo para a biblioteca de classes. Para procurar um arquivo, use o botão de diálogo. Display class Especifica a classe de controle padrão para o campo.
**AutoIncrement**
Para definir os valores inicial e de incremento depois de habilitar autoincremento para um campo, selecione valores nas caixas de rotação Next Value e Step. Para obter mais informações sobre autoincremento, consulte Valores de campo autoincremento em tabelas. Next Value Especifica o valor inicial para um campo usando autoincremento. Você pode selecionar um valor inteiro positivo ou negativo de 2.147.483.647 a -2.147.483.647. O valor padrão é 1. Step Especifica o valor de incremento para um campo usando autoincremento. Você pode selecionar um valor inteiro positivo diferente de zero de 1 a 255. O valor padrão é 1.
**Field comment**
Fornece um espaço para inserir notas sobre o campo.
