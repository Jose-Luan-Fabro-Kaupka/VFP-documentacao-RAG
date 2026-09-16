# Variável de sistema _CONVERTER

Contém o nome do aplicativo conversor do Microsoft Visual FoxPro.

```foxpro
_CONVERTER = cProgramName
```

#### Parâmetros
 **cProgramName**
Especifica um aplicativo conversor. Se o seu aplicativo conversor estiver em um diretório diferente do diretório padrão atual do Visual FoxPro, inclua um caminho com o nome do aplicativo. Você também pode especificar um aplicativo conversor no arquivo de configuração do Visual FoxPro incluindo uma linha usando a seguinte sintaxe: _CONVERTER = cProgramName

# Observações

A variável de memória de sistema _CONVERTER contém o nome do aplicativo que o Visual FoxPro usa quando você tenta abrir uma tela, relatório ou projeto criado em uma versão anterior do FoxPro. Por padrão, _CONVERTER contém Convert.app, instalado no diretório do Visual FoxPro. Você pode especificar um nome diferente para o aplicativo conversor.
