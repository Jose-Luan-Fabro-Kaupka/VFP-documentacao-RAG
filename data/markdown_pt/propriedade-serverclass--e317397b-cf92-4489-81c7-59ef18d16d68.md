# Propriedade ServerClass

Contém o nome de uma classe de servidor em um projeto. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Object.ServerClass
```

# Observações

Aplica-se a: Server Object

Os nomes das classes de servidor em um projeto também são exibidos na guia Servers, Caixa de diálogo Informações do projeto da caixa de diálogo Informações do projeto.

Servidores de automação são criados no Visual FoxPro adicionando classes definidas como OLEPUBLIC a um projeto e, em seguida, compilando um arquivo executável (.exe) ou biblioteca de vínculo dinâmico (.dll) a partir do projeto. Você pode ter quantas classes OLEPUBLIC desejar no projeto e elas podem ser definidas em arquivos de programa (.prg) ou bibliotecas de classes (.vcx).

Para obter informações sobre como criar servidores de automação personalizados, consulte Como: criar servidores de automação.
