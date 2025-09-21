
# Day 25 – Visitor Pattern

**Idea:** Add new operations to existing object structures without modifying them.  

## Useful for model inspection & reporting tools (walk over a model and extract details without modifying the model).

public interface IVisitor
{
    void Visit(Book book);
    void Visit(Electronics electronics);
}


public interface ICartItem
{
    void Accept(IVisitor visitor);
}


public class Book : ICartItem
{
    public string Title { get; }
    public double Price { get; }

    public Book(string title, double price)
    {
        Title = title;
        Price = price;
    }

    public void Accept(IVisitor visitor) => visitor.Visit(this);
}

public class Electronics : ICartItem
{
    public string Name { get; }
    public double Price { get; }

    public Electronics(string name, double price)
    {
        Name = name;
        Price = price;
    }

    public void Accept(IVisitor visitor) => visitor.Visit(this);
}

public class DiscountVisitor : IVisitor
{
    public void Visit(Book book)
    {
        Console.WriteLine($"Book '{book.Title}' discounted price: {book.Price * 0.9}");
    }

    public void Visit(Electronics electronics)
    {
        Console.WriteLine($"Electronics '{electronics.Name}' discounted price: {electronics.Price * 0.95}");
    }
}

public class TaxVisitor : IVisitor
{
    public void Visit(Book book)
    {
        Console.WriteLine($"Book '{book.Title}' tax: {book.Price * 0.05}");
    }

    public void Visit(Electronics electronics)
    {
        Console.WriteLine($"Electronics '{electronics.Name}' tax: {electronics.Price * 0.18}");
    }
}

class Program
{
    static void Main()
    {
        var cartItems = new List<ICartItem>
        {
            new Book("C# in Depth", 50),
            new Electronics("Laptop", 1000)
        };

        var discountVisitor = new DiscountVisitor();
        var taxVisitor = new TaxVisitor();

        Console.WriteLine("Applying Discounts:");
        foreach (var item in cartItems) item.Accept(discountVisitor);

        Console.WriteLine("\nApplying Taxes:");
        foreach (var item in cartItems) item.Accept(taxVisitor);
    }
}


