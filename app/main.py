class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        return (car.comfort_class * (self.clean_power - car.clean_mark) *
                self.average_rating / self.distance_from_city_center)

    def wash_single_car(self, car):
        return car.clean_mark > self.clean_power

    def serve_cars(self, cars_list: list):
        total_income = 0
        for car in cars_list:
            if self.wash_single_car(car):
                continue
            incomes = self.calculate_washing_price(car)
            total_income += incomes
            car.clean_mark = self.clean_power
        return round(total_income, 1)

    def rate_service(self, new_rating: float):
        self.count_of_ratings += 1
        self.average_rating = round(
            ((self.average_rating * (self.count_of_ratings - 1)) +
             new_rating) / self.count_of_ratings, 1)
