# Classe base DBF to HTML

Esta classe converte um cursor (.DBF) do Visual FoxPro para HTML. Hooks controlam o escopo, o layout visual e a geração de HTML. Para obter mais informações sobre criação de páginas Web a partir de tabelas do Visual FoxPro, consulte Genhtml.prg.

| Categoria | Internet |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Internet |
| Classe | _dbf2html |
| Classe base | Custom |
| Biblioteca de classes | _internet.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\dohtml.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um construtor para que você possa aceitar os valores atuais ou especificar os valores apropriados de cSource, cOutFile e nGenOutput. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes base.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade cSource | Especifica o arquivo de origem do qual gerar HTML. Padrão: "" |
| propriedade nGenOutput | Opções de saída _GENHTML. 0 = Gerar arquivo de saída. 1 = Gerar e exibir o arquivo de saída no editor do Visual FoxPro. 2 = Gerar e exibir o arquivo de saída no Internet Explorer. 3 = Gerar e exibir o arquivo de saída após exibir uma caixa de diálogo Salvar como. 4 = Criar objeto PUBLIC _oHTML e gerar um arquivo. 5 = Criar um objeto PUBLIC _oHTML sem gerar um arquivo. Padrão: 2 |
| propriedade cOutFile | Especifica o nome do arquivo HTML de saída. Padrão: "" |
| propriedade lAutoNameOutput | Especifica se _GENHTML deve nomear automaticamente o arquivo de saída com base na origem. Padrão: .T. |
| propriedade lUseCurrentAlias | Especifica se deve usar o alias atual como origem. Padrão: .T. |
| propriedade cScope | Especifica o escopo (por exemplo, NEXT ou ALL) para a saída. Padrão: "" |
| propriedade cStyle | Especifica o estilo visual conforme listado no campo ID de Genhtml.dbf. Padrão: "" |
| método GenHTML | Gera código HTML chamando o programa Genhtml.prg usando propriedades especificadas em cSource , cOutput e nGenOutput . Sintaxe: GenHTML( ) Retorno: nenhum Argumentos: nenhum |
