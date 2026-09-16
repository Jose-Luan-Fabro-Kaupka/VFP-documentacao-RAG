# Como: atualizar a lista do projeto

Mesmo depois que arquivos forem adicionados ao projeto sob controle de origem, outros desenvolvedores não poderão trabalhar com eles. Os desenvolvedores poderão usar manualmente o sistema de controle de origem para fazer check-out e check-in de arquivos, se necessário, mas os arquivos adicionados não serão exibidos no Project Manager para nenhum desenvolvedor, exceto o que os adicionou. Para disponibilizar os arquivos a outros desenvolvedores, atualize a lista do projeto.

Quando você atualiza a lista do projeto, o Visual FoxPro:
 - Gera uma nova lista local de arquivos do projeto (arquivo .pjm).
- Faz check-in da nova lista de arquivos do projeto (com a opção definida para manter o arquivo com check-out).
- Mescla as listas local e central de arquivos do projeto se houver diferenças. Se ocorrer um conflito de mesclagem, o Visual FoxPro exibe uma caixa de diálogo para ajudá-lo a resolver os conflitos de mesclagem.
- Reconstrói o arquivo local do projeto (.pjx) com base na lista mesclada de arquivos do projeto.
- Obtém cópias locais de arquivos adicionados ao projeto por outros desenvolvedores.
- Solicita que você obtenha as versões mais recentes dos arquivos do projeto.
- Atualiza a exibição no Project Manager para refletir as alterações.

### Para atualizar a lista do projeto
- No menu Project, escolha Source Control e, em seguida, escolha Update Project List.

Como parte dos procedimentos de atualização, o Visual FoxPro solicita que você obtenha as versões mais recentes dos arquivos. Se você já tiver um arquivo com check-out, como regra geral não deve obter a versão mais recente, porque sua versão quase certamente é mais atual do que a que está na rede.

Se você estiver obtendo a versão mais recente de um arquivo de texto (como um programa), o software de controle de origem pode tentar mesclar as alterações mais recentes com sua versão. Para obter mais informações sobre mesclagem de arquivos de texto, consulte Como: fazer check-in de arquivos.

Quando terminar, outros desenvolvedores também devem atualizar a lista do projeto (usando o mesmo procedimento) para poder trabalhar com os arquivos que você adicionou.
