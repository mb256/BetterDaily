import asyncio
import flet as ft


wisdom_list = [
    "Work on your willpower",
    "Be producer not consumer",
    "Be nice to people on the come up",
    "Watch others & then do the opposite",
    "Who you know matters more than what you know",
    "Never talk behind someone's back",
    "Make more mistakes",
    "Make reversible decisions quickly",
    "Focus on one thing at a time",
    "Don’t be the best, be the only",
    "If you don’t like something then change it",
    "Work smart not hard",
    "Assume you can learn something new from everyone",
    "Never disrespect your elders",
    "Don’t be scared of change, embrace it",
    "Live in the moment, not on your phone",
    "Always pay the bill",
    "Say no if you aren’t ready",
    "Present yourself in the way you wish to be perceived",
    "Mentally prepare yourself for your loved ones dying",
    "Never take rejection personally",
    "Don’t be embarrassed to take a nap",
    "Learn from those who disagree with you",
    "Never be late",
    "Be motivated by something greater than money",
    "Be fuelled by vision not fear",
    "Stand up to bullies",
    "Use your unfair advantages",
    "Skip the flashy car",
    "Prioritise your reputation",
    "Don't compare yourself to your friends",
    "Don’t let a bad day turn into a bad week",
    "Always Pay off your credit card",
    "Any job is better than no job",
    "Never invest without doing your research",
    "Being a great storyteller can get you anything you want",
    "Don’t live your life for others",
    "Have a solid paycheck routine",
    "Start investing now",
    "The quality of your questions will shape your future success",
    "Make sure to enjoy the journey, not just focus on the destination",
    "Nothing is ever free",
    "Stop waiting to be inspired",
    "Work hard now for an easier life later",
    "Tackle the tough tasks in the morning",
    "The name of a university means absolutely nothing",
    "Look after your back",
    "Don’t stress about being different—you don’t have to fit in",
    "Choose your partner wisely"
]


class Message(ft.Text):
    def __init__(self, message_list):
        super().__init__()
        self.message_list = message_list
        self.value = ""
        self.index = 0
        self.theme_style = ft.TextThemeStyle.HEADLINE_LARGE

    async def update_message(self):
        # Iterate over all quotes
        while True:
            # Iterate over letters in one quotes
            for letter in self.message_list[self.index]:
                self.value = self.value + letter
                self.update()
                await asyncio.sleep(0.05)
            # Increment index so it takes another quote from the list
            # (% len() will set index back to '0' once we went through whole list
            self.index = (self.index + 1) % len(self.message_list)
            await asyncio.sleep(6)
            self.value = ""


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    message = Message(wisdom_list)
    page.run_task(message.update_message)
    page.add(message)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
