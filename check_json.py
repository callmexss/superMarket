import os


def main():
    json_file = [x for x in os.listdir() if x.endswith('json')]
    app_file = "app.exe"
    for file in json_file:
        os.system(app_file + ' ' + file)
        tag = input("是否删除文件？")
        if tag.lower() == 'y' or not tag:
            os.remove(file)
            print(file + " has been removed.")
        else:
            continue


main()
