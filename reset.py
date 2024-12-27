import os
import argparse

def delete_screenshots():
    screenshots_path = "traffic_sim/screenshots"
    for filename in os.listdir(screenshots_path):
        file_path = os.path.join(screenshots_path, filename)
        os.remove(file_path)
    print("Screenshots deleted.")

def delete_labels():
    labels_path = "traffic_sim/labels"
    for filename in os.listdir(labels_path):
        file_path = os.path.join(labels_path, filename)
        os.remove(file_path)
    print("Labels deleted.")

def main():
    parser = argparse.ArgumentParser(description="Reset script for traffic simulation")
    parser.add_argument("action", choices=["screenshots", "labels"], help="The action to perform: delete screenshots or labels")

    args = parser.parse_args()

    if args.action == "screenshots":
        delete_screenshots()
    elif args.action == "labels":
        delete_labels()

if __name__ == "__main__":
    main()