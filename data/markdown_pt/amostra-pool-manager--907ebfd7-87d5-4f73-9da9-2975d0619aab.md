# Amostra Pool Manager

Arquivo: ...\Samples\Solution\Ffc\_PoolManager.scx

Esta amostra demonstra como usar a classe Pool Manager, que gerencia um pool ou coleção de objetos de uma classe e é útil quando você precisa usar objetos repetidamente por um curto período de tempo.

Esta amostra contém as seguintes classes.

| Classe | Biblioteca | Descrição |
| --- | --- | --- |
| _poolmanager | _poolmanager.vcx | Gerencia um pool, ou coleção, de objetos de uma única classe. |

# Agrupando objetos

Nesta amostra, formulários são coletados em um pool para que você possa reutilizar qualquer formulário disponível no pool em vez de ter que criar um novo formulário ao selecionar um cliente na lista suspensa.

Para usar a classe Pool Manager nesta amostra, as seguintes propriedades da classe Pool Manager devem ser definidas na janela Properties:

cClass = frmCustomer

cClassLibrary = frmCustomer.vcx

# Associando-se a eventos do Pool Manager

Você pode associar-se a eventos do _PoolManager. Nesta amostra, o evento Init do formulário contém código que associa os métodos de manipulador personalizados do formulário, PoolManager_ObjectRequested e PoolManager_ObjectReturned, aos eventos ObjectRequested e ObjectReturned do _PoolManager para que o status possa ser relatado no formulário de amostra:

```foxpro
BINDEVENT(This.PoolManager,"ObjectRequested",ThisForm,"PoolManager_ObjectRequested")
BINDEVENT(This.PoolManager,"ObjectReturned",ThisForm,"PoolManager_ObjectReturned")
```

# Solicitando objetos

Para solicitar um objeto do pool, chame o método Get do _PoolManager.

### Para abrir um formulário de cliente nesta amostra
- Selecione um nome de cliente na lista suspensa.
- Clique em View Customer .

Você pode abrir vários formulários clicando em View Customer repetidamente, o que solicita um objeto de formulário da classe Pool Manager cada vez. O método personalizado ViewCustomer do formulário contém o seguinte código:

```foxpro
loForm = ThisForm.PoolManager.Get(m.lcCustID)
If Vartype(m.loForm) == "O"
   loForm.Show()
EndIf
```

Nesta amostra, o método Get retorna um objeto não utilizado que existe no pool ou cria um novo objeto. Quando um novo formulário de cliente é criado, o código no evento Init do formulário associa-se aos métodos ObjectRequested e ObjectReturned do _PoolManager usando a variável privada `THISPOOLMANAGER` criada no método Get:

```foxpro
BINDEVENT(THISPOOLMANAGER,"ObjectRequested",This,"PoolManager_ObjectRequested")
BINDEVENT(THISPOOLMANAGER,"ObjectReturned",This,"PoolManager_ObjectReturned")
```

Esta associação de eventos torna possível que o formulário chame seu método Hide em vez do método Release para que o formulário retorne ao pool em vez de ser destruído.

# Devolvendo objetos

Para devolver objetos ao pool, chame o método Free do _PoolManager. Nesta amostra, o evento QueryUnload do formulário ocorre quando o formulário de cliente é fechado e devolve o formulário ao pool:

```foxpro
If Vartype(This.oPoolManager) == "O"
   This.oPoolManager.Free(This)
   NoDefault
EndIf
```
