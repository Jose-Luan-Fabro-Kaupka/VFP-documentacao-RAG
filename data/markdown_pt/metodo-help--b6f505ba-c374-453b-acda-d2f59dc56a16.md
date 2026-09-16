# Método Help

Abre a janela Help.

```foxpro
ApplicationObject.Help([cFileName] [, nContextID] [, cHelpTopic])
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo Help a ser aberto. Inclua um caminho com o nome do arquivo Help se o arquivo não estiver no diretório padrão.
**nContextID**
Especifica o tópico Help a ser exibido, com base no ID de contexto do tópico. nContextID é um número de contexto na seção MAP do arquivo de projeto de ajuda.
**cHelpTopic**
Especifica o tópico Help a ser exibido. Se você incluir apenas parte da grafia de um título de tópico, o Visual FoxPro abre a janela Help e exibe o tópico com o título mais próximo.

# Observações

Aplica-se a: Application Object | _VFP System Variable

Se nenhum dos argumentos opcionais for incluído, o tópico principal de ajuda é exibido.
