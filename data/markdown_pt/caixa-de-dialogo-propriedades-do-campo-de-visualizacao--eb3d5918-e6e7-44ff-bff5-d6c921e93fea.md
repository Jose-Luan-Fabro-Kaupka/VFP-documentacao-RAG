# Caixa de diálogo Propriedades do campo de visualização

Use para especificar opções para campos em uma visualização da mesma forma que você pode para campos em tabelas de banco de dados. Você pode definir propriedades para determinar o tipo de dados que o campo armazena, controlar a entrada de dados para visualizações atualizáveis e controlar a exibição do campo.

Esta caixa de diálogo aparece quando você seleciona um campo e clica no botão Properties na guia Fields dos Query and View Designers.
 **Field**
Especifica o nome do campo selecionado na visualização. Para definir propriedades em outros campos selecionados, você pode escolher na lista suspensa. O campo aparece com seu número sequencial de campo.

# Opções de validação de campo

Essas opções permitem controlar o conteúdo do campo.
 **Rule**
Especifica a expressão para a regra em nível de campo que controla quais valores podem ser inseridos no campo.
**Message**
Especifica a mensagem de erro exibida quando a regra em nível de campo é violada.
**Default value**
Especifica uma quantidade ou cadeia de caracteres que é o conteúdo de um campo quando um novo registro é adicionado. O valor padrão permanece no campo até que você insira um novo valor.

# Opções de exibição

Essas opções permitem controlar como os valores são inseridos ou exibidos no campo.
 **Format**
Especifica a expressão para maiúsculas/minúsculas, tamanho e estilo para exibição do campo na janela Browse, formulários ou relatórios. Configurações de propriedade no formulário e no relatório podem substituir esta expressão.
**Input Mask**
Especifica o formato dos valores conforme são inseridos no campo. Por exemplo, números de telefone podem ter o formato (999) 999-9999.
**Caption**
Especifica o rótulo que aparece para o campo na janela Browse, formulários ou relatórios. Configurações de propriedade no formulário ou relatório podem substituir esta configuração. Para especificar uma expressão para um Caption de campo, inclua o sinal de igual (=) antes da cadeia de caracteres do Caption. Se um sinal de igual não for encontrado, ele é tratado como um literal de cadeia de caracteres. Expressões não podem exceder 254 caracteres. Se a expressão exceder 254 caracteres, o Caption assume como padrão o nome do campo. Observação O suporte para usar expressões como Captions de campo deve ser usado apenas com tabelas DBC em aplicativos executados no Visual FoxPro 8.0 ou posterior. Em versões anteriores, a expressão aparece como um literal de cadeia de caracteres.

# Opções Mapear tipo de campo para classes

Se você planeja usar o campo de visualização em formulários, essas opções permitem especificar um tipo de controle padrão que aparece quando você solta o campo em um formulário.
 **Display library**
Especifica o arquivo de biblioteca de classes (.vcx) que contém a classe de controle que você deseja associar ao campo.
**Display class**
Especifica o tipo de controle que é criado quando o campo é solto em um formulário.

# Opções de mapeamento de dados

Por padrão, o campo de visualização tem as mesmas configurações de propriedade que seu campo associado em uma tabela. Essas opções são habilitadas apenas para visualizações remotas.
 **Data type (remote views only)**
Especifica o tipo de dados que este campo pode armazenar.
**Width (remote views only)**
Especifica o número de caracteres que este campo pode armazenar.
**Decimal (remote views only)**
Para tipos de dados numéricos, especifica o número de casas à direita do ponto decimal que este campo pode armazenar.
**Comment (remote views only)**
Fornece espaço para você digitar um comentário sobre o campo.
