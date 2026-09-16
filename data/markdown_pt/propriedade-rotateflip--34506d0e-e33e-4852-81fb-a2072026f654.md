# Propriedade RotateFlip

Especifica uma rotação ou inversão (flip) para uma imagem. Leitura/gravação em tempo de design e execução.

```foxpro
Image.RotateFlip [ = nValue ]
```

#### Parâmetros
 **nValue**
Tipo de dados numérico. A tabela a seguir lista os valores para nValue. Configuração nValue Descrição 0 RotateNoneFlipNone Especifica nenhuma rotação ou inversão. 1 Rotate90FlipNone Especifica uma rotação de 90 graus sem inversão. 2 Rotate180FlipNone Especifica uma rotação de 180 graus sem inversão. 3 Rotate270FlipNone Especifica uma rotação de 270 graus sem inversão. 4 RotateNoneFlipX Especifica nenhuma rotação e uma inversão horizontal. 5 Rotate90FlipX Especifica uma rotação de 90 graus seguida de uma inversão horizontal. 6 Rotate180FlipX Especifica uma rotação de 180 graus seguida de uma inversão horizontal. 7 Rotate270FlipX Especifica uma rotação de 270 graus seguida de uma inversão horizontal.

# Observações

Aplica-se a: Controle Image (Visual FoxPro)

Imagens .gif animadas não são suportadas.

Como uma imagem pode ter um arquivo .msk, o arquivo .msk deve estar formatado corretamente.

> **Observação:** O Visual FoxPro armazena uma única imagem na memória internamente. Se você usar essa imagem várias vezes, o Visual FoxPro a renderiza da mesma forma, independentemente de RotateFlip. Se desejar exibir a mesma imagem várias vezes em várias rotações, renomeie cada cópia da imagem que usar. Se você emitir o comando CLEAR...RESOURCES, o Visual FoxPro recarrega a imagem na memória e perde quaisquer configurações GDI+ anteriores.
