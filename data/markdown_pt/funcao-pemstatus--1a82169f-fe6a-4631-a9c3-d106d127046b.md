# Função PEMSTATUS( )

Recupera um atributo de uma propriedade, evento, método ou objeto.

```foxpro
PEMSTATUS(oObjectName | cClassName, cProperty | cEvent | cMethod
   | cObject, nAttribute)
```

#### Parâmetros
 **oObjectName**
Especifica o objeto cujo atributo de propriedade, evento, método ou objeto será retornado. oObjectName pode ser qualquer expressão avaliada como um objeto, como uma referência de objeto, uma variável de memória de objeto ou um elemento de matriz de objetos. Se oObjectName for um objeto contêiner, como um formulário, você poderá determinar os atributos dos objetos no objeto contêiner.
**cClassName**
Especifica a classe cujo atributo de propriedade, evento ou método será retornado.
**cProperty**
Especifica a propriedade cujo atributo será retornado.
**cEvent**
Especifica o evento cujo atributo será retornado.
**cMethod**
Especifica o método cujo atributo será retornado.
**cObject**
Especifica o objeto cujo atributo será retornado. Por exemplo, você pode usar o método AddObject para adicionar um objeto a um objeto contêiner e, em seguida, usar PEMSTATUS( ) para retornar informações sobre o objeto adicionado ao objeto contêiner.
**nAttribute**
Especifica um valor numérico que determina o atributo de propriedade, evento ou método a ser retornado. A lista a seguir apresenta os valores de nAttribute e o atributo correspondente de propriedade, evento ou método retornado. Atributo de propriedade, evento ou método de nAttribute: 0 Alterado. Se o valor da propriedade, método ou evento tiver sido alterado, PEMSTATUS( ) retornará um valor lógico verdadeiro (.T.). Caso contrário, PEMSTATUS( ) retornará um valor lógico falso (.F.). 1 Somente leitura (somente propriedades). Se a propriedade for somente leitura, PEMSTATUS( ) retornará um valor lógico verdadeiro (.T.). Caso contrário, PEMSTATUS( ) retornará um valor lógico falso (.F.). 2 Protegido. Se a propriedade, evento ou método for protegido, PEMSTATUS( ) retornará um valor lógico verdadeiro (.T.). Caso contrário, PEMSTATUS( ) retornará um valor lógico falso (.F.). 3 Tipo. PEMSTATUS( ) retorna uma cadeia de caracteres, por exemplo, Property, Event, Method ou Object, indicando se cProperty, cEvent, cMethod ou cObject é uma propriedade, evento, método ou objeto. 4 Definido pelo usuário. Se a propriedade, evento ou método for definido pelo usuário, PEMSTATUS( ) retornará um valor lógico verdadeiro (.T.). Caso contrário, PEMSTATUS( ) retornará um valor lógico falso (.F.). 5 Propriedade, evento, método ou objeto definido. Se a propriedade, evento, método ou objeto existir para oObjectName ou cClassName, PEMSTATUS( ) retornará um valor lógico verdadeiro (.T.). Caso contrário, ou para propriedades nativas ocultas, PEMSTATUS( ) retornará um valor lógico falso (.F.). 6 Propriedade, evento, método ou objeto herdado. Se a propriedade, evento, método ou objeto de oObjectName ou cClassName tiver sido herdado de outro objeto ou classe, PEMSTATUS( ) retornará um valor lógico verdadeiro (.T.). Caso contrário, PEMSTATUS( ) retornará um valor lógico falso (.F.).

# Valor de retorno

Character ou Logical. PEMSTATUS( ) retorna uma cadeia de caracteres ou um valor lógico para o atributo especificado.

# Observações

PEMSTATUS( ) não detecta alterações em elementos específicos de uma matriz quando ela é passada.
