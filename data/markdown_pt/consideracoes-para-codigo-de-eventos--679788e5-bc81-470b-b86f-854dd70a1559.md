# Considerações para código de eventos

Ao adicionar código a eventos, lembre-se das seguintes considerações:
 - O conjunto de eventos para classes básicas do Visual FoxPro é fixo e não pode ser estendido.
- Toda classe reconhece um conjunto fixo de eventos padrão, que inclui no mínimo os eventos Init, Destroy e Error.
- Contêineres não processam eventos associados aos controles que contêm.
- Se nenhum código de evento estiver associado a um controle, o Visual FoxPro verifica se existe código para o evento mais acima na hierarquia de classes do controle.
- A sequência de eventos pode afetar o local onde você adiciona código.

As seções a seguir contêm mais informações sobre as três últimas considerações.

# Eventos de objetos em contêineres

Cada objeto, mesmo aqueles em contêineres, recebe seus eventos independentemente. Por exemplo, suponha que um formulário contenha um botão de comando. Quando o usuário clica no botão de comando, apenas o evento Click do botão de comando é acionado, não o evento Click do formulário. Portanto, se existir código para o evento Click de um formulário, mas nenhum código existir para o evento Click do botão de comando, nada acontece quando o usuário clica no botão.

Essa consideração também se aplica a controles de grade. Uma grade contém colunas, que contêm cabeçalhos e controles. Quando um evento ocorre para um objeto interno, apenas o objeto associado ao evento reconhece o evento. O contêiner de nível superior não reconhece o evento.

> **Observação:** Existe uma exceção a essa regra. Se existir código de evento para um option button group ou um command button group, mas nenhum código de evento existir para o evento de uma opção ou botão específico no grupo, o código de evento do grupo é executado quando o evento da opção ou botão específico ocorre.

# Eventos de controles de classes definidas pelo usuário

Quando um evento ocorre para um controle baseado em uma classe definida pelo usuário, o Visual FoxPro verifica o controle em busca de código de evento. Se existir código no procedimento de evento do controle, o Visual FoxPro o executa. No entanto, se nenhum código existir no procedimento de evento do controle, o Visual FoxPro pesquisa o próximo nível acima na hierarquia de classes do controle em busca de código associado a esse evento. Se o Visual FoxPro encontrar código para o evento, ele executa esse código e não continua pesquisando mais acima na hierarquia.

# Considerações sobre a sequência de eventos

Ao determinar onde adicionar código de evento, lembre-se das seguintes considerações:
 - O evento Init de um formulário ocorre depois que todos os eventos Init dos controles no formulário ocorrem. Portanto, você pode incluir código no evento Init do formulário para manipular qualquer um dos controles no formulário antes que o formulário seja exibido.
- Se você quiser executar código quando o valor de uma caixa de listagem, combo box ou caixa de seleção mudar, adicione o código ao evento InteractiveChange do controle em vez do evento Click. O evento Click pode não ocorrer ou pode ser chamado mesmo que o valor não mude.
- Quando você arrasta um controle, outros eventos de mouse são suspensos. Por exemplo, os eventos MouseUp e MouseMove não ocorrem durante uma operação de arrastar.
- Os eventos Valid e When retornam um valor com True (.T.) como padrão. Se o código retornar False (.F.) ou 0 no evento When, o controle não pode receber foco. Se o código retornar False (.F.) ou 0 no evento Valid, o foco não pode sair do controle.
