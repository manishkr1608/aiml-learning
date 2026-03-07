
# Day 4 – Observer Pattern

**Idea:** An object (subject) maintains a list of dependents (observers) and notifies them when state changes.


Used in Event Handling

public interface IObserver
{
    void Update(string message);
}


public interface ISubject
{
    void Attach(IObserver observer);
    void Detach(IObserver observer);
    void Notify(string message);
}


using System.Collections.Generic;

public class NotificationManager : ISubject
{
    private readonly List<IObserver> _observers = new();

    public void Attach(IObserver observer) => _observers.Add(observer);
    public void Detach(IObserver observer) => _observers.Remove(observer);

    public void Notify(string message)
    {
        foreach (var observer in _observers)
            observer.Update(message);
    }

    // Example: system event triggers notifications
    public void NewEvent(string msg)
    {
        Console.WriteLine($"System Event: {msg}");
        Notify(msg);
    }
}



public class SlackNotifier : IObserver
{
    private readonly string _webhookUrl;

    public SlackNotifier(string webhookUrl)
    {
        _webhookUrl = webhookUrl;
    }

    public async void Update(string message)
    {
        using var client = new HttpClient();
        var payload = $"{{\"text\":\"{message}\"}}";
        var content = new StringContent(payload, Encoding.UTF8, "application/json");
        await client.PostAsync(_webhookUrl, content);
    }
}

class Program
{
    static void Main(string[] args)
    {
        var manager = new NotificationManager();

        // Slack webhook from your Slack app or integration
        var slack = new SlackNotifier("https://hooks.slack.com/services/XXXX/XXXX/XXXX");

        manager.Attach(slack);

        manager.NewEvent("🚀 New user signed up!");
        manager.NewEvent("⚠️ Server load is high.");
    }
}

We can notify different systems (logging, Slack, dashboard) when model finishes training or accuracy improves.
