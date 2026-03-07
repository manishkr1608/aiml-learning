
# Day 27 – Composite Pattern (AI Pipelines)

**Intent:** Treat individual and composed objects uniformly.  
Used when you have **hierarchical systems** (like ML pipelines or model ensembles).

## AI tie-in:

# Each ML preprocessing, model, and postprocess step = a node.

# Together they form a composite pipeline you can run end-to-end.

# Treat single objects (leaves) and compositions (nodes with children) uniformly via a common interface.

# Great for tree structures: menus, UI trees, file systems, XML/DOM, org charts, product catalogs, ACL/group hierarchies.

# Composite pattern helps organize multi-step AI pipelines for clarity, reuse, and flexibility.


## Menu System

using System;
using System.Collections.Generic;

// Component
public interface IMenuItem
{
    string Title { get; }
    void Execute();           // operation client cares about
    void Add(IMenuItem item); // optional for leaves (can throw or be no-op)
    void Remove(IMenuItem item);
    IEnumerable<IMenuItem> Children { get; }
}

// Leaf
public class CommandItem : IMenuItem
{
    private readonly Action _action;
    public string Title { get; }

    public CommandItem(string title, Action action)
    {
        Title = title;
        _action = action;
    }

    public void Execute() => _action();

    public void Add(IMenuItem item) => throw new InvalidOperationException("Leaf cannot contain children");
    public void Remove(IMenuItem item) => throw new InvalidOperationException("Leaf cannot contain children");
    public IEnumerable<IMenuItem> Children => Array.Empty<IMenuItem>();
}

// Composite
public class Menu : IMenuItem
{
    private readonly List<IMenuItem> _children = new();
    public string Title { get; }

    public Menu(string title) => Title = title;

    public void Execute()
    {
        Console.WriteLine($"Opening menu: {Title}");
        // Example behavior: list children
        foreach (var child in _children)
            Console.WriteLine($" - {child.Title}");
    }

    public void Add(IMenuItem item) => _children.Add(item);
    public void Remove(IMenuItem item) => _children.Remove(item);
    public IEnumerable<IMenuItem> Children => _children.AsReadOnly();
}

var fileMenu = new Menu("File");
fileMenu.Add(new CommandItem("New", () => Console.WriteLine("New file")));
fileMenu.Add(new CommandItem("Open", () => Console.WriteLine("Open file")));

var recentMenu = new Menu("Recent");
recentMenu.Add(new CommandItem("file1.txt", () => Console.WriteLine("Open file1")));
fileMenu.Add(recentMenu); // submenu

var mainMenu = new Menu("Main");
mainMenu.Add(fileMenu);
mainMenu.Add(new CommandItem("Help", () => Console.WriteLine("Open help")));

mainMenu.Execute(); // client treats Menu and CommandItem uniformly
