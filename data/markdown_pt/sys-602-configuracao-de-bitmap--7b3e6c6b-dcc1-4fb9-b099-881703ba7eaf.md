# SYS(602) - Configuração de bitmap

Retorna a configuração atual do bitmap no arquivo de configuração atual e desliga ou liga bitmaps off-screen em tempo de execução.

```foxpro
SYS(602 [, 0 | 1 ])
```

#### Parâmetros
 **0**
Desliga bitmaps off-screen em tempo de execução.
**1**
Liga bitmaps off-screen em tempo de execução.

# Valor de retorno

Tipo de dados Character. A tabela a seguir lista as configurações possíveis que SYS(602) pode retornar.

| Return value | Setting |
| --- | --- |
| 0 | Bitmaps off-screen estão desligados. |
| 1 | Bitmaps off-screen estão ligados. (Padrão) |

# Observações

Você pode usar bitmaps off-screen para armazenar uma imagem da área de trabalho atual e formulários para que possa renderizá-los se outro elemento, como uma janela, for desenhado sobre eles. No entanto, bitmaps off-screen usam muita memória, portanto você pode melhorar o desempenho em aplicativos Terminal Server desligando esses bitmaps usando SYS(602).

No entanto, esteja ciente de que alternar bitmaps off-screen pode afetar seu aplicativo. Por exemplo, controles de formulário podem aparecer normais; no entanto, escrever diretamente em um formulário usando um método como Line requer que bitmaps off-screen estejam ligados.

Se deseja determinar se um aplicativo está sendo executado em um Terminal Server, use `OS(10)`.
