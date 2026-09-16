# Comando PRINTJOB ... ENDPRINTJOB

Ativa as configurações para variáveis de sistema de trabalho de impressão.

```foxpro
PRINTJOB
      Commands
ENDPRINTJOB
```

#### Parâmetros
 **Commands**
Especifica os comandos do Visual FoxPro que são executados até que o trabalho de impressão seja concluído.

# Observações

PRINTJOB ... ENDPRINTJOB inicializa a impressora e certas variáveis de sistema que afetam a saída impressa. Ele pode enviar códigos de controle para a impressora, ejetar uma página da impressora antes e/ou depois de um trabalho de impressão, inicializar o número da coluna da impressora e controlar o número de cópias impressas.

PRINTJOB executa estas tarefas:
 - Envia códigos de controle de impressora iniciais, armazenados na variável de sistema _PSCODE, para a impressora. Para obter mais informações sobre códigos de controle de impressora, consulte o tópico System Variables Overview e o manual da sua impressora.
- Ejeta uma página se a variável de sistema _PEJECT estiver definida como BEFORE ou BOTH.
- Define a variável de sistema _PCOLNO como 0. _PCOLNO armazena o número da coluna da impressora.

ENDPRINTJOB executa estas tarefas:
 - Envia códigos de controle de impressora finais, armazenados na variável de sistema _PECODE, para a impressora. Você pode redefinir a impressora para a configuração que tinha antes de PRINTJOB ser emitido.
- Ejeta uma página se a variável de sistema _PEJECT estiver definida como AFTER ou BOTH.
- Faz loop de volta para PRINTJOB para imprimir outra cópia do relatório se a variável de sistema _PCOPIES estiver definida com um valor maior que 1 (o padrão). O valor da variável de sistema _PCOPIES determina o número de cópias. Quando o número de cópias impressas é igual ao valor de _PCOPIES, o Visual FoxPro sai do loop. O controle do programa então começa com o comando imediatamente após ENDPRINTJOB.

PRINTJOB e ENDPRINTJOB podem ser executados apenas a partir de um programa. Você não pode aninhar comandos PRINTJOB ... ENDPRINTJOB.
