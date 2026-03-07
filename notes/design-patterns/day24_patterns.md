
# Day 24 – Command Pattern

**Idea:** Encapsulate requests as objects, allowing parameterization and queuing of operations.  

## Command pattern lets you package training, evaluation, checkpoint saving, deployment as independent commands.
## This makes ML pipelines more modular, schedulable, and testable.

public interface ICommand
{
    void Execute();
}

public class OrderService
{
    public void PlaceOrder(int orderId)
    {
        Console.WriteLine($"Order {orderId} placed.");
    }

    public void CancelOrder(int orderId)
    {
        Console.WriteLine($"Order {orderId} cancelled.");
    }

    public void ShipOrder(int orderId)
    {
        Console.WriteLine($"Order {orderId} shipped.");
    }
}

public class PlaceOrderCommand : ICommand
{
    private readonly OrderService _orderService;
    private readonly int _orderId;

    public PlaceOrderCommand(OrderService service, int orderId)
    {
        _orderService = service;
        _orderId = orderId;
    }

    public void Execute() => _orderService.PlaceOrder(_orderId);
}

public class CancelOrderCommand : ICommand
{
    private readonly OrderService _orderService;
    private readonly int _orderId;

    public CancelOrderCommand(OrderService service, int orderId)
    {
        _orderService = service;
        _orderId = orderId;
    }

    public void Execute() => _orderService.CancelOrder(_orderId);
}

public class ShipOrderCommand : ICommand
{
    private readonly OrderService _orderService;
    private readonly int _orderId;

    public ShipOrderCommand(OrderService service, int orderId)
    {
        _orderService = service;
        _orderId = orderId;
    }

    public void Execute() => _orderService.ShipOrder(_orderId);
}

public class CommandInvoker
{
    private readonly Queue<ICommand> _commands = new();

    public void AddCommand(ICommand command) => _commands.Enqueue(command);

    public void ProcessCommands()
    {
        while (_commands.Count > 0)
        {
            var command = _commands.Dequeue();
            command.Execute();
        }
    }
}

class Program
{
    static void Main()
    {
        var orderService = new OrderService();

        var placeCommand = new PlaceOrderCommand(orderService, 101);
        var shipCommand = new ShipOrderCommand(orderService, 101);
        var cancelCommand = new CancelOrderCommand(orderService, 102);

        var invoker = new CommandInvoker();
        invoker.AddCommand(placeCommand);
        invoker.AddCommand(shipCommand);
        invoker.AddCommand(cancelCommand);

        invoker.ProcessCommands();
    }
}
