# SYS(2450) - Ordem do caminho de pesquisa da aplicação

Especifica como uma aplicação pesquisa dados e recursos, como funções, procedimentos, arquivos executáveis e assim por diante.

Você pode usar SYS(2450) para especificar que o Visual FoxPro pesquisa dentro de uma aplicação por um procedimento ou função definida pelo usuário (UDF) específico antes de pesquisar nos locais SET DEFAULT e SET PATH. Definir SYS(2450) pode ajudar a melhorar o desempenho de aplicações que são executadas em uma rede local ou de área ampla.

```foxpro
SYS(2450 [, 0 | 1 ])
```

#### Parâmetros
 **0**
Pesquisa nos locais de caminho e padrão antes de pesquisar na aplicação. (Padrão)
**1**
Pesquisa dentro da aplicação pelo procedimento ou UDF especificado antes de pesquisar nos locais de caminho e padrão.

# Valor de retorno

Tipo de dados Character. Chamar SYS(2450) sem parâmetros retorna um valor de "0" ou "1" especificando se o Visual FoxPro pesquisa nos locais de caminho e padrão antes de pesquisar na aplicação ou dentro da aplicação primeiro.

# Observações

Você pode usar SET PROCEDURE para garantir que o arquivo seja encontrado antes que a pesquisa de caminho ocorra. No entanto, você deve chamar SET PROCEDURE para cada arquivo.
