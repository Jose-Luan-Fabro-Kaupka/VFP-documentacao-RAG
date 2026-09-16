# Criação de referência de objeto

Em vez de fazer uma cópia de um objeto, você pode criar uma referência ao objeto. Uma referência usa menos memória que um objeto adicional, pode ser facilmente passada entre procedimentos e pode auxiliar na escrita de código genérico.

# Retornando uma referência a um objeto

Às vezes, você pode querer manipular um objeto por meio de uma ou mais referências ao objeto. Por exemplo, o programa a seguir define uma classe, cria um objeto baseado na classe e retorna uma referência ao objeto:

```foxpro
*--NEWINV.PRG
*--Returns a reference to a new invoice form.
frmInv = CREATEOBJECT("InvoiceForm")
RETURN frmInv

DEFINE CLASS InvoiceForm AS FORM
   ADD OBJECT txtCompany AS TEXTBOX
   * code to set properties, add other objects, and so on
ENDDEFINE
```

O programa a seguir estabelece uma referência ao objeto criado em Newinv.prg. A variável de referência pode ser manipulada exatamente da mesma forma que a variável de objeto:

```foxpro
frmInvoice = NewInv() && store the object reference to a variable
frmInvoice.SHOW
```

Você também pode criar uma referência a um objeto em um formulário, como no exemplo a seguir:

```foxpro
txtCustName = frmInvoice.txtCompany
txtCustName.Value = "Fox User"
```

> **Dica:** Depois de criar um objeto, você pode usar o comando DISPLAY OBJECTS para exibir a hierarquia de classes do objeto, configurações de propriedades, objetos contidos e métodos e eventos disponíveis. Você pode preencher um array com as propriedades (não as configurações de propriedades), eventos, métodos e objetos contidos de um objeto com a função AMEMBERS().

# Liberando objetos e referências da memória

Se uma referência a um objeto existe, liberar o objeto não limpa o objeto da memória. Por exemplo, o comando a seguir libera `frmInvoice`, o objeto original:

```foxpro
RELEASE frmInvoice
```

No entanto, como uma referência a um objeto pertencente a `frmInvoice` ainda existe, o objeto não é liberado da memória até que `txtCustName` seja liberado com o comando a seguir:

```foxpro
RELEASE txtCustName
```

# Verificando se um objeto existe

Você pode usar as funções TYPE( ), ISNULL( ) e VARTYPE( ) para determinar se um objeto existe. Por exemplo, as linhas de código a seguir verificam se um objeto chamado `oConnection` existe:

```foxpro
IF TYPE("oConnection") = "O" AND NOT ISNULL(oConnection)
   * Object exists
ELSE
   * Object does not exist
ENDIF
```

> **Observação:** ISNULL() é necessário porque .NULL. é armazenado na variável de objeto do formulário quando um usuário fecha um formulário, mas o tipo da variável permanece "O".
