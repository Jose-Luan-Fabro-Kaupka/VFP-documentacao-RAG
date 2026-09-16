# Propriedade CursorStatus

Especifica se o objeto CursorAdapter representado pela propriedade CursorAdapter Alias está anexado e como está anexado. O Visual FoxPro requer CursorStatus para determinar o estado do objeto CursorAdapter atual e a origem do cursor associado. Somente leitura.

```foxpro
CursorAdapter.CursorStatus [ = nValue ]
```

# Valor de retorno
 **nValue**
Tipo de dados numérico. A tabela a seguir lista os valores possíveis para nValue. nValue Descrição 0 CursorAdapter < Alias > não está anexado. (Padrão) 1 CursorAdapter < Alias > está anexado por meio do método CursorFill. 2 CursorAdapter < Alias > está anexado por meio do método CursorAttach.

# Observações

Aplica-se a: classe CursorAdapter
