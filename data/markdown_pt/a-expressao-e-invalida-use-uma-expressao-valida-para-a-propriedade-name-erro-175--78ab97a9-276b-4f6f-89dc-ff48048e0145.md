# A expressão é inválida. Use uma expressão válida para a propriedade "name" (Erro 1759)

A expressão que você inseriu para uma propriedade de grade não é válida. A expressão é removida da configuração da propriedade.
 - Se você estiver definindo a expressão no evento AfterRowColChange da grade, o erro em si faz o evento ser disparado novamente, levando a um loop recorrente de mensagens de erro. Pressione Cancelar na caixa de diálogo para desabilitar a expressão. Você não poderá definir ou alterar a expressão.
- A expressão contém erros de sintaxe. Certifique-se de que sua expressão é válida e sem erros de sintaxe.
- Variáveis na expressão não estão com escopo adequado. Certifique-se de que quaisquer variáveis que você use na expressão tenham escopo global ou escopo no formulário. Se sua expressão contém uma variável que é local à função na qual você está definindo a expressão, a variável sairá de escopo quando a função retornar. No entanto, a expressão será avaliada no futuro quando a grade tentar pintar, e isso causará um erro.
