# Comando DECLARE

Cria uma matriz unidimensional ou bidimensional.

> **Observação:** DECLARE é idêntico em operação e semelhante em sintaxe ao comando DIMENSION. Para obter mais informações, consulte DIMENSION Command .

```foxpro
DECLARE ArrayName1 (nRows1 [, nColumns1])
   [, ArrayName2 (nRows2 [, nColumns2])] ...
```

# Observações

Você pode usar colchetes ou parênteses para delimitar as expressões em DECLARE. Por exemplo, os dois comandos a seguir criam matrizes idênticas:

```foxpro
DIMENSION gaArrayOne(10), gaArrayTwo[2,4], gaArrayThree(3,3)
DIMENSION gaArrayOne[10], gaArrayTwo(2,4), gaArrayThree[3,3]
```

Quando o tamanho de uma matriz é aumentado ou diminuído com SET COMPATIBLE definido como ON ou DB4, o valor de cada elemento na matriz é reinicializado para .F.

> **Observação:** As matrizes do Visual FoxPro são baseadas em um — o primeiro elemento, linha ou coluna de uma matriz é especificado com o número 1. (Matrizes em outras linguagens de programação podem ser baseadas em zero; o primeiro elemento, linha ou coluna de uma matriz é especificado com o número 0.)
