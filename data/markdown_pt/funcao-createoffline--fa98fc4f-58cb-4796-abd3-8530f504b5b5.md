# Função CREATEOFFLINE( )

Coloca uma view existente offline.

```foxpro
CREATEOFFLINE(ViewName [, cPath])
```

#### Parâmetros
 **ViewName**
Especifica o nome da view existente a ser colocada offline. O banco de dados que contém a view existente deve estar aberto antes que você possa colocar a view existente offline.
**cPath**
Especifica o diretório no qual a view offline é colocada e o nome da view offline.

# Valor de retorno

Logical

# Observações

CREATEOFFLINE( ) retorna um valor lógico verdadeiro (.T.) se a view existente for colocada offline com sucesso; caso contrário, falso (.F.) é retornado.

Uma view offline é aberta com USE. Quando uma view offline está aberta, você pode acrescentar registros ou fazer alterações em registros na view offline. No entanto, você não pode usar os comandos CREATE TRIGGER, INSERT, PACK ou ZAP em uma view offline. Depois de fazer alterações na view offline, você pode atualizar os dados no servidor com suas alterações abrindo a view offline com USE e incluindo a cláusula ONLINE.

Você não pode atualizar o conteúdo de uma view offline com dados do servidor até que a view offline tenha sido aberta com USE e a cláusula ONLINE.

Use DROPOFFLINE( ) para colocar a view offline online novamente.
