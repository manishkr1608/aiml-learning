
# Day 8 – Proxy Pattern

Provide a surrogate/placeholder for another object to control access.  

Useful for lazy-loading heavy ML models or protecting access (e.g., paid API gateway).

security, performance, or additional behavior

Access Control – restrict direct access to sensitive objects (e.g., authentication before access).

Lazy Initialization – create heavy objects only when they are really needed.

Remote Proxy – represent an object in a different address space (like a local object standing in for a remote server).

Logging, Caching, or Monitoring – add behavior without changing the real object.

# Example

Smart Reference – perform housekeeping like reference counting, thread safety, etc.

ORM Lazy Loading (Hibernate, Entity Framework) → Proxy objects load related data only when accessed.

API Gateway → Acts as a proxy to multiple microservices, adding logging, caching, rate-limiting.

Reverse Proxy (NGINX, Apache) → Clients talk to the proxy, which forwards requests to the real servers.


using System;

// Subject
public interface IImage
{
    void Display();
}

// Real Subject (heavy object)
public class RealImage : IImage
{
    private string _filename;

    public RealImage(string filename)
    {
        _filename = filename;
        LoadFromDisk(); // Heavy operation
    }

    private void LoadFromDisk()
    {
        Console.WriteLine($"Loading image: {_filename}");
        // Simulate time-consuming operation
        System.Threading.Thread.Sleep(1000);
    }

    public void Display()
    {
        Console.WriteLine($"Displaying image: {_filename}");
    }
}

// Proxy (Lazy Loader)
public class ProxyImage : IImage
{
    private RealImage _realImage;
    private string _filename;

    public ProxyImage(string filename)
    {
        _filename = filename;
    }

    public void Display()
    {
        if (_realImage == null)
        {
            Console.WriteLine("Creating RealImage on demand...");
            _realImage = new RealImage(_filename); // Lazy initialization
        }
        _realImage.Display();
    }
}

// Client
class Program
{
    static void Main()
    {
        IImage image1 = new ProxyImage("photo1.jpg");
        IImage image2 = new ProxyImage("photo2.jpg");

        // Image not loaded yet (lazy)
        Console.WriteLine("Created proxy objects.");

        Console.WriteLine("\nFirst access:");
        image1.Display(); // Loads on demand

        Console.WriteLine("\nSecond access:");
        image1.Display(); // Already loaded, no reloading

        Console.WriteLine("\nAccess another image:");
        image2.Display(); // Loads only when accessed
    }
}

