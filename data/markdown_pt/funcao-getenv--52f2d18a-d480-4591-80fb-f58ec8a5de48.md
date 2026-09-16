# Função GETENV( )

Retorna o conteúdo da variável de ambiente MS-DOS especificada.

```foxpro
GETENV(cVariableName)
```

#### Parâmetros
 **cVariableName**
Especifica o nome da variável de ambiente. A cadeia de caracteres vazia é retornada se a variável de ambiente que você especifica não existir. Você pode localizar o diretório do Windows com a variável de ambiente WINDIR, que o Windows define quando inicia.

# Valor de retorno

Character

# Observações

Duas variáveis de ambiente estão sempre disponíveis: COMSPEC e PATH. Você pode criar suas próprias variáveis de ambiente com o comando SET do shell de comando.

Para informações adicionais sobre criação de variáveis de ambiente, consulte a documentação do produto Windows.

# Exemplo

```foxpro
CLEAR
? GETENV('PATH')  && Displays the search path
```
