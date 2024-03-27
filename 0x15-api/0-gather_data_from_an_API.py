#!/usr/bin/python3
'''
make a call to the restapi and display formated text
'''
if __name__ == '__main__':
    import requests as rq
    import sys

    usr_id = int(sys.argv[1])

    def get_task(usr_id=None):
        '''
        Get the number of task completed by user
        Args:
            id: id of the user
            return: dictionary of tasks completed
                    {
                         user_name:
                         task_completed:
                         total_task:
                         task: []
                    }
        '''
        usr_dict = dict()
        tasks = []
        task_comp = 0
        total_task = 0
        todo_arr = rq.get('https://jsonplaceholder.typicode.com/todos')
        todo_arr = todo_arr.json()
        for obj in todo_arr:
            if obj.get('userId') == usr_id:
                total_task = total_task + 1
                if (obj.get('completed')):
                    task_comp = task_comp + 1
                    tasks.append(obj.get('title'))
        else:
            name = get_name(usr_id)
            usr_dict.update({
                'tasks': tasks,
                'task_comp': task_comp,
                'total_task': total_task,
                'user': name
                    })
            return usr_dict

    def get_name(usr_id=None):
        '''
        get the name of the user passed
        '''
        usr_arr = rq.get('https://jsonplaceholder.typicode.com/users')
        if usr_arr.status_code == 200:
            resp = usr_arr.json()
            for obj in resp:
                if obj.get('id') == usr_id:
                    return (obj.get('name'))
        else:
            print(usr_arr.status_code)

    res = get_task(usr_id)

    def print_resp(obj):
        '''
        Prints formated output
        '''
        name = obj.get('user')
        task_comp = obj.get('task_comp')
        total_task = obj.get("total_task")
        print(f"Employee {name} is done with tasks({task_comp}/{total_task}):")
        for val in obj.get('tasks'):
            print(f"\t {val}")

    print_resp(res)
