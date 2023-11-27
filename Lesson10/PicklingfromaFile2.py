import pickle
from Time import Time

in_file = open('data.txt', 'rb')

unpickled_time = pickle.load(in_file)

unpickled_time.print_time()
