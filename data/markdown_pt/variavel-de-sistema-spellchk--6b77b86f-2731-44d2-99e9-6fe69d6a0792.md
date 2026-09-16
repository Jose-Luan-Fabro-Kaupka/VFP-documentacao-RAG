# Variável de sistema _SPELLCHK

Especifica um programa de verificação ortográfica para o editor de texto do Visual FoxPro.

```foxpro
_SPELLCHK = ProgramName
```

#### Parâmetros
 **ProgramName**
Especifica um programa de verificação ortográfica. Se o seu programa de verificação ortográfica estiver em um diretório diferente do diretório padrão atual, inclua um caminho com o nome do programa. Você também pode especificar um programa de verificação ortográfica no arquivo de configuração do Visual FoxPro. Inclua a linha: _SPELLCHK = ProgramName

# Observações

Por padrão, _SPELLCHK não está atribuído. Você pode usar um programa de verificação ortográfica fornecendo o nome do programa e seu caminho em _SPELLCHK. Depois de especificar um programa programaticamente ou na guia File Locations do menu Tools, Options, acesse o programa com o comando DO como no exemplo a seguir.

```foxpro
DO (_Spellchk)
```
