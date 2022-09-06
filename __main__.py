from utils.loader import Client, configData

if __name__ == '__main__':

    Client(configData['token']).__run__()
