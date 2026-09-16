# Propriedade Filter

Exclui registros que não atendem aos critérios na expressão especificada. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
DataEnvironment.Cursor.Filter[ = cExpr]
```

# Valor de retorno
 **cExpr**
Qualquer expressão do Visual FoxPro, normalmente uma expressão que opera em um conjunto de registros.

# Observações

Aplica-se a: Cursor Object | CURSORSETPROP( ) Function

Imita o comportamento de SET FILTER.

> **Observação:** Quando o objeto Cursor é acessado usando CURSORSETPROP( ), a propriedade Filter é somente leitura em tempo de execução.
