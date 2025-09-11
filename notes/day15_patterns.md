
# Day 15 – Builder Pattern

**Idea:** Separate construction of a complex object from its representation.

## Builder is useful for constructing ML pipelines dynamically with configurable steps.


public class CarBuilder
{
    private string _engine;
    private int _wheels;
    private string _color;

    public CarBuilder SetEngine(string engine)
    {
        _engine = engine;
        return this; // enables fluent API
    }

    public CarBuilder SetWheels(int wheels)
    {
        _wheels = wheels;
        return this;
    }

    public CarBuilder SetColor(string color)
    {
        _color = color;
        return this;
    }

    public Car Build()
    {
        return new Car(_engine, _wheels, _color);
    }
}

class Program
{
    static void Main(string[] args)
    {
        Car car = new CarBuilder()
                    .SetEngine("V8")
                    .SetWheels(4)
                    .SetColor("Red")
                    .Build();

        Console.WriteLine(car);
    }
}

Usage - API URL - POST/GET - Authentication - JSON Body
