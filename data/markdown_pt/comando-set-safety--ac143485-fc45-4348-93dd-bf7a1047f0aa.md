# Comando SET SAFETY

Determina se o Visual FoxPro exibe uma caixa de diálogo antes de substituir um arquivo existente, ou se regras de tabela ou campo, valores padrão e mensagens de erro são avaliados quando alterações são feitas no Table Designer ou com ALTER TABLE.

```foxpro
SET SAFETY ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Especifica que uma caixa de diálogo é exibida antes de você substituir um arquivo existente. A caixa de diálogo oferece a opção de substituir o arquivo existente. Para o Table Designer, especifica que regras de tabela ou campo, valores padrão e mensagens de erro são avaliados quando você salva alterações na estrutura de uma tabela. A validação de dados ocorre para regras de validação novas ou modificadas depois que você salva as alterações na estrutura da tabela. Se uma regra de validação contém uma UDF (função definida pelo usuário), a UDF não é avaliada e a regra de validação é ignorada. Para ALTER TABLE, regras de tabela ou campo, valores padrão e mensagens de erro são avaliados quando ALTER TABLE altera a estrutura da tabela. A validação de dados ocorre para regras de validação novas ou modificadas quando ALTER TABLE altera a estrutura da tabela. Se uma regra de validação contém uma UDF (função definida pelo usuário), a UDF não é avaliada e a regra de validação é ignorada.
**OFF**
Especifica que uma caixa de diálogo não é exibida antes de um arquivo existente ser substituído. Observe que, para servidores de automação .dll in-process, a configuração padrão de SET SAFETY é OFF. Para o Table Designer, especifica que regras de tabela ou campo, valores padrão e mensagens de erro não são avaliados quando você salva alterações na estrutura de uma tabela. No entanto, a validação de dados ocorre para regras de validação novas ou modificadas depois que você salva as alterações na estrutura da tabela. Para ALTER TABLE, regras de tabela ou campo, valores padrão e mensagens de erro não são avaliados quando ALTER TABLE altera a estrutura da tabela. A validação de dados não ocorre para regras de validação novas ou modificadas depois que ALTER TABLE altera a estrutura da tabela.

# Observações

SET SAFETY tem escopo na sessão de dados atual.
