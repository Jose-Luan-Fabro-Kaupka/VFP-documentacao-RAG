# Comando SET TABLEPROMPT

Habilita ou desabilita a exibição da Open Dialog Box (Visual FoxPro) em comandos que permitem ao usuário selecionar uma tabela (ou view) se nenhuma estiver aberta.

```foxpro
SET TABLEPROMPT ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) A caixa de diálogo Open é exibida quando nenhuma tabela ou view está aberta e um comando que requer uma tabela ou view aberta é executado. O comando SELECT - SQL do Visual FoxPro procura tabelas em todas as áreas de trabalho na sessão atual. Outros comandos procuram apenas uma tabela na área de trabalho atual, a menos que uma área de trabalho seja explicitamente especificada. Os seguintes são alguns dos comandos afetados pela configuração TABLEPROMPT. SELECT - SQL Command DELETE - SQL Command INSERT - SQL Command UPDATE - SQL Command BROWSE Command GO | GOTO Command INDEX Command PACK Command REPLACE Command (Visual FoxPro) REPORT FORM Command SET FILTER Command SKIP Command ZAP Command
**OFF**
A caixa de diálogo Open é suprimida quando nenhuma tabela ou view está aberta e um comando que requer uma tabela ou view aberta é executado. O comando falhará e um erro será gerado. Erros típicos são File "name" does not exist (Error 1) e No table is open in the current work area (Error 52) .

# Observações

Você pode usar SET("TABLEPROMPT") para determinar a configuração atual. Você também pode especificar um valor de inicialização para TABLEPROMPT em Config.fpw, o arquivo de configuração do Visual FoxPro.

Este recurso é suportado em cenários de servidor COM (MTDLL e DLL) em que os usuários não têm acesso a uma interface de usuário. SET TABLEPROMPT fornece suporte semelhante no Visual FoxPro. Você pode usar SYS(2335) - Unattended Server Mode para controlar estados modais para servidores COM.
