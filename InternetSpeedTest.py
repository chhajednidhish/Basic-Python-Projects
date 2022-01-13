import speedtest as st
import time

initTime = time.time()

test = st.Speedtest()       # Creating a test variable to test the speed
print("Calculating download speed...")
down = test.download()      # Creating down variable to store the download speed
print("Calculating upload speed...")
up   = test.upload()        # Creating up variable to store the upload speed
print(f"Download speed is {down}.")      
print(f"Uploading speed is {up}.")
timeTaken = time.time() - initTime
print(f"Time taken to calculate download and upload speed is {timeTaken} seconds.")