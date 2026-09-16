# Regras de Validação de Campo e Registro

As regras de validação de campo e registro controlam como e o tipo de dados que você pode inserir em campos e registros de tabelas de banco de dados. As regras de validação oferecem as seguintes vantagens:
 - Fornecem uma maneira de aplicar regras de negócio de forma consistente.
- Ajudam você a escrever menos código.
- São aplicadas para todos os usuários da tabela de banco de dados, independentemente dos requisitos do aplicativo.

Ao usar regras de validação, os valores inseridos em campos e registros são comparados com as expressões de regra que você especifica. Se um valor inserido não atender aos requisitos da expressão de regra, o valor é rejeitado.

Por exemplo, você pode criar uma regra que compara o valor de um campo de código postal com uma tabela separada contendo as abreviações de código postal do seu país ou região e rejeita qualquer valor que não exista como uma abreviação de código postal válida.

> **Dica:** Evite criar regras em nível de campo ou registro que sejam específicas do aplicativo. Em vez disso, crie e use regras em nível de campo e registro para aplicar integridade de dados e regras de negócio que sempre se aplicam aos dados em seu banco de dados, independentemente de como ou quem acessa os dados.

> **Observação:** As regras de validação são armazenadas no arquivo de banco de dados (.dbc). Remover ou excluir uma tabela de banco de dados remove e exclui todas as regras em nível de campo e registro associadas a essa tabela. No entanto, stored procedures referenciadas pelas regras de validação removidas ou excluídas permanecem.

As seções a seguir contêm mais informações sobre o trabalho com regras de validação:
 - Choosing Between Field and Record Validation Rules
- Checking Field and Record Validation Rules

# Escolhendo Entre Regras de Validação de Campo e Registro

Você pode usar uma regra de validação em nível de campo quando o seguinte se aplica:
 - Você deseja controlar o tipo de informação que um usuário pode inserir em um campo.
- Você pode validar os dados em um campo independentemente de qualquer outra entrada no registro.
- Você deseja comparar valores inseridos em um campo com os valores em outra tabela.

Por exemplo, você pode usar uma regra de validação em nível de campo para garantir que um usuário não insira um número negativo em um campo que requer um valor positivo.

Você usa regras de validação em nível de registro quando o seguinte se aplica:
 - Você deseja controlar o tipo de informação que um usuário pode inserir em um registro.
- Você deseja comparar os valores de dois ou mais campos no mesmo registro para garantir que cumpram as regras de negócio do banco de dados.

Por exemplo, você pode usar uma regra de validação em nível de registro para garantir que o valor em um campo seja sempre maior que outro no mesmo registro.

# Verificando Regras de Validação de Campo e Registro

As regras de validação de campo e registro estão ativas mesmo quando os dados estão em buffer. Geralmente, as regras de validação de campo são verificadas quando o valor do campo é alterado; as regras de validação de registro são verificadas quando o valor do registro é alterado.

> **Observação:** Se um valor de campo ou registro não foi alterado, as regras de validação não são verificadas. Quando nenhum valor foi alterado, você pode navegar pelos campos sem validar dados.

A tabela a seguir descreve mais especificamente quando o Visual FoxPro verifica regras de validação de campo dependendo do método de entrada de dados.

| Changing values using | Window or command | Field validation rule is checked |
| --- | --- | --- |
| User interface | Browse window Form Other window | When moving off the field. |
| Commands that do not specify fields | APPEND Command APPEND GENERAL Command APPEND MEMO Command BROWSE Command CHANGE Command DELETE Command EDIT Command GATHER Command | When changing the field value. The rule is checked in the field order specified in the command. |
| Commands that do not specify fields | APPEND Command with BLANK clause INSERT - SQL Command | When appending or inserting the record. |
| Commands that specify fields | UPDATE - SQL Command REPLACE Command | In the field order specified in the command. |

Em contraste, o Visual FoxPro verifica regras de validação de registro sempre que o ponteiro de registro sai do registro, independentemente do método que você usa para inserir dados. Além disso, em uma janela browse, a regra de validação de registro é verificada se você modificar um registro mas não mover o ponteiro de registro, e então fechar a janela browse. O Visual FoxPro gera quaisquer mensagens de erro que ocorram e então fecha a janela browse.

> **Cuidado:** Não inclua comandos ou funções em suas regras de validação que tentem mover o ponteiro de registro na área de trabalho atual onde as regras de validação são verificadas. Por exemplo, incluir comandos ou funções como SEEK, LOCATE, SKIP, APPEND, APPEND BLANK, INSERT ou AVERAGE, COUNT, BROWSE e REPLACE FOR em regras de validação pode verificá-los recursivamente, criando uma condição de erro.

> **Observação:** Quando um trigger é chamado, o Alias é sempre o do cursor sendo atualizado, independentemente do Alias selecionado no código que causou o disparo do trigger.

Quando uma regra de validação de registro causa um erro durante um aplicativo em execução, você precisa incluir código de tratamento de erros. Normalmente, este código não permite que o usuário saia de um formulário ou altere o ambiente ativo até que o usuário corrija o erro ou cancele as alterações no registro.
