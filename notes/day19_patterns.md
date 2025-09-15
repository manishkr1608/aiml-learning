
# Day 19 – Mediator Pattern

## Idea: Define an object that encapsulates how components interact, reducing direct dependencies.  

## Mediator helps when AI systems have multiple components (data loaders, trainers, evaluators) that need central coordination without direct coupling.

using System;
using System.Collections.Generic;

// Mediator interface
public interface IChatRoomMediator
{
    void Register(User user);
    void SendMessage(string from, string to, string message);
}

// Concrete Mediator
public class ChatRoomMediator : IChatRoomMediator
{
    private readonly Dictionary<string, User> _users = new();

    public void Register(User user)
    {
        if (!_users.ContainsKey(user.Name))
            _users.Add(user.Name, user);
        user.SetMediator(this);
    }

    public void SendMessage(string from, string to, string message)
    {
        if (to == "ALL")
        {
            // broadcast
            foreach (var u in _users.Values)
            {
                if (u.Name != from)
                    u.Receive(from, message);
            }
        }
        else if (_users.TryGetValue(to, out var recipient))
        {
            recipient.Receive(from, message);
        }
        else
        {
            Console.WriteLine($"[{from}] tried to message [{to}] but user not found.");
        }
    }
}

// Colleague base
public abstract class User
{
    protected IChatRoomMediator Mediator;
    public string Name { get; }

    protected User(string name)
    {
        Name = name;
    }

    internal void SetMediator(IChatRoomMediator mediator) => Mediator = mediator;

    public void Send(string to, string message)
    {
        Mediator.SendMessage(Name, to, message);
    }

    public abstract void Receive(string from, string message);
}

// Concrete Colleague
public class ConcreteUser : User
{
    public ConcreteUser(string name) : base(name) { }

    public override void Receive(string from, string message)
    {
        Console.WriteLine($"[{Name}] received from [{from}]: {message}");
    }
}

// Demo
public class Program
{
    public static void Main()
    {
        var chat = new ChatRoomMediator();

        var alice = new ConcreteUser("Alice");
        var bob = new ConcreteUser("Bob");
        var carol = new ConcreteUser("Carol");

        chat.Register(alice);
        chat.Register(bob);
        chat.Register(carol);

        alice.Send("Bob", "Hi Bob!");
        bob.Send("Alice", "Hey Alice — how are you?");
        carol.Send("ALL", "Hello everyone!");
    }
}
