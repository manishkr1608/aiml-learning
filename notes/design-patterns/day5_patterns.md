
# Day 5 – Decorator Pattern

Attach additional responsibilities to objects dynamically, without altering code.

Instead of subclassing, we "wrap" the original object inside another class that provides additional behavior.

Decorators let you add monitoring, logging, or timing around ML functions without changing core training logic.

Decorators implement the same interface but hold a reference to a component and extend its behavior.

public abstract class Stream : IDisposable
{
    public abstract int Read(byte[] buffer, int offset, int count);
    public abstract void Write(byte[] buffer, int offset, int count);
    public abstract void Flush();
}

FileStream -> the concrete component (basic reading/writing).

BufferedStream, CryptoStream, GZipStream -> decorators that wrap another stream and add functionality.

using System;
using System.IO;
using System.IO.Compression;

class Program
{
    static void Main()
    {
        string filePath = "example.txt";

        // Base component: FileStream
        using (FileStream fileStream = new FileStream(filePath, FileMode.Create))
        {
            // Decorator: GZipStream compresses data before writing
            using (GZipStream gzipStream = new GZipStream(fileStream, CompressionMode.Compress))
            using (StreamWriter writer = new StreamWriter(gzipStream))
            {
                writer.WriteLine("Hello, Decorator Pattern in .NET!");
            }
        }

        // Reading back with decorators
        using (FileStream fileStream = new FileStream(filePath, FileMode.Open))
        using (GZipStream gzipStream = new GZipStream(fileStream, CompressionMode.Decompress))
        using (StreamReader reader = new StreamReader(gzipStream))
        {
            string text = reader.ReadLine();
            Console.WriteLine(text);
        }
    }
}

--------------

public interface IService
{
    void Execute();
}

public class RealService : IService
{
    public void Execute()
    {
        Console.WriteLine("Executing real service...");
    }
}


// Decorator: Logging
public class LoggingServiceDecorator : IService
{
    private readonly IService _service;

    public LoggingServiceDecorator(IService service)
    {
        _service = service;
    }

    public void Execute()
    {
        Console.WriteLine("Logging: Service execution started.");
        _service.Execute();
        Console.WriteLine("Logging: Service execution finished.");
    }
}



We can use decorators for logging, caching, authentication, validation, etc.

