
S - Single Responsibility Principle

A Class should have only one responsibility

Wrong
public class DB
{
    public void Connect() { /* open connection */ }
    public void ExecuteQuery(string sql) { /* run query */ }
    public void Log(string message) { /* log query */ }
    public void MapResult() { /* map rows to objects */ }
    public void Commit() { /* commit transaction */ }
}

Problem: This class has multiple responsibilities: connection handling, 
	logging, data access, and object mapping.
	If logging changes, or mapping changes, or connection strategy changes → 
	DB class must be modified

Example:
1. If DB changes from SQL server to PostGres, Connection string changes, 
	retry strategy changes
2. TimeOut changes in Query execution
3. Logging endpoint changes, log level policy change
4. model changes, schema changes, datatype changes

with correct SRP:

public class DbConnection
{
    public void Open() { /* open DB connection */ }
    public void Close() { /* close DB connection */ }
}

// Handles only executing queries
public class DbCommand
{
    private readonly DbConnection _connection;
    public DbCommand(DbConnection connection)
    {
        _connection = connection;
    }
    public void Execute(string sql) { /* execute query */ }
}

// Handles only logging
public class DbLogger
{
    public void Log(string message) { /* log message */ }
}

// Handles mapping results: converting DB result to objects.
public class DbMapper
{
    public T Map<T>(object result) { /* map result to object */ }
}

Benefits

Each class has only one reason to change

Easier to test (unit test DbMapper without worrying about connections)

Promotes reusability (maybe you reuse DbLogger in other parts of system)

Makes the system modular

AI: keep data preprocessing separate from model training code.


------------------------

O – Open/Closed Principle (OCP)

Software entities should be open for extension, closed for modification.

Without OCP
public class DbLogger
{
    public void Log(string message, string type)
    {
        if (type == "Console")
            Console.WriteLine(message);
        else if (type == "File")
            File.AppendAllText("db.log", message);
    }
}

With OCP
public interface ILoggerSink
{
    void Log(string message);
}

public class ConsoleLogger : ILoggerSink
{
    public void Log(string message) => Console.WriteLine(message);
}

public class FileLogger : ILoggerSink
{
    public void Log(string message) => File.AppendAllText("db.log", message);
}

public class DbLogger
{
    private readonly ILoggerSink _sink;
    public DbLogger(ILoggerSink sink) => _sink = sink;

    public void Log(string message) => _sink.Log(message);
}

usage - 
var logger = new DbLogger(new ConsoleLogger());
logger.Log("Executing query...");

Summary
Extend behavior by adding new classes

No risky edits in existing, tested code

Easier maintenance & plug-in style flexibility

Adding new ML models via interfaces without changing existing pipeline.

----------------------------------

Liskov Substitution Principle (LSP)


Objects of a superclass should be replaceable with objects of a subclass without breaking the program’s behavior.

If class B is a subclass of class A, then anywhere you use A, you should be able to use B without surprises.

A subclass must not weaken the expectations of the base class.


we have base class DbConnection:

public abstract class DbConnection
{
    public abstract void Open();
}


Violation of LSP

public class SqlConnection : DbConnection
{
    public override void Open() => Console.WriteLine("SQL Server connection opened.");
}

public class FileConnection : DbConnection --- 
{
    public override void Open()
    {
        throw new InvalidOperationException("Cannot open a DB connection to a file!");
    }
}


With LSP

Create abstractions:

public abstract class Connection
{
    public abstract void Open();
}

public class DbConnection : Connection
{
    public override void Open() => Console.WriteLine("DB Connection opened.");
}

public class FileConnection : Connection
{
    public override void Open() => Console.WriteLine("File opened.");
}

Summary - 

LSP ensures subclasses don’t break expectations of their parents.

Violation usually happens when:

Subclass throws “NotSupported” exceptions

Subclass changes the meaning of methods (e.g., returns null when parent promised a valid object)

Fix: design better abstractions (don’t force subclasses into behaviors they can’t support).

Different regression models should be swappable without breaking evaluation logic.

----------------------------------------


Interface Segregation Principle (ISP):
Clients should not be forced to depend on interfaces they do not use.

Violates ISP:
public interface IDatabase
{
    void Connect();
    void ExecuteQuery(string sql);
    void LogQuery(string sql);
    void MapResult();
}

Class derived from above will break SRP

Solution - role-specific interfaces:

public interface IDbConnection
{
    void Connect();
}

public interface IDbCommand
{
    void ExecuteQuery(string sql);
}

public interface IDbLogger
{
    void LogQuery(string sql);
}

public interface IDbMapper
{
    T Map<T>(object result);
}


Summary

ISP prevents bloated interfaces.

Smaller interfaces → more flexibility, less coupling, easier testing.

A class should not have to implement methods that are irrelevant to it.

Separate model training interface from prediction interface.

------------------------------------------

Dependency Inversion Principle (DIP):

High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.

This encourages loose coupling and makes your code easier to change, extend, and test.

Without DIP (tight coupling):
public class OrderService
{
    public void PlaceOrder(Order order)
    {
        // Tied to Serilog's static API → hard to test/replace
        Serilog.Log.Information("Placing order {@Order}", order);
        // business logic...
    }
}

Can’t swap Serilog easily (e.g., NLog, custom sink).

Unit tests must load Serilog or you lose logs.



With DIP:

// Abstraction
public interface IAppLogger
{
    void Info(string message, object? ctx = null);
    void Warn(string message, object? ctx = null);
    void Error(Exception ex, string message, object? ctx = null);
}

// Implementations
// Console adapter
public class ConsoleLogger : IAppLogger
{
    public void Info(string m, object? c=null)  => Console.WriteLine($"INFO: {m} {c}");
    public void Warn(string m, object? c=null)  => Console.WriteLine($"WARN: {m} {c}");
    public void Error(Exception ex, string m, object? c=null) => 
        Console.WriteLine($"ERR: {m} | {ex} {c}");
}

// Serilog adapter
public class SerilogAdapter : IAppLogger
{
    private readonly Serilog.ILogger _log;
    public SerilogAdapter(Serilog.ILogger log) { _log = log; }
    public void Info(string m, object? c=null)  => _log.Information("{Message} {@Ctx}", m, c);
    public void Warn(string m, object? c=null)  => _log.Warning("{Message} {@Ctx}", m, c);
    public void Error(Exception ex, string m, object? c=null) => _log.Error(ex, "{Message} {@Ctx}", m, c);
}


// High-level module depends only on abstraction
public class OrderService
{
    private readonly IAppLogger _log;
    public OrderService(IAppLogger log) { _log = log; }

    public void PlaceOrder(Order order)
    {
        _log.Info("Placing order", new { order.Id, order.Total });
        // ...business logic...
    }
}

var svc = new OrderService(new ConsoleLogger());

Summary:

DIP decouples high-level business logic from low-level details.

Use interfaces/abstract classes for abstractions.

Makes your system:

Easier to swap implementations (e.g., SQL → NoSQL, SMTP → SendGrid)

Easier to unit test (mock abstractions)

More flexible & maintainable

Pipeline depends on abstractions, not concrete implementations.













