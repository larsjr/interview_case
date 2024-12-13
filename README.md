# Case for Glint Solar interview

## Setup
The easiest way to run the Python files in this project is to download 
[uv](https://docs.astral.sh/uv/getting-started/installation/) and then type

`uv run <filename>`

## Task 1
Task one is answered in the netcdf.py file. To execute the script write

`uv run netcdf.py`


## Task 2
Task two is answered in the map.py file. To start the server type

`uv run map.py`

and go to http://127.0.0.1:8081/ in your browser to view the map.


## Task 3
The file for 2019-01-01 has 187 920 coordinates. For each coordinate we have a total of 24 hourly values,
so the total number of values for max wave height is 4510080. 

The total size of the hmax values is 36MB. Including the other values (mwh, mwp, etc.) the total file size
is 44MB. 

Assuming that we use today's date, December 7, 2024, there are 27 369 days since January 1 1950. That 
means that the size of all files, assuming they are about the same as the data for 2019-01-01, would be
around 1204 GB (1,204,236MB). My main point of concern would be the sheer number of files and their total size.

Handling 27 000 files and calculating max wave height is not I would try to do in real-time when the
user clicks the map. I would first try a solution where we pre-process the data:

- Pre-compute the hmax for each coordinate for all hourly values for all the 27 369 files and store the values in a net netcdf file. 
- We can then work with only the number of files we feel comfortable storing, and can delete the processed files
- Once all historical data has been processed we can run a task each that reads the new data, and updates the hmax values for all coordinates
- Query the file with all the max values when the user clicks a point on the map
