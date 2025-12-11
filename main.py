import taskmanager
from argparse import ArgumentParser

def handle_add(args):
    tm.add_task(args.title)
    tm.save_tasks("tasks.json")
    print(f"task added. ID: {tm.next_id-1} ")

def handle_list(args):
    tm.list_all("tasks.json", args.status)

def handle_del(args):
    if tm.delete_task(args.id):
        tm.save_tasks("tasks.json")
        print(f"task deleted. ID: {args.id}")
    else: print("id has not been found")

def handle_upt(args):
    if tm.update_task(args.id, args.title):
        print(f"task updated. ID: {args.id}")
        tm.save_tasks("tasks.json")
    else: print("error. task hasnt been updated. wrong id???")

def handle_mark_done(args):
    if tm.change_status("tasks.json", args.id, "done"):
        print(f"task marked done. ID: {args.id}")
        tm.save_tasks("tasks.json")
    else: print("error. task hasnt been updated. wrong id???")

def handle_mark_inp(args):
    if tm.change_status("tasks.json", args.id, "in-progress"):
        print(f"task marked in progress. ID: {args.id}")
        tm.save_tasks("tasks.json")
    else: print("error. task hasnt been updated. wrong id???")



        #wywolanie obiektow, taskmanager, parser
tm = taskmanager.TaskManager()
tm.read_tasks("tasks.json")
parser = ArgumentParser()
subparses = parser.add_subparsers()
#dodawanie subparesrow
#add
add_parser = subparses.add_parser("add")
add_parser.add_argument("title")
add_parser.set_defaults(func=handle_add)

#list
list_parser = subparses.add_parser("list")
list_parser.set_defaults(func=handle_list)
list_parser.add_argument("--status", choices=["todo", "in-progress", "done"])

#delete
delete_parser = subparses.add_parser("del")
delete_parser.set_defaults(func=handle_del)
delete_parser.add_argument("id", type=int)

#update
update_parser = subparses.add_parser("update")
update_parser.set_defaults(func=handle_upt)
update_parser.add_argument("id", type=int)
update_parser.add_argument("title", type=str)

#mark done/in-progress
mark_parser = subparses.add_parser("mark-done")
mark_parser.set_defaults(func=handle_mark_done)
mark_parser.add_argument("id", type=int)

mark_parser = subparses.add_parser("mark-in-progress")
mark_parser.set_defaults(func=handle_mark_inp)
mark_parser.add_argument("id", type=int)


args = parser.parse_args()

args.func(args)
