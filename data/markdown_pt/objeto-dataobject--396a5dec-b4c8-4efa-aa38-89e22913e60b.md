# Objeto DataObject

Contêiner para dados transferidos de uma origem de arrastar OLE para um destino de soltar OLE. Disponível somente em tempo de execução.

```foxpro
oDataObject
```

# Observações

O objeto DataObject é um contêiner para dados transferidos de uma origem de arrastar OLE para um destino de soltar OLE e existe apenas durante a duração de um evento de arrastar e soltar OLE. O objeto DataObject não pode ser criado programaticamente e referências a ele tornam-se inválidas quando a operação de arrastar e soltar OLE é concluída. O DataObject é passado como o parâmetro oDataObject nos eventos OLEDragDrop, OLEDragOver, OLESetData e OLEStartDrag.

O DataObject pode armazenar vários conjuntos de dados, cada um em um formato diferente. Use os métodos GetFormat e GetData para determinar os formatos de dados e os dados no DataObject. Use os métodos SetFormat, SetData ou ClearData para adicionar formatos de dados e dados ao DataObject ou limpar todos os formatos de dados e dados do DataObject.
