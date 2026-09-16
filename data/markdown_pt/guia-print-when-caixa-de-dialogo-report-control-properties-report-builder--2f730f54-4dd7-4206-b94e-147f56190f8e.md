# Guia Print When, caixa de diálogo Report Control Properties (Report Builder)

Permite definir opções que suprimem a renderização da saída de controles de relatório sob várias condições.

> **Observação:** Esta guia substitui a funcionalidade da caixa de diálogo Print When nativa do Visual FoxPro quando o Report Builder está ativo.
 - How to: Suppress Repeated Values for Report Controls
- How to: Suppress Blank Lines in Report Controls
- How to: Specify Conditional Output for Report Controls

# Imprimir valores repetidos

Especifica se o mecanismo de relatório rastreia alterações entre valores sucessivos da saída do controle de relatório e renderiza somente quando o valor mudar.
 **Yes**
Renderiza a saída do controle sempre que a banda é processada pelo mecanismo de relatório.
**No**
Renderiza a saída do controle somente se o valor for diferente da última vez que a saída do controle foi avaliada.

# Também imprimir

Especifica condições adicionais para repetir valores de controles de relatório.
 **In first whole band of a new page/column**
Especifica que a saída do controle deve ser renderizada se a banda que o contém estiver sendo renderizada pela primeira vez em uma nova página ou coluna, substituindo a configuração de Print repeated values. Para obter mais informações, consulte Working with Report Bands.
**When this data group expression changes**
Especifica que a saída do controle deve ser renderizada se uma expressão de grupo de dados específica for avaliada para um valor diferente, substituindo a configuração de Print repeated values. Disponível somente quando pelo menos um grupo de dados existe no layout do relatório. Para obter mais informações, consulte Working with Report Data Groups.
**When band content overflows to new page/column**
Especifica que a saída do controle de relatório seja renderizada quando a banda que o contém transbordar para uma nova página ou coluna.

# Opções adicionais

As opções adicionais a seguir permitem suprimir linhas em branco e controlar a saída de controles de relatório e dados em controles de relatório.
 **Remove line if blank**
Especifica que o mecanismo de relatório pode contrair a banda de relatório verticalmente se a avaliação do controle de relatório resultar em nenhum conteúdo renderizável, e nenhum outro controle renderizável ocupar o espaço vazio em qualquer lado do controle.
**Print only when expression is true**
Especifica uma expressão lógica que o mecanismo de relatório avalia para decidir se renderiza a saída do controle de relatório.

> **Observação:** Quando você adiciona uma expressão à caixa Print only when expression is true, todas as outras opções na caixa de diálogo Print When ficam indisponíveis, exceto a caixa Remove line if blank.
