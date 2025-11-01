
# Day 33 – Template Method Pattern

**Idea:** Provide a template (skeleton) of an algorithm in a base class while allowing subclasses to implement concrete steps.

## The recipe (algorithm) stays the same — but ingredients or steps can vary in derived classes

## Template Method enforces a consistent lifecycle for experiments and production training runs, while letting teams plug in dataset/model-specific logic. It’s ideal for companies standardizing how models are produced, evaluated, and versioned.

| Role                  | Description                                                                             |
| --------------------- | --------------------------------------------------------------------------------------- |
| **Abstract Class**    | Defines the template method (overall algorithm) and declares abstract or virtual steps. 	|

| **Concrete Subclass** | Implements or overrides specific steps.                                                 |
| **Client**            | Calls the template method — doesn’t know which subclass is running.                     |


using System;
using System.Collections.Generic;

// ----- Abstract Class -----
public abstract class DataExporter
{
    // Template method — defines the skeleton
    public void Export()
    {
        var data = ReadData();
        var formatted = FormatData(data);
        WriteData(formatted);
    }

    // Steps — can vary per subclass
    protected abstract List<string> ReadData();
    protected abstract string FormatData(List<string> data);
    protected abstract void WriteData(string formattedData);
}

// ----- Concrete Class 1: CSV Exporter -----
public class CsvDataExporter : DataExporter
{
    protected override List<string> ReadData()
    {
        Console.WriteLine("Reading data from database...");
        return new List<string> { "Alice", "Bob", "Charlie" };
    }

    protected override string FormatData(List<string> data)
    {
        Console.WriteLine("Formatting data as CSV...");
        return string.Join(",", data);
    }

    protected override void WriteData(string formattedData)
    {
        Console.WriteLine("Writing CSV file: " + formattedData);
    }
}

// ----- Concrete Class 2: JSON Exporter -----
public class JsonDataExporter : DataExporter
{
    protected override List<string> ReadData()
    {
        Console.WriteLine("Reading data from API...");
        return new List<string> { "X", "Y", "Z" };
    }

    protected override string FormatData(List<string> data)
    {
        Console.WriteLine("Formatting data as JSON...");
        return $"[\"{string.Join("\",\"", data)}\"]";
    }

    protected override void WriteData(string formattedData)
    {
        Console.WriteLine("Uploading JSON to cloud storage: " + formattedData);
    }
}

// ----- Client -----
class Program
{
    static void Main()
    {
        Console.WriteLine("=== CSV Export ===");
        DataExporter csv = new CsvDataExporter();
        csv.Export();

        Console.WriteLine("\n=== JSON Export ===");
        DataExporter json = new JsonDataExporter();
        json.Export();
    }
}





