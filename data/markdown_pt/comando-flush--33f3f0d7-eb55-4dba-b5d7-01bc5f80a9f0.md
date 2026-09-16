# Comando FLUSH

Salva alterações de tabela e índice no disco.

Você pode usar FLUSH para salvar explicitamente no disco todas as alterações que faz em todas as tabelas e índices abertos. Você também pode salvar alterações em uma tabela específica especificando uma área de trabalho, alias de tabela ou caminho e nome de um arquivo atualmente aberto.

```foxpro
FLUSH [[IN nWorkArea | cTableAlias] | [cFileSpec]] [FORCE]
```

#### Parâmetros
 **[IN nWorkArea | cTableAlias ] | [ cFileSpec ]**
Especifica o número da área de trabalho, alias de tabela ou o nome de um arquivo atualmente aberto, por exemplo, um arquivo de índice ou um arquivo aberto usando a função FOPEN( ). Ao especificar um nome de arquivo, inclua o caminho, por exemplo, C:\MyApp\MyTable.dbf. Observação Se você especificar cFileSpec, apenas as alterações no arquivo especificado são salvas, a menos que cFileSpec seja o nome de um arquivo de tabela (.dbf), caso em que FLUSH se aplica ao arquivo memo da tabela (.fpt) e a todos os índices abertos para essa tabela, mesmo se a tabela estiver aberta em outra sessão de dados. Se você não especificar nWorkArea, cTableAlias ou cFileSpec, FLUSH se aplica a todas as tabelas e índices abertos na sessão de dados atual.
**FORCE**
Chama a função Windows API FlushFileBuffers para todos os arquivos afetados, mas não se aplica a arquivos temporários e arquivos abertos como somente leitura. Para obter mais informações, consulte a documentação online do MSDN.

# Observações

O Visual FoxPro salva automaticamente alterações no disco ao executar as seguintes operações:
 - Fechar uma tabela usando o comando USE, CLOSE ALL ou CLOSE DATABASES. Apenas as informações do arquivo ou arquivos que você fecha são salvas no disco.
- Desbloquear um registro ou arquivo. Apenas as informações do registro ou arquivo desbloqueado são salvas no disco.
