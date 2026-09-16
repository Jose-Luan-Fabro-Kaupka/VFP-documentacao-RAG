# Função CTOD( )

Converte uma expressão de caractere em uma expressão de data.

```foxpro
CTOD(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica uma expressão de caractere.

# Valor de retorno

Tipo de dados Date. CTOD( ) retorna um valor Date.

# Observações

> **Observação:** CTOD() pode criar valores Date ambíguos e gera um erro de compilação quando SET STRICTDATE está definido como 2. Para criar valores Date não ambíguos, use a função DATE( ).

# Exemplo

O exemplo a seguir usa CTOD( ) para converter dados Character em Date e depois realiza ações simples relacionadas a data.

```foxpro
SET CENTURY ON               && Shows the century value.
cDate="01/01/2003"
?CTOD(cDate)               && Returns 01/01/2003 as Date.
?GOMONTH(CTOD(cDate),12)   && Returns 01/01/2004.
?CTOD(cDate)+100            && Returns 04/11/2003.
```
