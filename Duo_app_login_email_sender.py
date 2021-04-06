import pathlib
from  APIcreds import APIcreds
import configparser
from retrieve_logs import get_logs
from  datetime import  datetime
import datetime as dt
from retrieve_integration_name import get_integration_name
from log import log
from  SMTPclient import sendemail


def retrieve_application_logs():

   print("Would you like to continually monitor apps accessed by target user? \n")
   answer =  input("Y/N: ").lower()
   if answer == 'y' or 'yes':
      print("Ok getting list of apps for target application!")

   else:
      print("Ok bye")
      exit(0)

   target_app = input('Enter an Ikey to get a list of logs for that application: ')


   cwd = pathlib.Path.cwd()
   if pathlib.Path.exists(cwd / 'API-creds.ini'):

      path = pathlib.Path(cwd / 'API-creds.ini')
      file = open(path, 'r')
      config = configparser.ConfigParser()
      config.read_file(file)
      api_settings = config['api_credentials']

   else:
      print('config file missing')
      exit(1)

   api_credentials = APIcreds()
   api_credentials.set_ikey(api_settings['ikey'])
   api_credentials.set_skey(api_settings['skey'])
   api_credentials.set_api_host(api_settings['api-host'])


      # Get current time plus 5
   now  = datetime.utcnow()
   mins_delta = dt.timedelta(minutes=5)
   #now_plus_5mins = now + mins_delta
   now_minus_5mins = now - mins_delta
   #unix_time_now_plus_5mins = now_plus_5mins.timestamp()
   unix_time_now_minus_5mins = now_minus_5mins.timestamp()

   integration_name = get_integration_name(api_credentials.get_ikey(), api_credentials.get_skey(), api_credentials.get_api_host(), target_app)
   logs = get_logs(api_credentials.get_ikey(), api_credentials.get_skey(), api_credentials.get_api_host(),target_app,unix_time_now_minus_5mins)


   users_accessed = list()



   for i in logs:
        print(i)
        log_object = log()
        if i['integration'] == integration_name:
            log_object.set_username(i['username'])
            log_object.set_integration_name(i['integration'])
            log_object.set_access_time(i['isotimestamp'])
        users_accessed.append(log_object)
        for i in users_accessed:
            print(i.get_username() + ' ' + i.get_integration_name() + ' ' + i.get_access_time() )


   sendemail(log_object.get_username(),log_object.get_integration_name(),log_object.get_access_time())










if __name__ == '__main__':
    retrieve_application_logs()
