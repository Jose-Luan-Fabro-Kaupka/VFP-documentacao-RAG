# Função EVL( )

Retorna um valor não vazio de duas expressões.

Você pode usar a função EVL( ) para retornar um valor substituto apropriado em vez de um valor vazio, como False (.F.) ou 0, de duas expressões. Você também pode usar essa funcionalidade para remover valores vazios de cálculos ou operações em que valores vazios não são suportados ou relevantes.

> **Observação:** O valor lógico do Visual FoxPro, False (.F.), e o valor numérico 0 também são avaliados como vazios.

```foxpro
EVL( eExpression1, eExpression2 )
```

#### Parâmetros
 **eExpression1 , eExpression2**
Especifica duas expressões. eExpression1 e eExpression2 podem ser de qualquer tipo de dados, exceto os seguintes: Campos General: Se eExpression1 ou eExpression2 representa um campo General, EVL( ) retorna um erro, "Operation is invalid for a General field. (Error 1912)" Referências de objeto.

# Valor de retorno

Character, Date, DateTime, Numeric, Currency, Logical, Object. EVL( ) retorna eExpression1 se ela não for avaliada como um valor vazio; caso contrário, retorna eExpresssion2.

# Exemplo

Os exemplos a seguir criam as variáveis de memória `glEmptyDate`, que contém um valor Date vazio, e `glEmptyNum`, que contém um valor Numeric vazio, 0.

Ao executar EVL( ) com `glEmptyDate`, EVL( ) retorna uma cadeia de caracteres vazia ("") ao avaliar `glEmptyDate` e uma cadeia de caracteres vazia, e `"None"` ao avaliar `glEmptyDate` e `"None"`.

```foxpro
STORE {  /  /  } TO glEmptyDate
? EVL(glEmptyDate,"")
? EVL(glEmptyDate, "None")
```

Ao executar EVL( ) com glEmptyNum, EVL( ) retorna uma cadeia de caracteres vazia ao avaliar glEmptyNum e uma cadeia de caracteres vazia, e "Empty" ao avaliar glEmptyNum e "Empty".

```foxpro
STORE 0 TO glEmptyNum
? EVL(glEmptyNum,"")
? EVL(glEmptyNum, "Empty")
```
