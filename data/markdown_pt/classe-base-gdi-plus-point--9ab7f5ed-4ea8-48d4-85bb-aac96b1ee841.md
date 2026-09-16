# Classe base GDI Plus Point

A classe gpPoint encapsula um par ordenado de coordenadas x e y que define um ponto em um plano bidimensional.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpPoint |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpBase ( Classe base GDI Plus Base ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpBase. Esta classe também implementa os métodos Clone e Init.

| Propriedades e métodos | Descrição |
| --- | --- |
| Método Clone | Clona um objeto de ponto. Sintaxe: ? THIS.Clone(toGpPoint) Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: toGpPoint , obrigatório, o objeto baseado em gpPoint a clonar. |
| Método Create | Cria um objeto de ponto a partir de coordenadas especificadas. Sintaxe: THIS.Create(tX,tY) Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: tX , obrigatório, a coordenada X do ponto a criar. tY , obrigatório, a coordenada Y do ponto a criar. |
| Propriedade GdipPoint | Cadeia de caracteres representando a estrutura GDI+ Point (composta por dois inteiros de 32 bits). Padrão: Vazio. |
| Propriedade GdipPointF | Cadeia de caracteres representando a estrutura GDI+ PointF (composta por dois valores float de precisão simples de 32 bits). Padrão: Vazio. |
| Método Init | Constrói um objeto Point durante a inicialização se passados argumentos apropriados. Sintaxe: CREATEOBJECT("gpPoint" [,tX,tY]) Valores de retorno: Lógico, representando sucesso ou falha. Se o método falhar, o objeto não é instanciado. Parâmetros: tX , obrigatório se a criação imediata do objeto for solicitada, representa a coordenada X do ponto. tY , obrigatório se a criação imediata do objeto for solicitada, representa a coordenada Y do ponto. |
| Método Set | Define um objeto de ponto a partir de coordenadas especificadas. Sintaxe: THIS.Set(tX,tY) Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: tX , obrigatório, a coordenada X do ponto a definir. tY , obrigatório, a coordenada Y do ponto a definir. |
| Propriedade X | A coordenada X do ponto. Padrão: 0 . |
| Propriedade Y | A coordenada Y do ponto. Padrão: 0 . |
