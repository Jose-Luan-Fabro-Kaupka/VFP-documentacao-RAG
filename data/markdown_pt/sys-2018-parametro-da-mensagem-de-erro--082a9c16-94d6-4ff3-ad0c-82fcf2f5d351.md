# SYS(2018) - Parâmetro da mensagem de erro

Retorna o parâmetro da mensagem de erro mais recente.

Para determinadas mensagens de erro, SYS(2018) retorna informações sobre a causa do erro mais recente, como os nomes de variáveis e arquivos, chamados de parâmetros da mensagem de erro. Essas mensagens de erro geralmente contêm um espaço reservado, por exemplo, "Class file "name" is invalid." Portanto, se você fizer referência a um nome de arquivo que não existe, o nome da variável será incluído na mensagem de erro.

```foxpro
SYS(2018)
```

# Valor de retorno

Character. SYS(2018) retorna o parâmetro da mensagem de erro.

# Exemplo

Suponha que você tente executar um programa chamado REPORTS, mas o programa não exista e seja exibida a mensagem de erro "File REPORTS does not exist." SYS(2018) retorna a palavra "REPORTS". A palavra "REPORTS" é o parâmetro da mensagem de erro.

```foxpro
? SYS(2018)
```
