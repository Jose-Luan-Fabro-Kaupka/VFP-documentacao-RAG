# Classe base GDI Plus Bitmap

A classe gpBitmap encapsula um bitmap GDI+, que consiste nos dados de pixel de uma imagem gráfica e seus atributos. Um objeto Bitmap é um objeto usado para trabalhar com imagens definidas por dados de pixel.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Classe | gpBitmap |
| Classe base | Custom |
| Biblioteca de classes | _GDIPLUS.vcx |
| Classe pai | gpImage ( Classe base GDI Plus Image ) |

# Observações

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, gpImage.

| Propriedades e métodos | Descrição |
| --- | --- |
| Método Create | Cria um objeto bitmap. Sintaxe: ? THIS.Create(tnWidth, tnHeight[, tnPixelFormat]) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tnWidth , obrigatório, largura do novo bitmap em pixels. tnHeight , obrigatório, altura do novo bitmap em pixels. tnPixelFormat , opcional, uma das constantes GDIPLUS_PIXELFORMAT_*, padrão GDIPLUS_PIXELFORMAT_32bppARGB . Observações: Este método é equivalente ao construtor .NET Bitmap(int, int, PixelFormat) . |
| Método CreateFromFile | Cria um objeto bitmap carregando de um arquivo. Sintaxe: ? THIS.CreateFromFile(tcFileName[, tlUseEmbeddedColorMgmt]) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tcFileName , obrigatório, o nome do arquivo a ler. tlUseEmbeddedColorMgmt , opcional, indica se as informações de gerenciamento de cores incorporadas no arquivo, em vez dos padrões, devem ser usadas para o objeto bitmap resultante. Observações: Este método é equivalente ao construtor .NET Bitmap(string,bool) . Este método sempre criará um bitmap rasterizado mesmo se o arquivo de origem estiver em um formato vetorial. Para manter o formato vetorial na memória, use a Classe base GDI Plus Image ( gpImage ). |
| Método CreateFromGraphics | Cria um objeto bitmap a partir de um objeto graphics especificando as propriedades do bitmap. Sintaxe: ? THIS.CreateFromGraphics(toGraphics, tnWidth, tnHeight) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: toGraphics , obrigatório, instância de gpGraphics ou handle GDI+ Graphics, a partir do qual criar o bitmap. tnWidth , obrigatório, largura do novo bitmap em pixels. tnHeight , obrigatório, altura do novo bitmap em pixels. Observações: Este método é equivalente ao construtor .NET Bitmap(int, int, Graphics) . O formato de pixel do bitmap não pode ser definido; o padrão será GDIPLUS_PIXELFORMAT_32bppARGB . |
| Método GetPixel | Obtém o valor de cor de um pixel individual. Sintaxe: nValue = THIS.GetPixel(tX, tY) Valores de retorno: Integer, valor de cor ARGB do pixel. Retorna null ( .NULL. ) em caso de falha. Parâmetros: tX , obrigatório, coordenada X inteira do pixel a obter. tY , obrigatório, coordenada X inteira do pixel a obter. Observações: Este método é equivalente ao .NET Bitmap.GetPixel(int, int) . |
| Método SetPixel | Define o valor de cor de um pixel individual. Sintaxe: THIS.SetPixel( tX, tY, tvColor ) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tX , obrigatório, coordenada X inteira do pixel a obter. tY , obrigatório, coordenada X inteira do pixel a obter. tvColor , obrigatório, objeto da Classe base GDI Plus Color ( gpColor ) ou valor inteiro de cor ARGB. Observações: Este método é equivalente ao .NET Bitmap.SetPixel(int, int,Color) . |
| Método SetResolution | Define a resolução do Bitmap em pontos por polegada. Sintaxe: THIS.SetResolution( tnDPIx, tnDPIy) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: tnDPIx , a resolução horizontal, em pontos por polegada, do bitmap. tnDPIy , a resolução vertical, em pontos por polegada, do bitmap. Observações: Este método é equivalente ao .NET Bitmap.SetResolution(float,float) . |
