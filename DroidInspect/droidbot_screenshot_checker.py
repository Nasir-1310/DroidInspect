import os
import shutil
from PIL import Image, ImageChops

def compare_screenshots(path1, path2):
    image1 = Image.open(path1)
    image2 = Image.open(path2)
    diff = ImageChops.difference(image1, image2)
    return diff.getbbox() is None  # Returns True if images are the same

def save_screenshot_with_check(device, output_dir, state, event, screenshot_count):
    previous_screenshot_path = os.path.join(output_dir, "previous_screenshot.jpg")
    current_screenshot_path = os.path.join(output_dir, "current_screenshot.jpg")
    temp_screenshot_path = os.path.join(output_dir, f"temp_screenshot_{screenshot_count}.jpg")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Take a new screenshot
    device.take_screenshot(temp_screenshot_path)

    if screenshot_count > 1:
        if compare_screenshots(temp_screenshot_path, previous_screenshot_path):
            print("Screenshots are similar, removing the latest state and event.")
            os.remove(temp_screenshot_path)
            return False
        else:
            shutil.copyfile(temp_screenshot_path, previous_screenshot_path)
    else:
        shutil.copyfile(temp_screenshot_path, previous_screenshot_path)

    shutil.copyfile(temp_screenshot_path, current_screenshot_path)
    save_state_and_event(output_dir, state, event, screenshot_count)
    shutil.copyfile(temp_screenshot_path, os.path.join(output_dir, f"screenshot_{screenshot_count}.jpg"))
    os.remove(temp_screenshot_path)
    return True

def save_state_and_event(output_dir, state, event, screenshot_count):
    state_file = os.path.join(output_dir, f"state_{screenshot_count}.json")
    event_file = os.path.join(output_dir, f"event_{screenshot_count}.json")

    with open(state_file, 'w') as sf:
        sf.write(state)

    with open(event_file, 'w') as ef:
        ef.write(event)

if __name__ == "__main__":
    import sys
    import json

    device = sys.argv[1]  # Placeholder for device object passed as a serialized string
    output_dir = sys.argv[2]
    state = sys.argv[3]
    event = sys.argv[4]
    screenshot_count = int(sys.argv[5])

    # Deserialize the device object
    device = json.loads(device)

    result = save_screenshot_with_check(device, output_dir, state, event, screenshot_count)
    print(json.dumps({"success": result}))
