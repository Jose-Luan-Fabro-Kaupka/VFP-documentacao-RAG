# Propriedade MemberClassLibrary

Especifica o nome da biblioteca de classes que contém a classe membro na propriedade MemberClass. Leitura/gravação em tempo de design e em tempo de execução.

Para um contêiner pai Column e seus membros de cabeçalho, use a propriedade HeaderClassLibrary em vez de MemberClassLibrary.

```foxpro
Object.MemberClassLibrary [ = cClassFile ]
```

# Valor de retorno
 **cClassFile**
Especifica o nome do arquivo que contém a classe membro em MemberClass.

# Observações

Aplica-se a: PageFrame Control | CommandGroup Control | OptionGroup Control | Grid Control

O Visual FoxPro inclui a biblioteca de classes visual (.vcx) ou o programa (.prg) MemberClassLibrary no projeto durante a compilação do projeto.

Se você definir MemberClassLibrary em tempo de execução, deve usar o nome completo do arquivo, incluindo a extensão.

Se você especificar MemberClassLibrary sem especificar MemberClass, o Visual FoxPro não gera um erro; no entanto, usa a classe base ao adicionar um novo membro e ignora a propriedade especificada.

Para informações adicionais sobre as propriedades MemberClassLibary e MemberClass, consulte MemberClass Property.
