# Form Wizard

Este wizard facilita o uso de uma única tabela para criar um formulário para entrada de dados. O wizard preencherá automaticamente o formulário com todos os campos da tabela, para que você possa excluí-los ou reorganizá-los como desejar. O tamanho do formulário é baseado na configuração Maximum design area na guia Forms da caixa de diálogo Options. O mapeamento de campos (o que um formulário exibe) é controlado pelas configurações na guia Field Mapping da caixa de diálogo Options, menu Tools. Esta guia não está disponível enquanto o Form wizard estiver aberto.

 Para acessar o Form wizard
 - No menu Tools, escolha Wizards e clique em Form.
- Na caixa de diálogo Wizard Selection, escolha Form Wizard.

Se você criar um formulário dentro de um banco de dados, o Form wizard pode usar configurações de input mask e format armazenadas no banco de dados. Depois de salvar o formulário, você pode abri-lo e modificá-lo posteriormente como qualquer outro formulário no Form designer.

# Etapa 1 - Select Fields

Nesta etapa, você pode escolher uma free table ou uma tabela dentro de um banco de dados como origem do seu formulário. Você só pode selecionar campos de uma única tabela ou view.

 Para selecionar os campos do seu formulário
 - Use os controles Databases and Tables para localizar e selecionar a tabela que deseja usar.
- Na janela Available fields, selecione um ou mais campos que deseja usar da tabela selecionada e use os botões de seta para movê-los para a janela Selected fields.

# Etapa 2 - Choose Form Style

Nesta etapa, você especifica a aparência dos controles no seu formulário. Quando você clica em qualquer um dos estilos listados na caixa de texto Style, o wizard exibe uma imagem na lupa como exemplo do estilo.

As opções Button Type referem-se aos botões de navegação do seu formulário.
 **Text Buttons**
Coloca texto de navegação nos botões do seu formulário.
**Picture buttons**
Coloca ícones de navegação nos botões do seu formulário.
**No buttons**
Não coloca botões no seu formulário, para que você possa impedir a navegação além dos dados exibidos ou inseridos.
**Custom**
Permite que você escolha entre dois tipos de janelas de dados com rolagem. Scrolling grid - Exibe os campos que você seleciona de um registro por vez. Scrolling grid (justified) – Exibe os campos que você seleciona de quantos registros couberem no formulário de uma só vez.

Os botões de navegação que o wizard cria no seu formulário são os seguintes.

| Botão | Ícone | Descrição |
| --- | --- | --- |
| Top | Move o ponteiro de registro para o primeiro registro. | |
| Prev | Move o ponteiro de registro um registro para trás. | |
| Next | Move o ponteiro de registro um registro para frente. | |
| Bottom | Move o ponteiro de registro para o último registro. | |
| Find | Exibe a caixa de diálogo Search. | |
| Print | Imprime um relatório. | |
| Add | Adiciona um novo registro ao final da tabela. | |
| Edit | Permite que um usuário altere valores no registro atual. | |
| Delete | Exclui o registro atual. | |
| Exit | Fecha o formulário. | |

> **Observação:** Depois que o wizard salva um formulário, você ainda pode adicionar campos a ele usando os mesmos estilos selecionando Quick Form no menu Form para abrir o Form builder.

Todos os controles criados pelo Form wizard e pelo Form builder estão no diretório \Wizards no arquivo Wizstyle.vcx. Se você desejar modificar os estilos, modifique as classes neste arquivo usando o Class designer.

# Etapa 3 - Sort Records

Selecione os campos na ordem em que deseja classificar os registros dentro de cada grupo. Por exemplo, se você estiver usando dois campos e tiver um campo de primeiro nome e um campo de sobrenome, então você pode escolher classificar por primeiro nome+sobrenome (como PaulWilson) ou por sobrenome+primeiro nome (como WilsonPaul). A forma como você classifica é determinada pela ordem em que selecionou esses campos.

Se sua tabela já tiver um ou mais índices, você pode selecionar a tag, que é listada abaixo dos campos na janela Available fields.

# Etapa 4 - Finish

Se você escolheu um grande número de campos anteriormente e deseja garantir que todos caibam no formulário, pode selecionar Add pages for fields that do not fit. Caso contrário, se o número de campos exceder o tamanho do formulário, o Visual FoxPro fornece um formulário com rolagem.

Você pode usar mapeamentos de campo especificados na caixa de diálogo Options do menu Tools ou substituir essas configurações com informações no banco de dados. Para visualizar o formulário antes de sair do Form Wizard, clique no botão Preview.

Depois de salvar o formulário, você pode abri-lo e modificá-lo posteriormente como qualquer outro formulário no Form designer.
