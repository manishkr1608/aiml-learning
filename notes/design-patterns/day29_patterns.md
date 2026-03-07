
# Day 29 – Interpreter Pattern 

**Intent:** Define a language and an interpreter to process domain-specific instructions.

## Used in ML systems that read config files or pipelines (YAML, DSL) and convert them into executable setups.
## Interpreter = flexible + scalable way to build configurable ML pipelines.

## A backend service supports dynamic business rules like:

## 	"Age > 18 AND (Country == 'IN' OR PremiumMember == true)"
##	You want to evaluate these rules at runtime against user data without hardcoding if/else chains.

public interface IExpression
{
    int Interpret();
}
public class NumberExpression : IExpression
{
    private readonly int _number;
    public NumberExpression(int number) => _number = number;

    public int Interpret() => _number;
}


public class AddExpression : IExpression
{
    private readonly IExpression _left;
    private readonly IExpression _right;

    public AddExpression(IExpression left, IExpression right)
    {
        _left = left;
        _right = right;
    }

    public int Interpret() => _left.Interpret() + _right.Interpret();
}

public class SubtractExpression : IExpression
{
    private readonly IExpression _left;
    private readonly IExpression _right;

    public SubtractExpression(IExpression left, IExpression right)
    {
        _left = left;
        _right = right;
    }

    public int Interpret() => _left.Interpret() - _right.Interpret();
}


class Program
{
    static void Main()
    {
        // Build tree: (5 + 3) - 2
        IExpression expr = new SubtractExpression(
                                new AddExpression(
                                    new NumberExpression(5),
                                    new NumberExpression(3)),
                                new NumberExpression(2));

        int result = expr.Interpret();

        Console.WriteLine($"Result = {result}");
    }
}


