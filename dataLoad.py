# Load Data to Historic PostGIS Table
from datetime import timedelta
from timeloop import Timeloop
import os, subprocess
import time

t1 = Timeloop()

@t1.job(interval=timedelta(seconds=2))
def load_features():    
    # import the data
    try:
            def load(args):
                    options = ['ogr2ogr']
                    options.extend(args)
                    # record the output!
                    subprocess.check_call(options,stderr=subprocess.STDOUT)

            load(['-f', 'PostgreSQL', 'PG:dbname=postgres user=postgres', '/var/lib/pgsql/postgresScripts/GeoTest/Data/test.json', '-nln', 'features'])
            print('Successfully Loaded All Rows Into Features Table At : {}'.format(time.ctime()))
    # record an error if there is one
    except subprocess.CalledProcessError as e:
            print(str(e.output))


if __name__ == '__main__':
     t1.start(block=True)
