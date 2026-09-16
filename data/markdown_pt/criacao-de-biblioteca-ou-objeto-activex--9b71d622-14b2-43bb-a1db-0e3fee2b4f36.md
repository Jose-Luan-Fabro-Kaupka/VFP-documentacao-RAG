# Criação de biblioteca ou objeto ActiveX

Você pode ampliar as capacidades do Visual FoxPro criando programas em C ou C++ que realizam tarefas exigidas pelo seu aplicativo. Por exemplo, se o seu aplicativo requer acesso direto às facilidades do Windows, você pode escrever um programa C ou C++ que faz chamadas à API do Windows e então retorna informações ao Visual FoxPro.

Você pode criar três tipos de programas para acessar a API do Visual FoxPro:
 - Um controle ActiveX (arquivo .ocx).
- Um objeto COM.
- Uma DLL específica do Visual FoxPro. Como a DLL pode ser chamada somente do Visual FoxPro, é costume usar a extensão de nome de arquivo .fll para o arquivo DLL.

Cada tipo de programa tem vantagens. Controles ActiveX têm as seguintes vantagens:
 - Podem ser acessados usando técnicas orientadas a objetos padrão, como definir suas propriedades e invocar seus métodos.
- Podem ser subclassificados, e seus métodos substituídos.
- São encapsulados e podem ser chamados (instanciados) várias vezes sem gerenciamento complexo de ambiente para preservar estados do usuário.
- Possuem passagem de parâmetros mais simples.
- Também podem ser chamados de outros programas Windows, se você programá-los com isso em mente.

Objetos COM têm as seguintes vantagens:
 - Podem ser acessados usando técnicas orientadas a objetos padrão, como definir suas propriedades e invocar seus métodos.
- Seus métodos podem ser substituídos.
- São encapsulados e podem ser chamados (instanciados) várias vezes sem gerenciamento complexo de ambiente para preservar estados do usuário.
- Possuem passagem de parâmetros mais simples.
- Também podem ser chamados de outros programas Windows, se você programá-los com isso em mente.

Bibliotecas de link dinâmico (.fll) do Visual FoxPro podem ser mais familiares para você se você usou versões anteriores do Visual FoxPro.
