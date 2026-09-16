# Método ClearData

Limpa todos os dados e formatos de dados do objeto DataObject de OLE drag-and-drop. Disponível apenas em tempo de execução.

```foxpro
oDataObject.ClearData
```

# Observações

Aplica-se a: DataObject Object

O método ClearData só pode ser executado no evento OLEStartDrag; chamar o método ClearData dos eventos OLEDragDrop ou OLE DragOver gera um erro.
