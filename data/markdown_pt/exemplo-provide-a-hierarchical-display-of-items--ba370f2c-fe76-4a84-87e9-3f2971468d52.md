# Exemplo Provide a Hierarchical Display of Items

Arquivo: ...\Samples\Solution\OLE\Outline.scx

Este exemplo mostra dois tipos diferentes de controles ActiveX, que você pode usar para estruturação em tópicos. Neste exemplo, uma estrutura de diretório é exibida. Um método personalizado no formulário chamado FillTree é chamado recursivamente para iterar por toda a estrutura de árvore.

O controle Treeview também permite exibir imagens com cada nó.

# Controle Treeview

O controle Treeview pode dar às suas aplicações uma aparência genuinamente Windows. Diferentemente do controle Outline, que usa métodos e índices de itens, o controle Treeview usa uma coleção Nodes.

> **Observação:** Para exibir imagens em um controle treeview, você deve adicionar um controle ImageList ao formulário.

```foxpro
* Add items to treeview control
o = THIS.PageFrame1.Page2.oleTreeview
IF cnt = 1
   oNode = o.nodes.add(,1,LOWER(m.path)+"_",LOWER(m.path),,)
   oNode.Image = "world"   &&name of image
ELSE
   oNode = o.nodes.add(m.pkey,4,LOWER(m.path)+"_",LOWER(m.path),,)
   oNode.Image = "fldr"   &&name of image
ENDIF
```
