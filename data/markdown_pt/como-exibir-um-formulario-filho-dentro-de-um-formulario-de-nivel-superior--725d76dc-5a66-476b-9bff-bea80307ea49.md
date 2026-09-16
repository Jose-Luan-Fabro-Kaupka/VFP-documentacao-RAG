# Como: exibir um formulário filho dentro de um formulário de nível superior

Se você criou um formulário filho no qual a propriedade ShowWindow está definida como 1 — In Top-Level Form, você não especifica diretamente o formulário de nível superior que atua como pai do formulário filho. Em vez disso, o Visual FoxPro atribui o formulário filho a um pai no momento em que a janela filha é exibida.

### Para exibir um formulário filho dentro de um formulário de nível superior
- Crie um formulário de nível superior.
- No código de evento do formulário de nível superior, inclua o comando DO FORM, especificando o nome do formulário filho a ser exibido. Por exemplo, crie um botão no formulário de nível superior e, no código do evento Click do botão, inclua um comando como este: DO FORM MyChild Observação O formulário de nível superior deve estar visível e ativo quando o formulário filho é exibido. Portanto, você não pode usar o evento Init do formulário de nível superior para exibir um formulário filho, porque o formulário de nível superior ainda não estará ativo.
- Ative o formulário de nível superior e, se necessário, acione o evento que exibe o formulário filho.
