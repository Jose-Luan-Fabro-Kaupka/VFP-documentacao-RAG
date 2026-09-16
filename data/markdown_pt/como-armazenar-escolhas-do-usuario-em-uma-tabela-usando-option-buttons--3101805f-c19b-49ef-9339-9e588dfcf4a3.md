# Como: armazenar escolhas do usuário em uma tabela usando option buttons

Embora não seja tão comum, você pode usar option buttons para obter informações de um usuário a serem armazenadas em uma tabela salvando a propriedade Caption (Visual FoxPro). Se você tem um aplicativo de testes padronizado, por exemplo, poderia usar option buttons para permitir que um usuário escolha entre as opções de múltipla escolha A, B, C ou D. Você também poderia usar option buttons para indicar o gênero em uma tabela de funcionários.

### Para armazenar a propriedade Caption de um option button em uma tabela
- Defina a propriedade Value do option button group como uma cadeia de caracteres vazia.
- Defina a propriedade Control do option button group para um campo de caracteres em uma tabela.

Por exemplo, se os captions dos option buttons em um grupo são "A", "B", "C" e "D", e o ControlSource do option button group é um campo de caracteres, quando um usuário escolhe o botão com o caption "B", "B" é armazenado no campo.

### Para ver um exemplo de um teste de múltipla escolha usando option buttons
- Execute Solution.app no diretório Visual FoxPro ...\Samples\Solution.
- Na exibição em árvore, clique em Controls e depois em Options buttons.
- Clique em Present a user with multiple choices.
