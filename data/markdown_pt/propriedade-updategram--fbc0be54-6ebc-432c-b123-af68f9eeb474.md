# Propriedade UpdateGram

Contém o XML UpdateGram gerado apenas nas seguintes condições:
 - O Visual FoxPro executa comandos insert, update ou delete.
- As propriedades UpdateCmdDataSourceType , InsertCmdDataSourceType e DeleteCmdDataSourceType estão definidas como "XML".

Somente leitura em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UpdateGram
```

# Valor de retorno

Tipo de dados Character. UpdateGram contém um XML UpdateGram.

# Observações

Aplica-se a: Classe CursorAdapter

Embora um objeto CursorAdapter possa gerar o XML UpdateGram, você deve implementar a operação de atualização real usando os protocolos apropriados, como SQL XML por HTTP, SQL XML OLEDB ou serviço Web XML para .NET.

Para obter mais informações sobre atualização automática e XML, consulte Gerenciamento de acesso a dados usando CursorAdapters.
