import os
current = os.getcwd()
print("当前工作目录：",current)

os.chdir("C:/")
print("新的工作目录",os.getcwd())

print("目录内容：",os.listdir())
#创建和删除目录
#os.mkdir("new_directory")
#os.rmdir("new_directory")

#删除文件
#os.remove("file_to_delete.txt")

#重命名文件
#os.rename("old_name.txt", "new_name.txt")

#获取环境变量
home_directory = os.getenv("HOME")
print("HOME 目录:", home_directory)

#执行系统命令
#os.system("ls -l")






