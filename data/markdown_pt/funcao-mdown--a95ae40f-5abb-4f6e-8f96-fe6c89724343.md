# Função MDOWN( )

Incluída para compatibilidade com versões anteriores. Use os eventos Click Event, MouseDown Event, MouseUp Event e RightClick Event em vez disso.

Determina se o botão do mouse está pressionado.

```foxpro
MDOWN()
```

# Valor de retorno

Valor de retorno - Logical

# Observações

MDOWN() retorna um valor verdadeiro (.T.) ou falso (.F.) dependendo de o botão do mouse estar pressionado ou não.

No FoxPro para MS-DOS e FoxPro para Windows, MDOWN() retorna valores apenas para o botão esquerdo do mouse.

Se o botão do mouse estiver pressionado quando MDOWN() é executado, verdadeiro (.T.) é retornado. Se o botão do mouse não estiver pressionado quando MDOWN() é executado, falso (.F.) é retornado.
