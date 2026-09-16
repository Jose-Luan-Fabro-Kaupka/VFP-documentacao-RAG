# Comando BUILD APP

Cria um arquivo de aplicativo padrão (.app) a partir de um projeto do Visual FoxPro.

> **Observação:** Antes de usar o comando BUILD APP, certifique-se de que o projeto contém todos os arquivos necessários para o aplicativo. Se arquivos necessários estiverem ausentes durante a compilação, o Visual FoxPro gera um erro. Para obter mais informações, consulte Trabalhando com projetos.

```foxpro
BUILD APP APPFileName FROM ProjectName [RECOMPILE]
```

#### Parâmetros
 **APPFileName**
Especifica o nome do arquivo do aplicativo a ser compilado. A extensão de arquivo padrão é .app. Observação Se existir um arquivo executável (.exe) com o mesmo nome raiz do arquivo .app que você criar, o arquivo .exe é excluído.
**FROM ProjectName**
Especifica o nome do projeto a partir do qual o aplicativo é compilado.
**[RECOMPILE]**
Especifica que o projeto seja compilado antes que o arquivo de aplicativo seja criado. Todos os arquivos de programa e de formato; código-fonte de formulários, etiquetas, relatórios e bibliotecas de classes visuais; e procedimentos armazenados em bancos de dados no projeto são compilados.
