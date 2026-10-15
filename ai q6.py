
# Vacuum Cleaner Problem

def vacuum_cleaner():
    rooms = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    location = 'A'

    while 'Dirty' in rooms.values():
        print("Vacuum cleaner is in Room", location)

        if rooms[location] == 'Dirty':
            rooms[location] = 'Clean'
            print("Room", location, "cleaned")

        elif location == 'A':
            location = 'B'
            print("Moving to Room B")

        else:
            location = 'A'
            print("Moving to Room A")

    print("\nAll rooms are clean!")
    print("Final State:", rooms)


vacuum_cleaner()
