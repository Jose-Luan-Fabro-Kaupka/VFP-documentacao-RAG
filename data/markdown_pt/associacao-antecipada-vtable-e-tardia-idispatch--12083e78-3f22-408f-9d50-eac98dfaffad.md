# Associação antecipada (vtable) e tardia (IDispatch)

Os servidores COM do Visual FoxPro são compatíveis tanto com a associação antecipada (vtable) quanto com a interface existente de associação tardia (IDispatch), conhecidas em conjunto como suporte a interface dupla. A associação descreve como os clientes acessam propriedades e métodos de um servidor. A associação antecipada oferece benefícios de desempenho para controladores de Automação compatíveis com ela, como o Visual Basic e o Microsoft Transaction Server. Embora os servidores Visual FoxPro sejam compatíveis com ambas as interfaces, a interface usada é determinada pelo cliente.

# Associação antecipada

Se o cliente puder detectar em tempo de compilação a qual objeto pertence uma propriedade ou método, poderá resolver a referência ao objeto nesse momento. O executável compilado conterá somente o código necessário para invocar as propriedades, métodos e eventos do objeto. Isso é chamado de associação antecipada.

### Exemplo: cliente Visual FoxPro

```foxpro
LOCAL xlApp1 As Excel.Application
xlApp1 = CreateObjectEx("Excel.Application","","")
```

### Exemplo: cliente Visual Basic

```foxpro
Dim xlApp1 As Excel.Application
Set xlApp1 = New Excel.Application
```

A associação antecipada reduz drasticamente o tempo necessário para definir ou recuperar o valor de uma propriedade, pois a sobrecarga da chamada pode representar uma parte significativa do tempo total. Para chamadas de métodos, a melhoria depende da quantidade de trabalho executada pelo método. Métodos curtos, nos quais a sobrecarga da chamada é comparável ao tempo necessário para concluir a tarefa, são os mais beneficiados.

# Associação tardia

Embora a associação tardia seja a forma mais lenta de invocar propriedades e métodos de um objeto, há situações em que ela é necessária. Por exemplo, no Visual Basic, você pode escrever uma função que usa uma variável de objeto para atuar em qualquer uma de várias classes de objetos. Como não se sabe antecipadamente qual classe de objeto será atribuída à variável, ela deve ser declarada como variável de associação tardia usando o comando DIM As Object do Visual Basic. No Visual FoxPro, você usaria a função CREATEOBJECT() em vez da função CREATEOBJECTEX().

### Exemplo: cliente Visual FoxPro

```foxpro
LOCAL xlApp2 As Excel.Application
xlApp2 = CreateObject("Excel.Application")
```

### Exemplo: cliente Visual Basic

```foxpro
Dim xlApp2 As Object
Set xlApp2 = CreateObject("Excel.Application")
```

As chamadas de métodos a objetos criados dessa forma podem ser mais lentas que as chamadas a métodos de objetos com associação antecipada, pois o cliente deve incluir no executável compilado um código que determine, em tempo de execução, se o servidor possui determinado método.
