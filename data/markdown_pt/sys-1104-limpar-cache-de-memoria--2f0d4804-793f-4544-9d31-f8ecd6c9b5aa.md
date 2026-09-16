# SYS(1104) - Limpar cache de memória

Limpa a memória em cache por programas e dados, e limpa e atualiza buffers para tabelas abertas.

```foxpro
SYS(1104 [, cAlias | nWorkArea])
```

#### Parâmetros
 **cAlias**
Especifica o alias de uma tabela ou cursor específico para o qual a memória em cache é limpa.
**nWorkArea**
Especifica a área de trabalho de uma tabela ou cursor específico para o qual a memória em cache é limpa.

# Valor de retorno

Caractere. SYS(1104) retorna o número de bytes que não puderam ser limpos. SYS(1104) retorna "0" se toda a memória for limpa.

# Observações

Você pode melhorar o desempenho chamando SYS(1104) após executar comandos que fazem uso extensivo de buffers de memória. Esta função também limpa buffers internos para tabelas abertas, forçando as tabelas a serem atualizadas, o que é útil com tabelas grandes e em ambientes multiusuário.

> **Observação:** O uso de SYS(1104) reduzirá o desempenho em aplicativos que têm um grande número de tabelas em buffer abertas.

Inclua o parâmetro opcional cAlias ou nWorkArea para limpar o cache de memória de uma tabela ou cursor específico. Isso pode ser útil em cenários multiusuário que usam a função INDEXSEEK( ) para pesquisar tabelas indexadas.
