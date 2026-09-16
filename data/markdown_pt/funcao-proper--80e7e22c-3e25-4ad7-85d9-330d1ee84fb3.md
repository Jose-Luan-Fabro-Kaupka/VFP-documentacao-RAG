# Função PROPER( )

Retorna, a partir de uma expressão de caracteres, uma cadeia de caracteres capitalizada de forma adequada para nomes próprios.

```foxpro
PROPER(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres da qual PROPER( ) retorna uma cadeia de caracteres capitalizada.

# Valor de retorno

Character

# Exemplo

```foxpro
STORE 'Visual FoxPro' TO gcExpr1
CLEAR
? PROPER(gcExpr1)  && Displays "Visual Foxpro"
STORE 'VISUAL FOXPRO' TO gcExpr2
? PROPER(gcExpr2)  && Displays "Visual Foxpro"
```
