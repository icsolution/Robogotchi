import random
import textwrap


class Robot:
    name = input('How will you call your robot?\n')
    battery = 100
    overheat = 0
    skill = 0
    boredom = 0
    rust = 0

    @classmethod
    def start_menu(cls):
        print(textwrap.dedent(f'''
        Available interactions with {cls.name}:
        exit - Exit
        info - Check the vitals
        work - Work
        play - Play
        oil - Oil
        recharge - Recharge
        sleep - Sleep mode
        learn - Learn
        '''))
        choice = input('Choose:\n').lower()
        if choice in ['info', 'exit']:
            exec(f'cls.{choice}()')
        elif cls.battery == 0 and choice != 'recharge':
            print(f'\nThe level of the battery is 0, {cls.name} needs recharging!')
        elif cls.boredom == 100 and choice != 'play':
            print(f'\n{cls.name} is too bored! {cls.name} needs to have fun!')
        elif choice == 'play':
            Play().select_game()
        elif choice in ['work', 'recharge', 'sleep', 'learn', 'oil']:
            exec(f'cls.{choice}()')
        else:
            print('\nInvalid input, try again!')
        cls.start_menu()

    @classmethod
    def info(cls):
        print(textwrap.dedent(f'''
        {cls.name}'s stats are: 
        the battery is {cls.battery},
        overheat is {cls.overheat},
        skill level is {cls.skill},
        boredom is {cls.boredom},
        rust is {cls.rust}.'''))
        cls.start_menu()

    @classmethod
    def work(cls):
        if cls.skill < 50:
            print(f'\n{cls.name} has got to learn before working!')
            cls.start_menu()
        else:
            cls.battery -= 10
            if cls.battery < 0:
                cls.battery = 0
            cls.boredom += 10
            if cls.boredom > 100:
                cls.boredom = 100
            cls.overheat += 10
            if cls.overheat >= 100:
                print(f'\nThe level of overheat reached 100, {Robot.name} has blown up! Game over. Try again?')
                exit()
            event = cls.events()
            print(textwrap.dedent(f'''
            {cls.name}'s level of boredom was {cls.boredom - 10}. Now it is {cls.boredom}.
            {cls.name}'s level of overheat was {cls.overheat - 10}. Now it is {cls.overheat}.
            {cls.name}'s level of the battery was {cls.battery + 10}. Now it is {cls.battery}.'''))
            if event:
                print(event)
            print(f'\n{cls.name} did well!')
            cls.start_menu()

    @classmethod
    def oil(cls):
        if cls.rust == 0:
            print(f'\n{cls.name} is fine, no need to oil!')
        else:
            rust = cls.rust
            cls.rust -= 20
            if cls.rust < 0:
                cls.rust = 0
            print(f'\n{cls.name}\'s level of rust was {rust}. Now it is {cls.rust}. {cls.name} is less rusty!')
        cls.start_menu()

    @classmethod
    def recharge(cls):
        if cls.battery == 100:
            print(f'\n{cls.name} is charged!')
        else:
            cls.battery += 10
            if cls.battery > 100:
                cls.battery = 100
            cls.overheat -= 5
            if cls.overheat < 0:
                cls.overheat = 0
            cls.boredom += 5
            if cls.boredom > 100:
                cls.boredom = 100
            print(textwrap.dedent(f'''
            {cls.name}'s level of overheat was {cls.overheat + 5}. Now it is {cls.overheat}.
            {cls.name}'s level of the battery was {cls.battery - 10}. Now it is {cls.battery}.
            {cls.name}'s level of boredom was {cls.boredom - 5}. Now it is {cls.boredom}.'''))

        print(f'\n{cls.name} is recharged!')
        cls.start_menu()

    @classmethod
    def sleep(cls):
        if cls.overheat > 0:
            previous_overheat = cls.overheat
            cls.overheat -= 20
            if cls.overheat < 0:
                cls.overheat = 0
            if cls.overheat != 0:
                print(textwrap.dedent(f'''
                {cls.name}'s level of overheat was {previous_overheat}. Now it is {cls.overheat}.

                {cls.name} cooled off!'''))
            else:
                print(textwrap.dedent(f'''
                {cls.name}'s level of overheat was {previous_overheat}. Now it is {cls.overheat}.

                {cls.name} is cool!'''))
        else:
            print(f'{cls.name} is cool!')
        cls.start_menu()

    @classmethod
    def learn(cls):
        if cls.skill == 100:
            print(f'''There's nothing for {cls.name} to learn!''')
        else:
            cls.skill += 10
            cls.battery -= 10
            if cls.battery < 0:
                cls.battery = 0
            cls.overheat += 10
            if cls.overheat >= 100:
                print(f'\nThe level of overheat reached 100, {Robot.name} has blown up! Game over. Try again?')
                exit()
            cls.boredom += 5
            if cls.boredom > 100:
                cls.boredom = 100
            print(textwrap.dedent(f'''
            {cls.name}'s level of skill was {cls.skill - 10}. Now it is {cls.skill}.
            {cls.name}'s level of overheat was {cls.overheat - 10}. Now it is {cls.overheat}.
            {cls.name}'s level of the battery was {cls.battery + 10}. Now it is {cls.battery}.
            {cls.name}'s level of boredom was {cls.boredom - 5}. Now it is {cls.boredom}.
            
            {cls.name} has become smarter!'''))
        cls.start_menu()

    @classmethod
    def events(cls):
        event = int(random.choice('0123'))
        if event == 0:
            return 0
        else:
            rust = cls.rust
            print()
            if event == 1:
                print(f'Oh no, {cls.name} stepped into a puddle!')
                cls.rust += 10
            elif event == 2:
                print(f'Oh, {cls.name} encountered a sprinkler!.')
                cls.rust += 30
            else:
                print(f'Guess what! {cls.name} fell into the pool!')
                cls.rust += 50
            if cls.rust >= 100:
                print(f'{cls.name} is too rusty! Game over. Try again?')
                exit()
            return f'''{cls.name}'s level of rust was {rust}. Now it is {cls.rust}.'''

    @staticmethod
    def exit():
        print('\nGame over')
        exit()


