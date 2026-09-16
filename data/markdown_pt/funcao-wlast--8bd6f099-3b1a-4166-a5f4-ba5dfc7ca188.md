# Função WLAST( )

Retorna o nome da janela que estava ativa antes da janela atual ou determina se a janela especificada estava ativa antes da janela atual.

```foxpro
WLAST([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica uma janela que WLAST( ) avalia. No Visual FoxPro, você também pode especificar o nome de uma barra de ferramentas. WLAST( ) retorna true (.T.) se a janela especificada estava ativa antes da janela atual; caso contrário, false (.F.) é retornado. False (.F.) também é retornado se a janela que você especifica não existir. O nome da janela que estava ativa antes da janela atual é retornado se você omitir WindowName.

# Valor de retorno

Caractere ou Lógico

# Observações

WLAST( ) retorna a cadeia de caracteres vazia se a janela que estava ativa antes da janela atual for a janela Debug, Trace ou Command. A execução do programa não é afetada ao trazer essas janelas para frente quando você está depurando um programa que usa WLAST( ).
