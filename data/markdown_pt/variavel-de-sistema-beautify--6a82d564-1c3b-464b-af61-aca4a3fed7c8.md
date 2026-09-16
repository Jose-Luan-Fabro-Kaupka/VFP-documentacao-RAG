# Variável de sistema _BEAUTIFY

Especifica o aplicativo de embelezamento para programas do Visual FoxPro e é executado quando você escolhe o comando Beautify no menu Tools.

```foxpro
_BEAUTIFY = cProgramName, aOptions
```

#### Parâmetros
 **cProgramName**
Especifica um aplicativo de embelezamento. Se o seu aplicativo de embelezamento estiver em um diretório diferente do diretório padrão atual, inclua um caminho com o nome do aplicativo. Você também pode especificar um aplicativo de embelezamento no seu arquivo de configuração incluindo uma linha usando esta sintaxe: _BEAUTIFY = cProgramName Observe que o seu aplicativo de embelezamento deve aceitar um único parâmetro, o nome do programa a ser embelezado. O seu aplicativo de embelezamento pode modificar o programa, gravar as modificações em um arquivo temporário e então retornar o nome do arquivo temporário ao FoxPro. O FoxPro lê o arquivo temporário de volta na sessão de edição sob o nome original do programa FoxPro e então exclui o arquivo temporário.
**aOptions**
Somente para uso interno

# Observações

O comando Beautify aparece no menu Tools quando você abre um programa ou arquivo de texto em uma janela de edição.
