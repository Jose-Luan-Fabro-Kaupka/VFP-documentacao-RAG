# Propriedade ErrorNo

Especifica o número de erro para um objeto Exception. Leitura/gravação em tempo de execução.

```foxpro
Exception.ErrorNo
```

# Valor de retorno

Tipo de dados numérico

# Observações

Aplica-se a: Exception Class (Visual FoxPro)

Se a exceção resultar de um comando THROW que especifica um valor para o parâmetro eUserExpression, o valor de ErrorNo é 2071.

Idêntico ao valor retornado pela função ERROR( ) e ao primeiro elemento no array produzido pela função AERROR( ).
