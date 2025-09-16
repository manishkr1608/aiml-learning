
# Day 21 – State Pattern

**Idea:** Allow an object to change its behavior when its internal state changes.  

## Useful for ML workflows with distinct phases (data prep -> training -> evaluation -> deployment).
## Instead of if/else blocks everywhere, each state defines its own behavior.

## The State Pattern lets an object alter its behavior when its internal state changes. Instead of large if/else or switch blocks checking a state enum throughout the codebase, you encapsulate each state’s behavior in its own class. The context delegates state-specific work to the current state object and may switch state objects as transitions occur.


public interface IOrderState
{
    void AddItem(OrderContext context, string item);
    void Pay(OrderContext context);
    void Ship(OrderContext context);
    void Cancel(OrderContext context);
    string Name { get; }
}

public class OrderContext
{
    private IOrderState _state;
    public string Id { get; }
    public List<string> Items { get; } = new();

    public OrderContext(string id)
    {
        Id = id;
        _state = new PendingState(); // initial state
    }

    public string StateName => _state.Name;

    public void SetState(IOrderState newState)
    {
        _state = newState;
        Console.WriteLine($"Order {Id} transitioned to {_state.Name}");
    }

    // Operations delegate to the state
    public void AddItem(string item) => _state.AddItem(this, item);
    public void Pay() => _state.Pay(this);
    public void Ship() => _state.Ship(this);
    public void Cancel() => _state.Cancel(this);
}

public class PendingState : IOrderState
{
    public string Name => "Pending";

    public void AddItem(OrderContext context, string item)
    {
        context.Items.Add(item);
        Console.WriteLine($"Added {item} to order {context.Id}");
    }

    public void Pay(OrderContext context)
    {
        // transition to Paid
        context.SetState(new PaidState());
    }

    public void Ship(OrderContext context)
    {
        Console.WriteLine("Cannot ship: order is still pending payment.");
    }

    public void Cancel(OrderContext context)
    {
        context.SetState(new CancelledState());
    }
}

public class PaidState : IOrderState
{
    public string Name => "Paid";

    public void AddItem(OrderContext context, string item)
    {
        Console.WriteLine("Cannot add items: order already paid.");
    }

    public void Pay(OrderContext context)
    {
        Console.WriteLine("Already paid.");
    }

    public void Ship(OrderContext context)
    {
        context.SetState(new ShippedState());
    }

    public void Cancel(OrderContext context)
    {
        // maybe refund then cancel
        context.SetState(new CancelledState());
    }
}

public class ShippedState : IOrderState
{
    public string Name => "Shipped";

    public void AddItem(OrderContext context, string item) =>
        Console.WriteLine("Cannot add items: order has been shipped.");

    public void Pay(OrderContext context) =>
        Console.WriteLine("Already paid.");

    public void Ship(OrderContext context) =>
        Console.WriteLine("Already shipped.");

    public void Cancel(OrderContext context) =>
        Console.WriteLine("Cannot cancel: order already shipped. Initiate return workflow instead.");
}

public class CancelledState : IOrderState
{
    public string Name => "Cancelled";

    public void AddItem(OrderContext context, string item) =>
        Console.WriteLine("Cannot modify: order cancelled.");

    public void Pay(OrderContext context) =>
        Console.WriteLine("Cannot pay: order cancelled.");

    public void Ship(OrderContext context) =>
        Console.WriteLine("Cannot ship: order cancelled.");

    public void Cancel(OrderContext context) =>
        Console.WriteLine("Already cancelled.");
}

class Program
{
    static void Main()
    {
        var order = new OrderContext("ORD-1001");
        Console.WriteLine(order.StateName); // Pending

        order.AddItem("Widget A");
        order.AddItem("Widget B");
        order.Pay();    // transition to Paid
        order.AddItem("Widget C"); // not allowed
        order.Ship();   // transition to Shipped
        order.Cancel(); // cannot cancel once shipped
    }
}
