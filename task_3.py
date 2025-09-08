class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам.')
            return None
        
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место.')
            return None
        
        else:
            points = 101 - place
            return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным.')
            return None
        
        else:
            points = meters * 0.5
            return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        points_from_place = self.get_points_for_place(place)
        points_from_meters = self.get_points_for_meters(meters)
        
        if points_from_place is not None and points_from_meters is not None:
            total = points_from_place + points_from_meters
            return total
        else:
            return None
        
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))