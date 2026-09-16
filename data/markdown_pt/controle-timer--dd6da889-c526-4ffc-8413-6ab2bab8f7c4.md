# Controle Timer

Cria um timer que pode executar código em intervalos regulares.

```foxpro
Timer
```

# Observações

O controle Timer, que é invisível para o usuário, é útil para processamento em segundo plano. Um uso típico do timer é verificar o relógio do sistema para determinar se é hora de executar um programa ou aplicativo.

Se um controle Timer tiver sua propriedade Enabled definida como True (.T.) e imediatamente definir a propriedade como False (.F.) após uma única execução, ele pode gerar seu evento Timer várias vezes. Isso ocorre quando a propriedade Interval é menor que ou aproximadamente igual ao tempo de execução do evento Timer. Isso pode ser corrigido aumentando o valor da propriedade Interval ou diminuindo o tempo de execução do evento Timer.

Para obter informações adicionais sobre como criar timers, consulte Using Controls.
