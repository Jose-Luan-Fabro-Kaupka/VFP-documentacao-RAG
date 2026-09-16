# Comando SET ODOMETER

Especifica o intervalo de relatório do contador de registros para comandos que processam registros.

```foxpro
SET ODOMETER TO [nRecords]
```

#### Parâmetros
 **TO [ nRecords ]**
Especifica o intervalo de relatório em número de registros. O valor de nRecords pode variar de 1 a 32.767 registros. O valor padrão é 100 registros.

# Observações

Use SET ODOMETER para alterar o intervalo no qual os comandos exibem informações sobre o número de registros processados.

Por exemplo, COPY TO exibe o número de registros que são copiados para um novo arquivo enquanto o comando está sendo executado. O contador de registros pode ser desativado emitindo SET TALK OFF.
