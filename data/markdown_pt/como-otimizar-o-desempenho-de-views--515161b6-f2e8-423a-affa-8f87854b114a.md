# Como: otimizar o desempenho de views

Você pode otimizar suas views definindo opções de busca de dados e desempenho. Use a caixa de diálogo Advanced Options para ajustar como os registros são recuperados em uma view ou como as atualizações são feitas no servidor ou nas tabelas de origem.

### Para definir opções avançadas
- No menu Query, escolha Advanced Options .
- Na caixa de diálogo Advanced Options, defina as informações de conexão e as opções de busca de dados que você precisa.
- Escolha OK .

Você pode controlar o número de linhas que o Visual FoxPro busca progressivamente de uma vez do banco de dados host com a propriedade Fetchsize da view e do cursor usando as funções DBSETPROP( ) e CURSORSETPROP( ). Para obter mais informações, consulte DBSETPROP( ) Function e CURSORSETPROP( ) Function.

Você pode usar o recurso de busca de memo atrasada para acelerar a recuperação de dados de views. Quando você escolhe delayed memo fetching, o Visual FoxPro não recupera o conteúdo de um campo Memo até que você escolha abrir e exibir o campo. Como o Visual FoxPro precisa do campo de chave e do nome da tabela para localizar uma linha na fonte de dados remota, você deve definir as seguintes propriedades usando as funções DBSETPROP( ) e CURSORSETPROP( ) para que a busca de Memo atrasada funcione:
 - Propriedade UpdateName ou propriedade UpdatableFieldList
- Propriedade KeyField ou propriedade KeyFieldList
- Propriedade Tables

No entanto, você não precisa definir as propriedades SendUpdates ou Updatable como ON para que a busca de memo atrasada funcione.
