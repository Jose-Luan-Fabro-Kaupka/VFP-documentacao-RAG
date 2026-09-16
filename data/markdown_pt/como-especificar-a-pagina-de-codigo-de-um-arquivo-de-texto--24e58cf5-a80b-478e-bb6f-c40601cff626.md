# Como: especificar a página de código de um arquivo de texto

Se você esquecer a página de código de um arquivo de texto que não faz parte de um projeto, não será possível determinar a página de código, porque um arquivo de texto não possui uma marca de página de código como os arquivos .dbf possuem. A melhor maneira de lembrar a página de código de um arquivo de texto é adicionar o arquivo a um projeto.

### Para especificar a página de código de um arquivo de texto
- Abra a janela Project Manager .
- Selecione o arquivo de texto cuja página de código você deseja especificar.
- No menu Project, escolha Project Info .
- Na caixa de diálogo Project Information , clique na guia Files.
- Clique com o botão direito no arquivo selecionado.
- No submenu, escolha Code Page . O Visual FoxPro exibe a caixa de diálogo Code Page .
- Escolha a página de código apropriada. O Visual FoxPro exibe as páginas de código disponíveis.

Se você conhece a página de código de um arquivo de texto, pode especificá-la usando a cláusula AS do comando Visual FoxPro apropriado. Para arquivos que você deseja importar ou anexar, pode especificar a página de código no comando IMPORT ou no comando APPEND. Para arquivos de consulta, programa e outros arquivos de texto já no seu computador, pode alterar a página de código usando o comando MODIFY QUERY, o comando MODIFY COMMAND e o comando MODIFY FILE.

Se não tiver certeza de qual página de código aplicar, substitua o número da página de código no comando pela função GETCP( ). GETCP( ) exibe a caixa de diálogo Code Page, permitindo que você selecione a página de código apropriada.

> **Observação:** Alguns caracteres não podem ser traduzidos entre páginas de código com sucesso. Além disso, o Visual FoxPro não suporta algumas traduções de página de código. Sempre verifique os resultados de uma alteração de página de código para garantir que seus dados foram traduzidos com sucesso.
