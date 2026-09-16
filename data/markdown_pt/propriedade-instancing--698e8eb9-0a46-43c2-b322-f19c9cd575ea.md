# Propriedade Instancing

Especifica como um servidor em um projeto pode ser instanciado. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Instancing[ = nExpression]
```

# Valor de retorno
 **nExpression**
Especifica como o servidor pode ser instanciado. A tabela a seguir lista os valores de nExpression com uma descrição de cada um. Configurações Constante FoxPro.h Descrição 0 SERVERINSTANCE_NOTCREATABLE Permite criar instâncias da classe somente dentro do Visual FoxPro. 1 SERVERINSTANCE_SINGLEUSE (Padrão) Permite criar uma instância da classe tanto dentro do Visual FoxPro quanto fora dele usando Automation. Cada solicitação de uma instância da classe por um cliente de automação fora do projeto faz com que uma cópia separada do servidor de automação seja iniciada. 2 SERVERINSTANCE_MULTIUSE Permite criar uma instância da classe tanto dentro do Visual FoxPro quanto fora dele usando Automation. Cada solicitação de uma instância da classe por um cliente de automação fora do projeto faz com que uma cópia já em execução do servidor de automação seja fornecida como origem da nova instância.

# Observações

Aplica-se a: Server Object
