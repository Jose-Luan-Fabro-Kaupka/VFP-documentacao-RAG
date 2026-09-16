# Visual FoxPro como front-end de aplicativo

Como desenvolvedor Visual FoxPro, você provavelmente acha natural projetar seus aplicativos em torno das ferramentas de design visual do programa. For example, you probably think of your application's user interface in terms of Visual FoxPro forms, menus, and reports. In addition, when you develop applications in Visual FoxPro, you most likely think of storing the application's data in Visual FoxPro tables.

Uma forma de integrar o Visual FoxPro em um aplicativo em toda a empresa é usar as ferramentas de design visual no Visual FoxPro, mas aprimorá-las com os recursos de outros produtos. Outra forma é criar a aparência e o comportamento do seu aplicativo usando Visual FoxPro, mas estender os recursos de armazenamento de dados do aplicativo aproveitando os recursos de outros programas ou opções de armazenamento de dados que não sejam Visual FoxPro. Você também pode fazer upsize dos seus dados Visual FoxPro movendo-os para um servidor de banco de dados.

# Estendendo as ferramentas de design visual no Visual FoxPro

As classes base dos controles Visual FoxPro foram projetadas para acomodar a vasta maioria das necessidades de interface de aplicativo. Visual FoxPro provides all the basic controls and interface elements that are required to create a standard Windows application. No entanto, você frequentemente descobrirá que seu aplicativo requer objetos ou controles além dos fornecidos nas classes base Visual FoxPro. Se for o caso, você pode estender as ferramentas de design visual criando subclasses e usando controles ActiveX.

### Criando subclasses

Um recurso extremamente poderoso do Visual FoxPro é a capacidade de criar subclasses dos controles base. By creating one or more subclasses, you can customize the basic Visual FoxPro controls in almost any way that's required for your application. This ability extends to being able to create new objects or controls that combine the features of other controls. For example, the grid control in Visual FoxPro contains not only its own container, properties, and methods, but those of the objects that appear in the grid such as buttons, text boxes, and so on.

Similarly, by subclassing base controls, you can extend the capabilities of Visual FoxPro by creating objects that add new features to existing base classes, or that combine the capabilities of several objects. For example, you can add visual features such as frames or three-dimensional effects to a text box. Or you could combine an image control, buttons, and a text box to create a bitmap-viewing control in which users can move through a series of .bmp files. Creating custom classes in this way can help you manage company-wide development by allowing you to create standardized controls that appear in all your applications. For more information, see Object-Oriented Programming.

### Usando controles ActiveX

Uma alternativa a criar um novo controle usando subclasses no Visual FoxPro é usar um controle ActiveX (arquivo .ocx). These controls are created independently from Visual FoxPro, and can be integrated not only into Visual FoxPro, but into many other Windows applications as well.

In effect, ActiveX controls are off-the-shelf components that you can integrate seamlessly into your application. Using ActiveX controls provides several benefits:
 - Economiza o tempo e o esforço necessários para criar, testar e manter um controle específico Visual FoxPro para realizar as mesmas tarefas. The more capable the ActiveX control, the more time you save.
- Muitos controles ActiveX já estão disponíveis de fornecedores terceiros para atender requisitos comuns de aplicativo. For example, if your application calls for you to display a calendar and allow users to choose dates on it, you can probably find an ActiveX control (perhaps several) that already manages this task.
- O mesmo controle pode ser usado em vários programas. For example, if it makes sense to do so, you can use the same ActiveX control in Visual FoxPro and Visual Basic. The same properties and methods are used in each case to manage the control, and the control will have the same appearance in all programs, making it easier for users to work with.
- Controles ActiveX frequentemente fornecem acesso a funcionalidade Windows que, de outra forma, seria difícil ou demorada de incluir usando apenas ferramentas Visual FoxPro. For example, you can find ActiveX controls that provide access to electronic mail (using Windows MAPI functions), to low-level Windows graphics functions, and so on. By including an ActiveX control, you can add these types of features to your application in a way that's easy to control using the ActiveX control's properties, methods, and events.

Em resumo, usar controles ActiveX permite estender seus aplicativos não apenas integrando funcionalidade em todo o Windows, mas adicionando uma aparência e comportamento comuns entre seu aplicativo e outros na mesma empresa. For more information about using ActiveX controls, see Sharing Information and Adding OLE. For information about creating your own ActiveX controls, see Accessing the Visual FoxPro API.

