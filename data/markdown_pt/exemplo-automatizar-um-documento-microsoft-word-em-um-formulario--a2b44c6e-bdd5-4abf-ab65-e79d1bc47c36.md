# Exemplo Automatizar um documento Microsoft Word em um formulário

Arquivo: ...\Samples\Solution\OLE\Oleword.scx

Este exemplo mostra como automatizar um objeto Word incorporado em um formulário, inserir texto formatado e depois formatar o texto. A automação típica com Word geralmente é feita usando o objeto "Word.Basic" usado interativamente com uma função CREATEOBJECT( ).

```foxpro
oForm = THISFORM
oForm.AddObject('oWordDoc','OleControl','WordDocument')
oForm.oWordDoc.Visible =  .t.
oForm.oWordDoc.DoVerb(0)
```
