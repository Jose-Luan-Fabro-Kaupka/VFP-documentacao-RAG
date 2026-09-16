# One-To-Many Form Wizard

Você pode usar esse assistente para criar um formulário de entrada de dados que atualize várias tabelas a partir de um único formulário. Por exemplo, você pode criar um formulário que atualize tabelas de clientes e pedidos. O tamanho do formulário é baseado na configuração Maximum design area da guia Forms da caixa de diálogo Options.

 Para acessar o One-To-Many Form Wizard
 - No menu Tools, escolha Wizards e clique em Form.
- Na caixa de diálogo Wizard Selection, escolha One-To-Many Form Wizard.

# Etapa 1 – Selecionar campos da tabela pai

Nesta etapa, você escolhe uma tabela livre ou uma tabela ou exibição de um banco de dados que fornecerá os dados dos campos de controle apresentados no formulário. Isso especifica qual campo da tabela pai ou de controle determina os registros selecionados na tabela filha ou controlada.

 Para selecionar os campos do formulário
 - Use os controles Databases e Tables para localizar e selecionar a tabela que deseja usar.
- Na janela Available fields, selecione um ou mais campos que deseja usar da tabela selecionada e use os botões de seta para movê-los para a janela Selected fields.

Você pode selecionar campos de apenas uma tabela ou exibição.

# Etapa 2 - Selecionar campos da tabela filha

Nesta etapa, você escolhe os campos da tabela relacionada. Isso determina quais campos de uma tabela filha ou controlada são exibidos no formulário. Por exemplo, a tabela pai pode conter apenas nomes, números de ID e endereços de clientes, enquanto a tabela filha pode conter informações de pedidos, como números de ID, valor, data, desconto e assim por diante. Um cliente pode ter muitos pedidos.

Assim como ocorre com os campos da tabela pai, você pode selecionar campos de apenas uma tabela ou exibição filha.

# Etapa 3 – Relacionar tabelas

Nesta etapa, você especifica na lista de campos como as tabelas pai e filha estão relacionadas. No exemplo da etapa 2, ambas as tabelas contêm o campo de ID do cliente, portanto essa é uma maneira de relacioná-las. Pode haver outras maneiras, dependendo dos campos disponíveis e do que você deseja relatar.

# Etapa 4 - Escolher o estilo do formulário

Nesta etapa, você escolhe o formato básico do formulário entre os estilos incorporados ao assistente. Quando você clica em um dos estilos listados na caixa Style, o assistente exibe uma imagem na lupa como exemplo do estilo.

As opções de tipo de botão referem-se aos botões de navegação do formulário. Os botões de navegação criados pelo assistente no formulário são os seguintes.
 **Text Buttons**
Coloca texto de navegação nos botões do formulário.
**Picture buttons**
Coloca ícones de navegação nos botões do formulário.
**No buttons**
Não coloca botões no formulário, permitindo impedir a navegação além dos dados exibidos ou inseridos.

> **Observação:** O tipo de botão Custom não está disponível no One-to-Many Form Wizard.

| Botão | Ícone | Descrição |
| --- | --- | --- |
| Top | Move o ponteiro de registro para o primeiro registro. | |
| Prev | Move o ponteiro de registro um registro para trás. | |
| Next | Move o ponteiro de registro um registro para frente. | |
| Bottom | Move o ponteiro de registro para o último registro. | |
| Find | Exibe a caixa de diálogo Search. | |
| Print | Imprime um relatório. | |
| Add | Adiciona um novo registro ao final da tabela. | |
| Edit | Permite que o usuário altere os valores do registro atual. | |
| Delete | Exclui o registro atual. | |
| Exit | Fecha o formulário. | |

> **Observação:** Depois que o assistente salva um formulário, você pode adicionar outros campos usando os mesmos estilos ao selecionar Quick Form no menu Form.

Todos os controles criados pelo Form Wizard e pelo Form Builder estão em Wizards\Wizstyle.vcx. Se quiser modificar os estilos, modifique as classes nesse arquivo.

# Etapa 5 – Classificar registros

Nesta etapa, você seleciona na tabela pai os campos na ordem em que deseja classificar os registros. Por exemplo, se estiver usando dois campos, um de nome e outro de sobrenome, poderá optar por classificar por nome+sobrenome (como PaulWilson) ou sobrenome+nome (como WilsonPaul). A classificação é determinada pela ordem em que você selecionou esses campos.

Se a tabela já tiver um ou mais índices, você poderá selecionar a marca de índice, que aparece abaixo dos campos, separada por uma linha, na janela Available fields.

# Etapa 6 - Concluir

Nesta etapa, você pode escolher como e quando usar o formulário.
 **Save form for later use**
Permite salvar o formulário como um arquivo que poderá ser aberto posteriormente.
**Save and run form**
Salva o formulário como um arquivo e o abre no Visual FoxPro para uso imediato.
**Save form and modify in the Form Designer**
Salva o formulário como um arquivo e o abre no Form Designer para que você possa modificá-lo.

Se você marcar a caixa de seleção Use field mappings, poderá usar os mapeamentos de campo especificados na caixa de diálogo Options do menu Tools. Para obter mais informações, consulte Guia Field Mapping, caixa de diálogo Options. Se usar tabelas de um banco de dados, poderá selecionar Override with DBC field display classes para que o formulário use informações do banco de dados; caso contrário, essa opção não estará disponível.

Para visualizar o formulário antes de sair do One-To-Many Form Wizard, clique no botão Preview.
