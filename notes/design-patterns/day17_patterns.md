
# Day 17 – Facade Pattern

**Idea:** Provide a simplified interface to a complex subsystem.  

Facade is useful to hide ML complexity from non-technical stakeholders (e.g., one .train() call instead of many subsystems).



public class FlightBookingService
{
    public void BookFlight(string from, string to)
    {
        Console.WriteLine($"Flight booked from {from} to {to}");
    }
}

public class HotelBookingService
{
    public void BookHotel(string location)
    {
        Console.WriteLine($"Hotel booked in {location}");
    }
}

public class CarRentalService
{
    public void BookCar(string location)
    {
        Console.WriteLine($"Car rented in {location}");
    }
}


public class TravelFacade
{
    private readonly FlightBookingService _flightService;
    private readonly HotelBookingService _hotelService;
    private readonly CarRentalService _carService;

    public TravelFacade()
    {
        _flightService = new FlightBookingService();
        _hotelService = new HotelBookingService();
        _carService = new CarRentalService();
    }

    public void BookTrip(string from, string to)
    {
        _flightService.BookFlight(from, to);
        _hotelService.BookHotel(to);
        _carService.BookCar(to);

        Console.WriteLine("Vacation package booked successfully!");
    }
}

class Program
{
    static void Main(string[] args)
    {
        TravelFacade travelFacade = new TravelFacade();
        travelFacade.BookTrip("New York", "Paris");
    }
}
