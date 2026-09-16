# Foundation Class SCX to HTML

Esta classe converte um formulário Visual FoxPro (.scx) em HTML. Esta classe fornece propriedades para controlar o escopo, o layout visual e a geração de HTML. Para obter mais informações, consulte Genhtml.prg.

| Categoria | Internet |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Internet |
| Classe | _scx2html |
| Classe base | Custom |
| Biblioteca de classes | _internet.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\dohtml.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Ao adicionar a classe a um formulário, o Visual FoxPro abre um builder para que você possa aceitar os valores atuais ou especificar os valores apropriados de cSource, cOutFile e nGenOutput. Ao soltar a classe em um projeto, você pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar Foundation Classes do Visual FoxPro para obter mais informações sobre o uso de foundation classes.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cOutfile | Especifica o nome do arquivo HTML a gerar. Padrão: "" |
| Propriedade cScope | Especifica o escopo (por exemplo, NEXT ou ALL, para a saída). Padrão: "" |
| Propriedade cSource | Especifica o arquivo .scx de origem do qual gerar o arquivo HTML. Padrão: "" |
| Propriedade cStyle | Especifica o estilo visual conforme listado no campo ID de Genhtml.dbf. Padrão: "" |
| Propriedade lAutonameoutput | Especifica se _GENHTML nomeia automaticamente o arquivo de saída com base em sua origem. Padrão: .T. |
| Propriedade nGenOutput | Especifica a opção de saída _GENHTML: 0 = Gerar um arquivo de saída.1 = Gerar e exibir um arquivo de saída no editor do Visual FoxPro.2 = Gerar e exibir um arquivo de saída no Internet Explorer.3 = Gerar e exibir um arquivo de saída após exibir uma caixa de diálogo SaveAs.4 = Criar um objeto PUBLIC _oHTML e gerar um arquivo.5 = Criar um objeto PUBLIC _oHTML sem gerar um arquivo. Padrão: 2 |
| Método GenHTML | Gera código HTML chamando o mecanismo _GENHTML usando propriedades especificadas em cSource , cOutFile e nGenOutput . Sintaxe: GenHTML( ) Retorno: nenhum Argumentos: nenhum |
