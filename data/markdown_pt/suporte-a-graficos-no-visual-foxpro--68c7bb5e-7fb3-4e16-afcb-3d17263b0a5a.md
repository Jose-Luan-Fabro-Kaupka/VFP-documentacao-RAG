# Suporte a gráficos no Visual FoxPro

O Visual FoxPro 8.0 e posterior substitui o suporte nativo para renderização dos formatos Graphics Interchange Format (.gif) e Joint Photographic Electronic Group (.jpeg) por Graphics Device Interface+ (GDI+) para Microsoft Windows XP e posterior. O Visual FoxPro suporta todos os formatos que o GDI+ manipula, incluindo arquivos .gif animados.

A tabela a seguir lista os formatos gráficos que o Visual FoxPro suporta.

| Extensão de arquivo | Nome do tipo de arquivo |
| --- | --- |
| .ani | Animated Cursor |
| .bmp | Bitmap |
| .cur | Cursor |
| .dib | Device Independent Bitmap |
| .emf | Windows Enhanced Metafile |
| .exif | Exchangeable Image File |
| .gif, .gfa | Graphics Interchange Format |
| .ico | Icon |
| .jpg, .jpeg, .jpe, .jfif | Joint Photographic Electronic Group, JPEG File Interchange Format |
| .png | Portable Networks Graphics |
| .tif, .tiff | Tag Image File Format |
| .wmf | Windows Metafile |

> **Observação:** No Visual FoxPro, arquivos cursor, animated cursor e icon podem ser usados como arquivos gráficos. Por exemplo, você pode especificar um arquivo animated cursor para a propriedade Picture do controle Image. No entanto, o controle Image exibe a representação estática do cursor.

Se o Visual FoxPro não reconhecer uma versão particular de um formato suportado nativamente, como .bmp, .dib, .cur, .ani ou .ico, ele os passa ao GDI+ para renderização. Portanto, conforme novos formatos de arquivo estáticos se tornam suportados em versões futuras do GDI+, o Visual FoxPro pode suportá-los automaticamente.

Com o GDI+, o Visual FoxPro inclui a propriedade RotateFlip no controle Image para que você possa rotacionar e inverter, ou virar, uma imagem. Para obter mais informações, consulte Propriedade RotateFlip.

> **Observação:** O GDI+ é instalado com o sistema operacional Windows XP e é necessário para executar o Visual FoxPro. O Visual FoxPro inclui um merge module para redistribuição com aplicativos personalizados executados em plataformas Windows 98, Windows Me e Windows 2000.

O Visual FoxPro fornece suporte a gráficos nas três áreas a seguir:
 - Linguagem
- Controles e objetos
- Interface do usuário

# Linguagem

Você pode usar a função GETPICT( ) para acessar a caixa de diálogo do Visual FoxPro que fornece acesso a formatos de arquivo válidos. Você também pode acessar gráficos por meio de propriedades nos controles e objetos descritos aqui.

# Controles e objetos

A tabela a seguir lista controles e objetos do Visual FoxPro com propriedades para as quais você pode especificar arquivos gráficos. Agora você pode especificar arquivos gráficos .gif, .jpg, .cur, .ani e .ico para essas propriedades além dos arquivos gráficos .bmp e .dib suportados em versões anteriores do Visual FoxPro.

| Controle ou objeto | Propriedades |
| --- | --- |
| Controle CheckBox | DisabledPicture DownPicture Picture |
| Controle CommandButton | DisabledPicture DownPicture Picture |
| Controle ComboBox | Picture |
| Objeto Container | Picture |
| Objeto Control | Picture |
| Objeto Custom | Picture |
| Objeto Form | Picture |
| Controle Image* | Picture |
| Controle ListBox | Picture |
| Controle OptionButton | DisabledPicture DownPicture Picture |
| Objeto Page | Picture |
| Variável de sistema _SCREEN | Picture |

* O Visual FoxPro suporta arquivos .gif animados somente para a propriedade Picture de um controle Image.

# Interface do usuário

Você pode escolher arquivos gráficos usando a caixa de diálogo Open em vários designers do Visual FoxPro. A caixa de diálogo Open para os seguintes designers inclui todos os formatos de arquivo gráfico válidos.

### Form Designer e Class Designer

Você pode localizar e selecionar uma imagem abrindo a caixa de diálogo Open nos designers Form e Class para uma propriedade nesses controles que suportam arquivos gráficos.

### Para selecionar uma imagem nos designers Form e Class
- Na janela Properties, clique duas vezes na propriedade Picture.

