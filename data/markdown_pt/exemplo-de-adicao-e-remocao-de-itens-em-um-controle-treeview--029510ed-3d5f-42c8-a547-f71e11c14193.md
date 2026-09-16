# Exemplo de adição e remoção de itens em um controle TreeView

Arquivo: ...\Samples\Solution\OLE\Bldtree.scx

Um controle TreeView exibe uma coleção de objetos Node, cada um composto por um rótulo e um bitmap opcional. Depois de criar o controle, você pode adicionar, remover, organizar e manipular objetos Node definindo propriedades e invocando métodos.

Este exemplo mostra como adicionar, excluir e selecionar nós por programação, gravar uma hierarquia TreeView em uma tabela e lê-la de uma tabela.

# Adição de nós

Cada nó precisa de uma chave exclusiva de caracteres, gerada pelo método NewKey neste formulário de exemplo.

```foxpro
*NewKey method
cKey = THIS.cNextKey
THIS.cNextKey = ALLTRIM(STR(VAL(THIS.cNextKey) + 1) + "_")
RETURN cKey
```

O método Add do controle adiciona novos nós. O código do evento Click de cmdNewNode adiciona um nó raiz.

```foxpro
o = THISFORM.oleTree
o.Nodes.Add(,1,THISFORM.NewKey(),"Click to edit text",0)
```

O código do evento Click de cmdNewChild adiciona um nó filho do nó selecionado.

```foxpro
o = THISFORM.oleTree
IF !ISNULL(o.SelectedItem) THEN
   o.Nodes.Add(o.SelectedItem.Key, 4, THISFORM.NewKey(), "Click to edit text",0)
ENDIF
```

# Exclusão de nós

Você pode excluir todos os nós chamando o método Clear.

```foxpro
THISFORM.oleTree.Nodes.Clear
```

Ou use o método Remove para excluir os nós selecionados. Todos os filhos do nó também serão excluídos.

```foxpro
THISFORM.oleTree.Nodes.Remove(THISFORM.oleTree.SelectedItem.Key)
```

# Gravação e leitura de hierarquias em tabelas

Para salvar a hierarquia em uma tabela e recarregá-la para edição, percorra todos os nós e grave Key, a Key do nó pai e Text nos campos apropriados.

```foxpro
FOR i = 1 TO loNodes.Count
   IF ISNULL(loNodes.Item(i).Parent)
      lcParent = "0_" && Root
   ELSE
      lcParent = loNodes.Item(i).Parent.Key
   ENDIF
   INSERT INTO (lcDBFName) VALUES ;
      (loNodes.Item(i).Key, ;
       lcParent, ;
       loNodes.Item(i).Text)
ENDFOR
```

Para reconstruir a hierarquia, percorra os registros usando os valores de chave pai, chave e texto armazenados.

```foxpro
* Fill the TreeView control with values in the table.
o = THISFORM.oleTree.Nodes
   SCAN
      IF ALLTRIM(parent) = '0_'
         o.add(,1,ALLTRIM(key),ALLTRIM(text),0)
      ELSE
         o.add(ALLTRIM(parent),4,ALLTRIM(key), ALLTRIM(text),0)
      ENDIF
      THISFORM.cNextKey = ALLTRIM(STR(VAL(key) + 1) + "_")
   ENDSCAN
```
