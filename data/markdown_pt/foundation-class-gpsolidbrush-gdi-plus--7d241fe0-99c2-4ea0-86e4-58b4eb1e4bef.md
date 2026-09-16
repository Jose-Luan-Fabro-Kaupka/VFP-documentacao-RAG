# Foundation Class gpSolidBrush GDI Plus

A classe gpSolidBrush fornece um objeto brush que preenche com uma cor sólida.

| Categoria | Relatórios |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpSolidBrush |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpBrush ( Foundation Class GDI Plus Brush ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpBrush. Esta classe também implementa o método Init.

| Propriedades e métodos | Descrição |
| --- | --- |
| Propriedade BrushColor | Especifica a cor de um objeto SolidBrush como um inteiro representando um valor ARGB. Padrão: Nenhum. |
| Método Create | Cria um objeto SolidBrush em uma cor especificada. Sintaxe: THIS.Create(tvColor) Valores de retorno: Logical, representando êxito ou falha. Parâmetros: tvColor, obrigatório, um objeto baseado em gpColor ou um número representando um valor de cor composto. |
| Método Init | Constrói um objeto SolidBrush durante a inicialização se receber argumentos apropriados. Sintaxe: CREATEOBJECT("gpSolidBrush" [, tvColor]) Valores de retorno: Logical, representando êxito ou falha. Se o método falhar, o objeto não é instanciado. Parâmetros: tvColor, obrigatório se a criação imediata do objeto for solicitada, um objeto baseado em gpColor ou um número representando um valor de cor composto. |
