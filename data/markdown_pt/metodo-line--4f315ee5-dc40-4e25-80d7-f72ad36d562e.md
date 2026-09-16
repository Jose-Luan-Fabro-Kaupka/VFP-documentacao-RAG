# Método Line

Desenha uma linha em um objeto Form. Há duas versões da sintaxe.

```foxpro
Object.Line(nXCoord2, nYCoord2)
```

```foxpro
Object.Line(nXCoord1, nYCoord1, nXCoord2, nYCoord2)
```

#### Parâmetros
 **nXCoord1 , nYCoord1**
Especifica as coordenadas do ponto inicial da linha. A unidade de medida é especificada pela propriedade ScaleMode do formulário.
**nXCoord2 , nYCoord2**
Especifica as coordenadas do ponto final da linha.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable

A largura da linha desenhada depende da configuração da propriedade DrawWidth. A forma como uma linha é desenhada no plano de fundo depende da configuração das propriedades DrawMode e DrawStyle. Após a execução do método Line, as propriedades CurrentX e CurrentY são definidas como nXCoord2, nYCoord2.
