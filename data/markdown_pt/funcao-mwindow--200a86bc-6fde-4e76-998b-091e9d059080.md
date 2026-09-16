# Função MWINDOW( )

Retorna o nome da janela sobre a qual o ponteiro do mouse está posicionado.

```foxpro
MWINDOW([cWindowName])
```

#### Parâmetros
**cWindowName**
Especifica um nome de janela. Se o ponteiro do mouse estiver sobre a janela especificada, MWINDOW( ) retornará true (.T.); caso contrário, retornará false (.F.).

# Valor de retorno

Character, Logical

# Observações

Se o nome opcional da janela for omitido, MWINDOW( ) retornará o nome da janela sobre a qual o ponteiro está posicionado ou uma cadeia vazia se estiver sobre a janela principal do Visual FoxPro ou qualquer outra janela que não faça parte do Visual FoxPro.
