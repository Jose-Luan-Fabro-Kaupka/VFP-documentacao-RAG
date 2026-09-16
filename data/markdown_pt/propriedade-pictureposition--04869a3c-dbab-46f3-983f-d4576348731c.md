# Propriedade PicturePosition

Especifica a localização de uma imagem em relação à sua legenda. Leitura/gravação em tempo de execução.

A imagem e a legenda, como uma unidade, aparecem centralizadas no controle. Se não houver legenda, a imagem será posicionada em relação ao centro do controle. PicturePosition é afetada pelas propriedades Picture, DownPicture e DisabledPicture. Para obter mais informações, consulte Propriedade Picture (Visual FoxPro), Propriedade DownPicture e Propriedade DisabledPicture.

> **Observação:** Para aplicar PicturePosition, especifique uma imagem na propriedade Picture. O tamanho da imagem é fixo. Para esticar, redimensionar ou cortar a imagem, use um controle Image. Arquivos .gif animados não são compatíveis.

```foxpro
Object.PicturePosition [ = nValue ]
```

#### Parâmetros
 **nValue**
Especifica o alinhamento da imagem. As configurações são: 0, à esquerda e alinhada ao topo da legenda; 1, à esquerda e centralizada; 2, à esquerda e alinhada à parte inferior; 3, à direita e alinhada ao topo; 4, à direita e centralizada; 5, à direita e alinhada à parte inferior; 6, acima e alinhada à esquerda; 7, acima e centralizada; 8, acima e alinhada à direita; 9, abaixo e alinhada à esquerda; 10, abaixo e centralizada; 11, abaixo e alinhada à direita; 12, imagem no centro do controle e legenda centralizada horizontal e verticalmente sobre a imagem; 13 (padrão), imagem no centro e legenda centralizada abaixo, mantendo-se relativa à parte inferior do botão quando redimensionado; 14, sem texto, com a imagem centralizada ocultando o texto de Caption. Dica: para usar 14, a propriedade Style deve ser 1 (Graphical). Use essa configuração para fornecer uma tecla de acesso sem exibir texto.

# Observações

Aplica-se a: controle CommandButton | controle OptionButton | controle CheckBox

Para controles CommandButton, o Visual FoxPro ignora PicturePosition se Style estiver definida como 1 (Invisible).

As propriedades WordWrap e AutoSize são compatíveis com PicturePosition.

As propriedades SpecialEffect e VisualEffect afetam a borda externa, mas não PicturePosition.

Versões anteriores ao Visual FoxPro 8.0 usam um algoritmo de posicionamento ligeiramente diferente das configurações padrão de 0 a 12. A imagem permanece centralizada, mas o texto fica relativo à parte inferior. PicturePosition igual a 7 produz comportamento semelhante; porém, ao reduzir o botão, o texto é cortado em vez de deslocado para cima. Definir PicturePosition como 13 corresponde ao comportamento das versões anteriores ao Visual FoxPro 8.0.
