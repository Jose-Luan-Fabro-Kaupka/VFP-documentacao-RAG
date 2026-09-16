# Otimizando formulários e controles

Você pode obter melhorias significativas nos formulários e controles de sua aplicação otimizando seu desempenho.

Por exemplo, ao usar um data environment para um formulário ou relatório, abrir tabelas pode ser muito mais rápido do que executar os comandos USE, SET ORDER e SET RELATION no evento Load do formulário. Quando você usa o data environment, o Visual FoxPro usa chamadas de baixo nível do mecanismo para abrir as tabelas e configurar os índices e relações.

# Limitando o número de formulários em um conjunto de formulários

Use conjuntos de formulários somente quando for necessário que um grupo de formulários compartilhe uma sessão de dados privada. Quando você usa um conjunto de formulários, o Visual FoxPro cria instâncias de todos os formulários e de todos os controles em todos os formulários do conjunto de formulários, mesmo que o primeiro formulário no conjunto de formulários seja o único sendo exibido. Isso pode consumir tempo e é desnecessário se os formulários não precisam compartilhar uma sessão de dados privada. Em vez disso, você deve executar o comando DO FORM para outros formulários quando necessário.

> **Observação:** Se você usar um conjunto de formulários, obterá algum ganho de desempenho ao acessar os formulários no conjunto de formulários porque os formulários já estarão carregados, mas não visíveis.

# Carregando dinamicamente controles de página em um page frame

Page frames, como conjuntos de formulários, carregam todos os controles de cada página quando o page frame é carregado, o que pode causar um atraso perceptível quando o page frame é carregado. Em vez disso, você pode carregar dinamicamente controles de página, conforme necessário, criando uma classe a partir dos controles em cada página e carregando-os quando a página é ativada.

As etapas a seguir descrevem como carregar dinamicamente controles de página:
 - Projete seu formulário como de costume, incluindo todos os controles em todas as páginas.
- Quando seu design estiver completo, vá para a segunda página do page frame e salve os controles como uma classe.
- Abra a classe que você criou para verificar se os controles ainda estão dispostos corretamente.
- Repita as etapas 2 e 3 para a terceira e as páginas subsequentes do page frame.
- No evento Activate da segunda e das páginas subsequentes do page frame, adicione objetos e torne-os visíveis. Por exemplo, se sua classe de controles se chama cnrpage1, você adicionaria o seguinte código: IF THIS.ControlCount = 0 THIS.AddObject("cnrpage1","cnrpage1") THIS.cnrpage1.Visible = .T. ENDIF

# Vinculando dinamicamente controles a dados

Você pode reduzir o tempo de carregamento de um formulário que contém muitos controles vinculados a dados se atrasar a vinculação desses controles até que sejam necessários.

As etapas a seguir descrevem o processo para vincular controles a dados dinamicamente:
 - Coloque as tabelas e views do formulário no data environment para que sejam abertas quando o formulário carregar.
- Para cada controle vinculado, adicione código ao evento GotFocus que vincula o controle ao valor de dados quando o controle recebe foco. Por exemplo, o código a seguir vincula um controle ComboBox ao campo customer.company: * Verificar se o controle já foi vinculado. IF THIS.RecordSource = "" * Definir a origem de registro para o valor correto * e definir o tipo de origem de registro como "fields" THIS.RecordSource = "customer.company" THIS.RecordSourceType = 6 THIS.Refresh ENDIF

# Atrasando a atualização da tela

Se você precisa fazer várias alterações na tela, por exemplo, alterar os valores de vários controles de uma vez, pode reduzir o tempo total necessário para atualizar a tela atrasando a atualização da tela até que todas as alterações sejam concluídas.

Por exemplo, suponha que você deseja tornar controles visíveis ou invisíveis, alterar cores de controles ou mover registros em controles vinculados. É recomendável atrasar a pintura desses controles até depois de concluir as alterações nos controles.

As etapas a seguir descrevem o processo para atrasar a atualização da tela:
 - Defina a propriedade LockScreen do formulário como True (.T.).
- Atualize os controles conforme necessário.
- Chame o método Refresh do formulário.
- Defina a propriedade LockScreen do formulário como False (.F.).

> **Dica:** Esta técnica não proporciona aumento de desempenho ao atualizar controles individuais.

Por exemplo, o código a seguir altera as propriedades de exibição de várias propriedades de uma vez, move para um novo registro e só então atualiza a tela com novas informações. Se LockScreen não estiver definido como True, cada uma dessas operações repinta os controles afetados individualmente e reduz o desempenho da operação de atualização:

```foxpro
THISFORM.LockScreen = .T.
THISFORM.MyButton.Caption = "Save"
THISFORM.MyGrid.BackColor = RGB (255, 0, 0) && Red
SKIP IN customers
SKIP IN orders
THISFORM.Refresh
THISFORM.LockScreen = .F.
```

# Reduzindo código em métodos usados com frequência

Como o método Refresh (Visual FoxPro) e o evento Paint são chamados com frequência, você pode melhorar o desempenho em formulários reduzindo a quantidade de código nesses métodos. Da mesma forma, para acelerar o tempo de carregamento de um formulário, você pode mover código do evento Init para um evento menos usado, como Activate (Visual FoxPro), Click e GotFocus. Em seguida, use uma propriedade no controle (como Tag (Visual FoxPro) ou uma propriedade personalizada) para rastrear se o controle já executou código que só precisa ser executado uma vez.
