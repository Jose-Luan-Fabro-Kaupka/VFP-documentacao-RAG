# Como: especificar aliases de destino para bandas Detail

Você pode especificar um alias de destino para cada banda Detail para variar a ordem de processamento de registros.

### Para especificar um alias de destino para uma banda Detail
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Edit Bands .
- Na caixa de diálogo Edit Bands, clique na banda Detail desejada e depois OK . A caixa de diálogo Detail Band Properties abre. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Detail é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Report Band Properties .
- Na caixa de diálogo Detail Band Properties, clique na guia Band.
- Na caixa Target alias expression, digite a expressão de alias de destino. Para construir uma expressão, clique no botão de reticências ( … ) para abrir o Expression Builder . Observação Colocar a expressão de destino entre aspas ( "" ) avalia a expressão como literal, enquanto omitir aspas avalia a expressão como uma variável contendo o alias de destino.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia Band, Caixa de diálogo Report Band Properties (Report Builder).
