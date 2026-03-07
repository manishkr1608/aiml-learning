
# Day 3 – Strategy Pattern (swappable behavior)


Define a common interface so you can swap algorithms at runtime.

The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
The client can choose the strategy at runtime without changing its own code.

Extract an algorithm/behavior into an interface.

Provide multiple implementations.

Client picks one (via DI, config, or user input).

This can be used to switch between multiple ML models


public interface IPaymentStrategy
{
    void Pay(decimal amount);
}

public class CreditCardPayment : IPaymentStrategy
{
    public void Pay(decimal amount) =>
        Console.WriteLine($"Paid {amount:C} using Credit Card.");
}

public class PayPalPayment : IPaymentStrategy
{
    public void Pay(decimal amount) =>
        Console.WriteLine($"Paid {amount:C} using PayPal.");
}

public class BitcoinPayment : IPaymentStrategy
{
    public void Pay(decimal amount) =>
        Console.WriteLine($"Paid {amount:C} using Bitcoin.");
}

public class PaymentProcessor
{
    private IPaymentStrategy _paymentStrategy;

    // Inject strategy (runtime selection)
    public PaymentProcessor(IPaymentStrategy strategy)
    {
        _paymentStrategy = strategy;
    }

    public void ProcessPayment(decimal amount)
    {
        _paymentStrategy.Pay(amount);
    }

    public void SetStrategy(IPaymentStrategy strategy)
    {
        _paymentStrategy = strategy;
    }
}

class Program
{
    static void Main()
    {
        // Choose payment method dynamically
        IPaymentStrategy paypal = new PayPalPayment();
        PaymentProcessor processor = new PaymentProcessor(paypal);

        processor.ProcessPayment(250);

        // Switch to another strategy at runtime
        processor.SetStrategy(new BitcoinPayment());
        processor.ProcessPayment(150);
    }
}


Open/Closed Principle — add new strategies without changing the context.
Easy to switch algorithms at runtime.
Keeps the context class simple (delegates to strategy).

CONS

Can lead to class explosion if you have too many strategies.
Clients must know which strategy to pick (can be handled by DI/config).
