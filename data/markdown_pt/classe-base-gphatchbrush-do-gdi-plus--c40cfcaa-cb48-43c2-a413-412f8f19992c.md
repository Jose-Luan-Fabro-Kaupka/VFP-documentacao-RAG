# Classe base gpHatchBrush do GDI Plus

A classe gpHatchBrush fornece um objeto brush que preenche com um padrão de hachura.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpHatchBrush |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpBrush ( GDI Plus Brush Foundation Class ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpBrush. Esta classe também implementa o método Init.

| Propriedades e métodos | Descrição |
| --- | --- |
| BackgroundColor Property | Especifica a cor do espaço entre as linhas de hachura, como um inteiro que define um valor ARGB. Padrão: Empty. |
| Create Method | Cria um objeto hatchbrush. Sintaxe: ? THIS.Create(tnStyle[, tvForeColor[, tvBackColor]]) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tnStyle , obrigatório, o padrão ou estilo de hachura a ser usado. Use uma constante conforme especificado no conjunto de constantes GDIPLUS_HatchStyle_*. tvForeColor , opcional, um inteiro ou objeto gpColor representando um valor de cor para a cor de primeiro plano do brush (linhas de hachura). tvBackColor , opcional, um inteiro ou objeto gpColor representando um valor de cor para a cor de fundo do brush (espaço entre as linhas de hachura). |
| ForegroundColor Property | Especifica a cor das linhas de hachura, como um inteiro que define um valor ARGB. Padrão: Empty. |
| HatchStyle Property | Especifica o estilo de hachura ou padrão. Use uma constante conforme especificado no conjunto de constantes GDIPLUS_HatchStyle_*. Padrão: 0 (GDIPLUS_HatchStyle_Horizontal) . |
| Init Method | Constrói um objeto hatchbrush durante a inicialização se forem passados argumentos apropriados. Sintaxe: CREATEOBJECT("gpHatchBrush"[,tnStyle[, tvForeColor[, tvBackColor]]]) Valores de retorno: Logical, representando sucesso ou falha. Se o método falhar, o objeto não é instanciado. Parâmetros: tnStyle , obrigatório se a criação imediata do objeto for solicitada, representando o padrão ou estilo de hachura a ser usado. Use uma constante conforme especificado no conjunto de constantes GDIPLUS_HatchStyle_*. tvForeColor , opcional, um inteiro ou objeto gpColor representando um valor de cor para a cor de primeiro plano do brush (linhas de hachura). tvBackColor , opcional, um inteiro ou objeto gpColor representando um valor de cor para a cor de fundo do brush (espaço entre as linhas de hachura). |
