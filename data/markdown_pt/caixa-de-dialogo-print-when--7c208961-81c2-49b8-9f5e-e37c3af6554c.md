# Caixa de diálogo Print When

Permite definir opções para condições que controlam a saída em controles de relatório.

> **Observação:** Dependendo da configuração da variável de sistema _REPORTBUILDER, esta caixa de diálogo pode ser substituída por uma interface de usuário alternativa. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER.

# Print repeated values

Especifica se o mecanismo de relatório rastreia alterações entre valores sucessivos da saída do controle de relatório e renderiza apenas quando o valor mudar.
 **Yes**
Renderiza a saída do controle sempre que a faixa é processada pelo mecanismo de relatório.
**No**
Renderiza a saída do controle somente se o valor for diferente da última vez em que a saída do controle foi avaliada.

# Also print

Especifica condições adicionais para repetir valores de controles de relatório.
 **In first whole band of new page/column**
Especifica que a saída do controle deve ser renderizada se a faixa que o contém estiver sendo renderizada pela primeira vez em uma nova página ou coluna, substituindo a configuração de Print repeated values. Para obter mais informações, consulte Trabalhando com faixas de relatório.
**When this group changes**
Especifica que a saída do controle deve ser renderizada se uma expressão de grupo de dados específica for avaliada com um valor diferente, substituindo a configuração de Print repeated values. Observação Disponível somente quando pelo menos um grupo de dados existe no layout da página. Para obter mais informações, consulte Trabalhando com grupos de dados de relatório.
**When detail overflows to new page/column**
Especifica que a saída do controle de relatório seja renderizada quando a faixa que o contém transbordar para uma nova página ou coluna.

# Additional options

As opções adicionais a seguir permitem suprimir linhas em branco e controlar a saída para controles de relatório e dados em controles de relatório.
 **Remove line if blank**
Especifica que o mecanismo de relatório pode contrair a faixa de relatório verticalmente se a avaliação do controle de relatório resultar em nenhum conteúdo renderizável, e nenhum outro controle renderizável ocupar o espaço vazio em qualquer lado do controle.
**Print only when expression is true**
Especifica uma expressão lógica que o mecanismo de relatório avalia para decidir se renderiza a saída do controle de relatório. Observação Quando você adiciona uma expressão à caixa Print only when expression is true, todas as outras opções na caixa de diálogo Print When ficam indisponíveis, exceto a caixa Remove line if blank.
