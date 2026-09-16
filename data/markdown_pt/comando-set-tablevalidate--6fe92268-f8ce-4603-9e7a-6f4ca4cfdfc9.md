# Comando SET TABLEVALIDATE

Especifica o nível de validação de tabela a ser executado. Use SET TABLEVALIDATE quando você desejar um nível mais baixo de verificação de integridade de tabela que a configuração padrão.

```foxpro
SET TABLEVALIDATE TO [nLevel]
```

#### Parâmetros
 **nLevel**
Especifica o nível de validação de tabela como a soma dos valores de bit. Observação A configuração padrão para nLevel é 3. A tabela a seguir descreve os bits e valores de bit que você pode adicionar para obter uma configuração para nLevel. Número do bit Valor do bit (aditivo) Descrição 0 0 Não executa validação de tabela. 0 1 Valida a contagem de registros ao abrir uma tabela. Observação O cabeçalho da tabela (.dbf) é bloqueado durante a validação. Esta operação pode resultar em escalabilidade reduzida quando as tabelas são abertas como compartilhadas, por exemplo, ao emitir o comando USE com a palavra-chave SHARED ou chamar os comandos SQL SELECT, UPDATE, INSERT ou DELETE contra uma tabela fechada, e SET EXCLUSIVE está definido como OFF. 1 2 Valida a contagem de registros ao acrescentar ou inserir registros e gravá-los em disco. 2 4 Suprime "File is in use (Error 3)" se o cabeçalho da tabela não puder ser bloqueado ao abrir a tabela. Requer definir o primeiro bit para validar a contagem de registros ao abrir uma tabela. Observação Ao abrir uma tabela, o comando USE tenta bloquear o cabeçalho da tabela apenas uma vez. Se o cabeçalho estiver bloqueado, o Visual FoxPro executa uma verificação rigorosa do cabeçalho, semelhante a SET TABLEVALIDATE definido como 1. Caso contrário, o Visual FoxPro suprime o erro "File is in use" e executa uma verificação de cabeçalho da maneira das versões anteriores ao Visual FoxPro 8.0. 3 8 Verifica o cabeçalho .dbf antes de salvar a operação de append em disco e modificar o cabeçalho.

# Observações

SET TABLEVALIDATE não tem funcionalidade de reparo; ele executa apenas verificações de integridade conforme especificado por nLevel.

SET TABLEVALIDATE não executa validação de tabela em arquivos temporários ou cursors.

Você pode definir SET TABLEVALIDATE em Config.fpw da seguinte forma:

```foxpro
TABLEVALIDATE = nLevel
```

Se uma tabela é aberta de forma exclusiva e SET TABLEVALIDATE está definido como 8 ou superior, a configuração é ignorada.
