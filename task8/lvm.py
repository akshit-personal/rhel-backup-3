#LVM Creation Automation
			os.system("tput setaf 3")
			print("\t\t\tWelcome To LVM Creation")
			os.system("tput setaf 7")
			print("\t\t\t------------------------")
			
			a1 = input("Enter Disk1 Name :")
			a2 = input("Enter Disk2 Name :")
			v = input("Enter Name Of Your Volume Group :")
			l = input("Enter Name Of Your Logical Volume :")
			s = input("Enter Size Of Your Logical Volume :")
			mp = input("Enter Mount Point Of Your LVM :")
			#pv creation 
			os.system("pvcreate /dev/"+a1)
			os.system("pvcreate /dev/"+a2)
			#vg creation
			os.system("vgcreate "+v+" /dev/"+a1+" /dev/"+a2)
			#lv creation
			os.system("lvcreate --size "+s+" --name "+l+" "+v)
			#Formatting LVM
			os.system("mkfs.ext4 /dev/"+v+"/"+l)
			#mounting LVM
			os.system("mkdir /"+mp)
			os.system("mount /dev/"+v+"/"+n+" "+"/"+mp)
			os.system("cd /"+mp)
