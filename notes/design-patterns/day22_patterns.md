
# Day 22 – Flyweight Pattern

**Idea:** Minimize memory usage by sharing as much data as possible between objects.

## Flyweight is critical in large NLP models where many tokens/embeddings are reused.
## Rather than duplicating vectors, cache and share them to save memory.

// Flyweight
public class CharacterStyle
{
    public string FontFamily { get; }
    public int FontSize { get; }
    public string Color { get; }

    public CharacterStyle(string fontFamily, int fontSize, string color)
    {
        FontFamily = fontFamily;
        FontSize = fontSize;
        Color = color;
    }

    public void Render(char character, int x, int y)
    {
        Console.WriteLine($"Drawing '{character}' at ({x},{y}) " +
                          $"with {FontFamily}, {FontSize}pt, {Color}");
    }
}

public class CharacterStyleFactory
{
    private readonly Dictionary<string, CharacterStyle> _styles = new();

    public CharacterStyle GetStyle(string fontFamily, int fontSize, string color)
    {
        string key = $"{fontFamily}_{fontSize}_{color}";
        if (!_styles.ContainsKey(key))
        {
            _styles[key] = new CharacterStyle(fontFamily, fontSize, color);
        }
        return _styles[key];
    }
}

public class Program
{
    public static void Main()
    {
        var factory = new CharacterStyleFactory();

        // All share same style object
        var style1 = factory.GetStyle("Arial", 12, "Black");
        var style2 = factory.GetStyle("Arial", 12, "Black");
        var style3 = factory.GetStyle("Times New Roman", 14, "Blue");

        style1.Render('H', 0, 0);
        style2.Render('e', 10, 0);
        style3.Render('T', 20, 0);

        Console.WriteLine(ReferenceEquals(style1, style2)); // True (shared)
    }
}

