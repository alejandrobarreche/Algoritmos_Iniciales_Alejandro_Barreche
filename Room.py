from Roomtype import HotelRoomType

class Room():
    """Python class to implement a basic version of a hotel room.

    This Python class implements the basic functionalities of a hotel room in a 
    simple hotel management system.

    Syntax
    ------
    obj = Room(room_type, room_number, room_state, room_price)

    Parameters
    ----------
    [in] room_type : Roomtype
        Valid values are "Individual", "Doble", "Suite".
    [in] room_number : int
        Unique number of the room.
    [in] room_state : str
        Occupancy state of the room. Expected values are "Ocupada" or "Desocupada".
    [in] room_price : float
        Price per night for the room.

    Returns
    -------
    obj : Room
        Python object output parameter that represents an instance of the class Room.

    Attributes
    ----------
    """
    #Here you start your code.
    
    numero_hab_usadas = []
    
    
    def __init__(self, room_type, room_number, room_state, room_price):
        self.room_type = room_type
        self.room_number = room_number
        self.room_state = room_state
        self.room_price = room_price
        
        
        
    #Getters 
    
    def get_room_type(self):
        if isinstance(self.room_type, HotelRoomType):
            return self.room_type
        else:
            raise ValueError("Invalid room type.")
    
    def get_room_number(self):
        if isinstance(self.room_number, int):
                return self.room_number
        else:
            raise ValueError("Invalid room number.")
    
    def get_room_state(self):
        if self.room_state in ["Ocupada", "Desocupada"]:
            return self.room_state
        else:
            raise ValueError("Invalid room state.")
    
    def get_room_price(self):
        if isinstance(self.room_price, (int, float)) and self.room_price > 0:
            return self.room_price
        else:
            raise ValueError("Invalid room price.")
    
    
    # Setters
    
    def set_room_type(self, new_type):
        if isinstance(new_type, HotelRoomType):
            self.room_type = new_type
        else:
            raise ValueError("Invalid type for room type.")
    
    def set_room_number(self, new_number):
        if isinstance(new_number, int) and new_number > 0:
            if new_number in Room.numero_hab_usadas:
                raise ValueError("This room number is already in use.")
            else:
                self.room_number = new_number
        else:
            raise ValueError("Invalid value for room number.")
    
    def set_room_state(self, new_state):
        if new_state in ["Ocupada", "Desocupada"]:
            self.room_state = new_state
        else:
            raise ValueError("Invalid room state.")
    
    def set_room_price(self, new_price):
        if isinstance(new_price, (int, float)) and new_price > 0:
            self.room_price = new_price
        else:
            raise ValueError("Invalid room price.")
    
    
    
    
    
    
    def is_occupied(self):
        if self.get_room_state() == "Ocupada":
            return True
        elif self.get_room_state() == "Desocupada":
            return False  
        
    def check_in(self):
        if not self.is_occupied():
            self.room_state = "Ocupada"
            return "Check-in realizado con éxito."
        else:
            return "La habitación ya está ocupada."

    def check_out(self):
        if self.is_occupied():
            self.room_state = "Desocupada"
            return "Check-out realizado con éxito."
        else:
            return "La habitación ya está desocupada."
    









def main():
    
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create a Room.")
    print("=================================================================")
    room1 = Room(HotelRoomType.DOBLE, 101, "Desocupada", 150)

    if room1.get_room_type() == HotelRoomType.DOBLE:
        print("Test PASS. The parameter room_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_number() == 101:
        print("Test PASS. The parameter room_number has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_state() == "Desocupada":
        print("Test PASS. The parameter room_state has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_price() == 150:
        print("Test PASS. The parameter room_price has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================")
    print("Test Case 2: Check-in a Room.")
    print("=================================================================")
    room2 = Room(HotelRoomType.SUITE, 102, "Desocupada", 300)
    check_in_result = room2.check_in()

    if check_in_result == "Check-in realizado con éxito." and room2.is_occupied():
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")

    print("=================================================================")
    print("Test Case 3: Check-out a Room.")
    print("=================================================================")
    check_out_result = room2.check_out()

    if check_out_result == "Check-out realizado con éxito." and not room2.is_occupied():
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")

    print("=================================================================")
    print("Test Case 4: Attempt Check-in on an Occupied Room.")
    print("=================================================================")
    room3 = Room(HotelRoomType.INDIVIDUAL, 103, "Ocupada", 100)
    check_in_result = room3.check_in()

    if check_in_result == "La habitación ya está ocupada.":
        print("Test PASS. Attempted check-in on an occupied room handled correctly.")
    else:
        print("Test FAIL. Check the method check_in() for occupied rooms.")

    print("=================================================================")
    print("Test Case 5: Attempt Check-out on a Vacant Room.")
    print("=================================================================")
    room4 = Room(HotelRoomType.DOBLE, 104, "Desocupada", 200)
    check_out_result = room4.check_out()

    if check_out_result == "La habitación ya está desocupada.":
        print("Test PASS. Attempted check-out on a vacant room handled correctly.")
    else:
        print("Test FAIL. Check the method check_out() for vacant rooms.")
        
        
if __name__ == "__main__":
    main()