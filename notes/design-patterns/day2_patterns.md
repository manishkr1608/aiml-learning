
Simple Factory Pattern

Factory pattern is creational design pattern

provides an interface for creating objects in a superclass, but allows subclasses to decide which class to instantiate.

instead of creating objects using new everywhere, we delegate that responsibility to a Factory class/method.

It makes the code extensible, and loosely coupled.


When object creation logic is complex.

When you want to decouple client code from specific implementations.

When you may need to introduce new product types without changing client code.

Applications might need to work with different databases, if DB is hardcoded then it will have problem changing in future



Bad one
public class Database
{
    private SqlConnection _connection;

    public Database(string connectionString)
    {
        _connection = new SqlConnection(connectionString);
    }

    public void Connect()
    {
        _connection.Open();
        Console.WriteLine("Connected to SQL Server");
    }
}


Correct one - 
public interface IDatabase
{
    void Connect();
}

public class SqlServerDatabase : IDatabase
{
    private string _connectionString;
    public SqlServerDatabase(string connectionString)
    {
        _connectionString = connectionString;
    }

    public void Connect()
    {
        Console.WriteLine("Connected to SQL Server with: " + _connectionString);
    }
}

public class MySqlDatabase : IDatabase
{
    private string _connectionString;
    public MySqlDatabase(string connectionString)
    {
        _connectionString = connectionString;
    }

    public void Connect()
    {
        Console.WriteLine("Connected to MySQL with: " + _connectionString);
    }
}

Database Factory:
public static class DatabaseFactory
{
    public static IDatabase CreateDatabase(string dbType, string connectionString)
    {
        switch (dbType.ToLower())
        {
            case "sqlserver":
                return new SqlServerDatabase(connectionString);
            case "mysql":
                return new MySqlDatabase(connectionString);
            default:
                throw new ArgumentException("Unsupported database type");
        }
    }
}


Cons -

It violates OCP since every new database type will need change in switch function of DatabaseFactory (Closed for modification)
It Violates DIP
	High-level code depends on the factory’s details like they have to pass "mysql" etc, 
	Factory depends on concrete implementations.it directly depends on low-level modules
	Abstractions depend on details. IDatabase was supposed to be the abstraction. But it can’t live independently: the only way to get one is through the detail-heavy factory that knows all concrete classes.

------------------

Factory Method:

The Factory Method Pattern defines an interface for creating objects, but lets subclasses decide which object to instantiate.

each subclass implements its own factory method to create the right object.

public interface IDatabase
{
    void Connect();
}

public class SqlServerDatabase : IDatabase
{
    public void Connect()
    {
        Console.WriteLine("Connected to SQL Server");
    }
}

public class MySqlDatabase : IDatabase
{
    public void Connect()
    {
        Console.WriteLine("Connected to MySQL");
    }
}

public abstract class DatabaseFactory
{
    // Factory Method
    public abstract IDatabase CreateDatabase();

    // Common logic that uses the product
    public void ConnectDatabase()
    {
        var db = CreateDatabase();
        db.Connect();
    }
}

public class SqlServerFactory : DatabaseFactory
{
    public override IDatabase CreateDatabase()
    {
        return new SqlServerDatabase();
    }
}

public class MySqlFactory : DatabaseFactory
{
    public override IDatabase CreateDatabase()
    {
        return new MySqlDatabase();
    }
}

It satisfies OCP since every new database added doesn't need to change any existing code. New DB support comes from adding a new class (extension), not modifying existing ones.

Cons
Every new DB often requires a new creator subclass.

If multiple similar objects needs to be created then it can't be done in Factory Method like Connection, Command, Transaction

----------

Abstract Factory Pattern

The Abstract Factory Pattern provides an interface to create families of related or dependent objects without specifying their concrete classes.
it produces a set of related objects (e.g., DbConnection, DbCommand, DbLogger, etc.) that are meant to work together.

public interface IDbConnection
{
    void Connect();
}

public interface IDbCommand
{
    void Execute(string query);
}

// SQL Server family
public class SqlServerConnection : IDbConnection
{
    public void Connect() => Console.WriteLine("Connected to SQL Server");
}
public class SqlServerCommand : IDbCommand
{
    public void Execute(string query) => Console.WriteLine($"Executing on SQL Server: {query}");
}

// MySQL family
public class MySqlConnection : IDbConnection
{
    public void Connect() => Console.WriteLine("Connected to MySQL");
}
public class MySqlCommand : IDbCommand
{
    public void Execute(string query) => Console.WriteLine($"Executing on MySQL: {query}");
}

Abstract Factory Interface
public interface IDatabaseFactory
{
    IDbConnection CreateConnection();
    IDbCommand CreateCommand();
}

Concrete Factories
public class SqlServerFactory : IDatabaseFactory
{
    public IDbConnection CreateConnection() => new SqlServerConnection();
    public IDbCommand CreateCommand() => new SqlServerCommand();
}

public class MySqlFactory : IDatabaseFactory
{
    public IDbConnection CreateConnection() => new MySqlConnection();
    public IDbCommand CreateCommand() => new MySqlCommand();
}


Client Code
class Program
{
    static void Main(string[] args)
    {
        // Choose family at runtime
        IDatabaseFactory factory = new SqlServerFactory();
        // IDatabaseFactory factory = new MySqlFactory();

        var connection = factory.CreateConnection();
        connection.Connect();

        var command = factory.CreateCommand();
        command.Execute("SELECT * FROM Users");
    }
}


Follows OCP, DIP
adding new DB families = extend by adding new concrete factories/products.

lets the pipeline swap models via config/CLI.

---------------------------------

Singleton:
exactly one instance of a class exists and provides a global access point to it.

public sealed class AppConfig
{
    private static AppConfig? _instance;
    private static readonly object _lock = new();

    public static AppConfig Instance
    {
        get
        {
            if (_instance is null)
            {
                lock (_lock)
                {
                    if (_instance is null) _instance = new AppConfig();
                }
            }
            return _instance;
        }
    }

    private AppConfig() { }
}


 sealed singleton breaks OCP since sealed block inheritance.

A classic Singleton breaks DIP because clients depend directly on the concrete singleton:
var logger = Logger.Instance;  // depends on concrete, not abstraction

In its DI form, it respects DIP.
services.AddSingleton<ILogger, Logger>();

one connection/client for performance; avoid global state when testing.










