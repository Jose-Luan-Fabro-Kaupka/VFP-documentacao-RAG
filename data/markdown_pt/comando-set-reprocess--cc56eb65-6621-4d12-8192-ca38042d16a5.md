# Comando SET REPROCESS

Especifica quantas vezes e por quanto tempo o Visual FoxPro tenta bloquear um arquivo ou registro após uma tentativa de bloqueio sem sucesso.

```foxpro
SET REPROCESS TO nAttempts [SECONDS] [SYSTEM] | TO AUTOMATIC [SYSTEM]
```

#### Parâmetros
 **TO nAttempts [SECONDS]**
Especifica o número de vezes que o Visual FoxPro tenta bloquear um registro ou arquivo após uma tentativa inicial sem sucesso. O valor padrão é 0, o valor máximo é 32.000. SECONDS especifica que o Visual FoxPro tenta bloquear um arquivo ou registro por nAttempts segundos. Está disponível somente quando nAttempts é maior que zero. Por exemplo, se nAttempts é 30, o Visual FoxPro tenta bloquear um registro ou arquivo até 30 vezes. Se você também incluir SECONDS ( SET REPROCESS TO 30 SECONDS ), o Visual FoxPro tenta continuamente bloquear um registro ou arquivo por até 30 segundos. Uma mensagem do sistema ("Waiting for lock ... ") aparece se SET STATUS estiver definido como ON. Se uma rotina ON ERROR estiver em vigor e tentativas de um comando de bloquear o registro ou arquivo não tiverem sucesso, a rotina ON ERROR é executada. No entanto, se uma função tentar o bloqueio, uma rotina ON ERROR não é executada e a função retorna false (.F.). Se uma rotina ON ERROR não estiver em vigor, um comando tenta bloquear o registro ou arquivo e o bloqueio não pode ser colocado, um alerta apropriado aparece (por exemplo, "Record is in use by another"). Se uma função tentar colocar o bloqueio, o alerta não é exibido e a função retorna false (.F.). Se nAttempts é 0 (o valor padrão) e você emite um comando ou função que tenta bloquear um registro ou arquivo, o Visual FoxPro tenta bloquear o registro ou arquivo indefinidamente. O Visual FoxPro exibe a mensagem do sistema "Attempting to lock... Press Escape to Cancel" enquanto tenta bloquear o registro ou arquivo. O bloqueio é colocado e a mensagem do sistema é limpa se o registro ou arquivo ficar disponível para bloqueio enquanto você aguarda. Se uma função tentou colocar o bloqueio, a função retorna true (.T.). Se você pressionar ESC em resposta à mensagem do sistema, um alerta apropriado aparece (por exemplo, "Record is in use by another"). Se uma função tentar colocar o bloqueio, o alerta não é exibido e a função retorna false (.F.). Se uma rotina ON ERROR estiver em vigor e um comando estiver tentando bloquear o registro ou arquivo, a rotina ON ERROR tem precedência sobre tentativas adicionais de bloquear o registro ou arquivo. A rotina ON ERROR é executada imediatamente. O Visual FoxPro não tenta bloqueios adicionais de registro ou arquivo e não exibe a mensagem do sistema. Se nAttempts é –1, o Visual FoxPro tenta bloquear o registro ou arquivo indefinidamente. Você não pode cancelar as tentativas de bloqueio pressionando a tecla ESC, e uma rotina ON ERROR não é executada. Definir nAttempts como -2 é equivalente a usar a cláusula TO AUTOMATIC. O Visual FoxPro exibe a mensagem do sistema "Waiting for lock ... " somente se SET STATUS estiver definido como ON. Se um bloqueio foi colocado por outro usuário no registro ou arquivo que você está tentando bloquear, você deve aguardar até que o usuário libere o bloqueio.
**TO AUTOMATIC**
Especifica que o Visual FoxPro tenta bloquear o registro ou arquivo indefinidamente (equivalente a definir nAttempts como –2 ). Esta cláusula é semelhante a definir nAttempts como -1, exceto que inclui a facilidade de abandonar a tentativa de bloquear um registro ou arquivo. A mensagem do sistema "Attempting to lock ... Press Escape to Cancel" aparece enquanto o Visual FoxPro tenta bloquear o registro ou arquivo. O bloqueio é colocado e a mensagem do sistema é limpa se o registro ou arquivo ficar disponível para bloqueio enquanto você aguarda. Se uma função é usada para colocar o bloqueio, a função retorna true (.T.). Se uma rotina ON ERROR não estiver em vigor e você pressionar ESC em resposta à mensagem do sistema, um alerta apropriado aparece (por exemplo, "Record is in use by another"). Se uma função tentar colocar o bloqueio, o alerta não é exibido e a função retorna false (.F.). Se uma rotina ON ERROR estiver em vigor e ESC for pressionado, a rotina ON ERROR é executada. Se uma função tentar colocar o bloqueio, uma rotina ON ERROR não é executada e a função retorna false (.F.).
**SYSTEM**
Especifica que SET REPROCESS se aplica à sessão de dados do sistema, que controla tabelas usadas internamente, como banco de dados, FoxUser, arquivos .scx e assim por diante. Para mais informações sobre bloqueio de registros e arquivos e compartilhamento de tabelas em uma rede, consulte Programming for Shared Access .

# Observações

A primeira tentativa de bloquear um registro ou arquivo nem sempre é bem-sucedida. Frequentemente, um registro ou arquivo está bloqueado por outro usuário na rede. SET REPROCESS determina se o Visual FoxPro faz tentativas adicionais de bloquear o registro ou arquivo quando a tentativa inicial não tem sucesso. Você pode especificar quantas vezes tentativas adicionais são feitas ou por quanto tempo as tentativas são feitas. Uma rotina ON ERROR afeta como tentativas de bloqueio sem sucesso são tratadas.

SET REPROCESS tem escopo na sessão de dados atual. SET REPROCESS SYSTEM tem escopo na sessão de dados do sistema.

> **Observação:** Alterações feitas na guia Data da caixa de diálogo Tools Options afetam apenas a sessão atual.

# Exemplo

```foxpro
SET ("REPROCESS")      && Returns the current session setting
SET("REPROCESS",1)   && Returns the system session setting
* In the config.fpw file, the following code changes the default session.
REPROCESS = 100
```
