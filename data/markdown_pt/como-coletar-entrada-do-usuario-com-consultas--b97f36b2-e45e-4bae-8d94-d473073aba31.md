# Como: coletar entrada do usuário com consultas

Se você deseja coletar valores que o usuário da aplicação insere em um formulário, pode criar variáveis para armazenar esses valores e usá-las imediatamente na instrução SQL SELECT ou executar a instrução posteriormente. Para obter mais informações sobre personalização de consultas usando instruções SQL SELECT, consulte Como: personalizar consultas usando instruções SQL SELECT e o comando SELECT - SQL.

### Para coletar valores de entrada do usuário para uso imediato
- Na instrução SQL SELECT, inclua o nome do formulário ou uma referência ao formulário onde apropriado.

O exemplo a seguir ilustra como coletar valores de entrada do usuário de um formulário usando uma referência abreviada que aparece na cláusula WHERE da instrução SQL SELECT. A referência abreviada, `THISFORM`, refere-se ao formulário atualmente ativo. Você deve substituir nomes de controle por `ControlName1` e `ControlName2`.

```foxpro
SELECT * ;
   FROM tastrade!customer ;
   WHERE customer.country = ;
    THISFORM.ControlName1.Value ;
   AND customer.region =
THISFORM.ControlName2.Value ;
   GROUP BY customer.postal_code ;
   ORDER BY customer.postal_code,
customer.company_name
```

Para armazenar valores de entrada do usuário de um formulário quando você não precisa usá-los enquanto o formulário está ativo, use variáveis no código. Por exemplo, se você não deseja usar referências a um controle, pode definir variáveis no código para armazenar os valores retornados pelo controle.

### Para coletar valores de entrada do usuário para uso posterior
- Defina a variável que deseja usar para armazenar o valor de entrada do usuário.
- Na instrução SQL SELECT, inclua o nome da variável onde apropriado.

O exemplo a seguir ilustra como coletar valores de entrada do usuário de um formulário usando a variável `cValue` para armazenar o valor retornado por um controle no formulário atualmente ativo. A referência abreviada, `THISFORM`, refere-se ao formulário atualmente ativo. A variável aparece na cláusula WHERE da instrução SQL SELECT para selecionar o país que corresponde a `cValue`.

```foxpro
cValue = THISFORM.ControlName.Value
SELECT * ;
   FROM tastrade!customer ;
   WHERE customer.country = cValue ;
   GROUP BY customer.postal_code ;
   ORDER BY customer.postal_code, ;
     customer.company_name
```

Se você não definir a variável antes de executar a consulta, aparece uma mensagem de erro informando que a variável não pôde ser encontrada. Se a variável não estiver definida no código, o Visual FoxPro assume que a variável está pré-inicializada.
