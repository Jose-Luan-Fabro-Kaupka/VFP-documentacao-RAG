# Como: especificar e distribuir ReportPreview.App

Quando você escreve e distribui aplicativos Visual FoxPro, provavelmente desejará permitir que seus usuários visualizem relatórios na tela. Se desejar aproveitar o novo mecanismo de relatório assistido por objetos para visualizar relatórios em seu aplicativo, então deve escolher se:
 - Escrever seu próprio contêiner de visualização personalizado, conforme descrito em Creating a Custom Preview Container .
- Distribuir ReportPreview.App com seu aplicativo.

Neste tópico, você aprenderá como redistribuir o ReportPreview.App, o aplicativo factory padrão do Preview Container, de duas maneiras:
 - Um arquivo App separado junto com seu próprio aplicativo.
- Um código-fonte integrado diretamente em seu próprio aplicativo.

# Redistribuindo ReportPreview.App com seu aplicativo

Por padrão, se ReportPreview.App existir no mesmo diretório dos arquivos de tempo de execução do Visual FoxPro, então _REPORTPREVIEW conterá o caminho completo e o nome do arquivo. One solution is to ensure that the setup program used to distribute your application places ReportPreview.App in the same directory as the run time files. Alternatively, you can distribute ReportPreview.App in the same directory as your application, providing you explicitly set _REPORTPREVIEW to that copy of the file.

### Para distribute ReportPreview.App with your application
- In the main program of your application, use code similar to the following: * Get the application's home directory: cHomeDir = CURDIR() && use whatever method you prefer * Set the system variable to use the fully-qualified path: _REPORTPREVIEW = m.cHomeDir+"ReportPreview.App" :

You could also use a line in CONFIG.FPW:

`_REPORTPREVIEW=<path>\ReportPreview.App`

# Integrando o código-fonte do Preview Container Factory em seu projeto

Em vez de distribuir o aplicativo compilado, você pode optar por incorporar o código-fonte da factory de visualização de relatório diretamente no projeto do seu aplicativo.

### Para integrate the preview container factory source into your application
- Unpack the xsource.zip file found in the Tools\xsource\ folder under the Visual FoxPro home directory.
- In the main program of your application, use code similar to the following: * Ensure the report builder source is pulled into the project: EXTERNAL PROCEDURE frxpreview.prg * Set the system variable to use the local source version: _REPORTPREVIEW = "frxpreview.prg" :
- Rebuild your project. The preview factory source code files will be added to your project and compiled in to your application.

### Arquivos de código-fonte compartilhados

ReportBuilder.App and ReportPreview.App have the following source files in common:
 - frxControls.vcx
- frxCommon.prg
- grabber.gif
- wwrite.ico
- foxpro_reporting.h

The Project Manager builds only one copy of each of these files into your application's project, depending on the order of the EXTERNAL statements in your main program.
