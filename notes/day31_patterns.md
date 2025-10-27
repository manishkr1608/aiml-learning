
# Day 31 – Prototype Pattern 

**Intent:** Create new objects by copying existing ones instead of building from scratch.

## Prototype is ideal for experiment tracking or hyperparameter exploration, where you reuse a baseline model and modify configurations without re-initializing everything.

## Object creation is expensive or complex, and

## You can reuse an existing instance as a “template.”

using System;

// ----- Prototype Interface -----
public interface IPrototype<T>
{
    T Clone();
}

// ----- Concrete Prototype -----
public class Employee : IPrototype<Employee>
{
    public string Name { get; set; }
    public string Department { get; set; }

    public Employee(string name, string department)
    {
        Name = name;
        Department = department;
    }

    // Clone method
    public Employee Clone()
    {
        return (Employee)this.MemberwiseClone(); // shallow copy
    }

    public override string ToString() => $"{Name} ({Department})";
}

// ----- Client -----
class Program
{
    static void Main()
    {
        // Create original object
        var emp1 = new Employee("Alice", "Engineering");

        // Clone it
        var emp2 = emp1.Clone();
        emp2.Name = "Bob"; // modify clone only

        Console.WriteLine("Original: " + emp1);
        Console.WriteLine("Clone:    " + emp2);
    }
}

**Examples**
## Entity templates (e.g., duplicate product configuration, document templates).

## Caching: reuse a preconfigured object instead of recreating it each time.

