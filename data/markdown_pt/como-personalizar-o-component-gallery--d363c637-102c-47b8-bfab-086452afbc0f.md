# Como: personalizar o Component Gallery

Você pode personalizar o Component Gallery alterando o comportamento padrão de catálogos, pastas e itens da galeria através das caixas de diálogo Properties apropriadas.

### Para criar um catálogo do Component Gallery
- Selecione o botão Options na barra de ferramentas do Component Gallery.
- Clique na guia Catalogs na caixa de diálogo Component Gallery Options.
- Clique em New e nomeie o novo catálogo na caixa de diálogo Open.
- Clique em OK.
- O Component Gallery adiciona o catálogo à treeview para que você possa começar a usá-lo como qualquer catálogo existente.

### Para alterar a configuração de um catálogo ou pasta
- Clique com o botão direito no catálogo ou pasta.
- No menu de atalho, clique em Properties.
- Na Catalog Properties Dialog Box ou Folder Properties Dialog Box, selecione a guia que contém as opções que você deseja configurar. Catálogos e pastas da galeria, conforme exibidos no Component Gallery Window Catalog pane, podem representar URLs, pastas ou arquivos em seu disco rígido. Você pode visualizar uma pasta da galeria como Web view ou como Explorer-level view, dependendo da forma como você especifica o nome na guia General da caixa de diálogo de propriedades da pasta.

# Web Views

Você pode especificar URLs ou arquivos como catálogos do Component Gallery ou como itens da galeria. Quando você configura um item como uma pasta da galeria, o item abre automaticamente como uma Web view no painel Object (direito) quando você o seleciona no Catalog pane.

### Para configurar um catálogo ou pasta da galeria como uma Web view
- Na Folder Properties Dialog Box, selecione a guia Node.
- No campo Dynamic folder, especifique a página Web ou nome do arquivo como nos exemplos a seguir: http:\\www.microsoft.com\ file:\\c:\my documents\testpage.htm file:\\c:\my documents\Wordfile.doc

Quando você destaca o ícone Web view no Catalog pane, a barra de ferramentas muda para incluir botões de navegação Web. A Web view refletirá as configurações do seu Windows Explorer.

# Explorer-level Views

Você pode especificar um diretório como uma pasta ou catálogo da galeria que tem características do Windows Explorer.

### Para configurar um catálogo ou pasta da galeria como uma Explorer-level view
- Na Folder Properties Dialog Box, selecione a guia Node.
- No campo Dynamic folder, especifique um nome de pasta ou arquivo e barra invertida (\) como valor, como nos exemplos a seguir: C:\My Documents\ Observação Esta especificação cria uma visualização de arquivos reais, diferente de outras visualizações do Component Gallery. Nesta visualização você pode excluir arquivos do seu disco. Para criar uma Explorer-level view que mantenha a proteção dos arquivos exibidos, especifique o destino usando uma designação de curinga como no exemplo a seguir: C:\My Documents\*.*

Evite usar curingas para criar pastas dinâmicas quando você pode esperar encontrar mais de 512 itens, a menos que tenha uma máquina rápida com grande quantidade de RAM.
