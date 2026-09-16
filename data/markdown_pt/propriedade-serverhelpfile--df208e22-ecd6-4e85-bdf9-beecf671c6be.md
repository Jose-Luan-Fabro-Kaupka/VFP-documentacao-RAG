# Propriedade ServerHelpFile

Especifica o arquivo de Ajuda para a biblioteca de tipos criada para classes de servidor em um projeto.

Você pode usar a propriedade ServerHelpFile para especificar um arquivo de Ajuda para a biblioteca de tipos criada ao compilar um arquivo .dll ou .exe que contém classes de servidor. Criar e especificar um arquivo de Ajuda fornece informações sobre as propriedades ou métodos em classes de servidor a partir de um navegador de classes ou objetos. Por exemplo, o Visual FoxPro inclui o Object Browser para que você possa visualizar informações da biblioteca de tipos.

```foxpro
Object.ServerHelpFile [= cHelpFileName]
```

# Valor de retorno
 **cHelpFileName**
Especifica o nome do arquivo de Ajuda para a biblioteca de tipos. Por padrão, cHelpFileName contém a cadeia de caracteres vazia ("").

# Observações

Aplica-se a: objeto Project (Visual FoxPro)
