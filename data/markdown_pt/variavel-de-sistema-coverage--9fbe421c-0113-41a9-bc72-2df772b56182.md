# Variável de Sistema _COVERAGE

Contém o nome do aplicativo Visual FoxPro que cria a saída de cobertura e profiler do Debugger.

```foxpro
_COVERAGE = cProgramName
```

#### Parâmetros
 **cProgramName**
Especifica um aplicativo de saída de cobertura. Se o aplicativo de saída de cobertura estiver em um diretório diferente do diretório padrão atual do Visual FoxPro, inclua um caminho com o nome do aplicativo. Você também pode especificar um aplicativo de saída de cobertura no arquivo de configuração do Visual FoxPro incluindo uma linha usando esta sintaxe: _COVERAGE = cProgramName

# Observações

Por padrão, _COVERAGE contém Coverage.app, instalado no diretório do Visual FoxPro. Você pode especificar um nome diferente para o aplicativo de saída de cobertura.
