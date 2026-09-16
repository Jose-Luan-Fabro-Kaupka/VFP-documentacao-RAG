# Comando INPUT

Incluído para compatibilidade retroativa. Use o Controle TextBox (Visual FoxPro) em vez disso.

Insere dados do teclado em uma variável de memória do sistema ou um elemento de array.

```foxpro
INPUT [expC] TO memvar
```

#### Parâmetros
expC

Incluir o expC para mostrar uma mensagem. expC é a mensagem que deseja mostrar.

memvar
memvar é a variável de memória do sistema ou um elemento de array no qual você deseja inserir dados inseridos do teclado. Se memvar é uma variável de memória do sistema que não existe, INPUT a cria.

A entrada de expressão do teclado determina o tipo de variável de memória do sistema ou elemento array criado. Se você inserir um valor numérico, uma variável de memória de sistema numérico ou elemento array é criado; se você inserir um valor de caráter, uma variável de memória de sistema de caracteres ou elemento array é criado, e assim por diante. Se você inserir um valor de caractere, ele deve ser delimitado por parênteses ou aspas simples ou duplas.

# Observações

INPUT está incluído para compatibilidade retroativa. Usar @ ... GET em vez disso.

INPUT é semelhante a ACCEPT, que não requer que as cadeias de caracteres sejam delimitadas e crie apenas variáveis de memória do sistema do tipo caráter.

# Exemplo

```foxpro
INPUT to mnum_exp
? mnum_exp
INPUT 'Enter company: ' TO mcompany
? mcompany
```

# Veja Também
- Elementos de linguagem compatíveis com o contrário
- Referência linguística (Visual FoxPro)
