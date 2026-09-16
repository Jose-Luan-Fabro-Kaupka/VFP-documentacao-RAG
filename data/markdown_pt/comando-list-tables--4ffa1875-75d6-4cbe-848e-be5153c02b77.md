# Comando LIST TABLES

Exibe sem pausar todas as tabelas e informações sobre as tabelas contidas no banco de dados atual.

```foxpro
LIST TABLES   [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]]
   [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona as informações retornadas por LIST TABLES para uma impressora. Você pode incluir PROMPT para exibir uma caixa de diálogo Print antes do início da impressão. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de LIST TABLES para o arquivo em disco especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se você deseja substituir o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, então o arquivo é substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

As informações retornadas incluem os nomes e caminhos das tabelas e são um subconjunto das informações mostradas usando LIST STATUS. No entanto, as informações exibidas usando LIST TABLES contêm somente informações relacionadas a tabelas e exibem as informações independentemente de as tabelas estarem abertas.

# Exemplo

O exemplo a seguir abre a tabela `customer` no banco de dados `testdata`. LIST TABLES é usado para listar informações sobre as tabelas no banco de dados.

```foxpro
CLOSE DATABASES
SET PATH TO (HOME(2) + 'data\')   && Sets path to database
OPEN DATABASE testdata  && Open testdata database
CLEAR
LIST TABLES  && Lists information about tables in the database
```
