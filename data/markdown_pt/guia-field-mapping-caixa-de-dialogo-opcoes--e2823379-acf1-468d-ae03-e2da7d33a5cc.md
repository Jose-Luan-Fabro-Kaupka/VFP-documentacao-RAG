# Guia Field Mapping, Caixa de diálogo Opções

Permite especificar que tipo de controle o Visual FoxPro cria quando você arrasta uma tabela ou campo para um formulário a partir do Data Environment Designer, Database Designer (Visual FoxPro) ou Janela do Gerenciador de projetos. Por exemplo, você pode especificar que o Visual FoxPro crie uma caixa de edição quando arrastar um campo Character para um formulário.

Quando você escolhe Definir como padrão — que aparece em cada guia na caixa de diálogo — o Visual FoxPro salva as configurações de opção no registro (banco de dados de registro do sistema Windows). Observe que nesta guia, escolher OK também salva as configurações de opção no registro.
 **Mapear campos para classes em operações de arrastar e soltar**
Exibe os mapeamentos atuais entre tipos de campo e classes (controles). A lista inclui: Tipo Todos os tipos de dados suportados para campos de banco de dados. O tipo de campo Multiple é usado para especificar a classe que será criada se você arrastar uma tabela inteira ou vários campos para um controle de uma vez. O tipo de campo Label é usado para especificar a classe que será criada para as legendas dos campos. Biblioteca de classes A biblioteca que contém a definição de classe a ser mapeada para um tipo de campo. Se esta coluna estiver em branco, o tipo de campo é mapeado para uma classe base do Visual FoxPro. Nome da classe A classe para a qual um tipo de campo é mapeado, que especifica o tipo de controle que será criado.
**Modificar**
Escolha este botão para exibir a Caixa de diálogo Modificar mapeamento de campo , onde você pode especificar um mapeamento diferente para o tipo de campo selecionado.

 Para modificar mapeamentos de campo
 - Na guia Field Mapping da caixa de diálogo Opções, escolha Modificar .
- Na caixa de diálogo Modificar mapeamento de campo, selecione um tipo de campo na lista Type.
- Para definir a classe que é criada sempre que você arrasta uma tabela ou vários campos, selecione Multiple .
- Para selecionar a biblioteca de classes (.vcx) que contém o controle que deseja associar ao tipo de campo selecionado, escolha Procurar .
- Selecione um nome de classe na lista Name. A classe que você especificar aqui será criada sempre que um campo do tipo selecionado for arrastado para um formulário.
- Escolha OK ou Aplicar para aceitar o mapeamento.

# Opções de banco de dados
 **Legenda de campo de arrastar e soltar**
Escolha esta opção se desejar que o Visual FoxPro use o nome do campo como legenda da classe sendo criada. Se você limpar esta opção, o Visual FoxPro não criará legendas de campo.
**Copiar comentário do campo**
Escolha esta opção para que o Visual FoxPro copie o comentário de um campo (se houver) para a propriedade Comment da nova classe ao criá-la.
**Copiar máscara de entrada do campo**
Escolha esta opção para que o Visual FoxPro copie a máscara de entrada de um campo (se houver) para a propriedade InputMask da nova classe ao criá-la.
**Copiar formato do campo**
Escolha esta opção para que o Visual FoxPro copie a especificação de formato de um campo (se houver) para a propriedade Format da nova classe ao criá-la.
