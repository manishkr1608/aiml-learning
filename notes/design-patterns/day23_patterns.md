
# Day 23 – Adapter Pattern (Deep Learning Edition)

**Idea:** Allow incompatible interfaces to work together by providing an adapter.

## Adapter helps connect different ML ecosystems (e.g., PyTorch models evaluated with sklearn metrics).

public interface ILogger
{
    void Log(string message);
}

public class LegacyLogger
{
    public void WriteLog(string msg)
    {
        Console.WriteLine($"[LegacyLog]: {msg}");
    }
}

public class LoggerAdapter : ILogger
{
    private readonly LegacyLogger _legacyLogger;

    public LoggerAdapter(LegacyLogger legacyLogger)
    {
        _legacyLogger = legacyLogger;
    }

    public void Log(string message)
    {
        // adapting interface
        _legacyLogger.WriteLog(message);
    }
}

public class Program
{
    public static void Main()
    {
        ILogger logger = new LoggerAdapter(new LegacyLogger());
        logger.Log("Application started");
    }
}
