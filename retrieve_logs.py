import duo_client
import json




def get_users(ikey, skey, host):

    admin_api = duo_client.Admin(
                            ikey=ikey,
                            skey=skey,
                            host=host)

    users = json.dumps(admin_api.get_authentication_log())
    users_to_dict = json.loads(users)

    locked_out_users = list()

    print(users)

    for i in users_to_dict:
        if i['status'] == 'locked out':
            locked_out_users.append(i['username'])


    for i in locked_out_users:
        print(i)




