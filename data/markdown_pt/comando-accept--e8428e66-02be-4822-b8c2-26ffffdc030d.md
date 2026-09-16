# Comando ACCEPT

Incluído para compatibilidade com versões anteriores. Use o TextBox Control (Visual FoxPro) em vez disso.

Aceita dados de cadeia de caracteres da tela.

```foxpro
ACCEPT [expC] TO memvar
```

#### Parâmetros
 expC

 A expressão de caracteres expC é o texto de prompt que aparece ao lado da área em que os dados são inseridos. No FoxPro for Windows e no FoxPro for Macintosh, o texto de prompt aparece na mesma fonte da fonte da janela principal do FoxPro. No entanto, os dados de caracteres que você insere aparecem em FoxFont de 9 pontos.

 memvar

 A variável de memória ou elemento de matriz em que os dados de caracteres são armazenados é especificada com memvar. Se a variável de memória ou o elemento de matriz não estiver definido, ele é criado automaticamente pelo ACCEPT.

 Se você pressionar Enter sem inserir dados, a variável de memória ou o elemento de matriz contém a cadeia de caracteres nula. Se você pressionar Esc quando SET ESCAPE estiver OFF, a variável de memória contém a cadeia de caracteres nula. Se você pressionar Esc quando SET ESCAPE estiver ON, a execução do programa é suspensa.

# Observações

ACCEPT está incluído para compatibilidade com versões anteriores. Use @ ... GET em vez disso.

Este comando permite inserir dados de caracteres diretamente em uma variável de memória ou elemento de matriz sem delimitar os caracteres com aspas.

Se você precisar realizar validação de dados ou capturar erros, @ ... GET é uma opção melhor.

ACCEPT difere de INPUT de duas maneiras. Com ACCEPT:

 - Os dados que você insere são sempre tratados como tipo caractere.
- Você não precisa colocar os dados inseridos entre aspas.

# Exemplo

Este exemplo solicita um nome de cliente e exibe a variável de memória que contém o nome inserido.

```foxpro
ACCEPT 'ENTER THE CUSTOMER NAME: ' TO mcustname
? mcustname
```
