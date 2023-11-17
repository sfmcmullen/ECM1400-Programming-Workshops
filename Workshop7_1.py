"""WORKSHOP 7"""
import sched
import time
import pyttsx3 as tts


def Question_1():
    """Order the quote using delays"""
    s = sched.scheduler(time.time, time.sleep)

    e1 = s.enter(0, 1, print_job_name, ("Everyone should know, ", ))
    e2 = s.enter(2, 1, print_job_name, ("because it teaches you, ",))
    e3 = s.enter(3, 1, print_job_name, ("how to think!",))
    e4 = s.enter(1, 1, print_job_name, ("how to program a computer, ",))
    s.run()


def Question_2():
    """Order the quote using priority and print after 1s"""
    s = sched.scheduler(time.time, time.sleep)

    e1 = s.enter(1, 1, print_job_name, ("Everyone should know, ", ))
    e2 = s.enter(1, 3, print_job_name, ("because it teaches you, ",))
    e3 = s.enter(1, 4, print_job_name, ("how to think!",))
    e4 = s.enter(1, 2, print_job_name, ("how to program a computer, ",))
    s.run()


def Question_3():
    """Use an announcement function to read the lines"""
    s = sched.scheduler(time.time, time.sleep)

    e1 = s.enter(1, 1, announcement, ("Everyone should know, ", ))
    e2 = s.enter(1, 3, announcement, ("because it teaches you, ",))
    e3 = s.enter(1, 4, announcement, ("how to think!",))
    e4 = s.enter(1, 2, announcement, ("how to program a computer, ",))
    s.run()
    

def print_job_name(name):
    """Prints job name"""
    print(name)


def announcement(message):
    """Announces a message"""
    tts.speak(message)


if __name__ == '__main__':
    Question_3()