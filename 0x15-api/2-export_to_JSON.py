#!/usr/bin/python3
'''
make a call to the restapi and display formated text
'''
if __name__ == '__main__':
    import json
    import requests as rq
    import sys

    usr_id = int(sys.argv[1])

    def get_task(usr_id=None):
        '''
        Get the number of task completed by user
        Args:
            usr_id: id of the user
        '''
        todo_arr = rq.get('https://jsonplaceholder.typicode.com/todos')
        todo_arr = todo_arr.json()
        username = get_name(usr_id)
        task_list = list()
        for obj in todo_arr:
            if obj.get('userId') == usr_id:
                task_list.append(task_info(obj, username))
        else:
            filename = f'{usr_id}.json'
            tasks = dict()
            tasks.update({f'{usr_id}': task_list})
            with open(filename, encoding="utf8", mode='w') as fp:
                json.dump(tasks, fp)

    def get_name(usr_id=None):
        '''
        get the name of the user passed
        '''
        usr_arr = rq.get('https://jsonplaceholder.typicode.com/users')
        if usr_arr.status_code == 200:
            resp = usr_arr.json()
            for obj in resp:
                if obj.get('id') == usr_id:
                    return (obj.get('username'))
        else:
            print(usr_arr.status_code)

    def task_info(obj, username):
        '''
        save to a file in json format
        '''
        task = dict()
        task.update({
            'task': obj.get('title'),
            'completed': obj.get('completed'),
            'username': username
        })
        return (task)

    get_task(usr_id)
