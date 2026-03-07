# Day 10 – Extending Decorator Pattern

**Idea:** Wrap objects to add behavior dynamically.  

## Decorators allow adding logging, monitoring, metrics to AI functions without changing core code → essential for production ML.

## often used when you want to extend the functionality of a class but don’t want to use inheritance

## Advantages:

# More flexible than inheritance.

# Responsibilities can be mixed and matched at runtime.

# Open/Closed Principle: you can add new functionality without modifying existing code.

## Drawbacks:

# Can lead to many small objects (complexity).

# Harder to debug because behavior is spread across multiple wrappers.


## System.IO namespace is full of decorators.

        ## Base component
        Stream fileStream = new FileStream("example.txt", FileMode.OpenOrCreate);

        # Decorator: adds buffering to improve performance
        Stream buffered = new BufferedStream(fileStream);

        # Decorator: adds text handling (read/write strings instead of bytes)
        TextWriter writer = new StreamWriter(buffered);

        writer.WriteLine("Hello, Decorator Pattern in .NET!");
        writer.Flush();
        writer.Close();

# Each wraps the previous one, dynamically extending its behavior without changing the original FileStream.


## Example: Timing ML model training

```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timing_decorator
def train_model(X, y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=200).fit(X, y)
    return model

    
