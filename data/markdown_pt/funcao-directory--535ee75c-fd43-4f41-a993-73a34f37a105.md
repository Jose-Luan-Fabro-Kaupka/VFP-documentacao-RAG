# Função DIRECTORY( )

Localiza o diretório especificado.

```foxpro
DIRECTORY(cDirectoryName [, nFlags])
```

#### Parâmetros
 **cDirectoryName**
Especifica o nome do diretório a localizar. Se você não incluir um caminho absoluto para o diretório que especifica, o Visual FoxPro procura o diretório em relação ao diretório padrão do Visual FoxPro.
**nFlags**
Especifica o tipo de valor que DIRECTORY( ) retorna quando o diretório existe, mas pode estar marcado com o atributo Hidden ou System. A tabela a seguir lista os valores para nFlags. nFlags Descrição 0 DIRECTORY( ) retorna False (.F.) se o diretório existe, mas está marcado com um atributo Hidden ou System. (Padrão) 1 DIRECTORY( ) retorna True (.T.) se o diretório existe, independentemente de seus atributos. Definir nFlags como 1 permite verificar arquivos ocultos ou de sistema.

# Valor de retorno

Tipo de dados Logical. DIRECTORY( ) retorna True (.T.) se o diretório especificado é encontrado no disco; caso contrário, retorna False (.F.).

# Observações

O comando SET DEFAULT especifica o diretório padrão do Visual FoxPro.

Você pode usar a função ADIR( ) para determinar atributos específicos do diretório.

Você pode usar os comandos CD e CHDIR para alternar para arquivos e diretórios ocultos.
