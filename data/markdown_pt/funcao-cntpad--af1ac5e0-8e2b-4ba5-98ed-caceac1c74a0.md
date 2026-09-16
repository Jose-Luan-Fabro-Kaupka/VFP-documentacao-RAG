# Função CNTPAD( )

Retorna o número de títulos de menu em uma barra de menu definida pelo usuário ou na barra de menu do sistema do Visual FoxPro.

```foxpro
CNTPAD(cMenuBarName)
```

#### Parâmetros
 **cMenuBarName**
Especifica o nome da barra de menu para a qual CNTPAD( ) retorna o número de títulos de menu.

# Valor de retorno

Numeric

# Exemplo

O comando a seguir usa CNTPAD( ) para exibir o número de títulos de menu na barra de menu do sistema do Visual FoxPro.

```foxpro
? CNTPAD('_MSYSMENU')
```
