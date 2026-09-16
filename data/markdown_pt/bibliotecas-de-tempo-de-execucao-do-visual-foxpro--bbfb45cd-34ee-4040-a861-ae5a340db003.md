# Bibliotecas de tempo de execução do Visual FoxPro

O Visual FoxPro inclui duas bibliotecas de tempo de execução para você distribuir com suas aplicações:
 - VFP VersionNumber R.dll
- VFP VersionNumber T.dll

VersionNumber indica o número da versão do Visual FoxPro que você usa para desenvolver suas aplicações. Essas bibliotecas de tempo de execução estão localizadas no diretório ..\Program Files\Common Files\Microsoft Shared\VFP.

VFPVersionNumberR.dll é a biblioteca de tempo de execução típica para a maioria dos tipos de aplicação. VFPVersionNumberT.dll é um tempo de execução multithread especial para aplicações de servidor em processo altamente escaláveis, como as criadas para uso com o Microsoft Transaction Server. Ambas as bibliotecas de tempo de execução compartilham o arquivo de recursos VFPVersionNumberRENU.dll. Para obter mais informações, consulte Biblioteca de tempo de execução VFP9R.DLL e Biblioteca de tempo de execução VFP9T.DLL.

Quando você constrói sua aplicação no Project Manager, a ação de build que você escolhe determina qual biblioteca de tempo de execução a aplicação ou servidor gerado usa. Apenas servidores Automation (.dll) podem usar a biblioteca de tempo de execução VFPVersionNumberT.dll. O método Build para objetos Project também permite escolher qual biblioteca de tempo de execução usar. Para obter mais informações, consulte Como: construir servidores Automation, Como: construir aplicações e Método Build.

> **Observação:** O arquivo de origem compilado, por exemplo, um executável (.exe) ou um servidor Automation, é marcado internamente para identificar qual biblioteca de tempo de execução usar quando chamado. A única maneira de alterar a biblioteca de tempo de execução que um servidor Automation usa é reconstruindo-o. Seu servidor pode determinar em tempo de execução qual biblioteca de tempo de execução está usando através da propriedade somente leitura Application StartMode. Você precisa saber qual biblioteca de tempo de execução está associada ao seu servidor Automation para poder escolher o tempo de execução certo a incluir na configuração. Para obter mais informações, consulte Automation e servidores COM.
