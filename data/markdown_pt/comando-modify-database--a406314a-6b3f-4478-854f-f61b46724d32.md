# Comando MODIFY DATABASE

Abre o banco de dados atual no Database Designer para que você possa modificar o banco de dados visualmente.

```foxpro
MODIFY DATABASE [DatabaseName | ?] [NOWAIT] [NOEDIT]
```

#### Parâmetros
 **[ DatabaseName | ?]**
Especifica o nome do banco de dados a ser modificado ou exibe a caixa de diálogo Open para que você possa procurar e selecionar um banco de dados.
**[NOWAIT]**
Continua a execução do programa depois que o Database Designer é aberto. O programa não aguarda o fechamento do Database Designer, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY DATABASE NOWAIT. Se NOWAIT for omitido, a execução do programa é pausada até que o Database Designer seja fechado. Observação NOWAIT é válido somente em um programa. Quando incluído com MODIFY DATABASE na janela Command, NOWAIT não tem efeito.
**[NOEDIT]**
Impede alterações no banco de dados.

# Observações

Chamar MODIFY DATABASE dispara o evento dbc_Activate. Para obter mais informações, consulte dbc_Activate Event.

Para obter mais informações, consulte Database Designer (Visual FoxPro) e How to: Open Databases.

# Exemplo

O exemplo a seguir fecha todos os bancos de dados abertos, define um caminho para o diretório Visual FoxPro ..\Samples\Northwind e abre o banco de dados de exemplo Northwind no Database Designer:

```foxpro
CLOSE DATABASES
SET PATH TO (HOME(2) + 'Northwind\')
MODIFY DATABASE Northwind
```
