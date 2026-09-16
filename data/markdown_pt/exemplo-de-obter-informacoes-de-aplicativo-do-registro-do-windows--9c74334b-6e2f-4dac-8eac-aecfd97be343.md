# Exemplo de obter informações de aplicativo do Registro do Windows

Arquivo: ...\Samples\Solution\WINAPI\Regfile.scx

Este exemplo mostra como acessar o registro do Windows usando o comando DECLARE-DLL nativo do Visual FoxPro. A API do Windows fornece várias funções que você pode usar para acessar, ler e gravar no registro. A biblioteca de classes Registry.prg em ...\Samples\Classes contém um conjunto completo dessas funções que você pode usar em seus aplicativos.

Neste exemplo específico, você pode usar funções de registro para verificar a existência de um determinado aplicativo. Por exemplo, você pode querer distribuir um aplicativo que depende do uso do Excel para automatizar a criação de uma Tabela Dinâmica. O registro contém o local, a versão e outras informações sobre um determinado aplicativo.
