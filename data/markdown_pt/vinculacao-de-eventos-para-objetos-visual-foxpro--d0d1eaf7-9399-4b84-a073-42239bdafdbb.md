# Vinculação de eventos para objetos Visual FoxPro

Você pode usar vinculação de eventos para acionar eventos, propriedades ou métodos de objetos nativos do Visual FoxPro a partir de outros objetos Visual FoxPro usando as seguintes funções:
 - BINDEVENT( ) Associa um evento de um objeto nativo Visual FoxPro ao método ou evento de outro objeto Visual FoxPro.
- UNBINDEVENTS( ) Desanexa eventos previamente vinculados a objetos Visual FoxPro.
- RAISEEVENT( ) Aciona, ou dispara, eventos para métodos personalizados definidos pelo usuário. Você também pode usar RAISEEVENT( ) para eventos e métodos nativos.
- AEVENTS( ) Recupera informações sobre o número de vinculações de eventos existentes.

Para um exemplo de solução demonstrando vinculação de eventos, acionamento programático de eventos, desvinculação de eventos e recuperação de eventos, consulte Bind, Raise, Unbind, and Retrieve Events Sample.

Para obter informações sobre vinculação de eventos de objetos Component Object Model (COM), consulte Event Binding for COM Objects e Função EVENTHANDLER( ).

# Vincular um evento

Você pode usar a função BINDEVENT( ) para anexar, ou vincular, um evento, método ou propriedade de um objeto Visual FoxPro, ou fonte de evento, ao método ou evento de outro objeto Visual FoxPro, ou manipulador de evento. O método que trata o evento atua como um "delegado" para o manipulador de evento.

Você pode vincular a qualquer método ou evento válido de objeto Visual FoxPro, incluindo os métodos Access e Assign. No entanto, tanto a fonte de evento quanto o manipulador de evento devem ser objetos Visual FoxPro válidos. Você não pode usar objetos COM ou vincular a métodos de objetos em coleções referenciadas pela variável de sistema _VFP porque essas coleções também passam pelo COM.

> **Observação:** Ao especificar objetos para vinculação de eventos, certifique-se de que estejam totalmente instanciados. Não vincule eventos, métodos ou propriedades a um objeto em seu evento Load ou Init porque o objeto pode ainda não estar totalmente instanciado e pode fazer a operação de vinculação falhar.

Você pode usar o mesmo objeto como fonte de evento e manipulador de evento. O exemplo a seguir mostra como `Form1` atua como fonte e manipulador:

```foxpro
BINDEVENT( Form1, "Resize", Form1, "myresize1" )
```

Você pode usar objetos diferentes da mesma classe como fonte de evento e manipulador. No entanto, o evento de um objeto usado como fonte de evento e manipulador não pode ser o mesmo que o método delegado.

Você pode vincular vários manipuladores de evento à mesma fonte de evento e evento em um ato referido como "multicast". Se vários manipuladores existirem para o mesmo evento, os eventos ocorrem na ordem primeiro a entrar, primeiro a sair (FIFO).

Você pode vincular vários métodos delegados de um manipulador de evento a uma fonte de evento e evento específicos. Por exemplo:

```foxpro
BINDEVENT( Form1, "Resize", oHandler, "myresize1" )
BINDEVENT( Form1, "Resize", oHandler, "myresize2" )
```

Você não pode vincular a um evento com parâmetros passados por referência. Embora chamar BINDEVENT( ) tenha sucesso, acionar o evento, por exemplo, usando RAISEEVENT( ), falha.

O Visual FoxPro não suporta vinculação de eventos em designers como os designers de formulário e classe, embora você possa obter referências de objeto usando as funções ASELOBJ( ) ou SYS(1270).

Para obter mais informações, consulte Função BINDEVENT( ), Função ASELOBJ( ) e SYS(1270) - Object Location. Para um exemplo, consulte Bind, Raise, Unbind, and Retrieve Events Sample.

# Desvincular um evento

Você pode usar a função UNBINDEVENTS( ) para desanexar eventos, métodos e propriedades que foram vinculados usando a função BINDEVENT( ) de objetos nativos Visual FoxPro. UNBINDEVENTS( ) retorna o número de eventos que desvincula se tiver sucesso. Você pode especificar uma fonte de evento de objeto Visual FoxPro ou uma referência de objeto, que pode ser usada como fonte de evento ou manipulador de evento.

Para obter mais informações, consulte Função UNBINDEVENTS( ).

# Acionar um evento

Você pode usar a função RAISEEVENT( ) para acionar, ou disparar, eventos para métodos personalizados e nativos. Chamar métodos diretamente não faz eventos ocorrerem, a menos que você defina os sinalizadores apropriados ao usar BINDEVENT( ) para anexar eventos a outros objetos. Portanto, você precisa de RAISEEVENT( ) para acionar esses eventos.

Para obter mais informações, consulte Função RAISEEVENT( ).

# Recuperar informações de vinculação de eventos

Você pode usar a função AEVENTS( ) para recuperar o número de eventos Visual FoxPro que estão atualmente vinculados a objetos Visual FoxPro. O Visual FoxPro armazena as informações em um array. Dependendo dos parâmetros que você passar, AEVENTS( ) retorna um array de um elemento contendo uma referência de objeto à fonte de evento ou um array que representa cada vinculação de evento existente como uma linha e contém informações sobre a vinculação em cinco colunas.

Para obter mais informações, consulte Função AEVENTS( ).
