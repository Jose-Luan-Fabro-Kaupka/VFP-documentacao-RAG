# Variável de sistema _PLOFFSET

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Define o deslocamento da página.

```foxpro
_PLOFFSET = expN
```

# Observações

_PLOFFSET está incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_PLOFFSET contém um valor numérico que determina o número de colunas da impressora (o deslocamento) da borda esquerda do papel até a borda esquerda do texto em toda a saída impressa. A saída enviada à tela não é afetada por _PLOFFSET. O espaço adicional de _LMARGIN é calculado a partir de _PLOFFSET.

_PLOFFSET pode conter um valor de 0 a 254. _PLOFFSET é equivalente a SET MARGIN. Ajustar um automaticamente altera o outro.

A configuração de _PLOFFSET não afeta relatórios criados com o Report Writer e executados com REPORT FORM. Embora _PLOFFSET seja ajustado enquanto um relatório criado com o Report Writer é executado, ele retorna ao valor original após a execução do relatório. A configuração Printer Indent na caixa de diálogo Page Layout do Report Writer determina o deslocamento da borda esquerda do papel.
