# Função BINDEVENT( )

Fornece a capacidade de executar código do usuário (um método de objeto) quando um evento ocorre.

Com a primeira forma da sintaxe abaixo, você pode usar BINDEVENT( ) para vincular eventos, propriedades ou métodos de objetos nativos do Visual FoxPro a outros objetos do Visual FoxPro.

Com a segunda variação de sintaxe abaixo, você pode vincular a eventos de mensagem do Windows (Win Msg).

> **Observação:** Se desejar vincular a eventos de objetos Component Object Model (COM), use a função EVENTHANDLER( ).

```foxpro
BINDEVENT(oEventSource, cEvent, oEventHandler, cDelegate [, nFlags])
```

```foxpro
BINDEVENT(hWnd | 0, nMessage, oEventHandler, cDelegate [, nFlags])
```

#### Parâmetros
 **oEventSource**
Especifica a origem do evento, que deve ser um objeto válido do Visual FoxPro.
**hWnd**
Especifica o identificador inteiro da janela que recebe mensagens do Windows. Se um valor 0 for passado, o evento especificado ( nMessage ) é capturado para todas as janelas. Você pode usar a propriedade hWnd (Visual FoxPro) para vincular mensagens do Windows (eventos) recebidas por _VFP, _SCREEN e formulário instanciado. Controles ActiveX também têm uma propriedade hWnd
**cEvent**
Especifica o nome do evento, método ou propriedade que deseja vincular.
**nMessage**
Especifica uma mensagem válida do Windows que é capturada. Consulte o MSDN (Microsoft Developer Network) para obter informações sobre mensagens do Windows.
**oEventHandler**
Especifica o objeto, que deve ser um objeto válido do Visual FoxPro, que trata o evento.
**cDelegate**
Especifica o método, ou "delegate", que trata o evento para oEventHandler . O método delegate deve ter os mesmos parâmetros que o evento especificado em cEvent . Você pode chamar a função AEVENTS( ) para recuperar uma referência de objeto à origem do evento. Se o método delegate não tiver parâmetros suficientes para tratar os passados pelo evento, o Visual FoxPro gera um erro. Ao capturar eventos de mensagem do Windows (Win Msg), o método cDelegate deve incluir uma instrução PARAMETERS para aceitar quatro parâmetros que são passados ao método. O formato dos parâmetros é idêntico ao formato da função Windows WindowProc. Consulte o MSDN (Microsoft Developer Network) para obter informações sobre a função Windows WindowProc. O método deve retornar um valor inteiro.
**nFlags**
Especifica um sinalizador de bit aditivo que você pode definir para a operação de vinculação de eventos. O parâmetro nFlags é ignorado quando uma vinculação de evento de mensagem do Windows é criada. nFlags Bits Tipo de evento Descrição 0 000 Objeto FoxPro Chama o código delegate antes do código do evento. (Padrão) 1 001 Objeto FoxPro Chama o código do evento antes do código delegate. 2 010 Objeto FoxPro Não aciona o evento (chama o código delegate) por chamada simples de método. 3 011 Objeto FoxPro Chama o código do evento antes do código delegate. Não aciona o evento (chama o código delegate) quando ocorrem chamadas simples de método. 4 100 Mensagem do Windows Impede a recursão de eventos semelhantes enquanto o código de evento do usuário está em execução. A tabela a seguir mostra se um evento é acionado quando o Bit 1 está desligado ou ligado. Acionamento de evento DESLIGADO (Padrão) LIGADO Interativo SIM SIM Programático SIM NÃO RAISEEVENT( ) SIM SIM

# Valor de retorno

Tipo de dados Numeric. BINDEVENT( ) retorna o número de vinculações para o evento do objeto.

BINDEVENT( ) sempre retorna 1 quando uma vinculação de evento de mensagem do Windows é criada. Nenhuma detecção de erro é executada; portanto, se valores hWnd e nMessage inválidos são especificados, 1 ainda é retornado e a vinculação permanece em vigor até ser liberada.

# Observações

Você pode vincular a qualquer evento, propriedade ou método válido de objeto do Visual FoxPro, incluindo os métodos Access e Assign. No entanto, o evento e os métodos delegate devem ser membros públicos da classe, não protegidos ou ocultos.

Você não pode vincular a um evento com parâmetros passados por referência. Embora chamar BINDEVENT( ) tenha sucesso, acionar o evento, por exemplo, usando RAISEEVENT( ), falha.

Ao vincular a uma propriedade, você deve vinculá-la diretamente e não ao método Assign. Se vincular diretamente ao método Assign, esteja ciente de que os métodos Access e Assign são marcados como Protected e não são visíveis exceto dentro da classe.

