# Comando VALIDATE DATABASE

Garante que os locais das tabelas e índices no banco de dados atual estão corretos.

```foxpro
VALIDATE DATABASE [RECOVER] [NOCONSOLE]
   [TO PRINTER [PROMPT] | TO FILE FileName]
```

#### Parâmetros
 **RECOVER**
Exibe caixas de diálogo que permitem localizar tabelas e índices que não estão nos locais contidos no banco de dados. A partir do Visual FoxPro 7, a cláusula RECOVER é suportada em programas.
**NOCONSOLE**
Suprime a saída de mensagens de erro para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.
**TO PRINTER [PROMPT]**
Direciona a saída de mensagens de erro de VALIDATE DATABASE para uma impressora. PROMPT exibe uma caixa de diálogo Print antes do início da impressão. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER .
**TO FILE FileName**
Direciona a saída de mensagens de erro para o arquivo especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, você será perguntado se deseja sobrescrever o arquivo.

# Observações

VALIDATE DATABASE garante que o banco de dados contém os locais corretos das tabelas e índices, que as tabelas no banco de dados contêm os campos corretos e que as tags de índice no banco de dados existem.

VALIDATE DATABASE opera no banco de dados atual. O banco de dados deve ser aberto para uso exclusivo incluindo a palavra-chave EXCLUSIVE quando você emitir OPEN DATABASE.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata` e usa VALIDATE DATABASE para garantir que os locais das tabelas e índices no banco de dados estão corretos.

```foxpro
CLOSE DATABASES
SET PATH TO (HOME(2) + 'Data\') && Sets path to database
OPEN DATABASE testdata EXCLUSIVE && Open testdata database
VALIDATE DATABASE
```
