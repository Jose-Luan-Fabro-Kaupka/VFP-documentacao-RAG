# Como: criar e usar aliases de tabela

Quando você abre uma tabela, o Visual FoxPro usa automaticamente o nome do arquivo da tabela como o alias padrão. Em certas condições, o Visual FoxPro atribui seu próprio alias padrão. No entanto, você também pode criar seu próprio alias.

> **Observação:** Após atribuir um alias definido pelo usuário, você deve usar o alias para se referir à tabela a partir de então.

### Para atribuir um alias definido pelo usuário a uma tabela
- Abra a tabela com o comando USE, o nome da tabela e a cláusula ALIAS com o alias de tabela que deseja.

Para obter mais informações, consulte Comando USE.

### Para referenciar um campo em uma tabela aberta de outra área de trabalho
- Coloque o nome da tabela ou alias e um ponto (.) ou o operador -> antes do nome do campo.

Por exemplo, suponha que você deseja acessar um campo chamado Contact em uma tabela chamada Customer que está aberta em uma área de trabalho diferente. O exemplo a seguir ilustra como você pode referenciar o campo:

`Customer.Contact`

Se a tabela que você deseja referenciar foi aberta com um alias, você pode usar o nome do alias. Por exemplo, se a tabela Customer foi aberta com o alias People, o exemplo a seguir ilustra como você pode referenciar o campo Contact com o alias:

`People.Contact`
