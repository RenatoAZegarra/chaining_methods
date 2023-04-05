class User:
    def __init__(self,first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {'Yes' if self.is_rewards_member else 'No'}")
        print(f"Gold Card Points: {self.gold_card_points}")
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Error: Not enough points to spend.")
            return self
        else:
            self.gold_card_points -= amount
            return amount

# Create a users
user1 = User("Brandon", "Roy", "broy@gmail.com", 30)
user2 = User("Jane", "Smith", "janeS@gmail.com", 25)
user3 = User("Bob", "List", "boblist@gmail.com", 40, True, 500)

#Chaining
user1.display_info().enroll().spend_points(50)
user2.display_info().enroll().spend_points(80)
user3.display_info().enroll().spend_points(40)


