# Como: remover arquivos de um projeto sob controle de código-fonte

Você pode remover arquivos individuais do controle de código-fonte se não quiser mais que façam parte do seu projeto sob controle de código-fonte. Você pode fazer isso, por exemplo, se um programa ou formulário se tornar obsoleto e não fizer mais parte do seu projeto.

### Para remover um arquivo do controle de código-fonte
- Na janela Project Manager, selecione o arquivo a remover.
- No menu Project, escolha Source Control e depois Remove Files from Source Control.
- Na caixa de diálogo Remove Files from Source Control, selecione os arquivos a remover e clique em OK.

Se você remover um arquivo de um projeto do Visual FoxPro que está sob controle de código-fonte, o Visual FoxPro solicitará se você deseja apenas remover o arquivo do projeto ou excluí-lo do disco. Uma configuração na caixa de diálogo Options determina se o Visual FoxPro também solicitará que você remova o arquivo do projeto sob controle de código-fonte.
 - Se Remove files from source control upon removal from project estiver marcado, o Visual FoxPro também solicitará que você remova o arquivo do projeto sob controle de código-fonte.
- Se Remove files from source control upon removal from project não estiver marcado, você não será solicitado e o arquivo permanecerá sob controle de código-fonte.

Depois que um arquivo foi removido do controle de código-fonte, cópias dele ainda podem existir nos computadores de outros desenvolvedores. Se for o caso, o arquivo é tratado como um arquivo local somente para esses desenvolvedores.
