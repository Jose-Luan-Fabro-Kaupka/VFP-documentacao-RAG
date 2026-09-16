# Comando PLAY MACRO

Executa uma macro de teclado.

```foxpro
PLAY MACRO MacroName [TIME nDelay]
```

#### Parâmetros
 **MacroName**
Especifica o nome da macro de teclado a ser executada.
**TIME nDelay**
Especifica o intervalo de tempo entre a entrega de cada tecla em uma macro de teclado. O tempo de atraso deve estar entre 0 e 10 segundos. nDelay pode ser avaliado como um número com fração decimal. Por exemplo, se você especificar nDelay igual a 1.5, as teclas da macro serão executadas com um atraso de um segundo e meio entre cada tecla.

# Observações

Você pode salvar uma série de teclas como uma macro de teclado escolhendo Macros no menu Tools. PLAY MACRO executa essa série de teclas. Executar macros de teclado dentro de programas permite que você crie programas de demonstração autônomos.

Se você emitir PLAY MACRO na janela Command, ele é executado imediatamente. Se PLAY MACRO for emitido em um programa, a execução é adiada até que o programa execute um comando que permita entrada de teclado. Exemplos de comandos que aguardam entrada são @ ... GET, BROWSE, CHANGE e EDIT.

Se uma série de comandos PLAY MACRO estiver pendente em um programa, o Visual FoxPro não executa os comandos na ordem em que foram emitidos. As macros são executadas em ordem inversa — o primeiro PLAY MACRO executa por último, o último PLAY MACRO executa primeiro — em sua ordem de baixo para cima dentro do programa.
