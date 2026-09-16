# Função ISREADONLY( )

Determina se uma tabela ou banco de dados foi aberto como somente leitura.

```foxpro
ISREADONLY([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea | cTableAlias**
Retorna o status de somente leitura de uma tabela aberta em outra área de trabalho. nWorkArea especifica o número da área de trabalho, e cTableAlias especifica o alias da tabela ou área de trabalho. ISREADONLY( ) retorna falso (.F.) se nenhuma tabela estiver aberta na área de trabalho especificada. Se você não especificar o número de uma área de trabalho nem o alias de uma tabela ou área de trabalho, a função ISREADONLY( ) retornará o status de somente leitura da tabela aberta na área de trabalho atual. ISREADONLY(0) retorna o status do banco de dados atual. Se não houver um banco de dados atual aberto, ISREADONLY(0) retornará um erro.

# Valor de retorno

Lógico

# Observações

ISREADONLY( ) retorna verdadeiro (.T.) se uma tabela estiver aberta como somente leitura; caso contrário, retorna falso (.F.).

Você pode abrir uma tabela como somente leitura incluindo a opção NOUPDATE ao abri-la com USE, marcando a caixa de seleção Read Only ao abrir a tabela na caixa de diálogo Open ou atribuindo à tabela atributos de somente leitura do MS-DOS.

Não é possível passar à função ISREADONLY( ) o alias de um banco de dados que não seja o atual. Para garantir que um banco de dados esteja presente, você pode usar um código como o seguinte:

```foxpro
!EMPTY(DBC())
```

Um cursor criado com o comando SELECT – SQL é sempre somente leitura.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer    NOUPDATE  && Open customer table read-only
CLEAR
? ISREADONLY('customer')  && Returns .T.
```
