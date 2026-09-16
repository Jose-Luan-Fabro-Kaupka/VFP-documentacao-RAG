# Como: editar registros do IntelliSense

Você pode adicionar novos itens à tabela IntelliSense ou editar itens existentes. Você pode editar itens definidos pelo usuário na tabela IntelliSense usando o Visual FoxPro IntelliSense Manager ou todos os registros do IntelliSense abrindo e navegando na tabela diretamente ou acessando a tabela programaticamente.

### Para adicionar novos itens à tabela IntelliSense
- No menu Tools, clique em IntelliSense Manager.
- No IntelliSense Manager, clique na guia Custom. A guia Custom lista todos os itens definidos pelo usuário na tabela IntelliSense.
- Na caixa Type, selecione o tipo de item desejado. Observação O botão Add torna-se disponível quando você seleciona inicialmente um tipo diferente de Command.
- Clique em Add. Um novo registro aparece no início da tabela exibida na guia Custom.
- Na caixa Replace, digite os caracteres a substituir pelo texto na caixa With. Observação Quando você digita os caracteres na caixa Replace na localização apropriada do cursor, o texto especificado na caixa With substitui o texto digitado.
- Na caixa With, digite os caracteres que deseja usar para substituir o texto na caixa Replace.
- Para adicionar código ao campo Data, clique em Script. Uma janela de editor abre para que você possa adicionar código ao campo Data desse item.
- Para visualizar e editar o registro inteiro, clique em Edit. A tabela IntelliSense abre para que você possa editar outros campos no registro.

Para obter mais informações, consulte a janela Visual FoxPro IntelliSense Manager.

### Para editar itens existentes definidos pelo usuário na tabela IntelliSense
- No menu Tools, clique em IntelliSense Manager.
- No IntelliSense Manager, clique na guia Custom. A guia Custom lista todos os itens definidos pelo usuário na tabela IntelliSense.
- Na lista de itens, selecione o item que deseja editar.
- Para visualizar e editar o registro inteiro, clique em Edit.

# Abrindo a tabela IntelliSense programaticamente

Você pode acessar a tabela IntelliSense programaticamente usando a variável de sistema _FOXCODE. Para obter mais informações, consulte a variável de sistema _FOXCODE.

### Para abrir a tabela IntelliSense programaticamente
- Na janela Command, digite as seguintes linhas de código: USE (_FOXCODE) SHARED BROWSE A tabela IntelliSense abre em uma janela Browse.
