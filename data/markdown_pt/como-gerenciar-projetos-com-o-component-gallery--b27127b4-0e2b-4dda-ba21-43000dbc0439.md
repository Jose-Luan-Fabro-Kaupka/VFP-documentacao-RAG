# Como: gerenciar projetos com o Component Gallery

Você pode usar o Component Gallery para criar Projects e Applications e gerenciar seu desenvolvimento. Use o Component Gallery para organizar componentes dentro do Component Gallery ou use os templates, builders e assistentes no Component Gallery para criar o projeto ou aplicativo desejado.

As pastas do Component Gallery representam um agrupamento arbitrário de itens da galeria. Você pode reorganizar os itens da galeria usando arrastar e soltar ou pode duplicar itens em outras pastas. Você pode copiar e renomear um catálogo ou pasta e reorganizar os itens que ele contém. Há poucos, se houver, limites sobre como você pode usar, modificar ou criar catálogos ou pastas.

As configurações padrão para catálogos e pastas permitem que você execute revisão e gerenciamento básicos com itens da galeria. Se você deseja modificar características de catálogos ou pastas, ou se deseja maior acesso às propriedades da galeria, selecione Advanced editing enabled na caixa de diálogo Component Gallery Options.

### Para criar um projeto ou um aplicativo a partir do Component Gallery
- Use o Application Wizard ou o template New Application na pasta Applications do catálogo Visual FoxPro.

Para catálogos e pastas, selecione guias e opções para a alteração que deseja fazer. Para detalhes, consulte Component Gallery Options Dialog Box na Ajuda.

# Movendo e visualizando itens no Component Gallery

Você pode mover itens no painel direito, Object, da janela Component Gallery para a área de trabalho ou para um projeto ou formulário aberto. O Project Manager reconhece o item referenciado pelo item do Component Gallery e o coloca no local apropriado no Project Manager. Itens do Component Gallery colocados na área de trabalho são não funcionais. Não há representação na área de trabalho para Database, Folder e itens da galeria que representam arquivos não visuais.

### Para mover itens do Component Gallery
- No painel direito, clique no item que deseja mover. O ícone Move, localizado no canto superior esquerdo da janela Component Gallery, muda conforme o item selecionado.
- Arraste e solte o ícone Move para a área de trabalho ou para um projeto ou formulário aberto.

Quando o Component Gallery não encontra o item original representado pelo item da galeria, uma caixa de diálogo Find abre para que você possa localizar o item.

A tabela a seguir identifica os itens da galeria incluídos no Visual FoxPro e seus comportamentos padrão.

| Tipo de item do Component Gallery | Project | Form | Screen | Controls |
| --- | --- | --- | --- | --- |
| Class (_ClassItem) | 6 | | | |
| File (_FileItem) | | | | |
| URL (_UrlItem) | 1 | | | |
| Form (_FormItem) | 9 | 11 | | |
| Report (_ReportItem) | 9 | 11 | | |
| Program (_ProgramItem) | 11 | | | |
| Menu (_MenuItem) | 10 | 11 | | |
| Image (_ImageItem) | 2 | 7 | 2 | |
| Sound (_SoundItem) | 3 | | | |
| Video (_VideoItem) | 3 | | | |
| ActiveX (_ActiveXItem) | | | | |
| Data (_DataItem) | 4 | | | |
| Template (_TemplateItem) | 5 | | | |
| Catalog (_CatalogItem) | 8 | | | |
| Sample (_SampleItem) | | | | |
| Project (_ProjectItem) | 11 | | | |

1 – Adicionar classe de hiperlink 2 – Adicionar uma classe de imagem ou definir uma propriedade Picture 3 – Adicionar uma classe multimídia 4 – Adicionar uma classe de grade 5 – Dependendo do tipo (por exemplo, formulário) cria um novo arquivo e o adiciona ao projeto 6 – Cria uma instância na Screen 7 – Define o papel de parede do Visual FoxPro 8 – Inicia uma nova janela Gallery com esse catálogo 9 – Adicionar uma classe Button para iniciar um formulário/relatório 10 – Adicionar um menu de atalho a um formulário 11 – Abre em um designer (modifica)

# Revisando e modificando classes

Como os itens do Component Gallery representam itens reais que podem ser objetos ou classes, você pode revisar ou modificar essas classes acessando o objeto original através do Component Gallery.

### Para revisar uma classe
- No Component Gallery, clique com o botão direito em uma classe.
- No menu de atalho, clique em View in Browser. Isso abre a janela Class Browser, para que você possa visualizar as propriedades e métodos da classe selecionada.

### Para modificar uma classe
- No Component Gallery, clique com o botão direito em uma classe.
- No menu de atalho, clique em Modify. Isso abre a classe no Class Designer.

# Criando e modificando formulários

Você pode usar o Component Gallery para duplicar ou modificar formulários e para adicionar formulários e outros itens da galeria a um projeto.

### Para criar um formulário a partir do Component Gallery
- Clique duas vezes em qualquer template ou selecione New Form no menu de atalho de qualquer template na pasta Forms do Component Gallery. -ou- Clique duas vezes no Form Wizard na pasta Forms do Component Gallery. -ou- Selecione Create Form no menu de atalho de itens do Component Gallery na pasta Forms do Component Gallery.
