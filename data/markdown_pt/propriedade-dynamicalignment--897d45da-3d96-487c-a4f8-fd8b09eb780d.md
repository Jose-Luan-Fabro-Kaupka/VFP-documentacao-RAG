# Propriedade DynamicAlignment

Especifica o alinhamento de texto e controles em um objeto Column. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Column.DynamicAlignment [= "cAlign"]
```

# Valor de retorno
 **cAlign**
Especifica uma expressão de caracteres que avalia para um valor conforme descrito na tabela a seguir. O valor de alinhamento é reavaliado em tempo de execução cada vez que o controle Grid é atualizado. cAlign avalia para Descrição 0 Middle Left. Alinha o texto à esquerda e centralizado verticalmente. 1 Middle Right. Alinha o texto à direita e centralizado verticalmente. 2 Middle Center. Alinha o texto no meio com espaços iguais à direita e à esquerda e centralizado verticalmente. 3 Automatic. (Padrão) Alinha o texto com base no tipo de dados da fonte de controle. Tipos numéricos, como Numeric , Double , Float , Currency e Integer, são alinhados à direita; controles com outros tipos de dados são alinhados à esquerda. 4 Top Left. Alinha o texto à esquerda e no topo da coluna. 5 Top Right. Alinha o texto à direita e no topo da coluna. 6 Top Center. Alinha o texto no meio com espaços iguais à direita e à esquerda e no topo da coluna. 7 Bottom Left. Alinha o texto à esquerda e na parte inferior da coluna. 8 Bottom Right. Alinha o texto à direita e na parte inferior da coluna. 9 Bottom Center. Alinha o texto no meio com espaços iguais à direita e à esquerda e na parte inferior da coluna.

# Observações

Aplica-se a: Objeto Column

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar esta propriedade.
