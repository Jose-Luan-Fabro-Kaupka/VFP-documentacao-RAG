# Função DDEEnabled( )

Habilita ou desabilita o processamento de troca dinâmica de dados (DDE), ou retorna seu estado.

```foxpro
DDEEnabled([lExpression1 | nChannelNumber [, lExpression2]])
```

#### Parâmetros
 **lExpression1**
Especifique true (.T.) ou false (.F.) para habilitar ou desabilitar globalmente o DDE.
**nChannelNumber**
Especifica o número do canal cujo estado será retornado.
**lExpression2**
Com o número do canal, use true (.T.) para habilitá-lo ou false (.F.) para desabilitá-lo.

# Valor de retorno

Logical

# Observações

DDEEnabled( ) permite controlar o processamento globalmente ou por canal. Pode proteger código crítico ou desabilitar vínculos por curtos períodos. Solicitações de clientes ficam em fila enquanto o processamento está desabilitado.

Sem argumentos opcionais, retorna o estado global.
