# Como: gerenciar documentos com o Application Builder

Depois de selecionar fontes de dados, você precisa planejar e escolher os documentos que deseja adicionar à aplicação. O Application Builder é particularmente eficaz para esta tarefa, pois não apenas adiciona o documento ao projeto, mas também o integra ao framework. Como o framework usa informações de documento estendidas armazenadas em uma meta-tabela, o Application Builder trata automaticamente dessa integração. A meta-tabela é armazenada na mesma pasta do projeto da aplicação e recebe o mesmo nome do projeto mais o sufixo "_app.dbf". As informações de documento estendidas armazenadas na meta-tabela do framework especificam o seguinte:
 - Um nome amigável a exibir na caixa de diálogo Open ou New.
- Se um formulário aparece na caixa de diálogo New.
- Se um formulário aparece na caixa de diálogo Open.
- Se um formulário usa uma barra de ferramentas de navegação.
- Se um formulário usa um menu de navegação.
- Se um formulário permite a abertura de várias instâncias.

Você pode fazer o builder criar automaticamente novos formulários e relatórios ao adicionar dados à aplicação. Esses documentos são gerados a partir dos assistentes associados.

Depois que um documento é adicionado ao framework da aplicação, ele aparecerá automaticamente na guia Forms ou Reports.

Ao abrir a guia Forms, você encontrará uma lista contendo os formulários que já adicionou à aplicação manualmente ou a partir de entradas na guia Data.

> **Observação:** É possível que um formulário em seu projeto não apareça na guia Forms. Isso ocorre porque esse formulário não está registrado na meta-tabela da aplicação. Você pode registrá-lo escolhendo o formulário usando o botão Add na página Forms Tab. Além disso, o botão Cleanup na Advanced Tab, Application Builder sincronizará os documentos em seu projeto com os registrados na meta-tabela. Você também pode editar ou remover qualquer um desses documentos na guia apropriada.

### Para adicionar documentos no Application Builder
- Clique no botão Add na guia de documento apropriada (Form ou Report) e selecione um documento. O framework da aplicação trata automaticamente de uma variedade de tipos de documento. Com formulários, você pode selecionar um arquivo de formulário (.scx), uma classe de formulário de uma biblioteca de classes (.vcx) ou um arquivo de programa (.prg) que contém código que executa um formulário. Com relatórios, você pode escolher um arquivo de relatório (.frx), arquivo de etiqueta (.lbx) ou arquivo de programa (.prg) que tem código para executar um relatório.
- Depois de adicionar o arquivo à lista de documentos, você pode escolher várias configurações em termos de como esse documento funciona na aplicação.

A guia Forms permite gerenciar as seguintes opções:
 - O nome amigável do formulário.
- Se o formulário é limitado a uma única instância.
- Se o formulário usa uma barra de ferramentas de navegação.
- Se o formulário usa um menu de navegação.
- Se o formulário aparece na caixa de diálogo New.
- Se o formulário aparece na caixa de diálogo Open. A guia Reports permite gerenciar as seguintes opções:
- O nome amigável do relatório.
- Se seu relatório aparece na caixa de diálogo Print Reports.

### Para editar documentos no Application Builder
- Abra qualquer formulário ou relatório listado destacando o documento e clicando no botão Edit. No caso de um formulário, você pode receber a seguinte mensagem: "Would you like to add a mediator object to this form to fully enable it for use with the application framework?" Se você responder "Yes", o Application Builder adiciona ao formulário um objeto que se comunica automaticamente diretamente com o objeto de aplicação usado pelo framework. Este objeto fornece funcionalidade adicional a formulários na aplicação. Por exemplo, ao fechar um formulário, o objeto pode detectar se há dados em buffer que não foram salvos e solicitar que você salve as alterações. Além disso, o objeto diferenciará entre um formulário iniciado usando a caixa de diálogo New versus a caixa de diálogo Open.
- No designer, edite seu documento como desejar. Você pode querer usar o Component Gallery para adicionar um plano de fundo ou classe foundation. Você pode usar o Component Gallery para adicionar características e funcionalidade especiais ao documento.

### Para remover documentos no Application Builder
- Você pode remover qualquer documento da meta-tabela destacando o documento e clicando no botão Remove. Depois que o documento é removido da aplicação, ele permanece no arquivo de projeto. Observação Sua aplicação será executada independentemente de um formulário ou relatório estar armazenado na meta-tabela. Enquanto você fornecer código que especifique como executar esse documento, a aplicação o tratará adequadamente. A vantagem de usar o Application Builder é que você não precisaria se preocupar com a aplicação executando formulários e relatórios. Isso é feito automaticamente.