O Visual FoxPro exibe a caixa de diálogo Open para você localizar e selecionar uma imagem.

### Project Manager

Você pode localizar, selecionar e adicionar um arquivo gráfico a um projeto no Project Manager.

### Para adicionar um arquivo gráfico a um projeto
- No Project Manager, selecione Other Files nas guias All ou Other e clique em Add.

O Visual FoxPro exibe a caixa de diálogo Open para você localizar e selecionar uma imagem.

# Suporte a imagens GDI+

GDI+ é uma interface de programação de aplicativos (API) baseada em classes para programadores C/C++. Ela permite que aplicativos usem gráficos e texto formatado tanto na exibição de vídeo quanto na impressora. Aplicativos baseados na API Microsoft Win32 não acessam hardware gráfico diretamente. Em vez disso, o GDI+ interage com drivers de dispositivo em nome dos aplicativos. O GDI+ também é suportado pelo sistema operacional Windows de 64 bits.

O GDI+ pode ser usado em todos os aplicativos baseados em Windows. O GDI+ está incluído nos sistemas operacionais Microsoft Windows XP e Windows Server 2003. O GDI+ é necessário e está disponível como redistribuível para aplicativos Visual FoxPro que executam nos sistemas operacionais Windows 2000, Windows Millennium Edition e Windows 98. Para baixar o redistribuível mais recente, visite o site da Web Microsoft Windows Platform SDK em http://www.microsoft.com/msdownload/platformsdk/sdkupdate/ ou o site da Web Microsoft Download Center em http://www.microsoft.com/downloads/.

O Visual FoxPro pode incluir as bibliotecas de runtime VFP9R.dll e VFP9T.dll. O arquivo GDIPlus.dll deve estar presente no diretório system do computador do usuário.

# Suporte a imagens .gif animadas

Arquivos .gif animados são uma variedade popular do formato de arquivo .gif. Eles usam a mesma extensão de arquivo (.gif) e contêm quadros de imagem específicos que percorrem em ciclo para produzir um efeito animado. O arquivo .gif animado contém o número de vezes que o arquivo .gif percorre em ciclo antes de parar. O Visual FoxPro suporta arquivos .gif animados da seguinte forma:
 - O Visual FoxPro suporta arquivos .gif animados somente para a propriedade Picture no controle Image.
- Arquivos .gif animados são exibidos tanto em tempo de design quanto em tempo de execução.
- O Visual FoxPro exibe apenas o primeiro quadro de um arquivo .gif animado quando ele aparece em qualquer outro lugar além do controle Image.
- O Visual FoxPro percorre em ciclo um arquivo .gif animado com base somente em sua configuração interna de contagem de loop.
- O Visual FoxPro pausa entre loops de animação por um segundo.
- Se o tamanho ou local do controle Image mudar em tempo de execução enquanto uma animação de imagem é reproduzida, o Visual FoxPro redefine para o primeiro quadro e continua.
- O Visual FoxPro desenha o tamanho da imagem .gif conforme especificado pelo autor do arquivo .gif, não o controle Image. O Visual FoxPro não recorta nem estica a imagem.
- Durante animações, a imagem inteira ou parte dela é apagada para que o próximo quadro possa ser redesenhado. O Visual FoxPro minimiza redesenho desnecessário para evitar cintilação. Se a posição da imagem for movida, por exemplo, o controle ou seu contêiner é movido, toda a imagem precisa ser redesenhada.
- Como o Visual FoxPro armazena internamente uma única representação de uma imagem particular como um bitmap off-screen, vários controles Image usando o mesmo arquivo .gif animado estão sempre sincronizados juntos. Se você quiser que as animações da mesma imagem se comportem de forma diferente para cada controle Image, deve criar uma cópia de cada arquivo .gif animado e renomear cada um.
- O autor de arquivos .gif animados pode especificar a quantidade de tempo entre quadros. Essa quantidade de tempo pode diferir entre cada quadro. Portanto, é possível que arquivos .gif animados tenham atrasos excessivamente longos entre quadros.
- Se você usar um arquivo .gif animado em um controle diferente de um controle Image, a animação da imagem não é reproduzida. No entanto, se você usar a imagem posteriormente em um controle Image, a imagem anima somente se você primeiro executar um comando CLEAR...RESOURCES. Isso ocorre porque a imagem já está armazenada na memória e o atributo de animação está sendo ignorado quando a imagem é renderizada em um controle que não seja Image. Você deve usar CLEAR...RESOURCES para recarregar a imagem na memória.
