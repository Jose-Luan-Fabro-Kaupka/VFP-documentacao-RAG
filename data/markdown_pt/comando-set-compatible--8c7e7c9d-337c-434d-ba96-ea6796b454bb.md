# Comando SET COMPATIBLE

Controla a compatibilidade com Microsoft FoxBASE+ e outras linguagens FoxPro.

```foxpro
SET COMPATIBLE FOXPLUS | OFF | DB4 | ON [PROMPT | NOPROMPT]
```

#### Parâmetros
 **FOXPLUS | OFF**
(Padrão) Essas duas palavras-chave podem ser usadas de forma intercambiável. Cada uma permite que programas criados no FoxBASE+ sejam executados no Microsoft Visual FoxPro sem alterações.
**DB4 | ON**
Essas duas palavras-chave podem ser usadas de forma intercambiável. Incluir qualquer palavra-chave afeta o comportamento dos comandos e funções listados abaixo.
**PROMPT | NOPROMPT**
Essas opções determinam se o Visual FoxPro exibe uma caixa de diálogo quando você abre uma tabela dBASE que contém um campo memo. Inclua a opção PROMPT para exibir a caixa de diálogo Convert Memos. Se você abrir uma tabela dBASE IV que contém um campo memo, o Visual FoxPro por padrão exibe a caixa de diálogo Convert Memos, que permite converter o arquivo memo dBASE para um formato Visual FoxPro. Você deve converter o arquivo memo para um formato Visual FoxPro para abrir a tabela no Visual FoxPro. Se você incluir NOPROMPT, a caixa de diálogo Convert Memos não é exibida quando você abre uma tabela dBASE IV que contém um campo memo. O arquivo memo dBASE é automaticamente convertido para um formato Visual FoxPro.

# Observações

Comandos e funções afetados por SET COMPATIBLE incluem LIKE( ), PLAY MACRO, SELECT( ) e STORE (quando STORE é usado com arrays).

SET COMPATIBLE não cria compatibilidade com outros comandos, funções ou recursos não suportados no Visual FoxPro. Por exemplo, não permite abrir um formulário de relatório criado em outros produtos com o Report Designer.

A tabela a seguir lista os comandos afetados por SET COMPATIBLE.
 Comandos
| @ ... GET com uma cláusula RANGE | PLAY MACRO |
| --- | --- |
| @ ... SAY com CHR(7) | READ com uma cláusula @ ... GET VALID |
| @ ... SAY com rolagem | READs aninhados |
| @ ... SAY quando STATUS está ON | READ |
| ACTIVATE SCREEN | RUN | ! |
| ACTIVATE WINDOW | SET COLOR TO |
| APPEND MEMO | SET BORDER |
| BROWSE | SET FIELDS |
| DECLARE | SET MESSAGE |
| DIMENSION | SET MEMOWIDTH |
| GO | GOTO com SET TALK ON | SET PRINTER to <file> |
| FSIZE( ) | STORE |
| INKEY( ) | SUM |
| LASTKEY( ) | TRANSFORM( ) com uma cláusula PICTURE numérica |
| LIKE( ) | SELECT( ) |
| Comandos de menu | SYS(2001, "COLOR") |
