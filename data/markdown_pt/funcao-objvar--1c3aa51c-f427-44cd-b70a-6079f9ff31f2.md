# Função OBJVAR( )

Incluída para compatibilidade com versões anteriores. Para controles, use a propriedade Name (Visual FoxPro).

Retorna o nome da variável de memória, elemento de array ou campo associado a um objeto.

```foxpro
OBJVAR([expN1> [, expN2]])
```

#### Parâmetros
 expN1

 Se expN1 for omitido, OBJVAR() retornará a variável de memória, o elemento de array ou o campo do objeto atualmente ativo. _CUROBJ pode ser usado para determinar esse objeto.

 Inclua expN1 para retornar esses dados para um objeto específico. expN1 corresponde à ordem de criação dos objetos: 1 para o primeiro, 2 para o segundo e assim por diante.

 OBJVAR() retorna a cadeia de caracteres vazia se expN1 for maior que o número de objetos.

 expN2

 READs aninhados são criados emitindo @ ... GETs e um READ em uma rotina chamada durante um READ. Eles podem ser aninhados em até cinco níveis. Para retornar nomes de variáveis de memória e elementos de array de outro nível, inclua o número opcional expN2. Se omitido, OBJVAR() usa o nível de leitura atual.

# Valor de retorno

Retorna: Character

# Observações

Você pode usar @ ... GET e @ ... EDIT para criar controles também chamados de objetos. São considerados objetos campos, caixas de seleção, listas, pop-ups, botões invisíveis, de ação e de opção, spinners e regiões de edição de texto. OBJVAR() retorna o nome da variável de memória, elemento de array ou campo no qual um deles armazena um valor.

Nomes de variáveis de memória e elementos de array são prefixados por M e ponto (M.). Nomes de campo são prefixados pelo alias da tabela e ponto.
