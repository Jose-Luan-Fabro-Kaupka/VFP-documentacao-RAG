# Como: usar opções de linha de comando ao iniciar o Visual FoxPro

Além de usar o comando SET e um arquivo de configuração, você pode especificar opções de inicialização incluindo uma opção de linha de comando. Por exemplo, usando opções de linha de comando, você pode suprimir a exibição da tela inicial do Visual FoxPro, que é exibida na inicialização do Visual FoxPro, ou especificar um arquivo de configuração não padrão.

### Para usar uma opção de linha de comando
- Na linha de comando ou em um atalho, adicione a opção após o nome do arquivo executável do Visual FoxPro, VFP VersionNumbe r.exe, onde VersionNumber representa o número da versão desta release ou qualquer arquivo .exe criado pelo Visual FoxPro. Observação Se a opção de linha de comando exigir argumentos, como um nome de arquivo, não coloque um espaço entre a opção e o argumento. Por exemplo, para especificar um arquivo de configuração, use um comando como: C:\Program Files\Microsoft Visual FoxPro VersionNumber \VFP VersionNumber .exe -CC:\MYAPP.FPW Separe várias opções com espaços simples.

A tabela a seguir lista as opções de linha de comando disponíveis no Visual FoxPro.

| Opção | Descrição |
| --- | --- |
| -A | Ignora o arquivo de configuração padrão e as configurações do Registro do Windows. |
| -BFileName,Duration | Exibe um arquivo gráfico personalizado (.bmp), .gif ou .jpg e especifica sua duração de exibição em milissegundos quando o Visual FoxPro inicia. Você também pode incluir a opção de linha de comando -B em um atalho do Visual FoxPro. Observação Se o bitmap que você especificar não puder ser localizado, o bitmap não será exibido quando o Visual FoxPro iniciar. |
| -CFileName | Especifica um arquivo de configuração, incluindo um caminho se necessário, diferente do arquivo padrão, Config.fpw. |
| -LFileName | Especifica um arquivo de recursos, incluindo um caminho se necessário, diferente do padrão, vfp*ENU.dll, para que você possa usar o Visual FoxPro em um idioma diferente do idioma atual especificado pelo Windows. |
| -R | Em versões anteriores, atualiza o Registro do Windows com informações sobre o Visual FoxPro, como associações para arquivos do Visual FoxPro. Em versões posteriores, use /regserver. |
| -T | Suprime a exibição da tela inicial do Visual FoxPro. Por padrão, quando o Visual FoxPro inicia, ele exibe uma tela inicial que mostra o logotipo do Visual FoxPro, o número da versão e outras informações. Se você preferir que os usuários do seu aplicativo não vejam essa tela inicial, você pode impedir que o Visual FoxPro a exiba usando a opção de linha de comando -T. |
| /? | Lista os argumentos de linha de comando disponíveis. Disponível no Visual FoxPro 7.0 e posterior. |
| /regserver | Registra as chaves de registro padrão do Visual FoxPro. |
| REGSVR32 server.dll | Registra um componente .dll. |
| /unregserver | Remove as chaves de registro padrão do Visual FoxPro. |
| /u server.dll | Remove um componente .dll. |
