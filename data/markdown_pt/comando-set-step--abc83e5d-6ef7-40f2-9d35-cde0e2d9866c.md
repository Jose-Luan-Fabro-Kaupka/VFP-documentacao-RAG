# Comando SET STEP

Abre a janela Trace e suspende a execução do programa para depuração.

```foxpro
SET STEP ON
```

#### Parâmetros
 **ON**
Abre a janela Trace e suspende a execução do programa.

# Observações

SET STEP é usado para depurar programas. Você pode inserir SET STEP ON em um programa no ponto em que deseja executar comandos individualmente.

Para obter informações sobre a janela Trace, consulte Testando e depurando aplicativos.

Você pode passar parâmetros a um programa e rastrear sua execução seguindo estas etapas:
 - Abra a janela Trace.
- No menu Program da janela Trace, escolha Open e selecione o programa a rastrear.
- Defina um ponto de interrupção na primeira linha executável do programa.
- Na janela Command, execute o programa com DO ... WITH os parâmetros.
