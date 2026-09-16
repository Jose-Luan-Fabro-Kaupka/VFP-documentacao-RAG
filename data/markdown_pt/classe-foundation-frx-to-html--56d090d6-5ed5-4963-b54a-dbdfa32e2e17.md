# Classe Foundation FRX to HTML

Esta classe converte um relatório Visual FoxPro (.FRX) para HTML.

| Categoria | Internet |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Internet |
| Classe | _frx2html |
| Classe base | Custom |
| Biblioteca de classes | _internet.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\dohtml.scx |

# Observações

A classe inclui propriedades para controlar o escopo e a geração de HTML. Para obter mais informações, consulte Genhtml.prg.

> **Observação:** No Visual FoxPro 9, o processamento FRX do Genhtml.prg usa a classe ReportListener que você registrou com o Report Output Application atual para fornecer saída HTML. Para obter mais informações, consulte ReportListener Foundation Classes .

Para usar esta classe, arraste a classe para um projeto ou formulário. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar os valores das propriedades cSource, cOutFile, nGenOutput e lAutonameOutput. Quando você solta a classe em um projeto, pode escolher adicionar a classe ou criar uma subclasse.

| Propriedades, eventos e métodos | Descrição |
| --- | --- |
| Propriedade cOutFile | Especifica o nome do arquivo HTML a ser criado. Padrão: "" |
| Propriedade cSource | Especifica o arquivo de origem do qual gerar HTML. Padrão: "" |
| Propriedade nGenOutput | Opções de saída _GENHTML: 1 = Gerar e exibir o arquivo de saída no editor do Visual FoxPro. Padrão: 20 = Gerar arquivo de saída. |
| Propriedade lAutoNameOutput | Especifica se _GENHTML deve nomear automaticamente o arquivo de saída com base na origem. Padrão: .T. |
| Propriedade cScope | Especifica o escopo (por exemplo, NEXT ou ALL) para a saída. Padrão: "" |
| Método GenHTML | Gera código HTML chamando o programa Genhtml.prg usando propriedades especificadas em cSource, cOutput e nGenOutFile. Sintaxe : GenHTML( ) Retorno : nenhum Argumentos : nenhum |
