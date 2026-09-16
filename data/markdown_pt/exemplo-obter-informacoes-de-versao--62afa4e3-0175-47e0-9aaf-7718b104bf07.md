# Exemplo Obter Informações de Versão

Arquivo: ...\Samples\Solution\WINAPI\Getver.scx

Este exemplo permite exibir informações de versão de um .dll ou .exe.

Uma nova função chamada GetFileVersion( ) foi adicionada ao Foxtool.fll , que permite obter informações de versão de um arquivo. O código a seguir ilustra como você pode chamar a função. Consulte Tools\Foxtools.hlp para obter detalhes sobre os elementos específicos do array.

```foxpro
SET LIBRARY TO FoxTools ADDITIVE
DIMENSION aFileVer[12]
nRetVal = GetFileVersion(GetFile("EXE"),@aFileVer)
IF nRetVal = 0
   DISPLAY MEMO LIKE aFileVer
ENDIF
SET LIBRARY TO
```

> **Observação:** O Visual FoxPro agora permite adicionar informações de Versão de Arquivo a arquivos EXE e DLL no momento da compilação. Essas informações de versão são armazenadas em um recurso de arquivo e podem ser acessadas usando o Windows Explorer. Arquivos EXE criados no Visual FoxPro 3.0 não terão um recurso de versão de arquivo.
