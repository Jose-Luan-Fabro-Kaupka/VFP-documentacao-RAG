# Função SKPBAR( )

Determina se um item de menu está habilitado ou desabilitado com SET SKIP OF.

```foxpro
SKPBAR(cMenuName, MenuItemNumber)
```

#### Parâmetros
 **cMenuName**
Especifica o nome do menu que contém o item.
**MenuItemNumber**
Especifica o número do item de menu cujo status (habilitado ou desabilitado) SKPBAR( ) retorna. O número do item de menu é atribuído quando o item de menu é criado com DEFINE BAR.

# Valor de retorno

Lógico

# Observações

SKPBAR( ) retorna true (.T.) se o item de menu estiver desabilitado e false (.F.) se o item de menu estiver habilitado.
