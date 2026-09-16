# Comando SET DATASESSION

Ativa a sessão de dados do formulário especificado.

```foxpro
SET DATASESSION TO [nDataSessionNumber]
```

#### Parâmetros
 **nDataSessionNumber**
Especifica a sessão de dados de um formulário a ser ativada. Se você omitir nDataSessionNumber , a sessão de dados 1 (a sessão de dados Global) é ativada.

# Observações

Por padrão, a sessão de dados 1, a sessão de dados Global, está ativa quando você inicia o Visual FoxPro.

A propriedade DataSession de um formulário determina se o formulário tem sua própria sessão de dados exclusiva quando o formulário é criado. Se a propriedade DataSession de um formulário estiver definida como 2, o formulário tem sua própria sessão de dados; caso contrário, uma sessão de dados não é criada para o formulário. Você pode usar a propriedade somente leitura DataSessionId do formulário para determinar o número da sessão de dados do formulário.

Uma sessão de dados é fechada quando o formulário que criou a sessão de dados é liberado.

SET DATASESSION normalmente é usado para depurar formulários. Deve-se ter cuidado ao emitir este comando quando um formulário está ativo, pois tabelas em sessões de dados não atuais não são acessíveis.

Os seguintes comandos SET têm escopo na sessão de dados atual:
 SET Commands
| SET ANSI | SET AUTOSAVE |
| --- | --- |
| SET BLOCKSIZE | SET CARRY |
| SET CENTURY | SET COLLATE |
| SET CONFIRM | SET CURRENCY |
| SET DATABASE | SET DATE |
| SET DECIMALS | SET DELETED |
| SET DELIMITERS | SET EXACT |
| SET EXCLUSIVE | SET FIELDS |
| SET FIXED | SET HOURS |
| SET LOCK | SET MARK TO |
| SET MEMOWIDTH | SET MULTILOCKS |
| SET NEAR | SET NULL |
| SET POINT | SET REPROCESS |
| SET SAFETY | SET SECONDS |
| SET SEPARATOR | SET SYSFORMATS |
| SET TALK | SET UNIQUE |
