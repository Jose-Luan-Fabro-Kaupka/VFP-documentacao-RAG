# Função RAISEEVENT( )

Você pode usar RAISEEVENT( ) para disparar, ou acionar, um evento a partir de um método personalizado. Embora RAISEEVENT( ) se aplique principalmente a métodos personalizados, você pode usá-la para disparar eventos e métodos nativos.

```foxpro
RAISEEVENT( oEventSource, cEvent [, eParm1...] )
```

#### Parâmetros
 **oEventSource**
Especifica a fonte do evento, que deve ser um objeto Visual FoxPro válido.
**cEvent**
Especifica o nome do evento, método ou propriedade que você deseja disparar.
**eParm1...**
Especifica um ou mais parâmetros a passar se o método tiver parâmetros.

# Valor de retorno

Tipo de dados Logical. RAISEEVENT( ) sempre retorna True (.T.).

# Observações

O Visual FoxPro dispara automaticamente eventos para métodos personalizados que estão vinculados a objetos usando BINDEVENT( ) se os métodos são chamados diretamente. Por exemplo, o seguinte código não dispara um evento:

```foxpro
oForm.GetMyData(cData)
```

Em vez disso, para disparar um evento para um método personalizado, você precisa fazer a seguinte chamada:

```foxpro
RAISEEVENT( oForm, "GetMyData", cData )
```

Você também pode alterar esse comportamento usando BINDEVENT( ) com nFlags definido como 2 ou 3.

O evento que você deseja disparar deve estar marcado como Public, não Hidden ou Protected.

Se você usar RAISEEVENT( ) em uma propriedade, o Visual FoxPro define a propriedade para ela mesma. O exemplo a seguir define a propriedade Caption para _SCREEN para o valor atual de Caption:

```foxpro
RAISEEVENT( _SCREEN, "Caption" )
```

Disparar um evento falha se você vincular a um evento, por exemplo, usando BINDEVENT( ), que tenha parâmetros passados por referência.

O Visual FoxPro ignora chamadas recursivas de RAISEEVENT( ) a um evento a partir do mesmo evento disparado.

# Exemplo

Ativar um formulário ou usar `Form1.Show` dispara o evento Activate do formulário. No entanto, chamar o evento Activate diretamente usando uma chamada como `Form1.Activate` não dispara o evento Activate. O exemplo a seguir mostra como você pode usar RAISEEVENT( ) para disparar o evento Activate:

```foxpro
RAISEEVENT( Form1, "Activate" )
```
