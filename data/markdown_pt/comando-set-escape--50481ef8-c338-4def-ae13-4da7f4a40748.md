# Comando SET ESCAPE

Determina se pressionar a tecla ESC interrompe a execução de programas e comandos.

```foxpro
SET ESCAPE ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Permite que a execução de comandos e programas seja interrompida quando o usuário pressiona ESC. Se o usuário pressionar ESC durante a execução de um comando ou programa enquanto o ponto de inserção está na janela Command, a seguinte mensagem aparece: *** INTERRUPTED *** Se o usuário pressionar ESC durante a execução de comando ou programa, o processamento é concluído na linha atual do programa e um alerta aparece com as seguintes três opções: (Padrão) Escolha Cancel para interromper imediatamente a execução do programa e retornar à janela Command. Escolha Suspend para pausar a execução do programa e retornar à janela Command. Esta opção é útil para depurar um programa. Escolher Resume no menu Program ou emitir RESUME na janela Command reinicia o programa na linha em que foi pausado. Escolha Ignore para continuar a execução do programa na linha em que foi pausado.
**OFF**
Impede que a execução de comandos e programas seja interrompida quando o usuário pressiona ESC.
