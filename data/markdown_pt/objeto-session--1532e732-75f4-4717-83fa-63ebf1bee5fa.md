# Objeto Session

Cria um objeto personalizado definido pelo usuário que gerencia sua própria sessão de dados.

```foxpro
DEFINE CLASS ClassName1 AS Session
```

# Observações

Essa classe personalizada definida pelo usuário só pode ser criada com o comando DEFINE CLASS. No entanto, você pode adicionar esse objeto a um formulário ou outro contêiner programaticamente.

Classes personalizadas definidas pelo usuário possuem propriedades, eventos e métodos, mas não têm representação visual. As mesmas regras gerais para definir outros tipos de classe se aplicam a elas. Use o objeto Session para gerenciar a memória com eficiência e garantir o comportamento seguro de várias instâncias de objetos em aplicativos multicamadas.

Consulte Programação orientada a objetos para obter mais informações sobre a criação de objetos personalizados como classes não visuais.

A partir do Visual FoxPro 7.0, os valores padrão de uma sessão de dados são:

| Configuração | Valor |
| --- | --- |
| EXCLUSIVE | ON |
| SAFETY | OFF |
| TALK | OFF |

Os valores padrão de um formulário com sessão de dados privada são:

| Configuração | Valor |
| --- | --- |
| EXCLUSIVE | OFF |
| SAFETY | ON |
| TALK | ON |

Um formulário que usa a sessão de dados padrão também usa as configurações existentes nessa sessão, pois ela foi criada antes do formulário.

Quando o objeto Session representa um servidor COM, todas as propriedades intrínsecas são tratadas como privadas.
