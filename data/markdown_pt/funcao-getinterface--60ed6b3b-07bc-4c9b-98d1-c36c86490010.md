# Função GETINTERFACE( )

Fornece acesso a propriedades, métodos e eventos de objetos COM por meio de vinculação antecipada.

```foxpro
GETINTERFACE(oObject [, cIID | cInterface[, cTypelib | cProgID]])
```

#### Parâmetros
 **oObject**
Especifica o objeto COM de destino.
**cIID**
Especifica o GUID da interface de destino de oObject . cIID pode ser uma interface como "IContextState" ou pode ser um GUID, como "{94631BEC-EE81-479A-AE64-A6CFC37B4799}". Se for "IDispatch", então GetInterface() retorna uma referência IDispatch (vinculação tardia) ao objeto. Se cIID não for especificado, então GetInterface() retornará a interface de vinculação antecipada para o objeto.
**cInterface**
Especifica o nome da interface.
**cTypelib**
Especifica o nome da biblioteca de tipos que contém a classe oObject .
**cProgID**
Especifica o nome do programa a ser usado para pesquisar a biblioteca de tipos.

# Retorna

Referência de interface de objeto COM

# Observações

GetInterface( ) se aplica apenas a objetos COM. Se você usar objetos nativos do Visual FoxPro, GetInterface( ) gera um erro. GetInterface( ) retorna uma referência de objeto com vinculação antecipada.

Quando uma DLL é compilada em uma plataforma Windows 95, Windows 98 ou Windows Me, o Visual FoxPro não inclui a biblioteca de tipos dentro da DLL. Quando você usa GETINTERFACE( ) e faz referência a uma DLL compilada em uma dessas plataformas, deve usar o nome da biblioteca de tipos em vez do nome da DLL, como no código a seguir:

```foxpro
oX = GETINTERFACE(x, "Imyclass", "myclass1.TLB")
```

Você pode usar o código a seguir para uma DLL compilada no Windows XP, Windows 2000 ou Windows NT:

```foxpro
oX = GETINTERFACE(x, "Imyclass", "myclass1.DLL")
```

# Exemplo

O exemplo de código a seguir fornece um método que você pode usar em seu servidor COM do Visual FoxPro para manipular transações em um aplicativo COM+. Este exemplo requer que você adicione o servidor COM contendo este código a um aplicativo COM+ antes que um cliente o chame.

```foxpro
LOCAL oMTX, oContext, oContextState
LOCAL lTxnState, lGetTxnState, lDone, lGetDone
lGetDone = .F.     && initialize setting
lGetTxnState = 0  && initialize setting
oMTX = CREATEOBJECT("MTXAS.APPSERVER.1")
oContext = oMTX.GetObjectContext()
oContextState = GetInterface(oContext,"IContextState")
* Handle activation setting (Doneness)
* Values: .T. - Deactivate, .F. - Leave activated
lDone = .T.
oContextState.SetDeactivateOnReturn(lDone)
oContextState.GetDeactivateOnReturn(@lGetDone)

* Handle transaction setting (Consistency)
* Values: 0 - commit, 1 - abort
lTxnState = 1
oContextState.SetMyTransactionVote(lTxnState)
oContextState.GetMyTransactionVote(@lGetTxnState)
```