> **Observação:** Se você vincular a uma propriedade que tem um método Assign, o método delegate pode ser acionado duas vezes. A primeira vez é quando a chamada de atribuição da propriedade é feita. A segunda vez é quando a propriedade é realmente definida, dentro do método Assign, para o parâmetro que é passado. O método delegate deve estar ciente dessa possibilidade.

As regras normais de herança se aplicam. Se o método delegate não contém nenhum código, o Visual FoxPro percorre a hierarquia pai.

Um manipulador de eventos é chamado quando um evento ocorre ou se é chamado como um método. Chamar o evento como um método aciona o evento, a menos que você especifique um valor nFlags de 2 ou 3.

Por padrão, o Visual FoxPro chama o método delegate antes do evento. No entanto, você pode alterar o comportamento padrão usando uma configuração nFlags.

Se você especificar uma propriedade como o evento que deseja vincular, o Visual FoxPro vincula essa propriedade a um método Assign implícito. Quando o valor dessa propriedade muda, o Visual FoxPro aciona um evento.

Se um parâmetro inválido for passado, o Visual FoxPro gera o erro "Function argument value, type, or count is invalid." No entanto, se ocorrer um problema durante a operação de vinculação, o Visual FoxPro não gera um erro. Você pode recuperar o valor de retorno de BINDEVENT( ) para verificar o número de vinculações.

Certos eventos de controle, como GotFocus, LostFocus, InteractiveChange e ProgrammaticChange, não funcionam se o segundo bit do parâmetro nFlags estiver definido, por exemplo, nFlags definido como 2. Esses eventos são tratados como chamadas de método internamente pelo Visual FoxPro, embora sejam considerados eventos. O mesmo comportamento se aplica ao método Refresh de um objeto em um formulário que é chamado quando o método Refresh do formulário é chamado. Certos eventos, como When e Valid, exigem código no evento para que ocorra.

BINDEVENT( ) não oferece suporte direto à propriedade Value porque ela é tratada pelo Visual FoxPro de maneira especial. Você deve usar os eventos InteractiveChange e ProgrammaticChange em vez disso. Além disso, a propriedade ActivePage não é suportada.

Se o evento original contém um comando NODEFAULT, o Visual FoxPro ainda processa o evento porque é possível que o método delegate seja chamado antes do evento. NODEFAULT se aplica somente a eventos nativos do Visual FoxPro.

Se você fizer uma chamada BINDEVENT( ) duplicada exata, o Visual FoxPro desconsidera a chamada, mas ainda retorna o número de vinculações para o evento do objeto. Se você alterar a configuração nFlags, pode chamar BINDEVENT( ) para revincular o evento.

Ao vincular a eventos de mensagem do Windows (Win Msg), somente um par hWnd para mensagem do Windows pode existir. Você pode passar um valor hWnd de 0 se desejar vincular todas as janelas ao mesmo evento de mensagem do Windows. Uma vinculação de evento de mensagem do Windows pode ser liberada com a função UNBINDEVENTS( ) e os comandos CLEAR. Além disso, se o objeto manipulador de eventos especificado com o parâmetro oEventHandler não existir mais, a vinculação é liberada quando sua mensagem do Windows ocorre.

Com uma vinculação de evento de mensagem do Windows, seu código de usuário será executado sempre que um evento ocorrer, incluindo cenários em que uma caixa de diálogo modal é exibida. Isso ocorre porque o Window Procedure deve sempre processar a mensagem e retornar. Como é possível que ocorra recursão com um evento enquanto seu código de usuário está em execução, você pode querer especificar um valor nFlags de 4 para impedir que isso aconteça.

> **Observação:** Uma vinculação de evento de mensagem do Windows deve ser usada com cuidado, pois seu código de usuário está vinculado a eventos acionados pelo sistema operacional Windows e esses eventos podem ocorrer em momentos em que você não os espera.

# Exemplo

O exemplo a seguir mostra como você pode manter o Class Browser posicionado no lado direito da área de trabalho do Visual FoxPro, independentemente de como a área de trabalho é redimensionada. BINDEVENT( ) associa o evento Resize da variável de sistema _SCREEN, ou área de trabalho do Visual FoxPro, com `oHandler`, que usa `myresize` como seu delegate. O código para `myresize` é executado quando o evento Resize é acionado.

```foxpro
PUBLIC oHandler
oHandler=NEWOBJECT("myhandler")
DO (_browser)
BINDEVENT(_SCREEN,"Resize",oHandler,"myresize")
DEFINE CLASS myhandler AS Session
   PROCEDURE myresize
      IF ISNULL(_obrowser) THEN
         UNBINDEVENTS(THIS)
      ELSE
         _obrowser.left = _SCREEN.Width - _obrowser.width
      ENDIF
   RETURN
ENDDEFINE
```
