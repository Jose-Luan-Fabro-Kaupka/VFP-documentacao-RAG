# GDI Plus API Wrapper Foundation Classes

A biblioteca de classes base GDI Plus API Wrapper Foundation, _GDIPLUS.vcx, contém uma coleção de classes que encapsulam a funcionalidade GDI+ Flat API para uso no Visual FoxPro. Você pode usar essas classes para adicionar recursos GDI+ a formulários e relatórios.

# Biblioteca de classes _GDIPLUS.vcx

| Classe | Descrição |
| --- | --- |
| GDI Plus Base Foundation Class | A classe base abstrata para todas as outras classes _GDIPLUS. Fornece alguns métodos utilitários básicos. |
| GDI Plus Bitmap Foundation Class | Encapsula um bitmap GDI+, que consiste nos dados de pixel de uma imagem gráfica e seus atributos. Um Bitmap object é um objeto usado para trabalhar com imagens definidas por dados de pixel. |
| GDI Plus Brush Foundation Class | A classe base abstrata para todas as classes Brush (por exemplo, as classes gpSolidBrush e gpHatchBrush). |
| GDI Plus Color Foundation Class | Encapsula uma cor GDI+, consistindo de 4 inteiros positivos (0..255) para os componentes vermelho, verde, azul e alfa. |
| GDI Plus Font Foundation Class | Define um formato particular para texto, incluindo face de fonte, tamanho e atributos de estilo. |
| GDI Plus FontFamily Foundation Class | Designa atributos compartilhados por um grupo de fontes relacionadas. |
| GDI Plus Graphics Foundation Class | Encapsula uma superfície de desenho GDI+. Fornece métodos para desenhar em uma janela ou outra tela. |
| GDI Plus HatchBrush Foundation Class | Um objeto brush que preenche com um padrão hatch. |
| GDI Plus Image Foundation Class | Encapsula uma imagem GDI+ e serve como classe base para tipos de imagem específicos (por exemplo, a classe gpBitmap). |
| GDI Plus Object Foundation Class | A classe base abstrata para todos os objetos GDI+. Fornece gerenciamento de handles GDI+ e o resultado de operações GDI+. |
| GDI Plus Pen Foundation Class | Um objeto pen, que é usado para desenhar linhas e curvas. |
| GDI Plus Point Foundation Class | Encapsula um par ordenado de coordenadas x e y que define um ponto em um plano bidimensional. |
| GDI Plus Rectangle Foundation Class | Encapsula um conjunto de quatro números que representam a localização e o tamanho de um retângulo. |
| GDI Plus Size Foundation Class | Armazena um par ordenado de números, tipicamente a largura e a altura de um retângulo. |
| GDI Plus SolidBrush Foundation Class | Um objeto brush que preenche com uma cor sólida. |
| GDI Plus StringFormat Foundation Class | Objeto que encapsula informações de layout de texto (como alinhamento e espaçamento de linha) e manipulações de exibição (como inserção de reticências e substituição de dígitos nacionais). |

# Observações

Microsoft Windows GDI+ expõe uma interface de programação de aplicativos (API) plana que consiste em cerca de 600 funções, que são implementadas em Gdiplus.dll e declaradas em Gdiplusflat.h. Essas funções são descritas no tópico de referência MSDN Library GDI+ Flat API.

As classes nesta biblioteca Visual FoxPro têm nomes que correspondem aproximadamente às classes wrapper que executam a mesma função no .NET Framework, para que você possa encontrar informações e exemplos adicionais úteis lendo material que cobre as classes .NET equivalentes. Por exemplo, para aprender sobre gpHatchBrush, você pode ler sobre a classe .NET HatchBrush.

Quando você usa funções GDI+, geralmente exibe os resultados em uma superfície de desenho de destino, frequentemente referida como device ou canvas. Você especifica sua superfície de desenho de destino fornecendo ao GpGraphics object um handle previamente atribuído a esta superfície, ou os meios para obter tal handle. Quando você está manipulando exibições de tela, pode criar este handle a partir de um handle de janela, como Window Manipulation Routines de um formulário. Quando você está criando saída de relatório, pode usar a propriedade GDIPlusGraphics Property do ReportListener.
