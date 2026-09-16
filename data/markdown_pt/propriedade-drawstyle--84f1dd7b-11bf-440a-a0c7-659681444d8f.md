# Propriedade DrawStyle

Especifica o estilo de linha a ser usado ao desenhar com métodos gráficos. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.DrawStyle[ = nStyle]
```

# Valor de retorno
 **nStyle**
As configurações para a propriedade DrawStyle são: Configuração Descrição 0 (Padrão) Solid 1 Dash 2 Dot 3 Dash-Dot 4 Dash-Dot-Dot 5 Transparent 6 Inside Solid Observação Se DrawWidth estiver definido como 1, DrawStyle produz o efeito descrito na tabela anterior para cada configuração. Mas se DrawWidth estiver definido com um valor maior que 1, as configurações 1 a 4 produzem uma linha sólida.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable
