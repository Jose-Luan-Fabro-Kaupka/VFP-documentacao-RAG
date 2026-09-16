# Como: editar código de eventos e métodos

Eventos são ações do usuário, como cliques e movimentos do mouse, ou ações do sistema, como a progressão do relógio do sistema. Métodos são procedimentos associados ao objeto e invocados especificamente de forma programática. Para uma discussão sobre eventos e métodos, consulte Object-Oriented Programming. Você pode especificar o código a ser processado quando um evento é disparado ou um método é invocado.

### Para editar código de evento ou método
- No menu View, escolha Code.
- Selecione o evento ou método na caixa Procedure.
- Na janela Edit, escreva o código que deseja que seja processado quando o evento for disparado ou o método for invocado. Por exemplo, você pode ter um botão de comando em um formulário com o Caption "Quit." No evento Click do botão, inclua a linha: THISFORM.Release Dica Para mover entre procedimentos na janela Code Editing, pressione PAGE DOWN ou PAGE UP.

Quando o usuário clica no botão de comando, o formulário é removido da tela e da memória. Se você não deseja liberar o formulário da memória, pode incluir a seguinte linha no evento click:

```foxpro
THISFORM.Hide
```

> **Observação:** Se o código associado ao evento Init de um form set, um formulário ou qualquer objeto em qualquer formulário em um form set retornar false (.F.), o formulário não será criado.
