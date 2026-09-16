# Como: determinar a página de código de um arquivo de projeto

Depois de adicionar um arquivo a um projeto, você pode determinar sua página de código. O método que você usa depende se o arquivo é uma tabela (arquivo .dbf) ou um arquivo de texto.

### Para determinar a página de código de um arquivo de texto
- Abra a janela Project Manager.
- Em Other, selecione o arquivo de texto cuja página de código você deseja saber.
- No menu Project, escolha Project Info.

### Para determinar a página de código de uma tabela
- Use a função CPDBF( ).

Quando você compila um aplicativo a partir de um projeto, o Project Manager integra automaticamente os arquivos no projeto, independentemente de quantas páginas de código diferentes eles tenham. O aplicativo resultante tem a página de código atual.

> **Observação:** Quando você adiciona um arquivo .dbf a um projeto, não precisa especificar uma página de código para o arquivo porque o Visual FoxPro determina automaticamente a página de código a partir da marca de página de código do arquivo. No entanto, quando você adiciona um arquivo de texto a um projeto, deve especificar uma página de código para o arquivo porque o Visual FoxPro não pode determinar a página de código automaticamente.

Para preparar um programa para uso com outra página de código, especifique a página de código original quando salvar ou compilar o programa na nova plataforma. Por exemplo, para preparar um programa criado com Visual FoxPro for Macintosh para uso com Visual FoxPro, especifique a página de código MS-DOS apropriada quando salvar ou compilar o programa com Visual FoxPro. Se você usar o comando COMPILE, especifique a página de código usando a cláusula AS. Alternativamente, especifique a página de código com o comando SET CPCOMPILE antes de compilar o programa.
