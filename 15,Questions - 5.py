class AnimalShelter:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.timestamp = 0

    def enqueue(self, animal_type):
        self.timestamp += 1
        if animal_type == 'dog':
            self.dog_queue.append((animal_type, self.timestamp))
        elif animal_type == 'cat':
            self.cat_queue.append((animal_type, self.timestamp))

    def dequeueAny(self):
        if not self.dog_queue and not self.cat_queue:
            return None
        elif not self.dog_queue:
            return self.cat_queue.pop(0)[0]
        elif not self.cat_queue:
            return self.dog_queue.pop(0)[0]
        else:
            if self.dog_queue[0][1] < self.cat_queue[0][1]:
                return self.dog_queue.pop(0)[0]
            else:
                return self.cat_queue.pop(0)[0]

    def dequeueDog(self):
        if not self.dog_queue:
            return None
        return self.dog_queue.pop(0)[0]

    def dequeueCat(self):
        if not self.cat_queue:
            return None
        return self.cat_queue.pop(0)[0]



animal_shelter = AnimalShelter()
animal_shelter.enqueue('dog')
animal_shelter.enqueue('cat')
animal_shelter.enqueue('dog')

print(animal_shelter.dequeueAny())  
print(animal_shelter.dequeueDog())  
print(animal_shelter.dequeueCat())  
