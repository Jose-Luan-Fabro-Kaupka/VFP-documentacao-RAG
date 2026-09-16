# Propriedade AllowInsert

Especifica se são permitidas operações de inserção em uma fonte de dados. Leitura/gravação em tempo de design e de execução.

```foxpro
CursorAdapter.AllowInsert [ = lValue ]
```

# Valor de retorno
**lValue**
Tipo de dados lógico. A tabela a seguir lista as configurações de lValue. lValue Descrição True (.T.) Permite operações de inserção. (Padrão) Quando a propriedade InsertCmd de CursorAdapter está vazia (""), o Visual FoxPro gera automaticamente um comando SQL INSERT. Para obter mais informações, consulte Gerenciamento de acesso a dados usando CursorAdapters. False (.F.) Não permite operações de inserção.

# Observações

Aplica-se a: classe CursorAdapter

AllowInsert não afeta a capacidade de inserir uma linha no próprio cursor.
