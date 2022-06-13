# print(os.listdir())
# list_of_dir =[(os.path.join(os.getcwd(), "dir1", "dir3", "dir4")), "dir2", "File.txt"]
# for i in list_of_dir:
#     if not os.path.exists(i):
#         os.makedirs(i)
#
# user_choice = input("For deleting folders enter yes: ")
# if user_choice == "yes":
#     for path in os.listdir("dir1"):
#         prefix = "dir1"
#         path = f"{prefix}/{path}"
#         if os.path.isdir(path):
#             try:
#                 os.rmdir(path)
#             except OSError:
#                 print("directory is not empty")
#     else:
        # os.rmdir(f"{os.getcwd()}\\dir2")
        # os.rmdir(f"{os.getcwd()}\\File.txt")