# Comando SET DELIMITERS

Incluído para compatibilidade com versões anteriores. Use a propriedade Format em vez disso.

Especifica se os campos de entrada @ ... GET são delimitados ou não.

```foxpro
SET DELIMITERS ON | OFF
SET DELIMITERS TO expC | TO DEFAULT
```

# Observações

SET DELIMITERS está incluído para compatibilidade com versões anteriores.

ON

 Emitir SET DELIMITERS ON exibe delimitadores em campos @ ... GET. Os caracteres delimitadores padrão são dois-pontos (:). Um dois-pontos é colocado à esquerda e à direita do campo para indicar onde inserir dados.

OFF

 Se SET DELIMITERS estiver OFF, nenhum delimitador é exibido em campos criados com @ ... GET. Esta é a configuração padrão.

TO expC

 Especifique um ou dois caracteres delimitadores com expC. Os campos são delimitados em ambos os lados pelo mesmo caractere se expC incluir um caractere. Se expC incluir dois caracteres, o primeiro caractere é o delimitador esquerdo e o segundo caractere é o delimitador direito.

TO DEFAULT

 Use SET DELIMITERS TO DEFAULT para redefinir os delimitadores para os dois-pontos padrão.
