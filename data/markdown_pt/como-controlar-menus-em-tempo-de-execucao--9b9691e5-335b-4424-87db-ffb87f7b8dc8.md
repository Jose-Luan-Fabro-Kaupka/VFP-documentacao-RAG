# Como: controlar menus em tempo de execução

Cada menu do Visual FoxPro tem dois nomes, e cada item de menu tem um nome e um número. O Visual FoxPro usa um nome na interface do usuário e o outro nome ou número no programa de menu gerado (.mpr). Você pode usar esses nomes ou números para referenciar e controlar menus e itens de menu em tempo de execução. Se você não fornecer um nome ou número ao criar menus e itens de menu, o Visual FoxPro cria um quando você gera o programa de menu.

Para um exemplo de adicionar e remover itens de menu em tempo de execução, consulte Solution.app no diretório Visual FoxPro ...\Samples\Solution.

> **Cuidado:** Evite usar nomes e números gerados pelo Visual FoxPro no código, porque eles mudam cada vez que você gera o programa de menu. Se você referenciar um nome ou número gerado, seu código pode falhar.

No Menu and Shortcut Designers, a coluna Prompt mostra o que aparece na interface do usuário, e a coluna à direita da caixa Result mostra o que aparece no programa gerado.

### Para especificar um nome para um pad de menu
- Na coluna Prompt, selecione o título de menu apropriado. Observação A coluna Result deve mostrar Command , Submenu ou Procedure — não Pad Name .
- Escolha o botão na coluna Options para exibir a caixa de diálogo Prompt Options.
- Na caixa Pad Name, digite o nome de sua escolha.
- Escolha OK para retornar ao Menu Designer .

### Para especificar um número para um item de menu
- Na coluna Prompt, selecione o item de menu apropriado. Observação A coluna Result deve mostrar Command , Submenu ou Procedure — não Bar # .
- Escolha o botão na coluna Options para exibir a caixa de diálogo Prompt Options.
- Na caixa Bar #, digite o número de sua escolha.
- Escolha OK para retornar ao Menu Designer . Dica Se você usar o recurso Quick Menu, não altere os nomes ou números que o Visual FoxPro fornece para menus ou itens de menu do sistema; caso contrário, você pode obter resultados imprevisíveis ao executar o programa de menu gerado.
