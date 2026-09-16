# Foundation Class GDI Plus Size

A classe gpSize armazena um par ordenado de números, normalmente a largura e a altura de um retângulo.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpSize |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpBase ( Foundation Class GDI Plus Base ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpBase. Esta classe também implementa os métodos Clone e Init.

| Propriedades e métodos | Descrição |
| --- | --- |
| Método Clone | Clona um objeto Size. Sintaxe: ? THIS.Clone(toGpSize) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: toGpSize , obrigatório, o objeto baseado em gpSize a clonar. |
| Método Create | Cria um objeto Size a partir de coordenadas especificadas. Sintaxe: THIS.Create(tW, tH) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tW , obrigatório, a largura do retângulo a criar. tH , obrigatório, a altura do retângulo a criar. |
| Propriedade GdipSize | String representando a estrutura GDI+ Size (composta por dois inteiros de 32 bits). Padrão: Vazio. |
| Propriedade GdipSizeF | String representando a estrutura GDI+ Size (composta por dois valores float de precisão simples de 32 bits). Padrão: Vazio. |
| Propriedade H | Valor de altura para o objeto Size. Padrão: 0 . |
| Método Init | Constrói um objeto Size durante a inicialização se receber argumentos apropriados. Sintaxe: CREATEOBJECT("gpSize" [,tW_Size, tH]) Valores de retorno: Logical, representando sucesso ou falha. Se o método falhar, o objeto não é instanciado. Parâmetros: tW_Size , obrigatório se a criação imediata do objeto for solicitada, representa a largura do objeto Size, ou outro objeto Size a ser clonado. tH , obrigatório se o primeiro parâmetro não foi um objeto Size a ser clonado. |
| Método Set | Define as coordenadas de um objeto Size a partir de componentes individuais. Sintaxe: THIS.Set(tW, tH) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tW , obrigatório, a largura do objeto Size. tH , obrigatório, a altura do objeto Size. |
| Propriedade W | Valor de largura para o objeto Width. Padrão: 0 . |
