# Como: selecionar índices em tempo de execução

Você pode fornecer a capacidade de os usuários organizarem registros interativamente quando clicam em um cabeçalho de coluna em uma grade em um formulário. Por exemplo, suponha que você deseja permitir que os usuários do aplicativo organizem registros em uma grade em um formulário clicando no cabeçalho da coluna pela qual desejam organizar os registros. Para fornecer essa capacidade, inclua o comando SET ORDER para alterar a ordem dos registros em um formulário em tempo de execução.

### Para organizar registros interativamente em um formulário
- Crie um formulário com um controle Grid.
- Defina a propriedade ColumnCount da grade para o número de campos que deseja exibir na grade.
- Para o cabeçalho de cada coluna na grade, insira código que inclua o comando SET ORDER no evento Click do cabeçalho que execute as seguintes tarefas: Define a ordem dos registros para uma chave de índice baseada na coluna. Atualiza o formulário.

Por exemplo, suponha que você criou um formulário baseado na tabela Customer no banco de dados de exemplo do Visual FoxPro, TestData, com uma grade contendo quatro colunas: Company, Contact, Postal_Code e Phone. A grade aparece ordenada alfabeticamente primeiro porque os registros nessa tabela foram inseridos alfabeticamente. No entanto, você pode então permitir que o usuário visualize a grade ordenada por nome de contato ou código postal inserindo o código que usa o comando SET ORDER no evento Click de cada cabeçalho de coluna.

A tabela a seguir descreve código de exemplo que você pode incluir no evento Click.

| Código | Comentário |
| --- | --- |
| SET ORDER TO Company GO TOP THISFORM.Refresh | No código do evento Click do cabeçalho Company, reordene a grade usando a chave de índice Company e atualize o formulário para exibir registros em ordem por nome da empresa. |
| SET ORDER TO Contact GO TOP THISFORM.Refresh | No código do evento Click do cabeçalho Contact, reordene a grade pela chave de índice Contact e atualize o formulário para exibir registros em ordem por nome de contato. |
| SET ORDER TO PostalCode GO TOP THISFORM.Refresh | No código do evento Click do cabeçalho Postal_Code, reordene a grade pela chave de índice PostalCode e atualize o formulário para exibir registros em ordem por código postal. |

No exemplo, quando o formulário é exibido pela primeira vez, a grade aparece em ordem alfabética por empresa. Quando o usuário clica no cabeçalho da coluna Contact, o Visual FoxPro exibe os registros na grade em ordem alfabética por nome de contato. Se o usuário clicar no cabeçalho da coluna Postal_Code, a grade é reordenada e exibida em ordem por código postal.
