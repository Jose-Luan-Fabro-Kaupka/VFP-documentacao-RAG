# Comando SET NEAR

Determina onde o ponteiro de registro é posicionado depois que FIND ou SEEK pesquisa um registro sem sucesso.

```foxpro
SET NEAR ON | OFF
```

#### Parâmetros
 **ON**
Posiciona o ponteiro de registro no registro correspondente mais próximo se uma pesquisa de registro usando FIND ou SEEK não for bem-sucedida. Com esta configuração, RECNO( ) retorna o número do registro correspondente mais próximo, FOUND( ) retorna false (.F.) e EOF( ) retorna false (.F.).
**OFF**
(Padrão) Posiciona o ponteiro de registro no final da tabela se uma pesquisa de registro usando FIND ou SEEK não for bem-sucedida. Com esta configuração, RECNO( ) retorna o número de registros na tabela mais 1, FOUND( ) retorna false (.F.) e EOF( ) retorna true (.T.).

# Observações

Uma pesquisa não é bem-sucedida quando nenhum registro atende aos critérios de pesquisa.

Emitir RECNO( ) com um argumento 0 retorna o número do registro correspondente mais próximo se uma pesquisa não for bem-sucedida, independentemente da configuração de SET NEAR.

SET NEAR tem escopo na sessão de dados atual.
