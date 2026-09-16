# Propriedade ScrollBars

Especifica o tipo de barras de rolagem de um controle EditBox, objeto Form ou controle Grid. Leitura/gravação em tempo de projeto; somente leitura em tempo de execução.

```foxpro
[Form.]Control.ScrollBars[= nType]
```

# Valor de retorno
 **nType**
Especifica o tipo de barras de rolagem do controle ou objeto. Para controles EditBox: 0 Nenhuma; 2 Vertical (Padrão). Para objetos Form: 0 Nenhuma (Padrão); 1 Horizontal; 2 Vertical; 3 Vertical e horizontal. Para controles Grid: 0 Nenhuma; 1 Horizontal; 2 Vertical; 3 Vertical e horizontal (Padrão).

# Observações

Aplica-se a: controle EditBox | objeto Form | controle Grid

ScrollBars é ignorada para a variável de sistema _SCREEN. Para obter mais informações, consulte Variável de sistema _SCREEN.

As barras de rolagem, se habilitadas, são exibidas automaticamente quando o formulário, a grade ou a caixa de edição contém mais informações do que o espaço disponível. A configuração da propriedade ScrollBars de um formulário é avaliada quando o formulário é instanciado.

> **Dica:** Para controlar o tamanho da barra de rolagem em tempo de execução, especifique um valor diferente de zero para nType.

> **Observação:** Valores de nType maiores que 0 exigem mais memória para acomodar o possível uso do método SaveAs. Para economizar memória, especifique nType = 0.
