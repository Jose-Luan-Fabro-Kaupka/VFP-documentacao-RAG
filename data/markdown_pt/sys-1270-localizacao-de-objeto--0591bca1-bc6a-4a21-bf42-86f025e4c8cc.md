# SYS(1270) - Localização de objeto

Retorna uma referência para um objeto no ponto especificado.

```foxpro
SYS(1270 [, nXCoord, nYCoord])
```

#### Parâmetros
 **nXCoord**
Especifica a coordenada horizontal em pixels relativa à área de trabalho do Windows.
**nYCoord**
Especifica a coordenada vertical em pixels relativa à área de trabalho do Windows.

# Valor de retorno

Cadeia de caracteres ou referência de objeto. SYS(1270) retorna uma referência ao objeto no local especificado por nXCoord e nYCoord, se incluídos. Se forem omitidos, retorna uma referência ao objeto na posição atual do mouse. Se não houver objeto na posição, retorna falso (.F.).

> **Observação:** Para formulários encaixáveis, SYS(1270) não retorna o objeto correto se o formulário estiver encaixado com outros e o mouse, ou as coordenadas, estiver sobre a barra de título do contêiner de encaixe.
