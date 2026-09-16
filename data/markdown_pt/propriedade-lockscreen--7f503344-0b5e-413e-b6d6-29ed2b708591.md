# Propriedade LockScreen

Determina se um formulário agrupa todas as alterações nas configurações de propriedades de seus objetos contidos. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.LockScreen[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade LockScreen são: Setting Description True (.T.) Os objetos contidos do formulário refletem alterações nas configurações de propriedades somente quando LockScreen é redefinido como falso (.F.), em vez de assim que as alterações são feitas. False (.F.) (Padrão) Os objetos contidos do formulário refletem alterações nas configurações de propriedades assim que as alterações são feitas.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable | ToolBar Object

Defina LockScreen como True (.T.) para reduzir atualizações irritantes da tela quando propriedades de apresentação como BackColor, FontName e assim por diante são alteradas durante a execução.

A propriedade LockScreen não impede que alterações no formulário sejam refletidas imediatamente. Por exemplo, mesmo se LockScreen estiver definido como true, o formulário é movido se você chamar seu método Move.

> **Observação:** Se você definir LockScreen como False (.F.), os controles contidos do formulário são repintados imediatamente.
