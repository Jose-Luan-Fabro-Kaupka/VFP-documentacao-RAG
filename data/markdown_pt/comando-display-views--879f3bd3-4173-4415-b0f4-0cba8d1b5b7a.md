# Comando DISPLAY VIEWS

Exibe informações sobre views SQL no banco de dados atual e indica se as views SQL são baseadas em tabelas locais ou remotas.

```foxpro
DISPLAY VIEWS [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]] [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona a saída de DISPLAY VIEWS para uma impressora. Você pode incluir PROMPT para exibir a caixa de diálogo Print antes do início da impressão. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DISPLAY VIEWS para o arquivo especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se você deseja substituir o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

Use DBGETPROP( ) para retornar informações adicionais sobre views SQL no banco de dados atual.

Views SQL são criadas com CREATE SQL VIEW.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata`. CREATE SQL VIEW é usado para criar uma view SQL local chamada `myview`. O View Designer é exibido, permitindo especificar tabelas e condições para a view SQL. Depois de salvar a view SQL que você criou, informações sobre as views SQL no banco de dados são exibidas.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
CREATE SQL VIEW myview
CLEAR
DISPLAY VIEWS
```
