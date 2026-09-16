# SYS(2015) - Nome exclusivo de procedimento

Retorna um nome exclusivo de procedimento com 10 caracteres, iniciado por sublinhado e seguido por uma combinação de letras e números.

```foxpro
SYS(2015)
```

# Valor de retorno

Caractere

# Observações

Use SYS(2015) para criar nomes exclusivos para itens como procedimentos, funções, arquivos, tabelas ou cursores. Você pode adicionar um prefixo ou alterar o comprimento do nome usando a função SUBSTR( ). Por exemplo, o código `"tmp"+SUBSTR(SYS(2015),4,3)` retorna `tmpCIOS`.

O nome retornado por SYS(2015) é criado com base na data e na hora do sistema. Chamar SYS(2015) mais de uma vez no mesmo intervalo de milissegundo retorna uma cadeia de caracteres exclusiva.
