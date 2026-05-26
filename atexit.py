import atexit
import time
def cleanup_database():
    print("cleaning the database for you")
    print("Database is closed and cleaned")
def release_camera():
    print("releasing the camera for you")
    print("Camera is released")
atexit.register(cleanup_database)
atexit.register(release_camera)
print("Program is running...")
time.sleep(5)
print("Program is exiting...")
