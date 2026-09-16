# Classe base GDI Plus Rectangle

A classe gpRectangle encapsula um conjunto de quatro números que representam a localização e o tamanho de um retângulo.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpRectangle |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpBase ( GDI Plus Base Foundation Class ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpBase. Esta classe também implementa os métodos Clone e Init.

| Propriedades e métodos | Descrição |
| --- | --- |
| Clone Method | Clona um objeto retângulo. Sintaxe: ? THIS.Clone(toGpRectangle) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: toGpRectangle , obrigatório, o objeto baseado em gpRectangle a ser clonado. |
| Create Method | Cria um objeto retângulo a partir de coordenadas especificadas. Sintaxe: THIS.Create(tX,tY, tW, tH) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tX , obrigatório, a coordenada X do retângulo a criar. tY , obrigatório, a coordenada Y do retângulo a criar. tW , obrigatório, a largura do retângulo a criar. tH , obrigatório, a altura do retângulo a criar. |
| CreateFromPointSize Method | Cria um retângulo a partir de um objeto gpPoint e um objeto gpSize. Sintaxe: THIS.CreateFromPointSize(toPoint,toSize) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: toPoint , obrigatório, um objeto ponto representando o ponto inicial do retângulo a criar. toSize , obrigatório, um objeto tamanho representando a largura e altura do retângulo a criar. |
| GdipPoint Property | Cadeia de caracteres representando uma estrutura GDI+ Point (composta de dois inteiros de 32 bits), fornecendo o ponto inicial do retângulo. Padrão: Vazio. |
| GdipPointF Property | Cadeia de caracteres representando uma estrutura GDI+ PointF (composta de dois valores float de precisão simples de 32 bits), fornecendo o ponto inicial do retângulo. Padrão: Vazio. |
| GdipRect Property | Cadeia de caracteres representando uma estrutura GDI+ Rect (composta de quatro inteiros de 32 bits), fornecendo o ponto inicial do retângulo. Padrão: Vazio. |
| GdipRectF Property | Cadeia de caracteres representando uma estrutura GDI+ RectF (composta de quatro valores float de precisão simples de 32 bits), fornecendo o ponto inicial do retângulo. Padrão: Vazio. |
| gdiRect Property | Cadeia de caracteres representando a estrutura Win32 "RECT" (como valores X, Y, X2, Y2). Observações: Esta propriedade é útil ao trabalhar com funções GDI do Windows, que esperam retângulos definidos como as coordenadas de dois cantos diagonalmente opostos, em vez de valores de topo, esquerda, largura e altura. Padrão: Vazio. |
| gpPoint Property | Ponto inicial ou de origem do retângulo representado como um objeto gpPoint. Padrão: Vazio. |
| gpSize Property | Largura e altura do retângulo como um objeto gpSize. Padrão: Vazio. |
| H Property | Altura do retângulo. Padrão: 0 . |
| Init Method | Constrói um objeto retângulo durante a inicialização se passados argumentos apropriados. Sintaxe: CREATEOBJECT("gpRectangle" [,tX_Rect_Point,tY_Size, tW, tH]) Valores de retorno: Logical, representando sucesso ou falha. Se o método falhar, o objeto não é instanciado. Parâmetros: tX_Rect_Point , obrigatório se a criação imediata do objeto for solicitada, representa a coordenada X do ponto inicial do retângulo, um objeto existente baseado em gpRectangle a ser clonado, ou um ponto superior esquerdo do retângulo. tY_Size , obrigatório se a criação imediata do objeto for solicitada e tX_Rect_Point não é um objeto do tipo gpRectangle, representa a coordenada Y do ponto inicial do retângulo, se tX_Rect_Point era a coordenada X do ponto, ou um objeto do tipo gpSize , se tX_Rec_Point era um objeto do tipo gpPoint . tW , obrigatório se os dois primeiros parâmetros eram coordenadas, representa a largura do retângulo a criar. tH , obrigatório se os dois primeiros parâmetros eram coordenadas, representa a altura do retângulo a criar. |
| Set Method | Define as coordenadas de um retângulo a partir de componentes individuais. Sintaxe: THIS.Set(tX, tY, tW, tH) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tX , obrigatório, a coordenada X do ponto inicial do retângulo a ser definido. tY , obrigatório, a coordenada Y do ponto inicial do retângulo a ser definido. tW , obrigatório, a largura do retângulo a ser definido. tH , obrigatório, a altura do retângulo a ser definido. |
| W Property | Largura do retângulo. Padrão: 0 . |
| X Property | Coordenada X do ponto inicial (superior esquerdo) do retângulo. Padrão: 0 . |
| X2 Property | Coordenada X do ponto final (inferior direito) do retângulo. Padrão: 0 . |
| Y Property | Coordenada Y do ponto inicial (superior esquerdo) do retângulo. Padrão: 0 . |
| Y2 Property | Coordenada Y do ponto final (inferior direito) do retângulo. Padrão: 0 . |