class Play(Robot):

    def __init__(self, ):
        self.user_score = self.robot_score = self.draw = 0
        self.robot_choice = self.user_choice = None

    def select_game(self):
        while True:
            game = input('\nWhich game would you like to play?\n').lower()
            if game == 'exit game':
                self.exit_game()
            if game == 'numbers':
                NumbersGame().play_game()
            elif game == 'rock-paper-scissors':
                RockPaperScissorsGame().play_game()
            else:
                print('\nPlease choose a valid option: Numbers or Rock-paper-scissors?')

    def display_result(self, winner):
        if winner == 'robot':
            print('The robot won!')
            self.robot_score += 1
        elif winner == 'user':
            print('You won!')
            self.user_score += 1
        else:
            print("It's a draw!")
            self.draw += 1

    def exit_game(self):
        if Robot.overheat >= 90:
            print(f'\nThe level of overheat reached 100, {Robot.name} has blown up! Game over. Try again?')
            exit()
        else:
            boredom = Robot.boredom
            overheat = Robot.overheat
            Robot.boredom -= 20
            if Robot.boredom < 0:
                Robot.boredom = 0
            Robot.overheat += 10
            print(textwrap.dedent(f'''
            You won: {self.user_score},
            The robot won: {self.robot_score},
            Draws: {self.draw}.'''))
            event = Robot.events()
            print(textwrap.dedent(f'''
            {Robot.name}'s level of boredom was {boredom}. Now it is {Robot.boredom}.
            {Robot.name}'s level of overheat was {overheat}. Now it is {Robot.overheat}.'''))
            if event:
                print(event)
            if Robot.boredom == 0:
                print(f'\n{Robot.name} is in a great mood!')
            Robot.start_menu()


class NumbersGame(Play):
    def __init__(self):
        super().__init__()

    def play_game(self):
        while not self.user_choice:
            self.user_choice = self.check_input()
        goal = random.randint(0, 1000000)
        self.robot_choice = random.randint(0, 1000000)
        print(f'\nThe robot entered the number {self.robot_choice}.')
        print(f'The goal number is {goal}.')
        if abs(goal - self.robot_choice) < abs(goal - self.user_choice):
            winner = 'robot'
        elif abs(goal - self.robot_choice) > abs(goal - self.user_choice):
            winner = 'user'
        else:
            winner = 'draw'
        super().display_result(winner)
        self.user_choice = None
        self.play_game()

    def check_input(self):
        choice = input('\nWhat is your number?\n')
        try:
            if choice == 'exit game':
                super().exit_game()
            elif int(choice) < 0:
                print("\nThe number can't be negative!")
            elif int(choice) > 1000000:
                print("\nInvalid input! The number can't be bigger than 1000000.")
            else:
                return int(choice)
        except ValueError:
            print("\nA string is not a valid input!")


class RockPaperScissorsGame(Play):
    def __init__(self):
        super().__init__()
        self.options = ['paper', 'rock', 'scissors']

    def play_game(self):
        while not self.user_choice:
            self.user_choice = self.check_input()
        self.robot_choice = random.choice(self.options)
        print(f'\nThe robot chose {self.robot_choice}')
        result = self.check_result()
        if self.user_choice == self.robot_choice:
            winner = 'draw'
        elif result[0] < result[1]:
            winner = 'user'
        else:
            winner = 'robot'
        super().display_result(winner)
        self.user_choice = None
        self.play_game()

    def check_input(self):
        while True:
            choice = input('\nWhat is your move?\n')
            if choice == 'exit game':
                super().exit_game()
            elif choice in self.options:
                return choice
            else:
                print('\nNo such option! Try again!')

    def check_result(self):
        user_index = self.options.index(self.user_choice)
        if user_index == 0:
            result = [self.options[-1]] + self.options[:2]
        elif user_index == 2:
            result = self.options[1:] + [self.options[0]]
        else:
            result = self.options
        return [result.index(self.user_choice), result.index(self.robot_choice)]


if __name__ == '__main__':
    pet = Robot()
    pet.start_menu()
