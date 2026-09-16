# Classe base GDI Plus Object Foundation

A classe gpObject é a classe base abstrata para todos os objetos GDI+. Ela fornece gerenciamento de identificadores GDI+ e o resultado das operações GDI+.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpObject |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpBase ( GDI Plus Base Foundation Class ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpBase.

| Propriedades e métodos | Descrição |
| --- | --- |
| Método GetHandle | Retorna o identificador GDI+ subjacente para este objeto. Sintaxe: ? THIS.GetHandle() Valores de retorno: Valor inteiro representando o identificador. Retorna null ( .NULL. ) se ocorrer um erro. Parâmetros: Nenhum. |
| Método GetStatus | Retorna o código de status da última função GDI+ chamada neste objeto. Consulte as constantes definidas GP_STATUS_*. Sintaxe: ? THIS.GetStatus() Valores de retorno: Valor inteiro representando o código de status. Parâmetros: Nenhum. |
| Método SetHandle | Define o identificador GDI+ nativo se ele foi obtido de uma fonte externa. Sintaxe: ? THIS.SetHandle(tvNewHandle,tlOwnsHandle) Valores de retorno: : Valor lógico, representando sucesso ou falha. Parâmetros: tvHandle , obrigatório, o identificador a ser atribuído. tlOwnsHandle , opcional, padrão false ( .F. ) . Indica se este objeto possui o identificador e pode excluí-lo quando este objeto realizar outras limpezas. |
| Propriedade Win32LastError | Retorna o último código de erro do Windows se GetStatus retornar GP_STATUS_Win32Error . Padrão: 0 . |
