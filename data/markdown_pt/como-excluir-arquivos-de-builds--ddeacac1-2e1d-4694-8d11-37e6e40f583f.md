# Como: excluir arquivos de builds

Antes de construir um arquivo distribuível para o projeto do seu aplicativo, exclua do processo de build os arquivos de projeto que os usuários alteram com seu aplicativo.

> **Observação:** Se você excluir um arquivo, certifique-se de que o Visual FoxPro possa localizar o arquivo excluído quando o aplicativo for executado. Se o Visual FoxPro não encontrar o arquivo excluído, solicita ao usuário que localize o arquivo. Por exemplo, quando um formulário referencia um arquivo de biblioteca de classes visual (.vcx), o formulário armazena um caminho relativo para essa biblioteca. Se você excluir a biblioteca, o formulário deve procurar a biblioteca usando o caminho relativo ou o caminho de pesquisa do Visual FoxPro conforme definido com o comando SET PATH. Se a biblioteca não for encontrada no local esperado, o Visual FoxPro solicita ao usuário que localize a biblioteca. Se a biblioteca estiver incluída no projeto, ela se torna parte do arquivo de aplicativo e o formulário sempre poderá localizar a biblioteca.

### Para excluir arquivos de um projeto
- Abra o projeto do seu aplicativo.
- No Project Manager , selecione o arquivo que pode ser modificado.
- No menu Project, escolha Exclude . Observação Se o arquivo já estiver excluído, o comando Exclude não estará disponível. Em vez disso, o comando Include aparece.

O símbolo Ø aparece ao lado dos nomes dos arquivos excluídos no Project Manager.

> **Dica:** Para visualizar todos os arquivos de projeto em uma única lista, escolha Project Info no menu Project. Na caixa de diálogo Project Information, clique na guia Files.

Para obter mais informações, consulte Project Manager Window e Files Tab, Project Information Dialog Box.
