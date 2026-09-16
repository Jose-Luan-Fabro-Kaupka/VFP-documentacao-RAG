# Comando SET COLOR OF SCHEME

Especifica as cores de um esquema de cores ou copia um esquema de cores para outro esquema de cores.

```foxpro
SET COLOR OF SCHEME nScheme1 TO   [SCHEME nScheme2 | ColorPairList]
```

#### Parâmetros
 **nScheme1**
Especifica o número do esquema de cores que você deseja alterar. Pode ser um valor de 1 a 24. Observação No Visual FoxPro, os esquemas de cores 13 a 15 são reservados para uso interno. Não use esses esquemas de cores.
**TO [SCHEME nScheme2 ]**
Especifica o número de um esquema de cores para o qual o esquema de cores nScheme1 é alterado.
**TO [ ColorPairList ]**
Especifica até 10 pares de cores que você deseja alterar em seu esquema de cores. Você pode alterar seletivamente as cores em um esquema de cores incluindo uma vírgula para cada par de cores que não deseja alterar. Por exemplo, para alterar o terceiro par de cores no esquema de cores 1 para branco brilhante e azul e deixar as demais configurações de cores inalteradas, use este comando: SET COLOR OF SCHEME 1 TO , , W+/B* Um par de cores também pode ser especificado com um conjunto de seis valores de cor RGB (vermelho, verde e azul) separados por vírgulas. Para alterar o terceiro par de cores no esquema de cores 1 para branco brilhante e azul e deixar as demais configurações de cores inalteradas, você pode usar este comando: SET COLOR OF SCHEME 1 TO , , RGB(255,255,255,0,0,255)

# Observações

Nem todos os elementos da interface podem ser controlados por esquemas de cores — janelas do sistema, como as janelas View e Command, a barra de menus do sistema e assim por diante, são sempre controladas pelas configurações de cores do Painel de Controle. Emitir SET COLOR OF SCHEME nScheme1 TO sem incluir uma cláusula opcional restaura as cores do esquema de cores atual.
