# Função COMPOBJ( )

Compara as propriedades de dois objetos e retorna True (.T.) se suas propriedades e valores de propriedades forem idênticos.

```foxpro
COMPOBJ(oExpression1, oExpression2)
```

#### Parâmetros
 **oExpression1 , oExpression2**
Especifica os objetos a comparar. oExpression1 e oExpression2 podem ser quaisquer expressões que sejam avaliadas como objetos, como referências de objeto, variáveis de objeto ou elementos de matriz de objetos.

# Valor de retorno

Lógico

# Observações

COMPOBJ( ) retorna False (.F.) se um objeto tiver uma propriedade que o outro não tenha ou se os objetos tiverem propriedades idênticas, mas os valores de uma ou mais propriedades forem diferentes.

# Exemplo

No exemplo a seguir, são criados dois ListBoxes chamados `lstMyList1` e `lstMyList2` e um ComboBox chamado `cmbMyCombo`. A propriedade Name de cada ListBox é exibida.

COMPOBJ( ) é usada para comparar as propriedades do primeiro ListBox com as propriedades do ComboBox. Como muitas propriedades são diferentes, .F. é exibido. Em seguida, COMPOBJ( ) é usada para comparar as propriedades do primeiro ListBox com as propriedades do segundo ListBox. Como as propriedades Name são diferentes, .F. é exibido. O segundo ListBox `lstMyList2` é substituído pelo primeiro ListBox `lstMyList1`, e COMPOBJ( ) é usada para comparar as propriedades. Como suas propriedades são idênticas, .T. é exibido.

```foxpro
lstMyList1 = CREATEOBJ('ListBox')  && Creates a ListBox
lstMyList2 = CREATEOBJ('ListBox')  && Creates a second ListBox
cmbMyCombo = CREATEOBJ('ComboBox')  && Creates a ComboBox
lstMyList1.Name = 'list1'
lstMyList2.Name = 'list2'
CLEAR
? lstMyList1.Name  && Displays List1 Name property
? lstMyList2.Name  && Displays List2 Name property
? COMPOBJ(lstMyList1, cmbMyCombo)     && Displays .F.
? COMPOBJ(lstMyList1, lstMyList2)     && Displays .F., different Names
lstMyList2.Name = lstMyList1.Name
? COMPOBJ(lstMyList1, lstMyList2)     && Displays .T., same properties
```
