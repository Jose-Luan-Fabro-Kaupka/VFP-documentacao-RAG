# Comando SUSPEND

Pausa a execução do programa e retorna ao Visual FoxPro interativo.

```foxpro
SUSPEND
```

# Observações

Enquanto um programa está pausado, você pode executar comandos intermediários, verificar valores de variáveis, abrir as janelas Trace e Debug, e assim por diante.

Todas as variáveis criadas enquanto o programa está pausado são PRIVATE.

Use RESUME para reiniciar a execução de um programa suspenso. A execução do programa continua na linha seguinte à linha que contém SUSPEND.
