"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Christian Kuhn
"""
__version__ = 7







# 1) main
# 2) print_user_info
# 3) filter_available_courses
# 4) print_courses
# 5) get_course_ids
# 6) choose_course
# 7) summarize_points
# 8) summarize_groups
# 9) plot_scores
# 10) plot_grade_trends

# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.
import canvas_requests

def main(user_id):
    return canvas_requests.get_user(user_id)

def print_user_info(user_dictionary):
    print('Name: ' + user_dictionary['name'])
    print('Title: ' + user_dictionary['title'])
    print('Primary Email: ' + user_dictionary['login_id'])
    print('Bio: ' + user_dictionary['bio'])

def filter_available_courses(course_dictionaries):
    filter_courses = []
    for course in course_dictionaries:
        if course['workflow_state'] == 'available':
            filter_courses.append(course)
    return filter_courses

def print_courses(course_dictionaries):
    for course in course_dictionaries:
        print('\t'+ str(course['id']) + ": " + course['name'])

def get_course_ids(course_dictionaries):
    course_ids = []
    for course in course_dictionaries:
        course_ids.append(course['id'])
    print()
    return course_ids

def choose_course(course_ids):
    user_input = input("Enter a valid id")
    user_input = int(user_input)
    while user_input not in course_ids:
        user_input = int(input("Enter a valid id"))
    return user_input

def summarize_points(submissions):
    possible = 0
    points_obtained = 0






if __name__ == "__main__":
    print_user_info(canvas_requests.get_user("hermione"))
    filter_available_courses(canvas_requests.get_courses('hermione'))
    print_courses(canvas_requests.get_courses('hermione'))
    get_course_ids(canvas_requests.get_courses('hermione'))
    choose_course(canvas_requests.get_courses('hermione'))
    # main
    # main('harry')
    
    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')