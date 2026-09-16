# Comando OPEN DATABASE

Abre um banco de dados.

```foxpro
OPEN DATABASE [FileName | ?] [EXCLUSIVE | SHARED] [NOUPDATE] [VALIDATE]
```

#### Parâmetros
 **FileName**
Especifica o nome do banco de dados a ser aberto. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribui automaticamente a extensão .dbc. Se você omitir FileName , a caixa de diálogo Abrir é exibida. Você pode especificar um nome de caminho como parte do nome do banco de dados. Observação O Visual FoxPro não reconhecerá um nome de caminho corretamente se um nome de disco ou diretório contiver um ponto de exclamação (!).
**?**
Exibe a caixa de diálogo Abrir, na qual você pode escolher um banco de dados existente ou inserir o nome de um novo formulário a ser criado.
**EXCLUSIVE**
Abre o banco de dados em modo exclusivo. Se você abrir o banco de dados de forma exclusiva, outros usuários não poderão acessá-lo e receberão um erro se tentarem obter acesso. Se você não incluir EXCLUSIVE ou SHARED, a configuração atual de SET EXCLUSIVE determina como o banco de dados é aberto.
**SHARED**
Abre o banco de dados em modo compartilhado. Se você abrir o banco de dados para uso compartilhado, outros usuários terão acesso a ele. Se você não incluir EXCLUSIVE ou SHARED, a configuração atual de SET EXCLUSIVE determina como o banco de dados é aberto.
**NOUPDATE**
Especifica que nenhuma alteração pode ser feita no banco de dados. Em outras palavras, o banco de dados é somente leitura. Se você omitir NOUPDATE, o banco de dados é aberto com acesso de leitura/gravação. As tabelas contidas no banco de dados não são afetadas por NOUPDATE. Para impedir alterações em uma tabela no banco de dados, inclua NOUPDATE em USE quando você abrir a tabela.
**VALIDATE**
Especifica que o Visual FoxPro garante que as referências no banco de dados são válidas. O Visual FoxPro verifica se as tabelas e índices referenciados no banco de dados estão disponíveis no disco. O Visual FoxPro também verifica se os campos e tags de índice referenciados existem nas tabelas e índices.

# Observações

Enquanto o banco de dados estiver aberto, todas as tabelas contidas nele estarão disponíveis. No entanto, as tabelas não são abertas implicitamente. Você deve abri-las com USE.

Quando USE é executado, o Visual FoxPro procura a tabela no banco de dados atual. Se a tabela não for encontrada, o Visual FoxPro procura então uma tabela fora do banco de dados. Isso significa que, se uma tabela em um banco de dados tiver o mesmo nome de uma tabela fora do banco de dados, a tabela no banco de dados será encontrada primeiro.

Você não pode abrir um banco de dados que está aberto de forma exclusiva por outro usuário.

Se você abrir um banco de dados duas vezes seguidas sem fechar o banco de dados, o banco de dados mantém as mesmas configurações especificadas com o primeiro comando DATABASE OPEN. Para alterar as configurações, você precisa fechar o banco de dados e então emitir o comando DATABASE OPEN com novas configurações. Por exemplo, se você abrir um banco de dados e especificar EXCLUSIVE, a função ISEXCLUSIVE retorna True (.T.). Se você executar o comando DATABASE OPEN usando o mesmo banco de dados e especificar SHARED, a função ISEXCLUSIVE ainda retorna True (.T.). Para abrir o banco de dados como compartilhado, você precisa fechar o banco de dados e então emitir o comando DATABASE OPEN usando a palavra-chave SHARED.

# Exemplo

No exemplo a seguir, OPEN DATABASE é usado para abrir o banco de dados `testdata`. DISPLAY DATABASE é usado para exibir informações sobre as tabelas no banco de dados.

```foxpro
CLOSE DATABASES
SET PATH TO (HOME(2) + 'Data\')     && Sets path to database
OPEN DATABASE testdata  && Open testdata database
DISPLAY DATABASE  && Displays table information
```
