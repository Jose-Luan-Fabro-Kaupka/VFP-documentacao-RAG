# Variável de sistema _TRANSPORT

Incluída para compatibilidade com versões anteriores.

Especifica o programa usado para transportar telas, etiquetas e relatórios entre diferentes plataformas e versões do FoxPro.

```foxpro
_TRANSPORT = program name
```

#### Parâmetros
 file name especifica o nome do seu programa de conversão e pode incluir um caminho.

Se você escrever seu próprio transportador, ele deve aceitar um parâmetro — o nome do relatório, etiqueta ou formulário de tela a transportar. Seu transportador deve retornar um parâmetro. O parâmetro pode ser um dos seguintes valores:

Código de retorno Significado

1 Transportado com sucesso

2 Aberto sem transportar

3 Transporte cancelado

Para obter mais informações sobre o transporte de telas, etiquetas e relatórios, consulte o capítulo "Transporting Files Platforms" no FoxPro Developer's Guide.

# Observações

Por padrão, _TRANSPORT contém TRANSPRT.PRG, o programa de conversão de telas, etiquetas e menus instalado no diretório ou pasta do FoxPro.

O programa que você especificar com _TRANSPORT é executado quando você tenta abrir uma tela, etiqueta ou relatório criado em uma versão anterior do FoxPro ou em uma plataforma FoxPro diferente. Para especificar um programa diferente de TRANSPRT.PRG para transportar suas telas, etiquetas e relatórios, armazene o nome do programa em _TRANSPORT. Se seu programa de conversão estiver em um diretório diferente do diretório padrão atual, inclua o caminho com o nome do programa.

Se você renomear TRANSPRT.PRG ou movê-lo para outro diretório, armazene o novo nome de arquivo e/ou seu diretório em _TRANSPORT.

Você também pode especificar um programa de conversão no arquivo de configuração do FoxPro incluindo a seguinte linha:

 _TRANSPORT = file name
