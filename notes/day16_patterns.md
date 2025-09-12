
# Day 16 – Chain of Responsibility Pattern

**Idea:** Pass a request through a chain of handlers until one processes it.  

## Useful for data preprocessing pipelines, where different steps (cleaning, scaling, encoding) are chained but loosely coupled.

public class Level1Support : Handler
{
    public override void HandleRequest(string request)
    {
        if (request == "Password Reset")
            Console.WriteLine("Level 1 handled: " + request);
        else
            _next?.HandleRequest(request);
    }
}

public class Level2Support : Handler
{
    public override void HandleRequest(string request)
    {
        if (request == "Software Installation")
            Console.WriteLine("Level 2 handled: " + request);
        else
            _next?.HandleRequest(request);
    }
}

public class ManagerSupport : Handler
{
    public override void HandleRequest(string request)
    {
        Console.WriteLine("Manager handled: " + request);
    }
}


class Program
{
    static void Main(string[] args)
    {
        // Build the chain
        var level1 = new Level1Support();
        var level2 = new Level2Support();
        var manager = new ManagerSupport();

        level1.SetNext(level2);
        level2.SetNext(manager);

        // Test
        level1.HandleRequest("Password Reset");        // handled by Level1
        level1.HandleRequest("Software Installation"); // handled by Level2
        level1.HandleRequest("Server Crash");          // handled by Manager
    }
}
