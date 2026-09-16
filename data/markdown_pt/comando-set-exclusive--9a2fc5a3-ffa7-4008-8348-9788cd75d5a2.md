# Comando SET EXCLUSIVE

Especifica se o Visual FoxPro abre arquivos de tabela para uso exclusivo ou compartilhado em uma rede.

```foxpro
SET EXCLUSIVE ON | OFF
```

#### Parâmetros
 **ON**
(O padrão para a sessão de dados global.) Limita a acessibilidade de uma tabela aberta em uma rede ao usuário que a abriu. A tabela não é acessível a outros usuários na rede. Diferentemente de FLOCK( ), SET EXCLUSIVE ON também impede que todos os outros usuários tenham acesso somente leitura. Um arquivo também pode ser aberto em uma rede para uso exclusivo incluindo a cláusula EXCLUSIVE com o comando USE. Não é necessário realizar bloqueio de registro ou arquivo em uma tabela aberta para uso exclusivo. Abrir uma tabela para uso exclusivo garante que o arquivo não possa ser alterado por outros usuários. Para alguns comandos, a execução não é possível até que uma tabela seja aberta para uso exclusivo. Esses comandos são INSERT, INSERT BLANK, MODIFY STRUCTURE, PACK, REINDEX e ZAP.
**OFF**
(O padrão para uma sessão de dados privada.) Permite que uma tabela aberta em uma rede seja compartilhada e modificada por qualquer usuário na rede. Para informações adicionais sobre bloqueio de registro e arquivo e compartilhamento de tabelas em uma rede, consulte Programação para acesso compartilhado .

# Observações

Alterar a configuração de SET EXCLUSIVE não altera o status de tabelas abertas anteriormente. Por exemplo, se uma tabela é aberta com SET EXCLUSIVE definido como ON, e SET EXCLUSIVE é posteriormente alterado para OFF, a tabela mantém seu status de uso exclusivo.

SET EXCLUSIVE tem escopo na sessão de dados atual.
