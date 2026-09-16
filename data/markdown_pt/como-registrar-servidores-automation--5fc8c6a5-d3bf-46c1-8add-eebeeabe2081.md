# Como: registrar servidores Automation

Você pode disponibilizar seu servidor Automation para outros aplicativos depois de adicionar o servidor ao Registro do Windows. Quando você compila um servidor Automation, ele é registrado automaticamente no computador em que foi compilado. Quando você usa o programa de instalação do Visual FoxPro para criar discos de instalação, o programa de instalação registra seu servidor no computador em que é instalado. No entanto, você também pode registrar servidores manualmente.

> **Observação:** O registro contém o nome de caminho completo do arquivo; portanto, se você mover o arquivo, precisará registrá-lo novamente.

### Para registrar um componente .exe
- Execute o arquivo .exe com a opção /regserver. Por exemplo, para registrar Myserver.exe, execute o seguinte comando: myserver /regserver

### Para remover uma entrada de registro de componente .exe
- Execute o arquivo .exe com a opção /unregserver. Por exemplo, para cancelar o registro de Myserver.exe, execute o seguinte comando: myserver /unregserver

### Para registrar um componente .dll
- Execute REGSVR32 com o nome do servidor. Por exemplo, para registrar Myserver.dll, execute o seguinte comando: REGSVR32 myserver.dll

### Para remover uma entrada de registro de componente .dll
- Execute REGSVR32 com o nome do servidor e a opção /u. Por exemplo, para cancelar o registro de Myserver.dll, execute o seguinte comando: REGSVR32 /u myserver.dll
