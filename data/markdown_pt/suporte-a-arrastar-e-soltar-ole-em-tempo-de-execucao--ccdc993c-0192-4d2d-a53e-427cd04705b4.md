# Suporte a arrastar e soltar OLE em tempo de execução

O suporte a arrastar e soltar OLE está disponível em tempo de execução para controles do Visual FoxPro e o editor de texto. Os controles e o editor de texto oferecem suporte a arrastar e soltar OLE interativamente em tempo de execução, e os controles fornecem suporte programático em tempo de execução. O objeto DataObject fornece suporte programático a arrastar e soltar OLE para os controles.

Dois modos de arrastar e soltar OLE estão disponíveis para controles do Visual FoxPro: modo intrínseco e modo manual. No modo intrínseco, o Visual FoxPro trata intrinsecamente uma operação de arrastar e soltar OLE. No modo manual, operações de arrastar e soltar OLE são tratadas programaticamente. Os eventos que ocorrem são determinados pelo modo de arrastar e soltar OLE. Para mais informações, consulte a seção "Modos intrínseco e manual de arrastar e soltar OLE".

# Arrastar e soltar em versões anteriores do Visual FoxPro

Versões anteriores do Visual FoxPro ofereciam suporte a arrastar e soltar programático para controles, tornando possível mover controles em um formulário. Essa forma de arrastar e soltar ainda é suportada. Se você usar as configurações padrão para as propriedades OLEDragMode e OLEDropMode, suas aplicações existentes serão executadas como antes, sem alterações.

# O objeto DataObject

O objeto DataObject é um contêiner para dados sendo transferidos de uma origem de arrastar OLE para um destino de soltar OLE, e existe apenas durante a duração de uma operação de arrastar e soltar OLE. O objeto DataObject não pode ser criado programaticamente e referências a ele se tornam inválidas assim que a operação de arrastar e soltar OLE é concluída. O DataObject é passado como o parâmetro oDataObject nos eventos OLEStartDrag, OLEDragOver, OLEDragDrop e OLESetData.

O DataObject pode armazenar vários conjuntos de dados, cada um em um formato diferente. A existência de um formato específico no DataObject pode ser determinada com o método GetFormat. Consulte o método GetFormat para uma lista dos formatos suportados pelo DataObject.

### Métodos do objeto DataObject

O objeto DataObject tem métodos que permitem manipular programaticamente os dados sendo arrastados e soltos. A tabela a seguir lista os métodos disponíveis em tempo de execução para o DataObject.

| Método | Descrição |
| --- | --- |
| ClearData | Limpa todos os dados e formatos de dados do objeto DataObject de arrastar e soltar OLE. |
| GetData | Recupera dados do objeto DataObject de arrastar e soltar OLE. |
| GetFormat | Determina se dados em um formato especificado estão disponíveis no DataObject de arrastar e soltar OLE. |
| SetData | Coloca dados e seu formato no DataObject de arrastar e soltar OLE. |
| SetFormat | Coloca um formato de dados sem dados no DataObject de arrastar e soltar OLE. |
