# Comando READ EVENTS

Inicia o processamento de eventos.

```foxpro
READ EVENTS
```

# Observações

Quando READ EVENTS é emitido, o Visual FoxPro inicia o processamento de eventos.

Emita CLEAR EVENTS para interromper o processamento de eventos. Quando CLEAR EVENTS é emitido, a execução do programa continua na linha imediatamente após READ EVENTS.

Observe que apenas um READ EVENTS pode estar ativo por vez. Se um READ EVENTS estiver em vigor, quaisquer comandos READ EVENTS subsequentes não terão efeito.
