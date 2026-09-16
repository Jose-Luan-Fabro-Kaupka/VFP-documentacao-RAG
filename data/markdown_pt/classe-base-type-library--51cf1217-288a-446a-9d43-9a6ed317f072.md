# Classe base Type Library

Esta classe usa o componente COM TlbInf32 para ler informações de tipo de bibliotecas de tipos. A rotina principal ExportTypeLib cria um arquivo de texto com saída da biblioteca de tipos.

| Categoria | Utilitários de arquivo |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _typelib |
| Classe base | Container |
| Biblioteca de classes | _utility.vcx |
| Classe pai | _container |
| Exemplo | ...\Samples\Solution\Winapi\typelib.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode então especificar os valores de propriedade apropriados no formulário no Form Designer.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes base.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade aTypeAttr[1,0] | Especifica a matriz para a estrutura TypeAttr. Padrão: .F. |
| propriedade aTypeFuncDesc[1,0] | Especifica uma matriz para a estrutura FuncDesc. Padrão: .F. |
| propriedade aTypeFuncDocs[3,0] | Especifica uma matriz para documentação de função. Padrão: .F. |
| propriedade aTypeFuncNames[1,0] | Especifica uma matriz de nomes de função. Padrão: .F. |
| propriedade aTypeFuncParms[1,0] | Especifica uma matriz dos parâmetros de função. Padrão: .F. |
| propriedade aTypeInfoDocs[3,0] | Especifica uma matriz para documentação TypeInfo. Padrão: .F. |
| propriedade aTypeLibDocs[3,0] | Especifica uma matriz para documentação TypeLib. Padrão: .F. |
| propriedade FuncNamesCount | Especifica o número de nomes para função TypeInfo. Isso é equivalente a total de parâmetros+1. Padrão: .F. |
| propriedade TypeInfoCount | Especifica o número de TypeInfos em TypeLib. Padrão: .F. |
| propriedade TypeInfoIndex | Uma referência de índice para TypeInfo. Padrão: .F. |
| propriedade TypeLibHandle | O identificador para TypeLib. Padrão: .F. |
| propriedade TypeLibName | Especifica o nome da biblioteca de tipos. Padrão: .F. |
| método ExportTypeLib | Exporta o conteúdo de um TypeLib para um arquivo de texto. Sintaxe: ExportTypeLib(cExportFile, lViewFile) Retorno: m.exportfile Argumentos: cExportFile especifica o arquivo a exportar. lViewFile especifica se deve abrir o arquivo em um visualizador após a exportação. |
| método GetDataType | Retorna o tipo de dados da função. Sintaxe: GetDataType(m.nvt) Retorno: nome do tipo de dados Argumentos: m.nvt especifica uma referência de item de dados. |
| método GetFuncDesc | Obtém informações de função TypeInfo e preenche matrizes. Sintaxe: GetFuncDesc(nFuncIndex) Retorno: matrizes TypeInfo, aTypeFuncParms, aTypeFuncNames, aTypeFuncDocs Argumentos: nFuncIndex especifica o índice da função. |
| método GetTypeInfo | Obtém TypeInfo e preenche matrizes TypeInfo. Sintaxe: GetTypeInfo(nTypeInfoNum) Retorno: nenhum Argumentos: nTypeInfoNum especifica uma referência à chave Typeinfo. |
| método GetTypeLib | Obtém informações TypeLib e preenche matrizes. Sintaxe: GetTypeLib( ) Retorno: nenhum Argumentos: nenhum |
