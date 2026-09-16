# SYS(15) - Tradução de caracteres

Incluído para compatibilidade com versões anteriores. Use o comando SET COLLATE Command em vez disso.

```foxpro
SYS(15, cTranslationExpression, cTranslated)
```

# Parâmetros
 **cTranslationExpression**
Especifica a expressão de caractere que SYS(15) usa para a tradução de cTranslated .
**cTranslated**
Especifica a expressão de caractere que é traduzida. SYS(15) pega o primeiro caractere em cTranslated e determina o valor ASCII do caractere. O caractere na mesma posição em cTranslationExpression que o valor ASCII é retornado. Este processo é repetido para cada caractere adicional em cTranslated . Se um caractere em cTranslated não tiver um caractere correspondente em cTranslationExpression , então o caractere não é traduzido.

# Valores de retorno

Caractere

# Observações

Esta função é destinada principalmente à conveniência de usuários europeus que devem usar caracteres acentuados. Como existem diferentes versões da maioria das vogais, indexar em campos contendo caracteres acentuados não preserva a ordem alfabética esperada.

Incluído com o Visual FoxPro está um arquivo de variáveis de memória chamado EUROPEAN.MEM que contém caracteres de tradução de exemplo. No FoxPro para MS-DOS e Visual FoxPro, EUROPEAN.MEM está localizado no diretório HOME( ). No FoxPro para Macintosh, EUROPEAN.MEM está localizado na pasta Goodies:Misc.

Armazenado em EUROPEAN.MEM está uma variável de memória de caractere chamada EUROPEAN, para uso com SYS(15) no FoxPro para MS-DOS. Outra variável de memória de caractere, EUROANSI, é fornecida para uso com SYS(15) no Visual FoxPro e FoxPro para Macintosh. Essas variáveis de memória podem ser usadas com SYS(15) para traduzir caracteres acentuados para os caracteres correspondentes sem os acentos.

Como exemplo, o comando a seguir pode ser usado no FoxPro para MS-DOS para indexar uma tabela em um campo contendo caracteres acentuados preservando a ordem alfabética normal:

```foxpro
INDEX ON SYS(15, european, field) TO european
```
