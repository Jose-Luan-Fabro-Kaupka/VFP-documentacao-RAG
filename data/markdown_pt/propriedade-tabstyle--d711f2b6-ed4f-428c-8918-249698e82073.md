# Propriedade TabStyle

Especifica se as guias Page em um page frame são justificadas ou não justificadas. Disponível em tempo de design e em tempo de execução.

```foxpro
PageFrame.TabStyle[ = nStyle]
```

# Valor de retorno
 **nStyle**
Um dos seguintes: nStyle Descrição 0 (Padrão) Justificado. A largura de cada guia Page é ajustada para acomodar seu caption. Se necessário, a largura de cada guia Page é aumentada para que as guias abranjam toda a largura do PageFrame. Esta configuração é ignorada se a propriedade TabStretch estiver definida como 1, Single Row. 1 Não justificado. A largura de cada guia Page não é ajustada para acomodar seu caption. A largura de cada guia Page não é ajustada para que as guias abranjam toda a largura do PageFrame. Esta configuração é ignorada se a propriedade TabStretch estiver definida como 1, Single Row.

# Observações

Aplica-se a: PageFrame Control
