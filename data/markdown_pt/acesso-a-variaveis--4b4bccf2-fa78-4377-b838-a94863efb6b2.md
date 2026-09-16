# Acesso a variáveis

As variáveis existem apenas enquanto um aplicativo está em execução ou durante a sessão do Visual FoxPro em que são criadas. Para especificar o escopo de uma variável, use as palavras-chave LOCAL, PRIVATE e PUBLIC.
 - LOCAL cria variáveis ou arrays que podem ser usados e modificados apenas no programa em que são criados e não podem ser acessados por programas de nível superior ou inferior. Variáveis e arrays locais são liberados assim que o programa que os contém deixa de ser executado.
- PRIVATE oculta variáveis ou arrays que foram definidos em um programa chamador do programa atual. Você pode então reutilizar esses nomes de variável no programa atual sem afetar as variáveis originais. Depois que o programa que contém PRIVATE deixa de ser executado, todas as variáveis e arrays que foram declarados como private ficam disponíveis novamente.
- PUBLIC define variáveis ou arrays globais. Variáveis e arrays globais podem ser usados e modificados em qualquer programa executado durante a sessão atual do Visual FoxPro. Qualquer variável ou array que você cria na janela Command é automaticamente public.

# Acessando variáveis

Se uma variável tem o mesmo nome de um campo, o Visual FoxPro sempre dá precedência ao nome do campo. Você pode referenciar a variável usando `m.` ou `m->` mais o nome da variável, como nos exemplos a seguir.

```foxpro
?  m.cFname
?  m->cFname      && print value in cFname
?  cFname         && prints contents of field cFname
```

Para obter mais informações sobre esses comandos, consulte os tópicos apropriados na Ajuda.

> **Observação:** Na programação orientada a objetos, você pode criar propriedades de objetos para armazenar valores em vez de usar variáveis. Para obter mais informações, consulte Programação orientada a objetos .
