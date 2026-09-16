# Como: instalar aplicativos adicionais

Esta versão inclui cópias de software adicional que você pode instalar e usar com o Visual FoxPro. Estes incluem:
 - InstallShield Express Limited Edition Fornece a capacidade de empacotar e implantar os aplicativos que você cria usando o Visual FoxPro. O Visual FoxPro inclui o InstallShield Express 5.0 Visual FoxPro Limited Edition. Note As edições limitada e completa do InstallShield Express 5.0 são consideradas duas versões do mesmo produto e não podem coexistir. Se você instalar uma versão em um computador onde outra já existe, a original é desinstalada automaticamente. Como a edição limitada contém menos recursos que a edição completa, você deve manter a edição completa em seu computador.
- Microsoft SOAP Toolkit 3.0 Samples Fornece amostras para demonstrar como consumir e publicar serviços Web XML. Visual FoxPro Prerequisites instala os componentes principais do SOAP Toolkit 3.0 necessários para acessar e publicar serviços Web XML no Visual FoxPro.
- Microsoft SQL Server 2000 Desktop Engine (MSDE) Fornece uma versão pessoal do SQL Server.

### Para instalar InstallShield Express Limited Edition
- Insira o CD do Visual FoxPro. A página inicial do Visual FoxPro Setup abre automaticamente.
- Clique em Install InstallShield Express .
- Siga as instruções no assistente de instalação do InstallShield Express.

Você também pode localizar o arquivo Setup.exe do InstallShield Express na pasta InstallShield no CD do Visual FoxPro.

> **Note:** O Visual FoxPro 9.0 instala seus merge modules redistribuíveis no mesmo local que o Visual FoxPro 8.0.

A versão do InstallShield Express incluída com o Visual FoxPro 9.0 usa automaticamente o local de merge module do Visual FoxPro 9.0.

> **Note:** O Visual FoxPro 9.0 requer certos merge modules ao criar um programa de instalação de aplicativo personalizado redistribuível do Visual FoxPro 9.0 usando InstallShield Express.

Você precisa incluir os seguintes merge modules ao criar seu programa de instalação personalizado:
 - Microsoft Visual FoxPro 9 Runtime Libraries
- Microsoft Visual C Runtime Library 7.1
- GDI Plus Redist
- MSXML 4.0
- MSXML 3.0 (necessário somente para funções CURSORTOXML)
- Microsoft Visual FoxPro 9 Runtime Language Libraries (arquivos de biblioteca de idioma específicos que podem ser necessários para aplicativos internacionais)
- Reporting Applications (necessário para o mecanismo de relatório do Visual FoxPro 9.0)

> **Note:** MSXML 4.0 consiste em dois merge modules (msxml4sxs32.msm e msxml4sys32.msm). MSXML 3.0 consiste em três merge modules (msxml3_wim32.msm, msxml3inf_wim32.msm e wdstddll_wim32.msm).

### Para instalar SOAP Toolkit 3.0 Samples
- Insira o CD do Visual FoxPro. A página inicial do Visual FoxPro Setup abre automaticamente.
- Clique em Install SOAP Toolkit 3.0 Samples .
- Siga as instruções no SOAP Toolkit 3.0 Samples Setup Wizard.

Você também pode localizar os arquivos Soapsdk.msi e Soapsamp.msi do SOAP Toolkit na pasta SOAPToolkit no CD do Visual FoxPro.

### Para instalar MSDE
- Insira o CD do Visual FoxPro. A página inicial do Visual FoxPro Setup abre automaticamente.
- Clique em Install Microsoft SQL Server Desktop Engine (MSDE) e siga as instruções de instalação que aparecem no arquivo Readme.

Você pode localizar o arquivo Setup.exe do MSDE na pasta SQLMSDE no CD do Visual FoxPro.

> **Note:** O Visual FoxPro inclui Microsoft SQL Server 2000 Desktop Engine Service Pack 3.0a. Para garantir que você tenha a versão e o Service Pack mais recentes instalados, visite a página Web do Microsoft SQL Server em http://www.microsoft.com/sql . Além disso, se você estiver distribuindo aplicativos Visual FoxPro personalizados que requerem MSDE, pode obter os merge modules redistribuíveis na página Web do Microsoft SQL Server para uso com programas de instalação baseados no Windows Installer.
