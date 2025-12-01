# custom exception class for Invalid age
class InvalidAgeError(Exception):
    pass

class FavouriteNumberException(Exception):
    def message(self, msg):
        print('\tFavouriteNumberException: ',msg)
        
class NegativeAgeError(Exception):
    pass