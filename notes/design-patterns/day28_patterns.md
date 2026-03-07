
# Day 28 – Bridge Pattern (Model–Data Integration)

**Intent:** Decouple abstraction from its implementation so they can vary independently.

## Bridge separates the model abstraction from data source implementation -> useful in MLOps for switching between data backends without code changes.

## It splits a big class or closely related classes into two hierarchies:

**Abstraction** -> defines the high-level control layer (the API clients use).

**Implementor** -> defines the low-level operations (the actual implementation).

## The abstraction delegates work to the implementor interface.
## You can vary both independently (e.g., new abstractions or new implementations).

## Example — Logging to Different Backends

public interface ILogFormatter
{
    string Format(string severity, string message);
}

public class TextFormatter : ILogFormatter
{
    public string Format(string severity, string message)
        => $"{DateTime.Now:u} [{severity}] {message}";
}

public class JsonFormatter : ILogFormatter
{
    public string Format(string severity, string message)
        => $"{{\"time\":\"{DateTime.Now:u}\",\"level\":\"{severity}\",\"message\":\"{message}\"}}";
}

public abstract class Logger
{
    protected readonly ILogFormatter _formatter;

    protected Logger(ILogFormatter formatter)
    {
        _formatter = formatter;
    }

    public abstract void Log(string severity, string message);
}

public class ConsoleLogger : Logger
{
    public ConsoleLogger(ILogFormatter formatter) : base(formatter) { }

    public override void Log(string severity, string message)
    {
        Console.WriteLine(_formatter.Format(severity, message));
    }
}

public class FileLogger : Logger
{
    private readonly string _path;

    public FileLogger(ILogFormatter formatter, string path) : base(formatter)
    {
        _path = path;
    }

    public override void Log(string severity, string message)
    {
        File.AppendAllText(_path, _formatter.Format(severity, message) + Environment.NewLine);
    }
}

class Program
{
    static void Main()
    {
        Logger consoleLogger = new ConsoleLogger(new TextFormatter());
        consoleLogger.Log("INFO", "User login successful");

        Logger fileLogger = new FileLogger(new JsonFormatter(), "app.log");
        fileLogger.Log("ERROR", "File not found");

        Console.WriteLine("Logs written.");
    }
}

