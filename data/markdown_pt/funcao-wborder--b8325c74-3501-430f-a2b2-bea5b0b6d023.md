# Função WBORDER( )

Determina se a janela ativa ou especificada tem uma borda.

```foxpro
WBORDER([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica o nome da janela para a qual WBORDER( ) retorna um valor lógico. WBORDER( ) retorna um valor lógico para a janela de saída ativa se você omitir um nome de janela.

# Valor de retorno

Logical

# Observações

WBORDER( ) retorna true (.T.) se a janela especificada tiver uma borda; caso contrário, WBORDER( ) retorna false (.F.). Por padrão, as janelas têm bordas. Inclua a cláusula NONE em DEFINE WINDOW para criar uma janela sem borda.
