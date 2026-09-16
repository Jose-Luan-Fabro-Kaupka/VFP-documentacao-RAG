# Comando JOIN

Incluído para compatibilidade com versões anteriores. Use SELECT - SQL Command em vez disso.

Cria uma tabela unindo duas tabelas existentes.

```foxpro
JOIN WITH expN | WITH expC
	TO file
	FOR expL
	[FIELDS field list]
	[NOOPTIMIZE]
```

# Observações

JOIN está incluído para compatibilidade com versões anteriores. Use SELECT - SQL em vez disso.

JOIN cria uma nova tabela a partir de duas outras tabelas: a tabela atual e uma segunda tabela identificada pelo número da área de trabalho ou alias. JOIN posiciona o ponteiro de registro no primeiro registro da tabela atual e pesquisa nos registros da segunda tabela.
