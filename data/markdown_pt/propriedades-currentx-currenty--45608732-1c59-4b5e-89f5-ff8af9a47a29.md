# Propriedades CurrentX, CurrentY

Especificam as coordenadas horizontal (X) e vertical (Y) para o próximo método de desenho. Não disponíveis em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Object.CurrentX[ = nXCoord]
Object.CurrentY[ = nYCoord]
```

# Valor de retorno
 **nXCoord**
Especifica a coordenada horizontal do formulário, na unidade de medida especificada pela propriedade ScaleMode do formulário.
**nYCoord**
Especifica a coordenada vertical do formulário, na unidade de medida especificada pela propriedade ScaleMode do formulário.

As coordenadas são medidas a partir do canto superior esquerdo de um objeto. CurrentX é 0 na borda esquerda de um objeto e CurrentY é 0 na borda superior. As coordenadas são expressas em foxels ou na unidade de medida atual definida pela propriedade ScaleMode.

Quando você usa os seguintes métodos gráficos, as configurações CurrentX e CurrentY são alteradas conforme indicado.

| Método | CurrentX, CurrentY definidos como |
| --- | --- |
| Box | O ponto final da caixa conforme especificado pelos dois últimos argumentos. |
| Circle | O centro do objeto. |
| Cls | 0, 0. |
| Line | O ponto final da linha. |
| Print | A próxima posição de impressão. |
| Pset | O ponto desenhado. |

# Observações

Aplica-se a: Form Object | _SCREEN System Variable
