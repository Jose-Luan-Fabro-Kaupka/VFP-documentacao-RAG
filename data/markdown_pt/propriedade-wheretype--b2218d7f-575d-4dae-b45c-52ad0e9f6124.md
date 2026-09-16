# Propriedade WhereType

Especifica os campos dos quais a cláusula WHERE consiste quando usada para atualizar tabelas. Ao trabalhar com esta propriedade para cursores regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** Definir WhereType para objetos CursorAdapter substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.WhereType [= nValue]
```

# Valor de retorno
 **nValue**
Tipo de dados numérico. A tabela a seguir lista os valores de nValue. nValue Descrição 1 ou DB_KEY (de FOXPRO.H) Inclui apenas os campos primários especificados pela propriedade KeyFieldList. 2 ou DB_KEYANDUPDATABLE (de FOXPRO.H) Inclui os campos primários especificados pela propriedade KeyFieldList e quaisquer campos atualizáveis. 3 ou DB_KEYANDMODIFIED (de FOXPRO.H) Inclui os campos primários especificados pela propriedade KeyFieldList e outros campos modificados. 4 ou DB_KEYANDTIMESTAMP (de FOXPRO.H) Inclui os campos primários especificados pela propriedade KeyFieldList e uma comparação de carimbos de data/hora.

# Observações

Aplica-se a: CursorAdapter Class

Para operações forçadas de atualização e exclusão, o CursorAdapter usa o valor 1 para a propriedade WhereType do CursorAdapter independentemente da configuração real. Caso contrário, o CursorAdapter respeita as configurações do usuário para WhereType.
