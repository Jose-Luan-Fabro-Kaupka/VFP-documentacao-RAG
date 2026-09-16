# Acelerando a recuperação de dados

Você pode acelerar a recuperação de dados gerenciando o número de linhas obtidas durante a busca progressiva, controlando o tamanho da busca e usando a busca adiada de campos Memo.

Também é possível usar a propriedade de exibição UseMemoSize para retornar campos de caracteres como campos Memo e depois desativar FetchMemo, permitindo que o aplicativo busque seletivamente esses campos de caracteres convertidos em campos Memo.

# Usando a busca progressiva

Quando você consulta uma fonte de dados remota, o Visual FoxPro recupera linhas completas de dados e cria um cursor do Visual FoxPro. Para acelerar a recuperação de dados remotos, o Visual FoxPro usa a busca progressiva de cursores de exibição e de cursores criados de forma assíncrona com passagem direta SQL. Em vez de exigir que você ou seu aplicativo aguardem a recuperação de todo o conjunto de dados, o Visual FoxPro executa uma consulta e busca apenas um pequeno subconjunto das linhas do conjunto de resultados no cursor local. Por padrão, esse subconjunto tem 100 linhas.

> **Observação:** Instruções síncronas de passagem direta SQL não usam busca progressiva. Todo o conjunto de resultados solicitado por uma instrução SQLEXEC( ) é recuperado antes que o controle retorne ao aplicativo.

À medida que o Visual FoxPro recupera linhas adicionais, o cursor local passa a conter uma quantidade cada vez maior dos dados consultados. Como as linhas são recuperadas da fonte de dados em momentos diferentes, suas informações não ficam automaticamente atualizadas. Se a conexão estiver operando no modo assíncrono, o Visual FoxPro devolverá o controle a você ou ao programa assim que buscar o primeiro subconjunto de dados. Durante o tempo ocioso, o Visual FoxPro busca em segundo plano as linhas restantes dos dados consultados, um subconjunto por vez, para o cursor local. Esse cenário permite usar no cursor os dados já obtidos sem aguardar os demais.

> **Observação:** Aumentar o número de linhas buscadas melhora o desempenho, mas reduz a capacidade de resposta da interface do usuário. Reduzir o número de linhas buscadas produz o efeito inverso.

# Buscando dados sob demanda

Você pode desativar a busca progressiva e buscar linhas somente conforme necessário usando a propriedade de banco de dados e cursor de exibição FetchAsNeeded. Isso pode tornar a recuperação de dados mais eficiente para exibições remotas ou que retornam conjuntos de resultados extremamente grandes.

Por padrão, a propriedade FetchAsNeeded é definida como false (.F.), o que significa que a busca progressiva é usada. Quando FetchAsNeeded é definida como true (.T.), as linhas são buscadas somente quando necessárias. Quando FetchAsNeeded está definida como true, não é possível executar uma atualização até que você conclua a busca, chame a função SQLCANCEL( ) no identificador da conexão atual ou feche a exibição.

Para observar o impacto do uso de FetchAsNeeded, defina essa propriedade como .T. em uma exibição que recupere um conjunto de resultados grande, abra uma janela de navegação para a exibição e role para baixo. A barra de status será atualizada para mostrar o número de linhas recuperadas conforme você percorre a janela.

### Controlando a busca do cursor

Para buscar o cursor inteiro, você pode emitir o comando GO | GOTO ou qualquer comando que exija acesso a todo o conjunto de dados.

> **Dica:** Embora seja possível usar o comando GOTO BOTTOM para buscar o cursor inteiro, em geral é mais eficiente criar uma exibição parametrizada que busque apenas uma linha por vez e execute uma nova consulta quando o usuário mudar de registro. Para obter mais informações sobre a criação de exibições de alto desempenho, consulte Como: otimizar o desempenho de exibições.

Os programas não fornecem processamento de loop ocioso. Para buscar cursores de exibição programaticamente, use os comandos GO nRecordNumber ou GOTO BOTTOM. Para buscar cursores criados com passagem direta SQL no modo assíncrono, chame a função assíncrona de passagem direta SQL uma vez para cada subconjunto de linhas.

### Cancelando uma instrução SQLEXEC( )

Você pode usar a função SQLCANCEL( ) para cancelar uma instrução SQLEXEC( ) ou uma exibição a qualquer momento. Contudo, se o servidor tiver concluído a criação do conjunto de resultados remoto e o Visual FoxPro tiver começado a buscá-lo para um cursor local, a função SQLCANCEL( ) cancelará a instrução SQLEXEC( ) e manterá o cursor local. Para excluir o cursor local, você pode emitir o comando USE, que fecha o cursor e cancela a busca.

