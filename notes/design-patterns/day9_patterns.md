
# Day 9 – Composite Pattern

**Idea:** Treat individual objects and groups of objects uniformly.  

it’ used when we want to represent part-whole hierarchies such as trees, menus, file systems, or organizational structures.

Composite pattern is useful to chain preprocessing, training, and evaluation steps into one unified AI pipeline.

----------------------------

using System;
using System.Collections.Generic;

// Component
public abstract class FileSystemItem
{
    protected string Name;

    public FileSystemItem(string name)
    {
        Name = name;
    }

    public abstract void Display(int depth);
}

// Leaf
public class File : FileSystemItem
{
    public File(string name) : base(name) { }

    public override void Display(int depth)
    {
        Console.WriteLine(new string('-', depth) + Name);
    }
}

// Composite
public class Directory : FileSystemItem
{
    private readonly List<FileSystemItem> _children = new List<FileSystemItem>();

    public Directory(string name) : base(name) { }

    public void Add(FileSystemItem item)
    {
        _children.Add(item);
    }

    public void Remove(FileSystemItem item)
    {
        _children.Remove(item);
    }

    public override void Display(int depth)
    {
        Console.WriteLine(new string('-', depth) + Name);

        foreach (var child in _children)
        {
            child.Display(depth + 2);
        }
    }
}

// Client
class Program
{
    static void Main(string[] args)
    {
        Directory root = new Directory("root");
        root.Add(new File("file1.txt"));
        root.Add(new File("file2.txt"));

        Directory subDir = new Directory("subdir");
        subDir.Add(new File("file3.txt"));
        subDir.Add(new File("file4.txt"));

        root.Add(subDir);

        root.Display(1);
    }
}

The Composite Pattern lets us represent the filesystem hierarchy as a tree structure where files are leaves and directories are composites. Both can be used through the same interface.

