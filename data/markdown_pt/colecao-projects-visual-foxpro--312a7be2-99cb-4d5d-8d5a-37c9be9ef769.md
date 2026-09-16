# Coleção Projects (Visual FoxPro)

Uma coleção de objetos de projeto.

```foxpro
Projects
```

# Observações

Aplica-se a: _VFP System Variable | Application Object

Uma coleção de projetos fornece acesso a objetos de projeto, permitindo manipular um projeto e arquivos e servidores dentro do projeto.

Os itens na coleção de projetos podem ser referenciados por número de índice ou por nome. Por exemplo, o código a seguir recompila o projeto aberto mais recentemente:

```foxpro
_VFP.Projects(1).Build()
```

O código a seguir recompila o projeto chamado MyProject:

```foxpro
_VFP.Projects('MyProject.pjx').Build()
```

Para obter mais informações sobre a coleção de projetos, consulte Project Manager Hooks.
