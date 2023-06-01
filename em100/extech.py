import struct
import numpy as np
import pandas as pd
import datetime
import argparse
import glob


def dataslicer(b):
    chunks = b.split(b'\xe0\xc5\xea')
    out = []
    one_minute = datetime.timedelta(minutes=1)
    for c in chunks:
        if len(c) < 5:
            continue

        M, d, y, h, m = struct.unpack("bbbbb", c[:5])
        acqtime = datetime.datetime(
            month=M,
            day=d,
            year=y+2000,
            hour=h,
            minute=m
        )
        
        good_data = c[5:]
        if (sz := len(good_data)) % 5 != 0:
            new_end = (sz // 5) * 5
            good_data = good_data[:new_end]
            print(new_end)
            
        for datapoint in struct.iter_unpack(">hhb", good_data):
            voltage = datapoint[0]/10
            amperage = datapoint[1]/1000
            cosphi = datapoint[2]/100  #????
            time = acqtime
            voltamps = voltage*amperage
            watts = voltamps * cosphi
            phi = np.arccos(cosphi)*180/np.pi
            out.append((
                time,
                voltage,
                amperage,
                voltamps,
                watts,
                cosphi,
                phi
            ))
            
            acqtime = time + one_minute
            
    return out
    

def datanicer(b):
    arr = dataslicer(b)
    columns = [
        "Time",
        "Volts",
        "Amps",
        "VoltAmps",
        "Watts",
        "CosPhi",
        "Phi"
    ]
    df = pd.DataFrame(
        data = arr,
        columns = columns
    )
    return df


def read_data(file):
    """ Ideally we'd be able to read any file,
    but the header files are still unknown to me. 
    """
    with open(file, 'rb') as binfile:
        data = binfile.read()
        
    # Check if it's a header file
    # header files start with "INFO:"
    # But data files start with gobbledegook
    # so we have to try/except because the 
    # gobbledegook will throw an exception
    # if we try to decode it.
    try:
        if data[0:5].decode() == 'INFO:':
            print("This is the header file. Try reading the other one instead")
            return
    except UnicodeDecodeError:
        pass
    
    return data


def read_to_array(file):
    data_bin = read_data(file)
    if data_bin is None:
        return
    return dataslicer(data_bin)


def read_to_pandas(file):
    data_bin = read_data(file)
    if data_bin is None:
        return
    return datanicer(data_bin)


def to_csv(file, csvfile):
    p = read_to_pandas(file)
    if p is None:
        return
    p.to_csv(csvfile, index=False)
