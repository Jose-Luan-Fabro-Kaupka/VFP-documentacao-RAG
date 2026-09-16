# Comando SET DELETED

Especifica se o Visual FoxPro processa registros marcados para exclusão e se eles estão disponíveis para uso com outros comandos.

```foxpro
SET DELETED ON | OFF
```

#### Parâmetros
 **ON**
Especifica que comandos que operam em registros, incluindo registros em tabelas relacionadas, usando um escopo ignoram registros que estão marcados para exclusão.
**OFF**
Especifica que comandos que operam em registros, incluindo registros em tabelas relacionadas, usando um escopo podem acessar registros marcados para exclusão. (Padrão) Observação Chamar SQL SELECT com SET DELETED OFF inclui registros que atendem aos critérios especificados no conjunto de resultados e define esses registros como disponíveis para processamento. Ou seja, SET DELETED OFF não é definido para os registros no conjunto de resultados.

# Observações

Consultas que usam DELETED( ) para testar o status dos registros podem ser otimizadas usando a tecnologia Rushmore Query Optimization se a tabela estiver indexada em DELETED( ).

Para obter mais informações sobre otimização de consultas, consulte Using Rushmore Query Optimization to Speed Data Access.

Você pode marcar registros para exclusão emitindo DELETE – SQL ou DELETE, ou escolhendo Delete Records... no menu Table a partir de uma janela Browse ou Edit.

Você pode recuperar registros emitindo RECALL ou escolhendo Recall Records... no menu Table a partir de uma janela Browse ou Edit.

> **Observação:** SET DELETED é ignorado se o escopo padrão do comando é o registro atual ou se você incluir um escopo de um único registro. A exceção existe com o comando SEEK, no qual caso SET DELETED é sempre respeitado. INDEX e REINDEX sempre ignoram SET DELETED e indexam todos os registros na tabela.

SET DELETED tem escopo na sessão de dados atual.
