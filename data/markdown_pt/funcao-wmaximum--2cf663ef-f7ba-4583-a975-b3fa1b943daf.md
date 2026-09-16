# Função WMAXIMUM( )

Determina se a janela ativa ou especificada está maximizada.

```foxpro
WMAXIMUM([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica o nome da janela que WMAXIMUM( ) avalia. Você pode especificar o nome de uma janela do sistema Visual FoxPro (a janela Command, a janela Data Session, uma janela Browse e assim por diante). Se você omitir WindowName , WMAXIMUM( ) retorna um valor lógico para a janela ativa. Você também pode usar a cadeia de caracteres vazia para WindowName para especificar a janela principal do Visual FoxPro.

# Observações

As janelas podem ser ampliadas para preencher a janela que as contém. No Visual FoxPro para Windows, a janela contêiner padrão é a janela principal.

Uma janela definida pelo usuário criada com DEFINE WINDOW pode ser maximizada somente se a palavra-chave ZOOM for incluída em sua definição.

WMAXIMUM( ) retorna true (.T.) se a janela atual ou especificada estiver maximizada; caso contrário, WMAXIMUM( ) retorna false (.F.). No Visual FoxPro, você pode incluir o nome de uma barra de ferramentas. No entanto, WMAXIMUM( ) sempre retorna false (.F.) para uma barra de ferramentas, pois barras de ferramentas não podem ser maximizadas.
