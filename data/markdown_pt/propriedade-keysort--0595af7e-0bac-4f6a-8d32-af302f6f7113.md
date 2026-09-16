# Propriedade KeySort

Especifica como o Visual FoxPro enumera os itens de uma coleção ao usar o comando FOR EACH. Disponível em tempo de design e execução.

```foxpro
Collection.KeySort [ = nValue ]
```

# Valor de retorno
 **nValue**
Os valores são: 0, índice crescente (padrão); 1, índice decrescente; 2, chave crescente; 3, chave decrescente.

# Observações

Aplica-se a: classe Collection

KeySort só se aplica a enumerações FOR EACH.

KeySort não afeta como o método Add acrescenta itens. Add sempre os adiciona por índice no final, a menos que você especifique eBeforeItem ou eAfterItem.

Uma coleção pode não ter chaves em nenhum item. Nesse caso, os valores 2 e 3 não se aplicam. Se você especificar 3, o Visual FoxPro usará 1.

Alterar KeySort dentro de um loop FOR EACH não afeta a sequência dos itens. Contudo, você pode aninhar enumerações para alterá-la. No exemplo, o loop externo usa KeySort igual a 1 e o interno usa 2:

```foxpro
oCollection.KeySort = 1
FOR EACH oItem IN oCollection
     oCollection.KeySort = 2
     FOR EACH oItem2 IN oCollection
     ENDFOR
ENDFOR
```

# Exemplo

Você pode definir KeySort assim:

```foxpro
* Sorts a collection in ascending index order
oCollection.KeySort = 0
```
