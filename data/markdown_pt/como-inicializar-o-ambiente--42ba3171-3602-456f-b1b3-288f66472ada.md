# Como: inicializar o ambiente

Quando o Visual FoxPro inicia, o ambiente de desenvolvimento padrão do Visual FoxPro estabelece certos valores para comandos SET e variáveis de sistema. No entanto, essas configurações podem não ser o melhor ambiente para seu aplicativo. Portanto, a primeira tarefa que o arquivo principal ou o objeto de aplicativo deve executar é configurar o ambiente para o aplicativo.

> **Dica:** É recomendável salvar as configurações iniciais do ambiente e modificá-las para configurar um ambiente específico para seu aplicativo. Para ver os valores padrão do ambiente de desenvolvimento do Visual FoxPro, inicie o Visual FoxPro sem um arquivo de configuração digitando VFP -C e depois chame o comando DISPLAY STATUS. Para obter mais informações, consulte DISPLAY STATUS Command.

### Para visualizar e salvar configurações do ambiente atual
- No menu Tools, clique em Options.
- Na caixa de diálogo Options, pressione e mantenha pressionada a tecla SHIFT enquanto clica em OK. Os comandos SET e outras configurações de ambiente são exibidos na janela Command.
- Na janela Command, copie e cole os comandos SET e as configurações de ambiente em um arquivo de programa de configuração.

Agora você pode editar os comandos SET e as configurações de ambiente conforme apropriado para seu aplicativo. No ambiente do seu aplicativo, você pode querer incluir código para executar o seguinte:
 - Inicializar variáveis.
- Estabelecer um caminho padrão.
- Abrir bancos de dados, tabelas livres e índices necessários. Se seu aplicativo requer acesso a dados remotos, a rotina de inicialização também pode solicitar ao usuário as informações de login necessárias.
- Referenciar arquivos de biblioteca e procedimento externos.

Por exemplo, suponha que você queria testar o valor padrão do comando SET TALK, armazenar o valor e definir TALK como OFF para seu aplicativo. Você pode colocar o seguinte código em seu procedimento de configuração:

```foxpro
IF SET('TALK') = "ON"
   SET TALK OFF
   cTalkVal = "ON"
ELSE
   cTalkVal = "OFF"
ENDIF
```

Para obter mais informações, consulte SET Command Overview.
