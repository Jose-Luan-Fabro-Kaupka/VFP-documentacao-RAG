# Cookies Foundation Class

Esta é uma classe Web simples para manipular cookies entre páginas Web. Esta classe foi projetada principalmente para uso com Microsoft Internet Information Servers, como o FoxISAPI.

| Category | Internet |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes \Internet |
| Class | _cookie |
| Base Class | Custom |
| Class Library | _internet.vcx |
| Parent Class | _custom |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário onde você pode especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Description |
| --- | --- |
| cCookie property | Name of the current cookie. Def ault: "" |
| CookieTable property | Name of the cookies table. Default: Cookies.dbf |
| DBFAlias property | Alias of the cookies table. Default: "" |
| MakeCookie method | Generates a unique cookie based on the system datetime. Syntax: MakeCookie( ) Return: none Arguments: none |
| GetCookie method | Gets a cookie from HTML server. Syntax: GetCookie(cStr) Return: none Arguments: cStr specifies the name of the cookie to be retrieved. |
| WriteCookieInfo method | Writes the cookie's information to the cookies table. Syntax: WriteCookieInfo( ) Return: none Arguments: none |
| FixURL method | Reads the URL and evaluates %-markers for reading the cookie. Syntax: FixURL(m.cStr) Return: Arguments: m.cStr specifies the name of the cookie to be retrieved. |
| GetVal method | Retrieves a value from the target string, cStr . Syntax: GetVal(cStr, cVal) Return: cVal Arguments: cStr specifies the name of the string to be searched for the value. cVal cVal specifies the value to be sought in the string, cStr . |
