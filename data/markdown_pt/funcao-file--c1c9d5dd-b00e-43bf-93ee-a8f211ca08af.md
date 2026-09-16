# Função FILE( )

Localiza o arquivo especificado.

```foxpro
FILE(cFileName [, nFlags])
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo a localizar. cFileName deve incluir a extensão do arquivo. Você pode incluir um caminho com o nome do arquivo para pesquisar um arquivo em um diretório ou em uma unidade diferente do diretório ou unidade atual. Se você não incluir um caminho com o nome do arquivo, o Visual FoxPro pesquisa no diretório padrão pelo arquivo. Se não encontrar o arquivo no diretório padrão, o Visual FoxPro pesquisa ao longo do caminho do Visual FoxPro, que é estabelecido com SET PATH .

> **Dica:** Arquivos incluídos em um aplicativo APP ou EXE do FoxPro têm precedência sobre os arquivos em disco. O caminho é irrelevante para esses arquivos. Use a função ADIR( ) para localizar o arquivo especificado somente em disco.
 **nFlags**
Especifica o tipo de valor que FILE( ) retorna quando o arquivo existe, mas pode estar marcado com o atributo Hidden ou System. A tabela a seguir lista os valores de nFlags . nFlags Descrição 0 FILE( ) retorna False (.F.) se o arquivo existir, mas estiver marcado com um atributo Hidden ou System. (Padrão) 1 FILE( ) retorna True (.T.) se o arquivo existir, independentemente de seus atributos de arquivo. Definir nFlags como 1 permite verificar arquivos ocultos ou de sistema.

# Valor de retorno

Tipo de dados Logical. FILE( ) retorna True (.T.) se o arquivo especificado estiver incluído em um aplicativo ou for encontrado em disco; caso contrário, retorna False (.F.).

# Observações

Você pode usar a função ADIR( ) para recuperar atributos específicos do arquivo.

Você pode usar os comandos CD e CHDIR para alternar para arquivos e diretórios ocultos.

# Exemplo

O exemplo a seguir exibe uma mensagem indicando se o arquivo de recursos do Visual FoxPro existe no diretório de inicialização do Visual FoxPro.

```foxpro
SET PATH TO HOME()
CLEAR
IF FILE('foxuser.dbf')
   WAIT WINDOW 'Visual FoxPro resource file present'
ELSE
   WAIT WINDOW 'Visual FoxPro resource file not present'
ENDIF
```
