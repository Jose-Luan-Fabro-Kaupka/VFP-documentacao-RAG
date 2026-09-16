# Variável de sistema _SHELL

Especifica um shell de programa.

```foxpro
_SHELL = cCommand
```

# Observações

A variável de memória de sistema _SHELL é usada para impedir o acesso à janela Command enquanto um programa está em execução no Visual FoxPro. O comando DO com o nome de um programa a ser executado geralmente é armazenado em _SHELL.

Você também pode especificar um comando a ser executado quando o Visual FoxPro é iniciado colocando o item de configuração SHELL no arquivo de configuração do Visual FoxPro.

O exemplo a seguir demonstra como _SHELL normalmente pode ser usado.
 - Um programa de inicialização chamado Mystart.prg é usado para iniciar outro programa chamado Myapp.prg. Mystart.prg armazena o comando para executar Myapp.prg em _SHELL. Isso inicia Myapp.prg. Antes que o Visual FoxPro exiba a janela Command, _SHELL é verificado para um comando. Se _SHELL contém um comando, ele é executado e o Visual FoxPro então armazena a cadeia de caracteres vazia em _SHELL.
- Depois que o código de inicialização em Myapp.prg é executado com sucesso, o comando para iniciar Myapp.prg é armazenado novamente em _SHELL. O Visual FoxPro não executa o comando nem armazena a cadeia de caracteres vazia em _SHELL, e o acesso à janela Command é impedido. (A janela Command não pode ser acessada quando _SHELL contém qualquer coisa além da cadeia de caracteres vazia).
- Antes que Myapp.prg termine a execução, ele armazena a cadeia de caracteres vazia em _SHELL para restaurar o acesso à janela Command. *** MYSTART.PRG *** ... _SHELL = "DO MYAPP.PRG" *** MYAPP.PRG *** *** Initialization Code *** ... *** Initialization Code successfully completed? *** _SHELL = "DO MYAPP.PRG" && Prevents access to Command window ... *** Clean up Code *** _SHELL = ""
