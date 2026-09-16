# Uso de comandos e funções

Os comandos e funções do Visual FoxPro executam uma ação ou retornam valores para uso em outros comandos e funções. Comandos e funções podem aceitar expressões como parâmetros ou podem aparecer em expressões. Você também pode usar funções definidas pelo usuário (UDFs) sempre que puder usar um comando ou função do Visual FoxPro.

Comandos e funções se comportam de maneira diferente:
 - Comandos executam uma ação. Por exemplo, você pode usar o comando BROWSE para examinar o conteúdo de uma tabela.
- Funções retornam um valor de um determinado tipo de dados. Por exemplo, a função DATE( ) retorna a data do sistema do seu computador. As funções terminam com um par de parênteses que as distinguem dos comandos.

As funções não são usadas isoladamente, mas sempre combinadas com um comando do Visual FoxPro. Por exemplo, o ponto de interrogação (?) é um comando que envia saída para a tela. DATE( ) é uma função que retorna a data atual do sistema. Você pode combiná-los para exibir a data do sistema na tela:

```foxpro
? DATE()
```

Comandos e funções possuem uma sintaxe prescrita para parâmetros e cláusulas que você pode fornecer. Para uma descrição completa da sintaxe de qualquer comando ou função, consulte Referência de linguagem (Visual FoxPro).
