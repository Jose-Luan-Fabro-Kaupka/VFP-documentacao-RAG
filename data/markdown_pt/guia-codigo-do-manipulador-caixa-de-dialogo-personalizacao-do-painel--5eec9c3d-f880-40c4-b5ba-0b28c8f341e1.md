# Guia Código do manipulador, caixa de diálogo Personalização do painel

A guia Código do manipulador especifica manipuladores para hiperlinks selecionados em um painel quando o tipo de painel é XML ou HTML e o hiperlink começa com `vfps:`. Por exemplo, o seguinte código abre uma janela do navegador para a URL especificada:

`Go to the VFP site`

A tabela a seguir lista os manipuladores padrão integrados ao Task Pane Manager.

| Manipulador padrão | Descrição |
| --- | --- |
| vfps:refresh | Recarrega o painel atual. |
| vfps:linkto | Abre uma janela do navegador para a URL especificada. A URL é especificada com o parâmetro url=cURL. |
| vfps:gotopane | Alterna o Task Pane Manager para o painel especificado. O painel é especificado com o parâmetro uniqueid=cPaneUniqueID. |
| vfps:help | Exibe a Ajuda especificada por tópico ou ID. A Ajuda é exibida usando os parâmetros ID=cTopicID ou Topic=cTopicName. |
| vfps:options | Exibe a caixa de diálogo Opções do painel de tarefas para o painel especificado. O painel é especificado com o parâmetro uniqueid=cPaneUniqueID. |
| vfps:message | Exibe uma caixa de mensagem informativa. A mensagem é especificada com o parâmetro msg=cMessage. |

Você pode incluir o parâmetro refresh com qualquer código de manipulador para que o painel seja recarregado imediatamente após a chamada do manipulador. Isso é útil quando o resultado do link pode afetar o conteúdo do painel. Você pode usar o parâmetro refresh com outros parâmetros, conforme mostrado no exemplo a seguir:

`vfps:message?msg=This is a message&refresh`

A tabela a seguir lista os parâmetros passados ao código quando você usa código de manipulador personalizado.

| Parâmetro | Descrição |
| --- | --- |
| cAction | Especifica a ação, que é o texto após vfps: e antes de quaisquer parâmetros. Por exemplo, o seguinte especifica o uso de um manipulador personalizado chamado MyAction : This is my handler |
| oParameters | Uma coleção dos parâmetros especificados. Além disso, se for um envio de formulário, a coleção também inclui os valores do formulário. Para recuperar um valor, chame a função GetParam( ) com o nome do parâmetro, conforme mostrado no exemplo a seguir: oParameters.GetParam("ParameterName") |
| oBrowser | Contém a referência de objeto ao objeto Window no controle do navegador no painel. Você pode usar isso para acessar métodos e propriedades DHTML. Por exemplo: oBrowser.document.all("SearchResults").style.display = "none" |
| oContent | Contém uma referência à definição de conteúdo do painel para que você possa recuperar valores de opção e a pasta PaneCache especificada na caixa de diálogo Opções do painel de tarefas. Este é o mesmo objeto passado para um script na guia Dados, caixa de diálogo Personalização do painel . |
 **Modificar**
Abre uma janela para editar o código do manipulador.
**Caixa de edição**
Exibe o código do manipulador.
