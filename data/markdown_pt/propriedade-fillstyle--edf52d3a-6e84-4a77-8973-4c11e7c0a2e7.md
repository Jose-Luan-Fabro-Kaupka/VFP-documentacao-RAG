# Propriedade FillStyle

Especifica o padrão usado para preencher formas e figuras criadas com os métodos gráficos Circle e Box. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.FillStyle[ = nStyle]
```

# Valor de retorno
 **nStyle**
Especifica o padrão usado para preencher uma forma ou figura. As configurações da propriedade FillStyle são: Configuração Descrição 0 Sólido. 1 (Padrão) Transparente. A propriedade FillColor é ignorada. 2 Linha horizontal. 3 Linha vertical. 4 Diagonal ascendente. Linhas diagonais ascendentes do canto superior esquerdo ao inferior direito. 5 Diagonal descendente. Diagonal descendente do canto inferior esquerdo ao superior direito. 6 Cruz. Linhas verticais e horizontais cruzadas formando quadrados. 7 Cruz diagonal.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable | Shape Control
