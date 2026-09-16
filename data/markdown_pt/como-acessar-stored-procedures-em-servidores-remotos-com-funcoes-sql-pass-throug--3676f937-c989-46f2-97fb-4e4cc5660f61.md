# Como: acessar stored procedures em servidores remotos com funções SQL Pass-Through

Você pode usar a tecnologia SQL pass-through do Visual FoxPro para criar e executar stored procedures em um servidor remoto. Stored procedures podem aumentar muito o poder, a eficiência e a flexibilidade do SQL, e melhorar dramaticamente o desempenho de instruções e lotes SQL. Muitos servidores fornecem stored procedures para definir e manipular objetos de banco de dados do servidor e para executar administração do sistema e do usuário no servidor.

> **Observação:** Os exemplos nesta seção usam sintaxe do Microsoft SQL Server, salvo indicação em contrário.

### Para chamar uma stored procedure do servidor
- Use a função SQLEXEC( ) com o nome da stored procedure.

Por exemplo, o código a seguir exibe os resultados da chamada de uma stored procedure chamada `sp_who` no SQL Server usando uma conexão ativa com a fonte de dados `sqlremote`:

```foxpro
nConnectionHandle = SQLCONNECT('sqlremote')
? SQLEXEC(nConnectionHandle, 'use pubs')
? SQLEXEC(nConnectionHandle, 'sp_who')
BROWSE
```

Para obter mais informações sobre a criação e execução de stored procedures em um servidor remoto, consulte a documentação do seu servidor.
