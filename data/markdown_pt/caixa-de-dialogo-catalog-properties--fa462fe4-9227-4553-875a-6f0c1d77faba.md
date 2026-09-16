# Caixa de diálogo Catalog Properties

Permite personalizar o comportamento de catálogos do Component Gallery acessando valores na tabela relacionada.

Esta caixa de diálogo aparece quando você clica em Properties no menu de atalho de um catálogo selecionado.

# Guia General

Permite especificar configurações globais para todos os catálogos. As seguintes configurações estão disponíveis nesta guia:
 **Name**
Exibe o valor no campo Text como o rótulo do componente no Component Gallery.
**Description**
Informações opcionais do campo Desc que são exibidas no painel de descrição do Component Gallery.
**Picture**
Valor no campo Folderpict que especifica o caminho e o nome do arquivo do gráfico usado para representar o item na galeria.
**Item picture**
Valor no campo Picture que especifica o caminho e o nome do arquivo do gráfico usado para representar itens neste catálogo que não têm imagem especificada.
**Item Desc.**
Valor no campo Typedesc que contém uma descrição que se aplica a todos os itens contidos neste catálogo ou pasta.

# Guia Node

Um nó é qualquer item selecionável da galeria. Permite especificar configurações globais para todos os catálogos. As seguintes configurações estão disponíveis nesta guia:
 **ID**
O nome da tabela mais o valor no campo ID para o catálogo selecionado.
**Link ID**
Se o item selecionado for um link, especifica o nome do item de origem.
**Classname**
O valor no campo Classname, que especifica o nome da classe do catálogo ou pasta selecionado.
**Class library**
O valor no campo Classlib, que especifica o nome e o caminho para a biblioteca de classes que contém o item da galeria.
**Itemclass**
O valor no campo Itemclass que especifica a classe padrão de itens no catálogo selecionado que não têm classe atribuída anteriormente.
**Dynamic Catalog**
Valor no campo Filename, que contém a expressão de destino, nome de arquivo ou URL que é iniciado quando você seleciona este item de catálogo dinâmico.

# Guia Scripts

Esta guia fornece um local para especificar eventos ou propriedades globais para todos os catálogos. As seguintes áreas estão disponíveis nesta guia:
 **Script**
O valor no campo Script que contém qualquer script de evento relacionado a este catálogo e seus itens.
**Properties**
O valor no campo Properties, que pode conter atribuições de valor a propriedades do item.

# Guia Comments

Permite especificar configurações globais para todos os catálogos. As seguintes configurações estão disponíveis nesta guia:
 **Comments**
O valor no campo Comment, que contém comentários do usuário sobre uso, características ou qualquer outra coisa.
**User**
O valor no campo User, que contém comentários do usuário sobre uso, características ou qualquer outra coisa.

# Guia Item Types

Permite especificar configurações globais para todos os catálogos. Você pode editar a configuração de catálogos existentes selecionando um tipo de catálogo na lista, ou pode adicionar um novo tipo clicando no botão Add.

A guia fornece uma listbox que permite selecionar um tipo de item existente para visualizar ou modificar suas opções. As seguintes configurações também estão disponíveis nesta guia:
 **Add button**
Permite adicionar novos tipos de item à galeria de componentes. Você pode então configurar e especificar as seguintes propriedades:
**Text**
Especifica o rótulo que é exibido no Component Gallery.
**Class**
Especifica o nome da classe do item selecionado.
**Class library**
Especifica o nome e o caminho para a biblioteca de classes que contém o item da galeria.
**File types**
Especifica as opções de extensão de arquivo que a caixa de diálogo GETFILE( ) fornecerá para este item.
**Item Type**
Especifica se o novo tipo de item é uma pasta ou um item da galeria.
**Properties**
Pode conter atribuições de valor a propriedades do item.
**Redirect**
Especifica quais extensões usar com base no tipo de item da galeria.
**Remove button**
Permite remover um tipo de item de galeria existente.
