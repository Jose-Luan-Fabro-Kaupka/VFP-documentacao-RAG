# Classe base de fonte GDI Plus

A classe gpFont define um formato específico para texto, incluindo atributos de tipo, tamanho e estilo da fonte.

| Categoria | Relatórios |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpFont |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpObject (Classe base de objeto GDI Plus) |

# Observações

A tabela a seguir lista as propriedades e os métodos públicos adicionados por essa classe à sua classe pai, gpObject. Ela também implementa os métodos Clone e Init.

Os valores listados como altura em na tabela equivalem à ascensão da célula (altura da fonte acima da linha) + descida da célula (altura da fonte abaixo da linha) - entrelinha interna da fonte. Os valores listados como espaçamento de linha equivalem à ascensão da célula + descida da célula + entrelinha externa.

| Propriedades e métodos | Descrição |
| --- | --- |
| Método Clone | Clona um objeto de fonte. Sintaxe: ? THIS.Clone(toFont) Valores de retorno: lógico, representando sucesso ou falha. Parâmetros: toFont, obrigatório, o objeto gpFont a clonar. |
| Método Create | Cria um objeto de fonte a partir de um conjunto especificado de atributos de fonte. Sintaxe: ? THIS.Create(tvFontNameOrFamily, [tnSize [, tnStyle[, tnUnits]]]) Valores de retorno: lógico, representando sucesso ou falha. Parâmetros: tvFontNameOrFamily, obrigatório, um objeto gpFontFamily ou uma cadeia de caracteres que representa o nome de uma fonte. tnSize, obrigatório, tamanho nas unidades especificadas. tnStyle, opcional, atributos de estilo de fonte conforme especificado nas constantes GDIPLUS_FontStyle_*. O valor padrão é GDIPLUS_FontStyle_Regular. tnUnits, opcional, unidades do tamanho da fonte conforme especificado nas constantes GDIPLUS_Unit_*. O valor padrão é GDIPLUS_Unit_Point. |
| Propriedade FontName | Nome da fonte, por exemplo, "Arial". Padrão: vazio. |
| Método GetHeight | Obtém o espaçamento de linha de uma fonte para determinado objeto gráfico, usando as unidades desse objeto gráfico. Sintaxe: nHeight = THIS.GetHeight(tvGraphics) Valores de retorno: número, altura da linha. Retorna nulo (.NULL.) em caso de erro. Parâmetros: tvGraphics, obrigatório, um objeto gpGraphics ou um identificador gráfico GDI+. |
| Método GetHeightGivenDPI | Obtém o espaçamento de linha de uma fonte dado um valor em pontos por polegada (DPI). Sintaxe: nHeight = THIS.GetHeightGivenDPI(tnDPI) Valores de retorno: número, altura da linha. Retorna nulo (.NULL.) em caso de erro. Parâmetros: tnDPI, obrigatório, um número de pontos por polegada. |
| Método Init | Constrói um objeto de fonte durante a inicialização se os argumentos apropriados forem fornecidos. Sintaxe: CREATEOBJECT("gpFont", tvFontNameOrFamily, [tnSize [, tnStyle[, tnUnits]]]) Valores de retorno: lógico, representando sucesso ou falha. Se o método falhar, o objeto não será instanciado. Parâmetros: tvFontNameOrFamily, obrigatório se a criação imediata do objeto for solicitada. Um objeto gpFontFamily ou uma cadeia de caracteres que representa o nome de uma fonte. tnSize, obrigatório, tamanho nas unidades especificadas. tnStyle, opcional, atributos de estilo de fonte conforme especificado nas constantes GDIPLUS_FontStyle_*. O valor padrão é GDIPLUS_FontStyle_Regular. tnUnits, opcional, unidades do tamanho da fonte conforme especificado nas constantes GDIPLUS_Unit_*. O valor padrão é GDIPLUS_Unit_Point. |
| Propriedade Size | O tamanho em da fonte usando as unidades deste objeto de fonte. Padrão: vazio. |
| Propriedade Style | Informações de estilo deste objeto de fonte, usando valores de constantes GDIPLUS_FontStyle_*. Padrão: vazio. |
| Propriedade Unit | A unidade de medida usada por esta fonte, usando valores de constantes GDIPLUS_Unit_*. Padrão: vazio. |
