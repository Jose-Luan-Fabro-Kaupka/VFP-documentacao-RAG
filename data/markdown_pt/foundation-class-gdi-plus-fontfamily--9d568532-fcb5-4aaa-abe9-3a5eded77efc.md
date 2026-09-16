# Foundation Class GDI Plus FontFamily

A classe gpFontFamily designa atributos compartilhados por um grupo de fontes relacionadas.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpFontFamily |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpObject ( Foundation Class GDI Plus Object ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpObject. Ela também implementa os métodos Clone e Init.

Valores listados como em height na tabela são equivalentes a cell ascent (altura da fonte acima da linha) + cell descent (altura da fonte abaixo da linha) - internal leading da fonte. Valores listados como line spacing são iguais a cell ascent + cell descent + external leading.

| Propriedades e métodos | Descrição |
| --- | --- |
| Método Clone | Clona um objeto de família de fontes. Sintaxe: ? THIS.Clone(toFontFamily) Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: toFontFamily , obrigatório, o objeto gpFontFamily a clonar. |
| Método Create | Cria um objeto de família de fontes a partir de um nome especificado. Sintaxe: ? THIS.Create(tcName) Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: tcName , obrigatório, o nome da família de fontes. |
| Propriedade FontName | Nome da família de fontes, como "Arial." Padrão: Vazio. |
| Propriedade gdipFontCollectionHandle | Handle para o objeto GDI+ FontCollection. Padrão: 0 . Observações: Esta classe não gerencia este handle de forma alguma, apenas o usa. |
| Método GetCellAscent | Fornece cell ascent em unidades de design desta família de fontes no estilo especificado. Sintaxe: nAscent =THIS.GetCellAscent([tnStyle]) Valores de retorno: Número. Retorna null ( .NULL. ) em caso de falha. Parâmetros: tnStyle , opcional, estilo de fonte conforme especificado nas constantes GDIPLUS_FontStyle_*. Valor padrão é GDIPLUS_FontStyle_Regular . |
| Método GetCellDescent | Fornece cell descent em unidades de design desta família de fontes no estilo especificado. Sintaxe: nDescent =THIS.GetCellDescent([tnStyle]) Valores de retorno: Número. Retorna null ( .NULL. ) em caso de falha. Parâmetros: tnStyle , opcional, estilo de fonte conforme especificado nas constantes GDIPLUS_FontStyle_*. Valor padrão é GDIPLUS_FontStyle_Regular . |
| Método GetEmHeight | Fornece em height em unidades de design desta família de fontes no estilo especificado. Sintaxe: nHeight =THIS.GetEmHeight([tnStyle]) Valores de retorno: Número. Retorna null ( .NULL. ) em caso de falha. Parâmetros: tnStyle , opcional, estilo de fonte conforme especificado nas constantes GDIPLUS_FontStyle_*. Valor padrão é GDIPLUS_FontStyle_Regular . |
| Método GetGenericMonospace | Fornece um objeto de família de fontes monospace genérico. Sintaxe: THIS.GetGenericMonospace() Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: Nenhum. Observações: Após retorno bem-sucedido deste método, o objeto representa uma família de fontes padrão do sistema, e todas as propriedades tornam-se somente leitura. |
| Método GetGenericSansSerif | Fornece um objeto de família de fontes sans serif genérico. Sintaxe: THIS.GetGenericSansSerif() Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: Nenhum. Observações: Após retorno bem-sucedido deste método, o objeto representa uma família de fontes padrão do sistema, e todas as propriedades tornam-se somente leitura. |
| Método GetGenericSerif | Fornece um objeto de família de fontes serif genérico. Sintaxe: THIS.GetGenericSerif() Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: Nenhum. Observações: Após retorno bem-sucedido deste método, o objeto representa uma família de fontes padrão do sistema, e todas as propriedades tornam-se somente leitura. |
| Método GetLineSpacing | Fornece line spacing em unidades de design desta família de fontes no estilo especificado. Sintaxe: nHeight =THIS.GetEmHeight([tnStyle]) Valores de retorno: Número. Retorna null ( .NULL. ) em caso de falha. Parâmetros: tnStyle , opcional, estilo de fonte conforme especificado nas constantes GDIPLUS_FontStyle_*. Valor padrão é GDIPLUS_FontStyle_Regular . |
| Método GetName | Fornece o nome desta família de fontes no idioma especificado. Sintaxe: cName =THIS.GetName([tnLanguageID]) Valores de retorno: Cadeia de caracteres. Retorna null ( .NULL. ) em caso de falha. Parâmetros: tnLanguage , opcional, identificador de idioma. Valor padrão é 0 . |
| Método Init | Constrói um objeto de família de fontes durante a inicialização se argumentos apropriados forem passados. Sintaxe: CREATEOBJECT("gpFontFamily", tcFontFamilyName) Valores de retorno: Lógico, representando sucesso ou falha. Se o método falhar, o objeto não é instanciado. Parâmetros: tcFontFamilyName , obrigatório se a criação imediata do objeto for solicitada. Uma cadeia de caracteres representando o nome de uma família de fontes. |
| Método IsStyleAvailable | Testa se um estilo de fonte solicitado pode ser fornecido nativamente nesta família de fontes. Sintaxe: ? THIS.IsStyleAvailable(tnStyle) Valores de retorno: Lógico. Parâmetros: tnStyle , obrigatório, estilo de fonte conforme especificado nas constantes GDIPLUS_FontStyle_*. Valor padrão é GDIPLUS_FontStyle_Regular . Observações: Embora tecnicamente correto, um valor de retorno False ( .F. ) desta função pode ser enganoso. O Windows geralmente pode sintetizar estilos de fonte quando o estilo específico para uma fonte não está disponível. |
