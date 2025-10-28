
# Day 32 – Flyweight Pattern 

**Intent:** Reuse shared data efficiently to minimize memory usage.


## Used for token embedding caching, shared feature maps, or serving large models where multiple sessions reuse vector representations.

## The Flyweight principle helps scale models to millions of inferences while controlling cost and memory overhead.

## The Flyweight Pattern is used to minimize memory usage by sharing data that’s common (called intrinsic state) among many objects.

## Only the unique data (called extrinsic state) is stored separately.

using System;
using System.Collections.Generic;

// ----- Flyweight -----
public class Circle
{
    private readonly string _color; // Intrinsic (shared)

    public Circle(string color)
    {
        _color = color;
    }

    // Extrinsic state passed from client
    public void Draw(int x, int y, int radius)
    {
        Console.WriteLine($"Drawing {_color} circle at ({x},{y}) with radius {radius}");
    }
}

// ----- Flyweight Factory -----
public class ShapeFactory
{
    private readonly Dictionary<string, Circle> _circles = new();

    public Circle GetCircle(string color)
    {
        if (!_circles.ContainsKey(color))
        {
            _circles[color] = new Circle(color);
            Console.WriteLine($"Created new circle of color {color}");
        }

        return _circles[color];
    }
}

// ----- Client -----
class Program
{
    static void Main()
    {
        var factory = new ShapeFactory();

        // Draw many circles, but reuse same color objects
        var red1 = factory.GetCircle("Red");
        red1.Draw(10, 20, 5);

        var red2 = factory.GetCircle("Red");
        red2.Draw(15, 25, 10);

        var blue = factory.GetCircle("Blue");
        blue.Draw(50, 50, 20);

        Console.WriteLine("\nTotal unique circle objects created: " + 2);
    }
}



