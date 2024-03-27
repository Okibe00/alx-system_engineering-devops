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
            usr_id: id of the user
        '''
        todo_arr = rq.get('https://jsonplaceholder.typicode.com/todos')
        todo_arr = todo_arr.json()
        username = get_name(usr_id)
        for obj in todo_arr:
            if obj.get('userId') == usr_id:
                save_to_file(obj, username)

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

    def save_to_file(obj, username):
        '''
        Prints formated output
        '''
        filename = '{}.{}'.format(usr_id, 'csv')
        line = '"{}","{}","{}","{}"\n'.format(
                                usr_id,
                                username,
                                obj.get('completed'),
                                obj.get('title')
                                )
        with open(filename, encoding='utf8', mode='a') as fp:
            fp.write(line)
    get_task(usr_id)
