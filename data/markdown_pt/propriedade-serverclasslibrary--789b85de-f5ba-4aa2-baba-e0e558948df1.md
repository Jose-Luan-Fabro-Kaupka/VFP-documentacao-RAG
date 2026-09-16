# Propriedade ServerClassLibrary

Contém o nome da biblioteca de classes ou programa que contém uma classe de servidor. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Object.ServerClassLibrary
```

# Observações

Aplica-se a: Objeto Server

O nome da biblioteca de classes ou programa que contém a classe de servidor também é exibido na guia Servidores, caixa de diálogo Informações do projeto do diálogo Informações do projeto.

Servidores Automation são criados no Visual FoxPro adicionando classes definidas como OLEPUBLIC a um projeto e, em seguida, criando um arquivo executável (.exe) ou biblioteca de vínculo dinâmico (.dll) a partir do projeto. Você pode ter quantas classes OLEPUBLIC desejar no projeto e elas podem ser definidas em arquivos de programa (.prg) ou bibliotecas de classes (.vcx).

Para obter informações sobre como criar servidores Automation personalizados, consulte Como: criar servidores Automation.
