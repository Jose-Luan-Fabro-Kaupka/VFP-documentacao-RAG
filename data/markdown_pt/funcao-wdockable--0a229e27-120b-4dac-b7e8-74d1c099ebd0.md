# Função WDOCKABLE( )

Retorna o estado de encaixe da janela especificada.

```foxpro
WDOCKABLE(cWindowName [, lEnable])
```

#### Parâmetros
 **cWindowName**
Especifica o nome da janela a avaliar.
**lEnable**
Especifica o estado de encaixe da janela indicada por cWindowName. Se a janela não oferecer suporte a encaixe, o Visual FoxPro ignorará lEnable.

# Valor de retorno

Tipo de dados Logical. Retorna o estado de encaixe atual da janela especificada.

# Observações

WDOCKABLE( ) sempre retorna False (.F.) para janelas que não podem ser encaixadas. Use WDOCKABLE( ) em janelas do Visual FoxPro compatíveis com encaixe. Para obter uma lista, consulte Como: encaixar janelas.