# Integrando funcionalidade de outros programas

Você pode descobrir ao desenvolver um aplicativo que outros programas são especialmente adequados para realizar certas tarefas. For example, Microsoft Word has unsurpassed merge letter capabilities, while Microsoft Excel is optimized to calculate complex formulas and easily create charts and graphs from them.

Em vez de emular esses recursos no Visual FoxPro, você pode tornar seu aplicativo uma solução em toda a empresa integrando-os ao aplicativo. This way you can match the requirement of your application to the best possible tool to address it.

You can integrate the functionality of other applications into Visual FoxPro in these ways:
 - Executar um assistente Visual FoxPro que torna dados Visual FoxPro disponíveis para uso por outro aplicativo.
- Escrever programas Visual FoxPro que usam Automation para se comunicar, controlar e compartilhar dados com outros programas Windows.

As seções a seguir fornecem detalhes sobre esses métodos de estender os recursos do Visual FoxPro.

### Usando assistentes

Vários assistentes Visual FoxPro permitem integrar dados Visual FoxPro com a funcionalidade de outros programas Windows. For example, you can send form letters to your customers by using the Mail Merge Wizard. When you run the wizard, you can specify a table or view that contains the Visual FoxPro data to use, and then either export the data to a suitable file format (such as comma-delimited) or specify that your word processing program use the Visual FoxPro OLE DB provider to access the data. If you use Microsoft Word, the wizard will even start the word processing program, create the blank merge document, and display the Mail Merge toolbar for you to link fields to your Visual FoxPro data.

Similarly, using Microsoft Excel and Microsoft Query, you can analyze your data using a pivot table, which summarizes data in columns and allows you to rearrange it to view it in different ways. By using the PivotTable Wizard in Visual FoxPro, you can use your application data as the source data for Microsoft Excel, and generate the pivot table in Microsoft Excel.

### Usando Automation

Uma forma mais poderosa de interagir com outros aplicativos é usar Automation. Using Visual FoxPro programs, you can access the objects exposed by other applications, and then control them by setting their properties and calling their methods. For example, Microsoft Excel exposes an application object as well as worksheets, columns, rows, and cells within the application object. You can directly manipulate any of these objects, including getting or setting data in them. In addition, you can usually control the application object using the full range of commands available in the program itself. For example, by managing the application object in Microsoft Excel, you can open, save, or print worksheets, invoke the Microsoft Excel chart wizard, and so on.

Automation is a particularly attractive and powerful way to work with Windows programs using Visual FoxPro for several reasons:
 - Você tem acesso direto ao outro programa, incluindo todos os seus objetos e comandos.
- Você pode compartilhar dados diretamente com o outro programa sem precisar exportá-los ou convertê-los para outro formato.
- Você pode controlar o outro programa usando o familiar modelo de propriedades e métodos.
- The other program doesn't necessarily need to be visible to the user when you invoke it. For example, you can invoke Microsoft Excel, place some data into cells, run a complex calculation on the data, read the result, and then display it in Visual FoxPro, all without ever displaying Microsoft Excel. Your user would continue to see only Visual FoxPro, unless you explicitly wanted to display Microsoft Excel.
- Os comandos (métodos e propriedades) para controlar o outro programa estão incorporados em programas Visual FoxPro familiares. You don't need to learn a different programming language in order to be able to control the other program.

Automation é particularmente poderosa porque é um método aberto para trabalhar com outros programas. In essence, Automation simply makes available to you the data and commands from other applications for you to use in the way best suited to your application.

Um cenário de exemplo ilustra como você pode integrar vários programas Windows. Imagine that you store your customer and sales data in Visual FoxPro. You'd like to create a sales report that summarizes quarterly sales.

One solution would be to use Automation to copy the Visual FoxPro sales data to cells in a Microsoft Excel worksheet. You can then invoke the Microsoft Excel chart wizard to create a chart of the data and copy it to the Windows Clipboard. Still using Automation, you can invoke Microsoft Word and create or open a sales report document (if you create it as a new document, you can insert standard text that you store in Visual FoxPro), and then paste in the chart you created in Microsoft Excel.

