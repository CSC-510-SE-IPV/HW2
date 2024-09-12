import subprocess


def random_array(arr):
    '''
    This function is going to genarate an array randomly and
    arr is an empty array
    '''
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
