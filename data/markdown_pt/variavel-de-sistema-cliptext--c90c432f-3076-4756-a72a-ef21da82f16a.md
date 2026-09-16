# Variável de sistema _CLIPTEXT

Contém o conteúdo da Área de Transferência.

```foxpro
_CLIPTEXT = cExpression
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caractere a armazenar na Área de Transferência.

# Observações

Você pode colocar uma expressão de caractere cExpression na Área de Transferência com STORE ou o operador de atribuição =.

# Exemplo

Estes exemplos colocarão caminhos longos na área de transferência.

```foxpro
_cliptext=_vfp.ServerName
```

ou

```foxpro
_cliptext=getfile()
```
