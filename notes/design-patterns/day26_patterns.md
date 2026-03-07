
# Day 26 – Proxy Pattern

**Idea:** Provide a surrogate or placeholder object to control access to another object.  

## Proxies are useful for AI inference endpoints → add logging, authentication, caching without changing the core model.

## It controls access to the real object — by adding lazy loading, security checks, logging, caching, or remote calls — without changing the client code.

public interface IImage
{
    void Display();
}

public class RealImage : IImage
{
    private readonly string _fileName;

    public RealImage(string fileName)
    {
        _fileName = fileName;
        LoadFromDisk(); // expensive operation
    }

    private void LoadFromDisk()
    {
        Console.WriteLine($"Loading {_fileName} from disk...");
    }

    public void Display()
    {
        Console.WriteLine($"Displaying {_fileName}");
    }
}

public class ProxyImage : IImage
{
    private RealImage _realImage;
    private readonly string _fileName;

    public ProxyImage(string fileName)
    {
        _fileName = fileName;
    }

    public void Display()
    {
        if (_realImage == null)
        {
            _realImage = new RealImage(_fileName); // lazy load
        }
        _realImage.Display();
    }
}

class Program
{
    static void Main()
    {
        IImage image = new ProxyImage("photo1.png");

        Console.WriteLine("Image created, but not loaded yet.");

        image.Display(); // loads from disk now
        image.Display(); // uses cached real object
    }
}
