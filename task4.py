class ScheduleEntry:
    """
    This class represents a schedule entry for a particular lesson.

    Attributes
    -----------
    - group_number: str, The number of the group attending the lesson.
    - subject: str, The subject of the lesson.
    - lecture_type: str, The type of lecture (e.g., lecture, seminar, lab).
    - classroom: str, The classroom where the lesson takes place.
    - time_slot: str, The time slot of the lesson.
    - day_of_week: str, The day of the week when the lesson occurs.
    - week_parity: str, The parity of the week for which the lesson is scheduled ('четная' or 'нечетная').
    - teacher: str, Optional. The teacher assigned to the lesson.
    """

    def __init__(self, group, subject, lecture_type, classroom, time_slot, day_of_week, week, teacher=None):
        self.group_number = group
        self.subject = subject
        self.lecture_type = lecture_type
        self.classroom = classroom
        self.time_slot = time_slot
        self.day_of_week = day_of_week
        self.week_parity = week
        self.teacher = teacher


class Schedule:
    """
    This class represents a schedule containing multiple schedule entries.

    Attributes
    -----------
    - entries: list, A list of ScheduleEntry objects representing individual lessons.

    Methods
    --------
    - add_entry(lesson): Adds a ScheduleEntry object to the schedule.
    - get_schedule(group_number, week_parity): Prints the schedule for a specified group and week parity.
    """

    def __init__(self):
        self.entries = []

    def add_entry(self, lesson):
        """
        Adds a ScheduleEntry object to the schedule.
        """
        self.entries.append(lesson)

    def get_schedule(self, group_number, week_parity):
        """
        Prints the schedule for a specified group and week parity.
        """
        print(f"Расписание для группы {group_number} ({week_parity} неделя):")
        for day in ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']:
            print(' ')
            print(day.capitalize())
            for slot in range(1, 6):
                for lesson in self.entries:
                    if (lesson.group_number == group_number and
                            (lesson.week_parity == week_parity or lesson.week_parity == 'чет/нечет') and
                            int(slot) == int(lesson.time_slot) and
                            day == lesson.day_of_week):
                        teacher = ""
                        for name, specialty in professors.items():
                            if lesson.subject in specialty and lesson.lecture_type in specialty:
                                teacher = name
                        print(
                            f"{lesson.time_slot}: {lesson.subject} ({lesson.lecture_type}), ауд.{lesson.classroom}, {teacher}")


with open("schedule_data.txt", "r", encoding="utf-8") as file:
    lessons = []
    for line in file:
        data = line.strip().split(";")
        lesson = ScheduleEntry(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        lessons.append(lesson)

professors = {}
with open("professor_data.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split(";")
        if data[0] in professors.keys():
            professors[data[0]] += list([data[1], data[2]])
        else:
            professors[data[0]] = list([data[1], data[2]])

group_number = input("Введите номер группы: ")
week_parity = input("Введите четность недели (четная/нечетная): ")

schedule = Schedule()

for lesson in lessons:
    schedule.add_entry(lesson)

schedule.get_schedule(group_number, week_parity)
