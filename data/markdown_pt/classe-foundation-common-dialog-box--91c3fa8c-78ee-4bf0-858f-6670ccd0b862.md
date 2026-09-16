# Classe Foundation Common Dialog Box

Você pode usar caixas de diálogo de sistema Abrir e Salvar arquivo que imitam as mais recentes do Windows em seus aplicativos. Por exemplo, você pode ter uma Places bar no lado esquerdo da caixa de diálogo.

| Categoria | Caixas de diálogo do sistema |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Dialogs |
| Classe | _comdlg |
| Classe base | Custom |
| Biblioteca de classes | _system.vcx |
| Classe pai | _custom |
| Amostra | ...\Samples\Solution\Ffc\Getfilex.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Item da Galeria de Componentes, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para mais informações sobre o uso de classes foundation.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| matriz aFileNames | Matriz de nomes de arquivo retornados da caixa de diálogo. Padrão: .F. |
| matriz aFileList | Matriz de filtros de extensão de arquivo passados para a caixa de diálogo. Padrão: .F. |
| propriedade cCustomFilter | Filtro personalizado que o usuário criou ao usar a caixa de diálogo. Padrão: nenhum |
| propriedade cDefaultExtension | Extensão de arquivo padrão a exibir. Padrão: nenhum |
| propriedade cFileName | Nome do arquivo selecionado ou inicialmente definido como padrão. Padrão: nenhum |
| propriedade cFilePath | Caminho do qual os arquivos foram selecionados. Padrão: nenhum |
| propriedade cFileTitle | Propriedade de título do arquivo do(s) arquivo(s) selecionado(s). Padrão: nenhum |
| propriedade cInitialDirectory | Diretório inicial do qual exibir arquivos. Padrão: nenhum |
| propriedade cTitleBar | Caption para a barra de título da caixa de diálogo. Padrão: nenhum |
| propriedade lAllowMultiSelect | Especifica se permite vários arquivos. Padrão: .F. |
| propriedade lFileMustExist | Especifica se permite apenas arquivos existentes a serem inseridos. Padrão: .F. |
| propriedade lHideReadOnly | Especifica se oculta arquivos somente leitura da lista. Padrão: .T. |
| propriedade lNewExplorer | Especifica se usa a nova interface de usuário do explorer e recursos como Places bar. Padrão: .T. |
| propriedade lNoChangeDir | Especifica se impede a alteração do diretório exibido. Padrão: .F. |
| propriedade lNoNetworkButton | Especifica se impede a inclusão de um botão de rede na caixa de diálogo. Padrão: .F. |
| propriedade lNoPlacesBar | Especifica se impede uma Places bar na caixa de diálogo. Padrão: .F. |
| propriedade lNoValidate | Especifica que os arquivos não são validados na caixa de diálogo. Padrão: .F. |
| propriedade lSaveDialog box | Especifica se usa a caixa de diálogo Salvar em vez da Abrir. Padrão: .F. |
| propriedade nFileCount | Especifica o número de arquivos selecionados na caixa de diálogo. Padrão: 0 |
| propriedade nFilterIndex | Especifica qual dos filtros foi selecionado na caixa de diálogo. Padrão: 0 |
| método AddFilter | Especifica os filtros de extensão de arquivo a usar ao exibir a caixa de diálogo. Sintaxe: AddFilter(cDescription, cSkeleton) Retorno: nenhum Argumentos: cDescription fornece uma descrição do filtro. cSkeleton especifica o esqueleto do filtro de extensão de arquivo. |
| método ClearFilters | Limpa todos os filtros de extensão de arquivo. Sintaxe: ClearFilters( ) Retorno: nenhum Argumentos: cUser especifica o nome do usuário a verificar |
| método ShowDialog box | Exibe a caixa de diálogo com várias opções, como filtros. Sintaxe: ShowDialog box( ) Retorno: nenhum Argumentos: nenhum |
| método TestDialog box | Script de teste para exibir uma caixa de diálogo. Sintaxe: TestDialog box( ) Retorno: nenhum Argumentos: nenhum |
