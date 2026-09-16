# SYS(3054) - Nível de otimização Rushmore Query

Habilita ou desabilita a exibição dos níveis de otimização Rushmore para consultas.

```foxpro
SYS(3054 [, 0 | 1 | 11 | 2 | 12] [, cMEMVAR])
```

#### Parâmetros
 **0**
(Padrão) Desabilita a exibição dos níveis de otimização Rushmore.
**1**
Habilita a exibição dos níveis de otimização de filtro Rushmore.
**11**
Habilita a exibição dos níveis de otimização de junção Rushmore.
**2**
Inclui a instrução SQL com a exibição dos níveis de otimização de filtro Rushmore.
**12**
Inclui a instrução SQL com a exibição dos níveis de otimização de junção Rushmore.
**cMEMVAR**
Especifica uma variável de memória PUBLIC ou LOCAL não declarada ou declarada na qual armazenar as informações do showplan. Se você não declarou cMEMVAR , o Visual FoxPro a cria como uma variável PRIVATE.

# Valor de retorno

Caractere

# Observações

SYS(3054) retorna a configuração atual do nível de otimização Rushmore como uma cadeia de caracteres para a tela ativa ou para uma variável de memória.

A saída do showplan exibe o alias da tabela como referência para o nome da tabela.

Use SYS(3054) para melhorar o desempenho de consultas determinando em que medida a consulta é otimizada pela tecnologia Rushmore.

Emita SYS(3054, 1) para exibir o nível de otimização de filtro Rushmore após a execução de uma consulta. O nível de otimização de filtro é exibido na janela ativa.

A tabela a seguir lista os três níveis de otimização Rushmore:

| Nível de otimização | Descrição |
| --- | --- |
| None | A consulta não pôde ser otimizada com a tecnologia Rushmore. |
| Partial | Algumas expressões na consulta puderam ser otimizadas com a tecnologia Rushmore. As tags de índice usadas para otimização Rushmore são listadas. |
| Full | A consulta foi totalmente otimizada com a tecnologia Rushmore. As tags de índice usadas para otimização Rushmore são listadas. |

Se SYS(3054,1) indicar que uma consulta não pôde ser otimizada ou pôde ser otimizada apenas parcialmente, você pode modificar a consulta para aproveitar a otimização Rushmore.

Emita SYS(3054, 11) para exibir o nível de otimização de junção Rushmore após a execução de uma consulta. O nível de otimização é exibido na janela ativa.

Emita SYS(3054, 0) para interromper a exibição do nível de otimização Rushmore após a execução de uma consulta.

Para obter mais informações sobre a tecnologia Rushmore e a otimização de consultas, consulte Using Rushmore Query Optimization to Speed Data Access.

# Exemplo

O código a seguir exibe o nível de otimização Rushmore após executar uma consulta:

```foxpro
LOCAL cmemvar
=SYS(3054,11,"cmemvar")
SELECT * FROM HOME()+"labels.dbf"
? cmemvar
```
