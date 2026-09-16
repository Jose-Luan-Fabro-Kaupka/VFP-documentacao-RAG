# Como: editar objetos OLE em formulários e tabelas

Quando você adiciona um objeto OLE a uma tabela ou formulário, pode editar os dados e as configurações de exibição do objeto em tempo de design ou em tempo de execução.

> **Observação:** Você não pode editar os dados de um objeto OLE em um controle OLE Bound em tempo de design.

Alguns objetos OLE incorporados suportam edição no local, de modo que você pode editar o objeto na janela usada pelo seu aplicativo. Por exemplo, se você clicar duas vezes em um objeto de planilha do Microsoft Excel em um campo General, os títulos dos menus mudam para refletir a estrutura de menus do Microsoft Excel e as barras de ferramentas padrão do Microsoft Excel são exibidas. Você ou o usuário do aplicativo pode editar o objeto do Microsoft Excel sem sair do seu aplicativo. No entanto, os menus padrão File, Program e Window do Visual FoxPro não são substituídos.

> **Observação:** Somente objetos incorporados podem ser editados no local, não objetos vinculados.

Se você criar um título de menu e quiser que ele seja exibido mesmo enquanto o usuário edita um objeto OLE, selecione Negotiate na caixa de diálogo Prompt Options do Menu Designer. Para obter mais informações, consulte Designing Menus and Toolbars ou a cláusula NEGOTIATE no tópico Comando DEFINE PAD.

Você também pode abrir o servidor Automation em outra janela, editar os dados ou as características de exibição lá e ter os novos valores refletidos no seu aplicativo quando retornar a ele.

### Para editar dados em um campo General em uma tabela
- Abra a tabela desejada em uma janela de navegação.
- Clique duas vezes no campo General que deseja editar. Uma janela de edição é aberta para o campo General.
- Na janela de edição, clique duas vezes no objeto para editar os dados.

### Para editar objetos incorporados ou vinculados em um formulário durante o design do formulário
- Selecione o objeto que representa os dados.
- Com o ponteiro do mouse sobre o objeto, clique o botão direito do mouse.
- No menu de atalho, escolha o tipo de objeto e, em seguida, escolha Edit ou Open .

### Para editar objetos ou dados de campos General em um formulário durante a execução do formulário
- No menu Edit, selecione o objeto. Por exemplo, se o objeto é uma planilha do Microsoft Excel, selecione Spreadsheet Object no menu Edit. Dica Você também pode clicar com o botão direito no objeto se a propriedade AutoVerbMenu estiver definida como True. Escolha o tipo de objeto e, em seguida, escolha Edit ou Open.
- Para editar o objeto visualmente, escolha Edit no submenu. -ou- Para editar o objeto em uma janela separada, escolha Open no submenu. Cuidado Se você alterar os dados em um objeto durante a execução de um formulário, o Visual FoxPro salva as alterações somente se os dados estiverem vinculados ou associados a um controle OLE Bound. Alterações associadas a um controle OLE Container não são salvas.
