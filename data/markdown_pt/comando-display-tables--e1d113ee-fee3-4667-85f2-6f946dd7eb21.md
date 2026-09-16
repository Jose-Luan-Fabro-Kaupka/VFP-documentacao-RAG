# Comando DISPLAY TABLES

Exibe nomes e informações sobre todas as tabelas contidas no banco de dados atual.

```foxpro
DISPLAY TABLES [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]] [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona a saída de DISPLAY TABLES para uma impressora. Você pode incluir PROMPT para exibir uma caixa de diálogo Imprimir antes do início da impressão. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DISPLAY TABLES para o arquivo especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se você deseja substituir o arquivo.
**ADDITIVE**
Acrescenta ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

As informações retornadas são um subconjunto das informações mostradas usando DISPLAY STATUS. No entanto, as informações exibidas usando DISPLAY TABLES contêm apenas informações relacionadas a tabelas e exibem as informações independentemente de as tabelas estarem abertas ou não.

As seguintes informações são exibidas:
 - Nome da tabela
- Caminho da tabela

# Exemplo

O exemplo a seguir abre a tabela `customer` no banco de dados `testdata`. DISPLAY TABLES é usado para exibir informações sobre as tabelas no banco de dados.

```foxpro
CLOSE DATABASES
SET PATH TO (HOME(2) + 'Data\')   && Sets path to database
OPEN DATABASE testdata  && Open testdata database
CLEAR
DISPLAY TABLES  && Displays information about tables in the database
```
