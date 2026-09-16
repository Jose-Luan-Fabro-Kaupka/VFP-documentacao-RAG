# Função FERROR( )

Retorna um número correspondente ao erro de função de arquivo de baixo nível mais recente.

```foxpro
FERROR()
```

# Valor de retorno

Numeric

# Observações

FERROR( ) retorna 0 se uma função de arquivo de baixo nível é executada com sucesso. Um valor positivo é retornado se uma função não é executada com sucesso. A tabela a seguir lista cada número de erro retornado por FERROR( ) e a causa do erro.

| Número do erro | Causa do erro |
| --- | --- |
| 2 | Arquivo não encontrado |
| 4 | Muitos arquivos abertos (sem handles de arquivo) |
| 5 | Acesso negado |
| 6 | Handle de arquivo inválido fornecido |
| 8 | Sem memória |
| 25 | Erro de seek (não é possível fazer seek antes do início de um arquivo) |
| 29 | Disco cheio |
| 31 | Erro ao abrir arquivo |
