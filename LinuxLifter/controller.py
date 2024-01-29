import sys
import concurrent.futures
import subprocess
import string


def startThread(scriptName, startString, shaString):
        
    result = subprocess.run(['python3', scriptName, startString, shaString], capture_output=True)
    return result.stdout

def main():
    shaText = sys.argv[1]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for c in string.ascii_lowercase:
            futures.append(executor.submit(startThread, 'shaGenerator.py', str(c), shaText))
            print("starting thread: starting character -- " , c)

        # Iterate over the results as they complete
        for future in concurrent.futures.as_completed(futures):
            output = future.result().decode('utf-8').strip('\n')
            print(output)
            if output != "No match!": 
                break

if __name__  == "__main__":
    main()