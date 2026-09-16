# Propriedade AllowUpdate

Especifica se operações de atualização contra uma fonte de dados são permitidas. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** AllowUpdate não afeta a capacidade de atualizar uma linha no cursor em si.

```foxpro
CursorAdapter.AllowUpdate [ = lValue ]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista as configurações para lValue . lValue Descrição True (.T.) Permite operações de atualização. (Padrão) Quando a propriedade UpdateCmd do CursorAdapter está vazia (""), o Visual FoxPro gera um comando UPDATE - SQL automaticamente. Para obter mais informações, consulte Gerenciamento de acesso a dados usando CursorAdapters . False (.F.) Não permite operações de atualização.

# Observações

Aplica-se a: Classe CursorAdapter
