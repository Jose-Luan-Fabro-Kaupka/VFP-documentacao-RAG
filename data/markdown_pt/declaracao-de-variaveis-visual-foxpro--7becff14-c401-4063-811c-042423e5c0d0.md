# Declaração de variáveis (Visual FoxPro)

Você pode comparar como a declaração de variáveis difere entre o Visual FoxPro e outras linguagens de programação. No Visual FoxPro, você não atribui um tipo de dados a uma variável. No entanto, é recomendável nomear sua variável com um prefixo que sugira o tipo de dados com o qual planeja usá-la. Outras linguagens exigem que você atribua um tipo de dados a uma variável quando a declara. Para obter mais informações, consulte Convenções de nomenclatura de variáveis.

> **Observação:** Quando você armazena um valor em uma variável e a variável não existe, o Visual FoxPro a declara implicitamente com escopo PRIVATE. Outras linguagens que exigem declaração explícita de variáveis retornam um erro. Para criar variáveis no Visual FoxPro com escopo PUBLIC ou LOCAL, você deve declará-las explicitamente com o comando PUBLIC ou LOCAL. Para obter mais informações, consulte Comando PUBLIC e Comando LOCAL.

| Visual FoxPro | BASIC |
| --- | --- |
| As variáveis são declaradas implicitamente sem tipagem de dados. | As variáveis podem ser declaradas implicitamente, e o nome da variável determina o tipo de dados. |

| Pascal | C/C++ |
| --- | --- |
| As variáveis devem ser declaradas explicitamente e atribuídas a um tipo de dados. | As variáveis devem ser declaradas explicitamente e atribuídas a um tipo de dados. |
