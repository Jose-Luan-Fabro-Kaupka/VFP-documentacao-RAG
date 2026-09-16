# Comando HELP

Abre a janela Help.

```foxpro
HELP   [Topic | ID nContextID] [IN [WINDOW] WindowName | IN [WINDOW]
   SCREEN | IN [WINDOW] [NOWAIT]
```

#### Parâmetros
 **Topic**
Especifica o tópico de ajuda a ser exibido. Se você incluir apenas uma grafia parcial de um título de tópico, o Visual FoxPro abre a janela Help e exibe o tópico com o título mais próximo.
**ID nContextID**
Especifica o tópico de ajuda a ser exibido, com base no ID de contexto do tópico. Quando você está usando ajuda no estilo gráfico, nContextID é um número de contexto na seção MAP do arquivo de projeto de ajuda.
**IN [WINDOW] WindowName**
Abre a janela Help dentro de uma janela pai. A janela Help não assume as características da janela pai na qual é colocada. Se a janela Help é ativada dentro de uma janela pai, ela não pode ser movida para fora da janela pai. Se a janela pai for movida, a janela Help se move com ela. Antes de poder abrir a janela Help a partir de uma janela pai, a janela pai deve primeiro ser definida com DEFINE WINDOW .
**IN [WINDOW] SCREEN**
Coloca explicitamente a janela Help na janela principal do Visual FoxPro.
**NOWAIT**
Na ajuda no estilo gráfico, o argumento NOWAIT não tem efeito, e a execução do programa sempre continua depois que o comando HELP foi emitido.

# Observações
