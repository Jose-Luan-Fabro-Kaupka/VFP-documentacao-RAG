# Propriedade Order (Visual FoxPro)

Especifica a tag de índice controladora para um objeto Cursor. Disponível em tempo de design e em tempo de execução.

```foxpro
DataEnvironment.Cursor.Order[ = cTagName]
```

# Valor de retorno
 **cTagName**
Especifica uma tag de índice existente para uma tabela.

# Observações

Aplica-se a: Objeto Cursor

Se a propriedade ChildOrder de um objeto relation estiver definida, a propriedade Order é ignorada.

Use a propriedade Order para especificar a ordem na qual os registros são exibidos ou acessados. Definir a propriedade Order altera a ordem do índice e move o ponteiro de registro para o primeiro registro no cursor.
