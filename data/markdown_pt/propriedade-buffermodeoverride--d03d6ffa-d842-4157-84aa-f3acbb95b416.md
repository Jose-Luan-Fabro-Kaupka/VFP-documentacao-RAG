# Propriedade BufferModeOverride

Especifica se deve substituir a propriedade BufferMode definida no nível do formulário ou form set. Disponível em tempo de design e em tempo de execução.

```foxpro
DataEnvironment.Cursor.BufferModeOverride[ = nValue]
```

# Valor de retorno
 **nValue**
As configurações da propriedade BufferModeOverride estão listadas na tabela a seguir: Configuração Descrição 3 Bufferização otimista por linha. Permite edições em um único registro e bloqueia o registro somente quando ele é gravado no disco. Você pode usar TABLEREVERT( ) para desfazer suas alterações. 5 Bufferização otimista por tabela. Permite edições em todos os registros e não os bloqueia até que os registros sejam gravados no disco com TABLEUPDATE( ). Você pode usar TABLEREVERT( ) para desfazer suas alterações.

Aplica-se a: Cursor Object | CursorAdapter Class
