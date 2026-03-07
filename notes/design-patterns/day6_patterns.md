
# Day 6 – Adapter Pattern

**Idea:** Allow incompatible interfaces to work together by creating a wrapper (adapter).  

Use Adapter to create standard interfaces for different ML libraries (sklearn, TensorFlow, PyTorch), so pipelines don’t break.

integrate legacy or third-party libraries that don’t follow project’s abstractions.

Using an Adapter keep new code clean, while still leveraging existing libraries.


public interface ILogger
{
    void LogInfo(string message);
    void LogError(string message);
}

// Old third-party or legacy logger
public class LegacyLogger
{
    public void LogMessage(string severity, string message)
    {
        Console.WriteLine($"{severity.ToUpper()}: {message}");
    }
}

// Adapter makes LegacyLogger compatible with ILogger
public class LoggerAdapter : ILogger
{
    private readonly LegacyLogger _legacyLogger;

    public LoggerAdapter(LegacyLogger legacyLogger)
    {
        _legacyLogger = legacyLogger;
    }

    public void LogInfo(string message)
    {
        _legacyLogger.LogMessage("Info", message);
    }

    public void LogError(string message)
    {
        _legacyLogger.LogMessage("Error", message);
    }
}

class Program
{
    static void Main()
    {
        // Legacy logger
        LegacyLogger legacyLogger = new LegacyLogger();

        // Adapter wraps it
        ILogger logger = new LoggerAdapter(legacyLogger);

        // Client only knows ILogger
        logger.LogInfo("Application started.");
        logger.LogError("Something went wrong!");
    }
}

