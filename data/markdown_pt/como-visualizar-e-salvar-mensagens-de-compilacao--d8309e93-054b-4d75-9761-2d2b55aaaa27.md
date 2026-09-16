# Como: visualizar e salvar mensagens de compilação

Quando você compila um projeto, aplicativo ou biblioteca de vínculo dinâmico, o Visual FoxPro inclui mensagens de status e erro de compilação em um arquivo de erro, que é um arquivo de texto com a extensão de nome de arquivo .err, conforme ocorrem durante o processo de compilação. O arquivo .err tem o mesmo nome base do seu projeto e é criado no diretório atual. Quando você compila ou recompila um projeto, aplicativo ou biblioteca de vínculo dinâmico, as mensagens de compilação também são incluídas no mesmo arquivo .err.

Se o processo de compilação for interrompido, você pode abrir o arquivo .err para revisar essas mensagens. Você também pode selecionar a opção Exibir erros na caixa de diálogo Opções de compilação para exibir uma janela de edição para o arquivo .err após a conclusão do processo de compilação, para que possa revisar quaisquer erros.

> **Observação:** Se nenhum erro ocorrer durante a compilação, o arquivo .err é removido.

Durante o processo de compilação, as mensagens de status de compilação aparecem na barra de status. Após a conclusão do processo de compilação, o número de erros de compilação aparece na barra de status.

### Para exibir ou visualizar o arquivo de erro
- Compile o projeto, aplicativo ou arquivo de biblioteca de vínculo dinâmico seguindo as etapas em Como: testar um projeto ou Como: compilar aplicativos .
- Para exibir o arquivo de erro automaticamente após a conclusão do processo de compilação, quando a caixa de diálogo Opções de compilação estiver aberta, selecione a caixa de seleção Exibir erros. -OU- Para visualizar o arquivo de erro após a conclusão do processo de compilação, no menu Projeto, escolha Erros .

Para obter mais informações, consulte Caixa de diálogo Opções de compilação.

Você também pode especificar se deseja incluir mensagens de compilação usando o comando SET LOGERRORS. Para obter mais informações, consulte Comando SET LOGERRORS.

Você também pode visualizar e salvar mensagens de status de compilação que aparecem na janela Saída de depuração quando ela está aberta no Depurador. Para obter mais informações, consulte Janela Saída de depuração e Janela Depurador.

### Para incluir mensagens de erro de compilação no arquivo de erro
- Compile o projeto, aplicativo ou arquivo de biblioteca de vínculo dinâmico seguindo as etapas em Como: testar um projeto ou Como: compilar aplicativos , respectivamente.
- Na caixa de diálogo Opções de compilação, selecione a caixa de seleção Recompilar todos os arquivos.
