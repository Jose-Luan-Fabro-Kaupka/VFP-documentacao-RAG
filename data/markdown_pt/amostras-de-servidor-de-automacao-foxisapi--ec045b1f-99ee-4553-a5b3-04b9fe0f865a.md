# Amostras de servidor de automação FoxISAPI

O Visual FoxPro inclui uma extensão ISAPI chamada Foxisapi.dll que permite acessar servidores de automação personalizados do Visual FoxPro de qualquer servidor Web compatível com ISAPI, como o Microsoft Internet Information Services (IIS) versão 5.0 ou posterior e o Microsoft Personal Web Server. A extensão FoxISAPI funciona criando uma instância de um servidor de automação do Visual FoxPro e então chamando um método nesse servidor que retorna HTML. O HTML é passado do servidor Web de volta para um navegador Web como o Microsoft Internet Explorer.

> **Observação:** O Foxisapi.dll destina-se exclusivamente como uma extensão ISAPI de exemplo para ilustrar o uso de servidores de automação do Visual FoxPro com um servidor Web compatível com ISAPI. O Foxisapi.dll não deve ser usado em sistemas de produção ou protegidos.

O Visual FoxPro inclui duas amostras de servidor de automação FoxISAPI que demonstram como você pode usar o poder do Visual FoxPro para suportar dinamicamente um site Web. A primeira amostra, FoxWeb, um Servidor de Automação de Internet Visual FoxPro Simplificado, localizada na pasta Samples\Servers\FoxIsapi\FoxWeb, é uma amostra simples projetada para demonstrar conceitos básicos do FoxISAPI. Esta amostra orienta você pelo processo de configuração e implantação de servidores FoxISAPI, tanto locais quanto remotamente. Além disso, a amostra percorre as etapas necessárias para implementar pooling de servidores para melhor escalabilidade.

A segunda amostra, FoxIs, um Servidor de Internet Visual FoxPro, localizada na pasta Samples\Servers\FoxIsapi\FoxIs, é uma amostra mais complexa que contém rotinas para mapear o conteúdo visual e funcional de um formulário do Visual FoxPro para HTML. Os conceitos são os mesmos do FoxWeb; o FoxISAPI instancia um servidor e invoca um método para retornar HTML. Como a amostra FoxIs usa um formulário visual, oferece versatilidade adicional permitindo executá-la como um programa autônomo, de clientes OLE e de um navegador Web.

Se você não está familiarizado com a criação de servidores de automação do Visual FoxPro, consulte Como: criar servidores de automação.

# Componentes FoxISAPI

A tabela a seguir lista os arquivos principais da amostra de servidor de automação FoxWeb e uma descrição de cada um.

| Arquivo | Descrição |
| --- | --- |
| Foxisapi.dll | O componente principal das amostras de servidor de automação FoxISAPI, FoxWeb e FoxIs. Foxisapi.dll é usado com IIS ou Microsoft Personal Web Server. Foxisapi.dll cria uma instância de um servidor de automação do Visual FoxPro e executa um método nesse servidor. O método então retorna o HTML exibido no navegador Web. Foxisapi.dll é usado principalmente com o Visual FoxPro; no entanto, pode ser usado com qualquer servidor de automação. |
| Foxisapi.ini | Um arquivo de inicialização para o arquivo Foxisapi.dll que permite configurar o Foxisapi.dll. |
| Odebug.prg | Um programa Visual FoxPro usado para depurar seus aplicativos de Internet. |

# Configurando componentes FoxISAPI

Para instalar os componentes principais do FoxISAPI, siga estas etapas:
 - Copie os arquivos Foxisapi.dll e Foxisapi.ini para a pasta de scripts do seu servidor Web. Por exemplo, C:\InetPub\scripts\.
- Copie o arquivo de programa Oldebug.prg para a pasta raiz do Visual FoxPro (a localização retornada pela função HOME( )). Por exemplo, C:\Program Files\Microsoft Visual FoxPro\.
