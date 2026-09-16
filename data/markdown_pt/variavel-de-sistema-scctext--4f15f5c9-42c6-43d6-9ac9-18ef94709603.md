# Variável de sistema _SCCTEXT

Especifica um programa de conversão do Visual FoxPro que trata da tradução de arquivos binários do Visual FoxPro em equivalentes de texto e vice-versa.

```foxpro
_SCCTEXT = cProgramName
```

#### Parâmetros
 **cProgramName**
Especifica um programa de conversão de controle de código-fonte. Se seu programa de conversão de controle de código-fonte estiver em um diretório diferente do diretório padrão atual, inclua um caminho com o nome do programa. Você também pode especificar um programa de conversão de controle de código-fonte em seu arquivo de configuração incluindo uma linha usando esta sintaxe: _SCCTEXT = cProgramName

# Observações

Por padrão, _SCCTEXT contém Scctext.prg, um programa de conversão do Visual FoxPro que trata da tradução de arquivos binários do Visual FoxPro em equivalentes de texto e vice-versa. Esses arquivos de texto são usados como base para comparar e mesclar versões de arquivos binários do Visual FoxPro por meio de um aplicativo de controle de código-fonte.
