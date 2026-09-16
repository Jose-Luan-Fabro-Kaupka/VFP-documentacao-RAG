# Testando e recompilando servidores COM para XML Web Services

Ao recompilar seu servidor COM, você pode gerar arquivos de suporte a XML Web service automaticamente criando um project hook para o projeto do servidor COM que chama o mecanismo de XML Web service para recompilar os arquivos de suporte a XML Web service. Você pode selecionar essa opção na caixa de diálogo Advanced da Visual FoxPro XML Web Services Publisher dialog box. O project hook (WSHOOK) é armazenado na biblioteca de classes foundation de XML Web services, _WS3Utils.vcx, localizada na pasta Visual FoxPro ..\Ffc. Para obter mais informações, consulte XML Web Services Foundation Classes.

Quando você está trabalhando e testando seu XML Web service, é provável que o IIS armazene em cache seu servidor COM por motivos de desempenho. Para recompilar seu servidor COM, pode ser necessário primeiro encerrar o processo que está usando o servidor COM, por exemplo, o aplicativo COM+ IIS Out-Of-Process Pooled Applications; caso contrário, uma mensagem de negação de acesso é gerada durante o processo de compilação do projeto. Esse processo pode ser trabalhoso se você precisar testar e recompilar o servidor COM com frequência. O project hook na biblioteca de classes foundation de XML Web service, _WS3Utils.vcx, pode encerrar esse processo para você.

> **Observação:** Pode ser necessário alterar a configuração padrão no project hook para que o aplicativo seja encerrado, dependendo da plataforma de SO e da versão do IIS em execução.

Para obter mais informações, consulte XML Web Services Foundation Classes.
