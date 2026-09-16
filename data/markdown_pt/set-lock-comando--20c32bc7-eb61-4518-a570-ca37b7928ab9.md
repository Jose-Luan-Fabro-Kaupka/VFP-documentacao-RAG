# SET LOCK Comando

Ativa ou desativa o bloqueio automático de arquivos em determinados comandos.

```foxpro
SET LOCK ON | OFF
```

#### Parâmetros
 **ON**
Especifica que os comandos listados abaixo bloqueiam automaticamente a tabela quando são executados. Isso fornece acesso somente leitura a outros usuários na rede e garante que você esteja usando os dados mais atuais.
**OFF**
(Padrão) Permite o acesso compartilhado de tabelas com os comandos listados abaixo. Use SET LOCK OFF se não precisar das informações mais atuais de uma tabela.

# Observações
O Visual FoxPro não bloqueia um arquivo ao executar comandos que exigem acesso somente leitura a uma tabela. Esses comandos incluem o seguinte:

| Commands | |
| --- | --- |
| AVERAGE | JOIN (ambos os arquivos) |
| CALCULATE | LIST |
| COPY TO | LABEL |
| COPY TO ARRAY | REPORT |
| COUNT | SORT |
| DISPLAY (com escopo) | SUM |
| INDEX | TOTAL |

Enquanto são executados, esses comandos não alteram o conteúdo de uma tabela e o acesso à tabela fica disponível para outros usuários na rede. Assim, a tabela pode ser alterada enquanto você executa um desses comandos. Por exemplo, você pode começar a imprimir um relatório usando REPORT antes que outro usuário altere um registro incluído no relatório. Seu relatório agora contém informações desatualizadas.

SET LOCK tem como escopo a sessão de dados atual.
