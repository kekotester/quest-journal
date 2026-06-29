import json
class Quests:
    def __init__(self, *, name, description, is_done):
        self.name = name
        self.description = description
        self.is_done = is_done

    def __str__(self):
        return f"{self.name} - {self.is_done} \n {self.description}"

    def complete_quest(self, *, quest):
        quest.is_done = True

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "is_done": self.is_done
        }
    @classmethod
    def from_dict(cls,*, data):
        return cls (
            name = data["name"],
            description = data["description"],
            is_done = data["is_done"]
        )


class Task_Quests:
    def __init__(self):
        self.quests = []

    def add_quest(self,*, quest):
        self.quests.append(quest)

    def show_quests(self):
        for quest in self.quests:
            print(quest)


    def load_quests(self, *, loaded_data):
        for data in loaded_data:
            self.quests.append(Quests.from_dict(data=data))

    def save(self, *, filename):
        quests_data = [quest.to_dict() for quest in self.quests]
        with open (filename, "w", encoding="utf-8") as file:
            json.dump(quests_data, file, indent=4)

        print(f"Saved {filename}")

    def load(self,*, filename):
        with open (filename, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)

        self.load_quests(loaded_data=loaded_data)

task_quests = Task_Quests()

task_quests.load(filename="quests_journal.json")
task_quests.show_quests()

task_quests.save(filename="quests_journal.json")
