# Comando DISPLAY PROCEDURES

Exibe os nomes dos procedimentos armazenados no banco de dados atual.

```foxpro
DISPLAY PROCEDURES [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]]
   [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona para uma impressora as informações retornadas por DISPLAY PROCEDURES. Você pode incluir PROMPT para exibir uma caixa de diálogo Imprimir antes do início da impressão. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DISPLAY PROCEDURES para o arquivo especificado por FileName. Se o arquivo já existir e SET SAFETY estiver definido como ON, o Visual FoxPro exibirá uma solicitação perguntando se você deseja substituir o arquivo.
**ADDITIVE**
Acrescenta ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo será substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela ativa definida pelo usuário.

# Observações

Procedimentos armazenados são criados com APPEND PROCEDURES, COPY PROCEDURES ou MODIFY PROCEDURE.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata` e usa DISPLAY PROCEDURES para exibir os procedimentos armazenados (se houver) no banco de dados. Se não houver procedimentos armazenados no banco de dados, você poderá executar o exemplo do tópico Comando APPEND PROCEDURES para adicionar um procedimento ao banco de dados.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
CLEAR
DISPLAY PROCEDURES  && Displays stored procedures in the database
```
