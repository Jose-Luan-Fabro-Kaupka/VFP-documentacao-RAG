# Substituição de macro (Visual FoxPro)

Você pode substituir nomes por variáveis usando substituição de macro. Para usar substituição de macro, coloque um e comercial (&) antes da variável para informar ao Visual FoxPro que use o valor da variável como um nome e use um ponto (.) para encerrar a expressão de substituição de macro.

Por exemplo, a instrução print a seguir produz "FoxPro":

```foxpro
x = "Fox"
? "&x.Pro"
```

Um comando ou função contendo uma expressão de nome é executado mais rapidamente que um contendo substituição de macro, portanto use uma expressão de nome em vez de substituição de macro sempre que possível. Para obter mais informações sobre substituição de macro, consulte o tópico & Command na Ajuda.
