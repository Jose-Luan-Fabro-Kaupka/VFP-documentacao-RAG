# Como: usar tabelas de outros bancos de dados

Você pode usar dados de uma tabela não associada ao banco de dados atual.

> **Dica:** Para acessar uma tabela associada ou não associada a um banco de dados, especifique o caminho completo. No entanto, você pode aumentar o desempenho usando somente o nome da tabela.

### Para usar dados de uma tabela de outro banco de dados
- Execute uma das seguintes opções: Use o comando USE com um ponto de interrogação (?) para exibir a caixa de diálogo Use e clique em Other . -OU- Use o comando USE e preceda o nome da tabela com o nome do banco de dados seguido imediatamente por um ponto de exclamação (!). Dica O ponto de exclamação é usado para referenciar uma tabela em um banco de dados diferente do banco de dados atual. -OU- Crie uma view em seu banco de dados que referencie a tabela.

Para obter mais informações, consulte Comando USE e Trabalhando com views (Visual FoxPro).

Por exemplo, o código a seguir demonstra como você pode abrir uma tabela chamada MyTable em outro banco de dados chamado MyDatabase2 e navegar na tabela:

```foxpro
USE MyDatabase2!MyTable
BROWSE
```
