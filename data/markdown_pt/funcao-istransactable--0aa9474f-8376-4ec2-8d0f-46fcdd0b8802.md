# Função ISTRANSACTABLE( )

Retorna um valor lógico que indica se uma tabela livre ou um cursor livre oferece suporte a transações.

```foxpro
ISTRANSACTABLE([nWorkArea | cAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho da tabela livre ou do cursor livre para a qual ISTRANSACTABLE( ) determina se há suporte a transações.
**cAlias**
Especifica o alias da tabela ou cursor para o qual ISTRANSACTABLE( ) determina se há suporte a transações.

# Valor de retorno

Logical. Retorna True (.T.) se uma tabela livre ou um cursor livre oferece suporte a transações; caso contrário, retorna False (.F.).

# Observações

Use a função MAKETRANSACTABLE( ) para permitir que uma tabela livre ou um cursor livre ofereça suporte a transações.
