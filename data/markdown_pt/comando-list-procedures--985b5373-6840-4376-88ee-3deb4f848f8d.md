# Comando LIST PROCEDURES

Exibe continuamente os nomes dos procedimentos armazenados no banco de dados atual.

```foxpro
LIST PROCEDURES   [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]]   [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona as informações retornadas de LIST PROCEDURES para uma impressora. Você pode incluir PROMPT para exibir uma caixa de diálogo Imprimir antes do início da impressão. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de LIST PROCEDURES para o arquivo em disco especificado com FileName. Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se você deseja substituir o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

Procedimentos armazenados são criados com MODIFY PROCEDURES.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata` e usa LIST PROCEDURES para listar os procedimentos armazenados (se houver) no banco de dados.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
CLEAR
LIST PROCEDURES  && Lists stored procedures in the database
```