O comando USE não cancelará uma instrução SQLEXEC( ) se ela ainda não tiver criado um cursor local. Para determinar se o Visual FoxPro criou um cursor local, chame a função USED( ).

# Controlando o tamanho da busca

Você controla o número de linhas buscadas de uma só vez pelo aplicativo em um servidor remoto definindo a propriedade FetchSize da exibição. FetchSize especifica quantos registros são buscados por vez do servidor remoto para o cursor local, por meio de busca progressiva ou de chamadas assíncronas de passagem direta SQL. O valor padrão é 100 linhas.

### Para controlar o número de registros buscados por vez em uma exibição
- No View Designer, escolha Advanced Options no menu Query. Na área Data Fetching da caixa de diálogo Advanced Options, use o controle giratório para definir um valor em Number of Records to Fetch at a time. -ou-
- Defina a propriedade FetchSize com a função DBSETPROP( ) para definir o tamanho da busca na definição da exibição. -ou-
- Defina a propriedade FetchSize com a função CURSORSETPROP( ) para definir o tamanho da busca no cursor de exibição ativo. Por exemplo, o código a seguir define que a exibição Customer_remote_view busque progressivamente 50 linhas por vez: ? DBSETPROP('Customer_remote_view', 'View', 'FetchSize', 50)

# Usando a busca adiada de campos Memo

Um aplicativo bem projetado costuma usar a busca adiada de campos Memo para acelerar o download de conjuntos de resultados que contêm campos Memo ou General. Isso significa que o conteúdo desses campos não é baixado automaticamente com o conjunto de resultados. Em vez disso, os demais campos da linha são baixados rapidamente, e o conteúdo dos campos Memo e General só é buscado quando você o solicita ao abrir o campo correspondente. A busca adiada oferece o download mais rápido das linhas e permite que o conteúdo dos campos Memo ou General, que pode ser muito grande, seja buscado somente quando necessário para o usuário.

Por exemplo, seu formulário pode incluir um campo General que exibe uma imagem. Para melhorar o desempenho, use a busca adiada de campos Memo para impedir o download da imagem até que o usuário escolha um botão "Preview" no formulário. O código por trás do botão "Preview" busca então o campo General e o exibe no formulário.

Para controlar a busca adiada de campos Memo, use a propriedade FetchMemo da exibição ou do cursor. FetchMemo especifica se o conteúdo dos campos Memo ou General será buscado quando a linha for baixada. O valor padrão é true (.T.), o que significa que os campos Memo e General são baixados automaticamente. Se os dados contiverem grandes quantidades de dados de campos Memo ou General, você poderá perceber um melhor desempenho ao definir FetchMemo como false (.F.).

> **Observação:** A exibição deve ser atualizável para que a busca adiada de campos Memo funcione, pois o Visual FoxPro usa os valores dos campos-chave estabelecidos pelas propriedades de atualização para localizar a linha de origem no servidor ao recuperar o campo Memo ou General. Para obter informações sobre como tornar uma exibição atualizável, consulte Como: atualizar dados em uma exibição.

Use a função DBSETPROP( ) para definir a propriedade FetchMemo em uma exibição e a função CURSORSETPROP( ) para defini-la em um cursor.

# Otimizando o desempenho da busca de dados

Você pode usar as recomendações a seguir ao definir propriedades de conexão e de exibição para otimizar a busca de dados. A propriedade PacketSize da conexão é a que mais influencia o desempenho. Também é possível otimizar a busca usando conexões síncronas.

| Objeto | Propriedade | Configuração |
| --- | --- | --- |
| Conexão | PacketSize | 4K a 12K1 |
| Conexão | Asynchronous2 | .F. |
| Exibição | FetchSize3 | máximo |

1. Defina um valor maior para linhas que contenham mais dados; experimente para encontrar o melhor valor.
2. Use conexões síncronas para aumentar o desempenho em até 50%, a menos que você queira poder cancelar instruções SQL enquanto elas são executadas no servidor.
3. O efeito de FetchSize depende muito do tamanho dos registros do conjunto de resultados buscado. No modo síncrono, ela não afeta significativamente o desempenho; portanto, defina-a conforme necessário para o processamento assíncrono de passagem direta SQL e a busca progressiva de exibições. Reduzir FetchSize melhora significativamente a capacidade de resposta durante a busca progressiva de uma exibição, mas reduz a velocidade da busca. Aumentá-la melhora o desempenho da busca da exibição.

O desempenho real depende muito da configuração do sistema e dos requisitos do aplicativo.
