# Função ATN2( )

Retorna o arco tangente em todos os quatro quadrantes a partir de valores especificados.

```foxpro
ATN2(nYCoordinate, nXCoordinate)
```

#### Parâmetros
 **nYCoordinate**
Especifica a coordenada y.
**nXCoordinate**
Especifica a coordenada x.

# Valor de retorno

Numeric

# Observações

ATN2( ) retorna o ângulo (em radianos) entre a reta y = 0 e a reta que conecta as coordenadas especificadas e a origem (0, 0) do sistema de coordenadas.

ATN2( ) retorna um valor entre – pi/2 e +pi/2.

Você pode converter o valor retornado por ATN2( ) para graus com RTOD( ). Você pode especificar o número de casas decimais exibidas no resultado com SET DECIMALS.

# Exemplo

```foxpro
CLEAR
? PI()  && Displays 3.14
? ATN2(0,-1)  && Displays 3.14
STORE COS(PI()) TO gnXCoord
STORE SIN(PI()) TO gnYCoord
? ATN2(gnYCoord,gnXCoord)  && Displays 3.14
? ATN2(gnYCoord,gnXCoord)/PI()  && Displays 1.00
```
