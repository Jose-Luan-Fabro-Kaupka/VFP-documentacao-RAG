# Propriedade Icon (Visual FoxPro)

Para formulários, especifica o ícone exibido para um formulário em tempo de execução quando o formulário é minimizado. Disponível em tempo de design e em tempo de execução.

Para um objeto de projeto, especifica o ícone exibido para um aplicativo .exe distribuído.

```foxpro
Object.Icon[ = cFileName]
```

# Valor de retorno
 **cFileName**
Para um formulário, especifica o nome e o caminho do arquivo do ícone a exibir quando o formulário é minimizado. Para um aplicativo .exe distribuído, especifica o nome e o caminho do arquivo do ícone exibido para o aplicativo.

# Observações

Aplica-se a: Objeto Form | Objeto Project (Visual FoxPro) | Variável de sistema _SCREEN

Para formulários, use a propriedade Icon para especificar um ícone personalizado para qualquer formulário que o usuário possa minimizar em tempo de execução. Por exemplo, você pode atribuir um ícone exclusivo a um formulário para indicar a função do formulário. Digite o nome do arquivo do ícone na janela Propriedades em tempo de design. O nome do arquivo que você digitar deve ter a extensão .ico e formato de ícone. Se você não especificar um ícone personalizado, o ícone padrão do Visual FoxPro para formulários é usado.

Você pode usar a Biblioteca de ícones do Microsoft Visual FoxPro em HOME( )+"graphics\icons" como fonte de ícones.

> **Observação:** Se você definir a propriedade Icon em tempo de design e o arquivo que especificar não existir, o Visual FoxPro exibe uma mensagem de erro, mas a propriedade permanece definida para o arquivo que você especificou. O Visual FoxPro ignora a propriedade Icon em tempo de execução se ela estiver definida para um arquivo que não existe.

Para um objeto de projeto, use a propriedade Icon para especificar o ícone exibido para um aplicativo .exe distribuído. Você não pode especificar um ícone para um aplicativo Visual FoxPro .app distribuído.