This is just one way you can use Automation to make Visual FoxPro part of an enterprise-wide solution. By becoming familiar with the objects and methods available in programs that you typically use, you can imagine many more ways to make each program enhance the capabilities of the other. For details about Automation, see "Manipulating Objects with Automation" Sharing Information and Adding OLE.

# Estendendo recursos de armazenamento de dados no Visual FoxPro

Os recursos de tabela de dados e indexação do Visual FoxPro geralmente são mais do que adequados aos requisitos de um aplicativo, quer você esteja preocupado com velocidade ou tamanho do banco de dados. However, there are times when you might want to extend Visual FoxPro by using data that's stored in some other format. This might be true if:
 - Your application needs access to legacy data that's created and maintained by an existing application. For example, suppose that, as part of your sales application, you need access to data being maintained by an accounting application that was written using a different program, perhaps even on a different platform.
- You want to optimize data access by using a database server, which can greatly speed data access, particularly in very large databases.
- You want to share data with other programs, and therefore want to store the data in a format that's accessible to all the programs.
- The data is best suited to the format of a particular program (such as a spreadsheet). This might be true, for example, if your application required only occasional access to data that was otherwise being maintained by the other program.

If the data you need is in the format of a spreadsheet, word processing document, or other Windows program, you can access it using Automation. For example, you might do this if your application required a collection of form letters. In that case, the letters might be stored as Microsoft Word documents, and your application would use Automation to invoke Word, open the appropriate letter, and insert or substitute text as necessary.

Uma abordagem mais comum para usar dados que não sejam Visual FoxPro é usar um OLE DB provider para acessá-los. OLE DB providers allow you to connect to data in the format of other programs — typically other database programs — and query or edit the data using standard SQL commands.

For example, you might decide that security and transaction processing capabilities are a vital part of your application, so you decide to store the data using Microsoft SQL Server. To access the data, you define a connection to SQL Server, using the SQL Server OLE DB provider. You can then run queries and other SQL commands using ADO, and retrieve the results into an ADO recordset or a CursorAdapter for further processing in Visual FoxPro.

Other applications can access the same data and take advantage of the same features. For example, a Microsoft Excel worksheet can get its data from the same SQL Server database. Not only will the worksheet enjoy the same performance advantages that your application does, it can also take advantage of the security and transaction processing features of the server, which aren't otherwise available in a Microsoft Excel worksheet.

In some instances, you might want to go further and use SQL commands that are specific to the data source you're accessing with the OLE DB provider. For example, Microsoft SQL Server allows you to create and run stored procedures, which can manipulate data at the server (rather than in your application). To take advantage of stored procedures, you can send "native" SQL statements to the database server. Pass-through SQL commands also allow you to perform system administration tasks on the server, and in some instances they will execute faster than similar SQL statements executed in Visual FoxPro.

Para obter mais informações sobre estender recursos de armazenamento de dados no Visual FoxPro, consulte Manipulating Objects with Automation, Accessing Remote Data Using Views e Planning Client/Server Applications.

# Fazendo upsize de dados Visual FoxPro

Você pode optar por manter seus dados em tabelas Visual FoxPro ou em outra plataforma, como um servidor de banco de dados. Or you can do both: keep your data in Visual FoxPro tables while you're developing, or until your database grows large, and then move (or upsize) the data to another platform.

For example, you can prototype your application by keeping all the data in local Visual FoxPro tables. This gives you the flexibility to modify your tables, views, and indexes as you develop the application without the complexities of managing tables on a database server. You can keep sample data in the local tables so you can test your forms, reports, and other programs. When the database structure is complete, you can upsize your data to a database server and put the application into production.

Another way to work is to keep your data in Visual FoxPro tables only as long as is practical. When the database grows large, you can upsize it and take advantage of the optimized performance provided by a database server. The exact point at which it makes sense to upsize your database depends on many factors, including the complexity of the database, the performance of your local computer or network, and the demands of your application.

Finally, you can prototype your database in Visual FoxPro, and then upsize it in order to share the data with other applications that can also access a database server. Similarly, you can upsize the database in order to take advantage of the security and server-side transaction processing capabilities of the database server.

Para detalhes sobre upsize de bancos de dados, consulte Upsizing Visual FoxPro Databases.
