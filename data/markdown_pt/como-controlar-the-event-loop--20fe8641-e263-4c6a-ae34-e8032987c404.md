# Como: Controlar the Event Loop

Depois de configurar o ambiente e exibir a interface do usuário inicial, seu aplicativo precisa estabelecer o loop de eventos an para poder detectar e responder à interação do usuário. Quando o usuário sai do aplicativo, seu aplicativo deve fornecer uma maneira de encerrar o loop de eventos the.

> **Nota:** Você precisa estabelecer uma maneira de sair do loop de eventos the antes de iniciá-lo. Certifique-se de que a interface do usuário do aplicativo tenha um mecanismo, por exemplo, um botão Sair ou um comando Sair menu, para encerrar o loop de eventos the.

### Para estabelecer o loop de eventos the
- No arquivo principal da sua aplicação, inclua o comando READ EVENTS.

O comando READ EVENTS faz com que o Visual FoxPro comece a processar eventos do usuário, como cliques do mouse e pressionamentos de teclas. Para obter mais informações, consulte READ EVENTS Comando.

> **Nota:** Se você não incluir o comando READ EVENTS, seu aplicativo retornará ao sistema operacional após a execução. É importante colocar o comando READ EVENTS corretamente em seu arquivo principal porque todo o processamento no arquivo principal é suspenso a partir do momento em que ele executa o comando READ EVENTS até que ele execute um comando CLEAR EVENTS subsequente. Por exemplo, você pode chamar o comando READ EVENTS como o comando last em um procedimento de inicialização e após inicializar o ambiente e exibir a interface do usuário.

Após o início do loop de eventos the, o aplicativo é executado sob o controle the do elemento da interface do usuário exibido pela última vez. Por exemplo, suponha que você inclua apenas o comando following no arquivo principal:

```foxpro
DO FORM STARTUP.SCX
```

O aplicativo exibe o formulário Startup.scx. Dentro do ambiente de desenvolvimento, seu aplicativo pode ser executado corretamente na janela de comando the. No entanto, se você executar o aplicativo a partir de um menu ou tela, o aplicativo aparecerá brevemente e será encerrado.

### Para finalizar o loop de eventos the
- Chame o comando CLEAR EVENTS usando um comando ou botão menu em um formulário.

O comando CLEAR EVENTS suspende o processamento de eventos the e o controle returns para o programa que chamou o comando READ EVENTS.

> **Observação:** Normalmente, você chama o comando CLEAR EVENTS de um menu ou botão em um formulário. O arquivo principal do programa não deve chamar CLEAR EVENTS diretamente.

Para obter mais informações, consulte CLEAR Comandos.
