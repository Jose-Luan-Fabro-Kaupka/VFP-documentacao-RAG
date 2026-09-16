# Como: definir estiramento de controles de relatório

Você pode especificar que controles em relatórios e etiquetas estiquem, ou expandam e contraiam automaticamente para acomodar a saída que geram. Por exemplo, um controle Field que contém uma expressão de campo memo pode avaliar quantidades variáveis de texto de registro para registro. Portanto, você pode definir o controle para esticar conforme a quantidade de informações que contém. Se você estiver usando uma forma como borda ao redor de um ou mais controles de expressão de campo, também pode especificar que a forma estique para acomodar o tamanho variável dos controles que abrange.

Controles que podem esticar podem afetar a posição de outros controles que aparecem abaixo deles no layout. Você pode definir os outros controles para flutuar, ou ajustar a posição automaticamente conforme mudanças no tamanho dos controles acima deles. Para obter mais informações sobre ajustar automaticamente a posição de controles de relatório, consulte Como: ajustar a posição de controles de relatório.

A ilustração a seguir mostra como controles de relatório de estiramento e flutuação funcionam.

As seções a seguir contêm informações sobre trabalhar com controles de estiramento:
 - Especificando estiramento para controles de relatório
- Exibindo bordas para controles esticáveis

# Especificando estiramento para controles de relatório

Os seguintes tipos de controle podem ser definidos para esticar:
 - Field/Expression
- Linha vertical
- Retângulo / Retângulo arredondado

Para controles Line, Rectangle e Rounded Rectangle, você pode especificar que estiquem em relação à altura da banda que os contém ou, se agrupados, em relação ao maior controle no grupo.

> **Cuidado:** Você deve definir flutuação para controles que estão posicionados abaixo de controles que esticam; caso contrário, a saída gerada por controles que esticam pode sobrepor a saída em controles que aparecem abaixo deles. A saída de controles também pode ser sobrescrita no layout da página quando qualquer uma das seguintes condições ocorrer:
 - Você posiciona um controle que permanece fixo em relação à parte inferior da banda e posiciona um controle de estiramento abaixo dele que permanece fixo em relação à parte superior da banda.
- Você posiciona um controle que permanece fixo em relação à parte superior da banda e posiciona um controle de estiramento acima dele que permanece fixo em relação à parte superior da banda.

### Para especificar estiramento para um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório desejado. A caixa de diálogo de propriedades do controle de relatório abre. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER .
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia General se ela não estiver selecionada.
- Na guia General, escolha uma das seguintes opções: Para controles Field, clique em Stretch with overflow . Para controles Rectangle, Rounded Rectangle ou Line vertical, na área Stretch downwards, clique na configuração de estiramento desejada.

Para obter mais informações, consulte Guia General, Caixa de diálogo Propriedades do controle de relatório (Report Builder).

Para exemplos, consulte o relatório de exemplo Wrapping.frx no diretório ...\Samples\Solution\Reports do Visual FoxPro.

### Para posicionar um controle de relatório de estiramento abaixo de outro
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, posicione um controle de relatório abaixo do outro.
- Clique duas vezes no controle de relatório que aparece acima do outro controle. A caixa de diálogo de propriedades do controle de relatório abre. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER .
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia General se ela não estiver selecionada.
- Na área Object position, clique em Fix relative to top of band , e então OK .
- Clique duas vezes no controle de relatório que aparece abaixo do outro controle. A caixa de diálogo de propriedades do controle de relatório abre.
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia General se ela não estiver selecionada.
- Na área Object position na guia General, clique em Float , e então OK .

Para obter mais informações, consulte Guia General, Caixa de diálogo Propriedades do controle de relatório (Report Builder).

# Exibindo bordas para controles esticáveis

Você pode usar um controle Shape como borda ao redor de um controle de relatório e especificar que ele estique com o controle.

### Para exibir uma borda para um controle de estiramento
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, desenhe uma borda arrastando um controle de relatório Rectangle ou Rounded Rectangle ao redor do controle de relatório que estica.
- Clique duas vezes no controle de relatório Rectangle ou Rounded Rectangle. A caixa de diálogo Rectangle Properties do controle de relatório abre. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Rectangle/Line ou Round Rectangle é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER , Caixa de diálogo Rectangle/Line e Caixa de diálogo Round Rectangle .
- Na caixa de diálogo Rectangle Properties, clique na guia General se ela não estiver selecionada.
- Na área Stretch downwards, clique em Stretch relative to tallest object in group , e então OK .
- Arraste uma caixa de seleção ao redor do controle Rectangle ou Rounded Rectangle.
- No menu Format, clique em Group .

Agora você pode manipular ambos os controles permanentemente como uma única unidade. O controle Rectangle ou Rounded Rectangle estica quando o controle de relatório dentro de seus limites estica.

Para obter mais informações, consulte Como: adicionar formas a relatórios e Como: agrupar controles de relatório.
