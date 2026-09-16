# Classe básica GDI Plus StringFormat

A classe gpStringFormat fornece um objeto que encapsula informações de layout de texto (como alinhamento e espaçamento entre linhas) e manipulações de exibição (como inserção de reticências e substituição de dígitos nacionais).

| Categoria | Relatórios |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpStringFormat |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpObject ( Classe básica GDI Plus Object ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpObject. Esta classe também implementa os métodos Clone e Init .

| Propriedades e métodos | Descrição |
| --- | --- |
| Propriedade Alignment | Alinhamento horizontal do texto especificado usando valores indicados pelas constantes GDIPLUS_STRINGALIGNMENT_* . Padrão: GDIPLUS_STRINGALIGNMENT_Near . Observações : Em um ambiente de ordem de leitura da esquerda para a direita, GDIPLUS_STRINGALIGNMENT_Near é equivalente a "alinhamento à esquerda" e GDIPLUS_STRINGALIGNMENT_Far é equivalente a "alinhamento à direita". |
| Método Clone | Clona um objeto StringFormat. Sintaxe: ? THIS.Clone(toGpStringFormat) Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: toGpStringFormat , obrigatório, o objeto baseado em gpStringFormat a clonar. |
| Método Create | Cria um objeto StringFormat com sinalizadores e informações de idioma opcionais. Sintaxe: THIS.Create([tnFlags[, tnLangID]]) Valores de retorno: Lógico, representando sucesso ou falha. Parâmetros: tnFlags , opcional, valor inicial para a propriedade FormatFlags . tnLangID , opcional, um identificador de idioma inteiro. |
| Propriedade FormatFlags | Sinalizadores de formatação de cadeia de caracteres especificados usando uma combinação de valores de bit, usando valores definidos pelas constantes GDIPLUS_STRINGFORMATFLAGS_* . Padrão: Vazio. |
| Método GetGenericDefault | Constrói um objeto StringFormat equivalente ao System.Drawing.StringFormat.GenericDefault do .NET. Sintaxe: THIS.GetGenericDefault(tlMakeClone) Valores de retorno: Lógico, representando sucesso ou falha. Observações: Após o retorno bem-sucedido deste método, o objeto representa um formato de cadeia de caracteres padrão do sistema e todas as propriedades tornam-se somente leitura. |
| Método GetGenericTypographic | Constrói um objeto StringFormat com propriedades Generic Typographic definidas como seriam pelo System.Drawing.StringFormat.GenericTypographic do .NET. Sintaxe: THIS.GetGenericTypographic(tlMakeClone) Valores de retorno: Lógico, representando sucesso ou falha. Observações: Após o retorno bem-sucedido deste método, o objeto representa um formato de cadeia de caracteres padrão do sistema e todas as propriedades tornam-se somente leitura. |
| Propriedade HotkeyPrefix | Configuração HotkeyPrefix com valores indicados pelas constantes GDIPLUS_HOTKEYPREFIX_* . |
| Método Init | Constrói um objeto StringFormat durante a inicialização se receber argumentos apropriados. Sintaxe: CREATEOBJECT("gpStringFormat" [, tnFlags[, tnLangID]]) Valores de retorno: Lógico, representando sucesso ou falha. Se o método falhar, o objeto não é instanciado. Parâmetros: tnFlags , opcional, valor inicial para a propriedade FormatFlags . tnLangID , opcional, um identificador de idioma inteiro. |
| Propriedade LineAlignment | Alinhamento vertical da linha de texto especificado usando valores indicados pelas constantes GDIPLUS_STRINGALIGNMENT_* . Padrão: GDIPLUS_STRINGALIGNMENT_Near . Observações : Em um ambiente de ordem de leitura de cima para baixo, GDIPLUS_STRINGALIGNMENT_Near é equivalente a "alinhamento superior" e GDIPLUS_STRINGALIGNMENT_Far é equivalente a "alinhamento inferior". |
| Propriedade Trimming | Sinalizadores que especificam como o texto é cortado quando transborda o retângulo de layout, usando valores indicados pelas constantes GDIPLUS_STRINGTRIMMING_* . Padrão: GDIPLUS_STRINGTRIMMING_None . |
