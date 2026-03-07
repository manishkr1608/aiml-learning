
# Day 30 – Memento Pattern 

**Intent:** Capture and restore an object’s state without exposing its implementation details.

## Used for checkpointing during training.

## Enables “rollback” to previous versions for experiments, drift control, and auditing.

## The Memento Pattern captures and externalizes an object's internal state so it can be restored later — without breaking encapsulation. 
## Real-world uses: undo/redo in editors, save/restore game state, transaction checkpoints, and time-travel debugging.

**Concept**

## Originator — the object whose state we want to save/restore (e.g., Document).

## Memento — immutable snapshot of the originator’s state. The originator creates and consumes it.

## Caretaker — stores mementos (e.g., undo/redo stacks) but does not read/modify their contents.


using System;
using System.Collections.Generic;

// ----- Memento -----
public class EditorMemento
{
    public string Content { get; }

    public EditorMemento(string content)
    {
        Content = content;
    }
}

// ----- Originator -----
public class TextEditor
{
    private string _content = "";

    public void Type(string words)
    {
        _content += words;
    }

    public string GetContent() => _content;

    // Save current state
    public EditorMemento Save()
    {
        return new EditorMemento(_content);
    }

    // Restore to previous state
    public void Restore(EditorMemento memento)
    {
        _content = memento.Content;
    }
}

// ----- Caretaker -----
public class History
{
    private readonly Stack<EditorMemento> _mementos = new();

    public void Backup(EditorMemento memento)
    {
        _mementos.Push(memento);
    }

    public EditorMemento Undo()
    {
        if (_mementos.Count == 0) return null;
        return _mementos.Pop();
    }
}

// ----- Client -----
class Program
{
    static void Main()
    {
        var editor = new TextEditor();
        var history = new History();

        editor.Type("Hello ");
        history.Backup(editor.Save());

        editor.Type("World!");
        history.Backup(editor.Save());

        editor.Type(" More text here.");
        Console.WriteLine("Current: " + editor.GetContent());

        // Undo last change
        editor.Restore(history.Undo());
        Console.WriteLine("After Undo: " + editor.GetContent());

        // Undo again
        editor.Restore(history.Undo());
        Console.WriteLine("After second Undo: " + editor.GetContent());
    }
}


