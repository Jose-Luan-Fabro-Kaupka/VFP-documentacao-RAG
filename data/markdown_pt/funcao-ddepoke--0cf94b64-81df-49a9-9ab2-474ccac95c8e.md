# Função DDEPoke( )

Envia dados entre aplicativos cliente e servidor em uma conversa de troca dinâmica de dados (DDE).

```foxpro
DDEPoke(nChannelNumber, cItemName, cDataSent
   [, cDataFormat [, cUDFName]])
```

#### Parâmetros
**nChannelNumber**
Especifica o número do canal do aplicativo para o qual os dados são enviados. Se for um canal de servidor, DDEPoke( ) enviará os dados em resposta a uma solicitação ou a um vínculo de notificação ou automático estabelecido anteriormente.
**cItemName**
Especifica o nome do item para o qual os dados são enviados. O nome do item é específico do aplicativo e deve ser compreendido por ele. Por exemplo, o Microsoft Excel aceita R1C1 como um nome de item válido que se refere à primeira célula de uma planilha.
**cDataSent**
Especifica os dados enviados ao nome de item indicado por cItemName.
**cDataFormat**
Especifica o formato usado para enviar os dados. O formato padrão é CF_TEXT. Nesse formato, os campos são delimitados por tabulações e os registros por um retorno de carro e uma alimentação de linha.
**cUDFName**
Permite a transferência assíncrona de dados. Se cUDFName for omitido, o cliente aguardará pelo período especificado com DDESetOption( ). Se você especificar o nome de uma função definida pelo usuário em cUDFName, a execução do programa cliente continuará imediatamente após a solicitação. Quando os dados estiverem disponíveis no aplicativo servidor, a função indicada será executada. A função definida pelo usuário recebe seis parâmetros nesta ordem: Parâmetro Conteúdo Número do canal O número do canal do aplicativo servidor. Ação XACTCOMPLETE (transação bem-sucedida). XACTFAIL (falha na transação). Item O nome do item; por exemplo, R1C1 para uma célula de planilha do Microsoft Excel. Dados Os novos dados (REQUEST) ou os dados passados (POKE ou EXECUTED). Formato O formato dos dados; por exemplo, CF_TEXT. Número da transação O número da transação retornado por DDEPoke( ). Use DDEAbortTrans( ) para cancelar uma transação não concluída. Se a transação falhar, use DDELastError( ) para determinar o motivo. Quando cUDFName é incluído, DDEPoke( ) retorna um número de transação em caso de êxito ou –1 se ocorrer um erro.

# Valor de retorno

Lógico

# Observações

DDEPoke( ) envia os dados como uma cadeia de caracteres para o nome de item no aplicativo especificado pelo número do canal.

Se os dados forem enviados com êxito, DDEPoke( ) retornará true (.T.). Se não puderem ser enviados, retornará false (.F.). Se a função assíncrona definida pelo usuário cUDFName for incluída, DDEPoke( ) retornará um número de transação; se ocorrer um erro, retornará –1.
