# Objetos no Visual FoxPro

Quando um objeto é criado a partir de uma classe, ele existe como instância dessa classe. A classe descreve os dados, características e funcionalidades dos objetos. No Visual FoxPro, eles podem ser formulários, conjuntos de formulários, controles etc. Também possuem propriedades e métodos e detectam e respondem a eventos. Suas propriedades, métodos e eventos são definidos pela classe de origem.

Crie objetos com o Form Designer ou CREATEOBJECT( ). Consulte Criação de objetos a partir de classes, Form Designer ou Função CREATEOBJECT( ).

# Recursos dos objetos

Objetos possuem:
 - Propriedades de objetos
- Métodos de objetos
- Eventos de objetos

### Propriedades de objetos

Um objeto possui propriedades ou atributos específicos. Seus valores podem ser definidos e modificados para determinar suas características, em tempo de design ou execução, conforme a propriedade.

Por exemplo, um computador pode ter cor, tamanho, forma, localização e estado. Da mesma forma, um CheckBox inclui:
 - Caption
- Enabled
- Top
- Visible

Consulte Como: definir propriedades de objetos e Como: adicionar propriedades a classes.

### Métodos de objetos

Métodos contêm procedimentos para executar tarefas específicas. Diferem dos procedimentos padrão porque estão vinculados ao objeto e são chamados de forma diferente.

Um CheckBox inclui:
 - Drag
- Move
- ReadExpression
- Refresh

Métodos podem ser incluídos em eventos ou usados independentemente. Fora de eventos, devem ser chamados explicitamente por código. Também podem ser criados e estendidos.

### Eventos de objetos

Um objeto pode detectar e responder a ações específicas chamadas eventos. Um evento é uma atividade predeterminada que ocorre por ação do usuário ou sistema. Exemplos incluem clicar ou mover o mouse, pressionar teclas, inicializar um objeto e encontrar uma linha que gera erro.

Um CheckBox inclui:
 - MouseEnter
- MouseUp
- MouseDown
- RightClick

Eventos podem ter métodos associados. Código no evento Click é executado quando Click ocorre. Embora amplo, o conjunto de eventos é fixo; não é possível criar novos eventos.

Para obter mais informações, consulte Eventos no Visual FoxPro.
