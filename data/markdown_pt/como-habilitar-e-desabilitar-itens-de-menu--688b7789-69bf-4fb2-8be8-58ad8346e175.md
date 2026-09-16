# Como: habilitar e desabilitar itens de menu

Você pode habilitar ou desabilitar um menu ou item de menu com base em uma condição lógica.

### Para habilitar ou desabilitar um menu ou item de menu
- Na coluna Prompt, selecione o título de menu ou item de menu apropriado.
- Escolha o botão na coluna Options para exibir a caixa de diálogo Prompt Options.
- Selecione Skip For. O Expression Builder aparece.
- Na caixa Skip For, digite a expressão que determina se o menu ou item de menu está habilitado ou desabilitado. Se a expressão avaliar como false (.F.), o menu ou item de menu está habilitado. Se a expressão avaliar como true (.T.), o menu ou item de menu está desabilitado e não pode ser selecionado ou escolhido. Para detalhes, consulte DEFINE BAR e DEFINE PAD. Observação Depois que o sistema de menu tiver sido exibido, você pode habilitar e desabilitar menus e itens de menu usando o Comando SET SKIP OF.

Em um menu, uma marca de seleção ao lado de um item de menu indica que ele está em vigor. Por exemplo, se você colocar uma marca de seleção ao lado do item Credit no menu Customer criado anteriormente, Credit está em vigor.

### Para marcar o estado de um item de menu
- Em tempo de execução, coloque uma marca de seleção ao lado de um item de menu usando o Comando SET MARK OF.

Para um exemplo de desabilitar e marcar o estado de itens de menu, execute Solution.app no diretório Visual FoxPro ...\Samples\Solution.
