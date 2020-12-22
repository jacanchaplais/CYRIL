import pandas as pd

def now_stamp():
    return pd.Timestamp.today()

def start_timer():
    return now_stamp()

def end_timer():
    return now_stamp()

def format_data(start, stop):
    return {'start': [start], 'stop': [stop]}

def save(data, out_dir='data/raw/', key='work'):
    data_frame = pd.DataFrame(data=data)
    data_frame.to_hdf(out_dir + '/work.h5', key=key)

if __name__ == '__main__':
    input("Press enter to start a work session")
    start = start_timer()
    input("Press enter to end the work session")
    stop = end_timer()

    data = format_data(start, stop)
    save(data)
