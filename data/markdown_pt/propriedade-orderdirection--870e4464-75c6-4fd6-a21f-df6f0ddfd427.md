# Propriedade OrderDirection

Especifica uma ordem ascendente ou descendente para a tag de índice controladora especificada pela propriedade Order de um objeto Cursor. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** OrderDirection é ignorada quando a propriedade Order do cursor está vazia.

```foxpro
Cursor.OrderDirection  [= nValue]
```

# Valor de retorno
 **nValue**
Especifica um valor que determina a ordem de um índice de cursor. A tabela a seguir lista os valores de nValue . nValue Descrição 0 Ordem de índice baseada em como o arquivo de índice ou a tag é definida, por exemplo, usando o comando INDEX. (Padrão) 1 Define a ordem do índice como ascendente. 2 Define a ordem do índice como descendente.

# Observações

Aplica-se a: Objeto Cursor

Definir OrderDirection como ordem ascendente ou descendente é equivalente a chamar o comando SET ORDER com a palavra-chave ASCENDING ou DESCENDING. No entanto, você pode alterar o índice controlador e sua ordem para um cursor sem alterar as propriedades OrderDirection e Order. Alterações na propriedade OrderDirection não afetam a ordem do índice até que a propriedade Order também seja alterada.
