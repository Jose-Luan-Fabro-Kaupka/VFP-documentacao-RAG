# Como: estender arquivos de banco de dados

Cada registro no arquivo de banco de dados (.dbc) tem um campo Memo chamado User. Você pode usar esse campo para armazenar informações adicionais sobre cada registro no arquivo de banco de dados. Você também pode adicionar campos definidos pelo usuário ao final de um arquivo de banco de dados.

> **Observação:** Para modificar a estrutura de um arquivo de banco de dados, você deve abrir o arquivo de banco de dados de forma exclusiva.

> **Cuidado:** Não altere nenhum campo existente definido pelo Visual FoxPro em um arquivo de banco de dados. Qualquer alteração feita em um arquivo de banco de dados pode afetar a validade do seu banco de dados.

### Para adicionar um campo a um arquivo de banco de dados
- Feche o banco de dados.
- Use o comando USE com o nome do arquivo de banco de dados, incluindo a extensão de nome de arquivo .dbc, e a palavra-chave EXCLUSIVE.
- Na linha seguinte, use o comando MODIFY STRUCTURE. O Table Designer é aberto para o arquivo de banco de dados.

Agora você pode adicionar campos ao arquivo de banco de dados.

> **Dica:** Ao adicionar um novo campo a um arquivo de banco de dados, comece o nome do campo com a letra "U" para designá-lo como um campo definido pelo usuário. Essa designação evita que seu campo entre em conflito com quaisquer extensões futuras do arquivo de banco de dados.

Por exemplo, o código a seguir primeiro fecha o banco de dados MyDatabase, abre o arquivo de banco de dados MyDatabase.dbc de forma exclusiva e, em seguida, abre o Table Designer para o arquivo de banco de dados para que você possa adicionar campos:

```foxpro
CLOSE MyDatabase
USE MyDatabase.dbc EXCLUSIVE
MODIFY STRUCTURE
```
