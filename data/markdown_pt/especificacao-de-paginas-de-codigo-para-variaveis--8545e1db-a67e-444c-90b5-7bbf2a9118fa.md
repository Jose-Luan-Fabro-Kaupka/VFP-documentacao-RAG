# Especificação de páginas de código para variáveis

Você pode querer manipular dados internacionais de certas maneiras. Por exemplo, você pode querer traduzir os dados em uma variável para outra página de código, ou pode querer impedir a tradução de dados em um campo de caractere ou memo.

# Traduzindo dados em variáveis

Se o código em seu aplicativo incluir uma variável contendo dados de outra página de código, você pode traduzir os dados para a página de código adequada usando a função CPCONVERT( ). Por exemplo, suponha que a variável `x` contenha dados criados com a página de código Macintosh (10000). Para traduzir os dados para a página de código Windows (1252), execute o seguinte comando:

```foxpro
cConvert=CPCONVERT(10000,1252,x)
```

No Windows, os dados convertidos parecem exatamente como você os vê no Macintosh. Por exemplo, um caractere que parece "" no Macintosh parece idêntico no Windows.
