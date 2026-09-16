# Classe Foundation GDI Plus Brush

A classe gpBrush é a classe base abstrata para todas as classes de pincel (por exemplo, as classes gpSolidBrush e gpHatchBrush).

| Category | Reporting |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Output\GDIplus |
| Class | gpBrush |
| Base Class | Custom |
| Class Library | _GDIPLUS.vcx |
| Parent Class | gpObject ( GDI Plus Object Foundation Class ) |

# Observações

Esta classe não adiciona novas propriedades ou métodos ao conjunto exposto por seu pai, gpObject. Ela implementa o método Clone.

| Properties and methods | Description |
| --- | --- |
| Clone Method | Clona um objeto de pincel. Um novo objeto de pincel GDI+ é criado do mesmo tipo e com os mesmos valores de propriedade do objeto de origem. Sintaxe: ? THIS.Clone(toBrush) Valores de retorno: Logical, representando sucesso ou falha. Parâmetros: toBrush, obrigatório, o objeto de pincel a clonar. |
