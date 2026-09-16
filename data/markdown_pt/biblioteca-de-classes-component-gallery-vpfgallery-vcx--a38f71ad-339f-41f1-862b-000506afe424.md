# Biblioteca de classes Component Gallery (Vpfgallery.vcx)

A biblioteca de classes Component Gallery, Vpfgallery.vcx, fornece os tipos de item como classes.

| Tipo de item | Descrição |
| --- | --- |
| Class (_ClassItem) | O tipo de item genérico para qualquer classe Visual FoxPro. Pode ser de arquivos .vcx ou .prg. |
| File (_FileItem) | Este é qualquer arquivo. O Visual FoxPro lê o Registro para funções shell e as adiciona ao menu. A galeria inclui uma rotina de pesquisa que verifica extensões específicas e redireciona o tipo de item. A galeria suporta convenções de nomenclatura UNC para desenvolvimento em equipe (compartilhamento de Catálogos em redes). |
| ActiveX (_ActiveXItem) | Este é um controle ou servidor ActiveX, como um .ocx criado pelo Visual Basic CCE ou .exe/.dll criado pelo Visual FoxPro. |
| Data (_DataItem) | Esta é uma fonte de dados Visual FoxPro (.dbc, .dbf, View, e assim por diante). |
| Image (_ImageItem) | Este é um tipo de item File cujo arquivo tem uma extensão de arquivo de imagem, como .bmp, .jpg, .gif, .ico, .cur, .ani, e assim por diante. |
| Sound (_SoundItem) | Este é um tipo de item File cujo arquivo tem extensão .wav ou .rmi. |
| Video (_VideoItem) | Este é um tipo de item File cujo arquivo tem extensão .avi. |
| URL (_UrlItem) | Este é um tipo de item Web e inclui documentos Web e locais, como arquivos HTML. |
| Sample (_SampleItem) | Este é um tipo de item File para arquivos que executam no Visual FoxPro e podem ser um arquivo executável Visual FoxPro, como .app, .exe, .prg, .scx ou .frx. |
| Template (_TemplateItem) | Este é um tipo de item Script que abre um construtor para o elemento Visual FoxPro representado pelo tipo do item destacado, incluindo formulários e relatórios. |
| Catalog (_CatalogItem) | Este é um tipo Component Gallery que permite adicionar e abrir catálogos Visual FoxPro. |
| Form (_FormItem) | Este é um tipo para formulários Visual FoxPro (.scx). |
| Report (_ReportItem) | Este é um tipo para relatórios Visual FoxPro (.frx). |
| Menu (_MenuItem) | Este é um tipo para menus Visual FoxPro (.mnx). |
| Program (_ProgramItem) | Este é um tipo para programas Visual FoxPro (.prg). |
| Project (_ProjectItem) | Este é um tipo para projetos Visual FoxPro (.pjx). |

Você pode usar o Class Browser para examinar os detalhes de qualquer uma dessas classes.

Para detalhes sobre outras classes usadas no Component Gallery, consulte Visual FoxPro Foundation Classes A-Z ou use a Class Browser Window para examinar as bibliotecas na pasta Ffc.
