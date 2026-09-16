# Função GETAUTOINCVALUE( )

Retorna o último valor gerado para um campo com autoincremento dentro de uma sessão de dados.

```foxpro
GETAUTOINCVALUE([nDataSessionNumber | 0])
```

#### Parâmetros
 **nDataSessionNumber**
Especifica o número da sessão de dados para a qual o valor do campo com autoincremento é retornado. O valor do campo com autoincremento é retornado para a sessão de dados atual se você omitir os parâmetros nDataSessionNumber e 0. Use SET DATASESSION para ativar uma sessão de dados específica.
**0**
Especifica que o último valor de campo com autoincremento retornado é derivado do escopo atual (função, método, procedimento). Use isso para impedir que eventos fora desse bloco de código atual, como ON KEY LABEL, executem código que possa alterar o valor inesperadamente.

# Valor de retorno

Tipo de dados numérico. O valor retornado por GETAUTOINCVALUE( ) é o último valor de autoincremento gerado, mesmo se um campo não foi atualizado com sucesso com o valor de autoincremento. .NULL. é retornado se um valor de autoincremento ainda não foi gerado para uma sessão de dados. Por exemplo, .NULL. é retornado se uma sessão de dados é aberta e nenhuma atualização ocorreu.

# Observações

O valor do campo com autoincremento é atualizado para operações de tabela como o comando APPEND, o comando INSERT, o comando APPEND FROM e o comando BLANK quando a opção AUTOINC está incluída. Consulte Autoincrementing Field Values in Tables para obter mais informações sobre campos com autoincremento.
