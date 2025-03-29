import time

start_time = time.time()
run_duration = 24 * 3600  # 24 hours in seconds

def main():
    while True:
        elapsed_time = time.time() - start_time
        hours = elapsed_time / 3600
        print(f"Script has been running for {hours:.2f} hours.")

        if elapsed_time >= run_duration:
            print("24 hours reached. Stopping script.")
            break  # Exit the loop after 24 hours

        time.sleep(60)  # Waits for 60 seconds before the next iteration

if __name__ == "__main__":
    main()
