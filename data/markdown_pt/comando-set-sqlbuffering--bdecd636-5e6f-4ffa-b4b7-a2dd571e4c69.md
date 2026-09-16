# Comando SET SQLBUFFERING

Especifica se os dados em uma instrução SQL - SELECT são baseados em dados em buffer ou em dados gravados em disco.

```foxpro
SET SQLBUFFERING ON | OFF
```

#### Parâmetros
 **ON**
Especifica que a instrução SQL - SELECT usa dados em buffer local, se disponíveis. Se os dados não estiverem em buffer, os dados do disco são usados.
**OFF**
(Padrão) Especifica que a instrução SQL - SELECT usa dados do disco.

# Observações

Este comando SET tem escopo na sessão de dados atual. Se você deseja mais controle no nível da tabela, use a cláusula WITH (BUFFERING = ON | OFF) na instrução SQL - SELECT. Ela substitui a instrução SET SQLBUFFERING.

Você pode usar SET("SQLBUFFERING") para consultar a configuração atual.
