# Propriedade DataSession

Especifica se um objeto pode ser executado em sua própria sessão de dados com um data environment exclusivo. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.DataSession[ = nSession]
```

# Valor de retorno
 **nSession**
Especifica um valor numérico para a propriedade DataSession. A tabela a seguir lista os valores de nSession. Configuração Descrição 1 Sessão de dados padrão. (Padrão, exceto para objetos Session) 2 Sessão de dados privada. Cria uma nova sessão de dados para cada instância criada. (Padrão para objetos Session.)

# Observações

Aplica-se a: Form Object | FormSet Object | _SCREEN System Variable | Session Object | ToolBar Object
