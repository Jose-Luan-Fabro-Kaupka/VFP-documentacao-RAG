# Função CPDBF( )

Retorna a página de código com a qual uma tabela aberta foi marcada.

```foxpro
CPDBF([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica o número da área de trabalho.
**cTableAlias**
Especifica o alias da tabela. Inclua nWorkArea ou cTableAlias para especificar uma tabela aberta em uma área de trabalho diferente da área de trabalho atual. CPDBF( ) retorna 0 se uma tabela não estiver aberta na área de trabalho especificada. Se uma tabela não tiver o alias especificado com cTableAlias , o Visual FoxPro gera uma mensagem de erro.

# Observações

DISPLAY STRUCTURE também exibe a página de código com a qual uma tabela aberta foi marcada.

Para obter informações adicionais sobre páginas de código e o suporte internacional do Visual FoxPro, consulte Páginas de código suportadas pelo Visual FoxPro e Desenvolvimento de aplicativos internacionais.
