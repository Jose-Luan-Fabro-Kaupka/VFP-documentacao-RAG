# Comando SET EVENTLIST

Especifica eventos a rastrear na Debug Output Window ou em um arquivo especificado com SET EVENTTRACKING.

```foxpro
SET EVENTLIST TO [EventName1 [, EventName2 ...] [ADDITIVE]]
```

#### Parâmetros
 **EventName1 [, EventName2 ...]**
Especifica os nomes dos eventos a rastrear. Você pode incluir qualquer número de nomes de eventos separados por vírgulas.
**ADDITIVE**
Especifica que os eventos EventName1 , EventName2 ... são adicionados ao conjunto de eventos atualmente sendo rastreados. Se ADDITIVE for omitido, somente os eventos EventName1 , EventName2 ... são rastreados.

# Observações

Emita SET EVENTLIST TO sem nenhum nome de evento para remover todos os eventos do conjunto de eventos sendo rastreados. Você também pode especificar eventos a rastrear na Event Tracking Dialog Box.
