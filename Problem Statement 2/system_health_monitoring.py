import psutil
import logging

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)  # Added interval for accurate measurement
    if cpu_usage > 80:
        logging.warning(f'CPU usage is high: {cpu_usage}%')
    else:
        logging.info(f'CPU usage is normal: {cpu_usage}%')

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > 80:
        logging.warning(f'Memory usage is high: {memory_usage}%')
    else:
        logging.info(f'Memory usage is normal: {memory_usage}%')

def check_disk_space():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > 80:
        logging.warning(f'Disk space is low: {disk_usage}%')
    else:
        logging.info(f'Disk space is normal: {disk_usage}%')

def check_running_processes():
    running_processes = len(psutil.pids())
    if running_processes > 100:
        logging.warning(f'Number of running processes is high: {running_processes}')
    else:
        logging.info(f'Number of running processes is normal: {running_processes}')

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()

if __name__ == '__main__':
    main()
