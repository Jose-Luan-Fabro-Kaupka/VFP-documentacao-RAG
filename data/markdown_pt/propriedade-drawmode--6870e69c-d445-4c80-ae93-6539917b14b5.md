# Propriedade DrawMode

Determina, em conjunto com as propriedades de cor, como uma forma ou linha é exibida na tela. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.DrawMode[ = nMode]
```

# Valor de retorno
 **nMode**
As configurações para a propriedade DrawMode são: Configuração Descrição 1 Blackness Pen. A forma é desenhada em preto. 2 NotMerge Pen. Inverso da configuração 15. 3 Mask Not Pen. Combinação das cores comuns ao BackColor e ao inverso do ForeColor. 4 Not Copy Pen. Inverso da configuração 13. 5 Mask Pen Not. Combinação das cores comuns ao ForeColor e ao inverso do BackColor. 6 Invert. Inverso do BackColor. 7 XOR Pen. Combinação das cores no ForeColor e no BackColor, mas não em ambos. 8 Not Mask Pen. Inverso da configuração 9. 9 Mask Pen. Combinação das cores comuns ao ForeColor e ao BackColor. 10 Not XOR Pen. Inverso da configuração 7. 11 NOP. Nenhuma operação. A saída permanece inalterada. Na prática, essa configuração desativa o desenho. 12 Merge Not Pen. Combinação do BackColor e do inverso do ForeColor. 13 (Padrão). Copy Pen. Cor especificada pela propriedade ForeColor. 14 Merge Pen Not. Combinação do ForeColor e do inverso do BackColor. 15 Merge Pen. Combinação do ForeColor e do BackColor. 16 Whiteness Pen. A forma é desenhada em branco.

# Observações

Aplica-se a: Objeto Form | Controle Line | Variável de sistema _SCREEN | Controle Shape

Use a propriedade DrawMode para produzir efeitos visuais com controles Shape ou Line ou ao desenhar com métodos gráficos. Conforme uma nova forma é desenhada, o Visual FoxPro compara cada pixel no padrão com o pixel correspondente no plano de fundo existente e, em seguida, aplica operações bitwise. Por exemplo, a configuração 7 usa o operador exclusive OR (XOR) para combinar um pixel do padrão de desenho com o pixel de plano de fundo.

O efeito exato da configuração da propriedade DrawMode depende de como a cor de uma linha desenhada em tempo de execução se combina com as cores já na tela. As configurações 1, 6, 7, 11, 13 e 16 produzem os resultados mais previsíveis.
