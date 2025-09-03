class Employee:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours:
            return self.hours
        else:
            return (7 - self.rest_days) * 8

    def get_email(self):
        if self.email:
            return self.email
        else:
            return f"{self.name}@email.com"

    def salary(self):
        return self.get_hours() * self.__class__.hourly_payment
    
emp1 = Employee('Алексей Смирнов', hours=10, rest_days=0, email=None)

# Вычислим количество часов
print(f'Количество часов: {emp1.get_hours()}')  # Вернет явно установленные часы

# Узнаем e-mail сотрудника
print(f'Электронная почта: {emp1.get_email()}')  # Возвратит введённый email

# Посмотрим зарплату сотрудника
print(f'Заработная плата: {emp1.salary()} рублей')  # Подсчёт зарплаты
