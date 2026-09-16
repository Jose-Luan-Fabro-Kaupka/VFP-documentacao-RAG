# Classe base GDI Plus Pen

A classe gpPen fornece um objeto pen, usado para desenhar linhas e curvas.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpPen |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpObject ( Classe base GDI Plus Object ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpObject. Esta classe também implementa os métodos Clone e Init.

| Propriedades e métodos | Descrição |
| --- | --- |
| Propriedade Alignment | Alinhamento de linhas desenhadas com este pen em curvas fechadas e polígonos, de acordo com o conjunto de constantes GP_PENALIGNMENT_*. |
| Método Clone | Clona um objeto pen. Sintaxe: ? THIS.Clone(toGpPen) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: toGpPen , obrigatório, o objeto baseado em gpPen a clonar. |
| Método Create | Constrói um objeto pen de uma cor especificada. Sintaxe: THIS.Create(tvColor[, tnWidth[, tnUnit]]) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tvColor , obrigatório, um objeto gpColor ou valor numérico representando um valor de cor composto. tnWidth , opcional, largura do pen, padrão 1.0 . tnUnit , opcional, unidade para o valor tnWidth, padrão GDIPLUS_Unit_World . |
| Método CreateFromBrush | Cria um pen a partir de um objeto brush existente. Sintaxe: THIS.CreateFromBrush(toBrush[, tnWidth[, tnUnit]]) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: toBrush , obrigatório, um objeto derivado de gpBrush . tnWidth , opcional, largura do pen, padrão 1.0 . tnUnit , opcional, unidade para o valor tnWidth, padrão GDIPLUS_Unit_World . |
| Propriedade DashCap | Define o estilo de cap no final dos traços, para linhas tracejadas, conforme especificado pelas constantes definidas GDIPLUS_DashCap_*. Padrão: GDIPLUS_DashCap_Flat . |
| Propriedade DashOffset | Define as distâncias do início de uma linha ao início de um padrão de traço. Padrão: 0 |
| Propriedade DashStyle | Define o estilo usado para linhas tracejadas, conforme especificado pelas constantes definidas GDIPLUS_DashStyle_*. Padrão: GDIPLUS_DashStyle_Solid . |
| Propriedade EndCap | Define o estilo de cap no final de linhas desenhadas com este objeto pen, conforme especificado pelas constantes definidas GDIPLUS_LineCap_*. Padrão: GDIPLUS_LineCap_Flat . |
| Método Init | Constrói um objeto pen durante a inicialização se receber argumentos apropriados. Sintaxe: CREATEOBJECT("gpPen" [,tvColor[, tnWidth[, tnUnit]]]) Valores de retorno: Logical, representando sucesso ou falha. Se o método falhar, o objeto não é instanciado. Parâmetros: tvColor , obrigatório se a criação imediata do objeto for solicitada, um objeto gpColor ou valor numérico representando um valor de cor composto. tnWidth , opcional, largura do pen, padrão 1.0 . tnUnit , opcional, unidade para o valor tnWidth, padrão GDIPLUS_Unit_World . |
| Propriedade LineJoin | Define o estilo de junção para as extremidades de duas linhas consecutivas desenhadas com este pen, conforme especificado pelas constantes definidas GDIPLUS_LineJoin_*. Padrão: GDIPLUS_LineJoin_Miter . |
| Propriedade MiterLimit | O limite da espessura da junção em um canto em esquadria (proporção máxima permitida entre o comprimento da esquadria e a largura do traço). Padrão: 10.0 . |
| Propriedade PenColor | Indica a cor deste objeto pen, usando um inteiro para especificar um valor ARGB. Padrão: 0 (preto opaco). |
| Propriedade PenType | Define o tipo de linhas desenhadas com este objeto pen, conforme definido pelas constantes GDIPLUS_PenType_*. Somente leitura. Observações: Esta propriedade se aplica apenas a derivados de gpPen , como os criados a partir de brushes. Apenas pens sólidos ( GDIPLUS_PenType_SolidColor ) podem ser criados com a classe base gpPen Foundation. |
| Propriedade PenUnit | Indica a unidade para medir largura e outros valores, conforme especificado pelas constantes GDIPLUS_UNIT_*. Padrão: GDIPLUS_Unit_World . |
| Propriedade PenWidth | Define a largura do objeto pen. Padrão: 1.0 . |
| Propriedade StartCap | Define o estilo de cap no início de linhas desenhadas com este objeto pen, conforme especificado pelas constantes definidas GDIPLUS_LineCap_*. Padrão: GDIPLUS_LineCap_Flat . |
