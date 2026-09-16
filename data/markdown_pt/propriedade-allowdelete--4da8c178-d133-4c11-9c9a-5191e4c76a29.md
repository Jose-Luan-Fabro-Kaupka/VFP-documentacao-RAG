# Propriedade AllowDelete

Especifica se operações de exclusão contra uma fonte de dados são permitidas. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** AllowDelete não afeta a capacidade de excluir uma linha no próprio cursor.

```foxpro
CursorAdapter.AllowDelete [ = lValue ]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. A tabela a seguir lista as configurações para lValue . lValue Descrição True (.T.) Permite operações de exclusão. (Padrão) Quando a propriedade DeleteCmd do CursorAdapter está vazia (""), o Visual FoxPro gera automaticamente um comando SQL DELETE. Para obter mais informações, consulte Gerenciamento de acesso a dados usando CursorAdapters . False (.F.) Não permite operações de exclusão.

# Observações

Aplica-se a: Classe CursorAdapter
