# Variável de sistema _THROTTLE

Especifica a velocidade de execução de programas quando a janela Trace está aberta.

```foxpro
_THROTTLE = nSeconds
```

#### Parâmetros
 **nSeconds**
Especifica o atraso em segundos entre a execução de cada linha do programa. O valor padrão de inicialização é 0, sem pausa entre a execução das linhas do programa. nSeconds pode variar de 0 a 5,5 segundos. Por exemplo, se nSeconds for 0,5 segundos, ocorre um atraso de 1/2 segundo entre a execução das linhas do programa.

# Observações

A janela Trace, uma das ferramentas de depuração disponíveis no Visual FoxPro, exibe o código-fonte de um programa conforme o programa é executado. A janela Trace destaca cada linha no programa quando a linha é executada. O valor numérico de _THROTTLE determina o atraso entre a execução de cada linha do programa quando a janela Trace está aberta.

> **Observação:** A opção Trace Between Breaks no menu Program da janela Trace deve estar ativada para que ocorra um atraso.
