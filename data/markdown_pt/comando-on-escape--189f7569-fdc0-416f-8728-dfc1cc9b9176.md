# Comando ON ESCAPE

Especifica um comando que é executado quando você pressiona a tecla ESC durante a execução de um programa ou comando.

```foxpro
ON ESCAPE   [Command]
```

#### Parâmetros
 **Command**
Especifica o comando do Visual FoxPro a ser executado. Após a execução do comando, a execução do programa é retomada na linha imediatamente posterior à linha do programa que estava sendo executada quando você pressionou ESC. No entanto, se um procedimento especificado com ON ESCAPE incluir RETRY, a linha do programa que estava sendo executada quando você pressionou ESC será executada novamente.

# Observações

Normalmente, ON ESCAPE usa DO para executar um procedimento.

Se ON ESCAPE e ON KEY estiverem ativos e você pressionar ESC, o Visual FoxPro executará o comando especificado com ON ESCAPE.

Use ON ESCAPE sem um comando para que nenhum comando seja executado quando ESC for pressionada (o padrão).

> **Observação:** O Visual FoxPro não executa uma rotina ON ESCAPE se SET ESCAPE estiver definido como OFF.

# Exemplo

O exemplo a seguir configura um loop infinito, mas define uma rotina ON ESCAPE para encerrá-lo.

```foxpro
SET ESCAPE ON
ON ESCAPE DO stopit
WAIT WINDOW 'Press ESC to stop loop' NOWAIT
glMoreLoop = .T.
DO WHILE glMoreLoop
ENDDO
RETURN
PROCEDURE stopit
glMoreLoop = .F.
RETURN
```
