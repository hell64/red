class Car:
    def __init__(self, car_class, fuel_type, transmission, brand, price):
        self.car_class = car_class
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.brand = brand
        self.price = price

class RentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def display_available_cars(self):
        print("Доступні авто для оренди:")
        for index, car in enumerate(self.cars):
            print(f"{index + 1}. {car.brand} ({car.car_class}, {car.fuel_type}, {car.transmission}): ₴{car.price} за день")

    def rent_car(self, car_index, num_days):
        if car_index >= 0 and car_index < len(self.cars):
            car = self.cars[car_index]
            total_cost = car.price * num_days
            print(f"Оренда {car.brand} ({car.car_class}, {car.fuel_type}, {car.transmission}) на {num_days} діб.")
            print(f"Фінальна ціна: ₴{total_cost}")
        else:
            print("Невірний вибір автомобіля.")

