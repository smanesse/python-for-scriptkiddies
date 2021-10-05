import sys
import concurrent.futures
import requests


POOL_SIZE = 10

host = sys.argv[2]
if not host.endswith("/"):
    host = host + "/"


def do_something(arg):
    # do whatever you need to do here
    response = requests.get(host + arg)
    if response.status_code != 404:
        print(arg, response.status_code)
    return response.status_code

def get_tasks():
    # this is an example of how to read in a list of strings from a file
    l = []
    with open(sys.argv[1], "rt") as f:
        for line in f:
            l.append(line.strip())
    return l


def main():
    # get the tasks
    tasks = get_tasks()

    # initialize our pool of threads - "workhorses"
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=POOL_SIZE)

    # store the "future" of each task as key=value (future = task)
    # this way we can retrieve the input for a given future
    futures = {}
    for task in tasks:
        future = pool.submit(do_something, task)
        futures[future] = task

    # initialize list of failed tasks
    failed_tasks = []

    # wait until all the tasks have finished
    for future in concurrent.futures.as_completed(futures):
        try:
            # get the result of the task - it's done now!
            res = future.result()

            # return something like None or False if something goes wrong in the task - 
            # then we mark as failed and save for later
            if not res:
                failed_tasks.append(res)
                
        except Exception as e:
            # if the task raised an exception, we note it here instead of blowing up
            failed_tasks.append(f"{futures[future]} threw exception {e}")

    # afterwards, print all the failed tasks
    print("Failed tasks:")
    for task in failed_tasks:
        print(task)


# entry point for the program
if __name__ == "__main__":
    main()
