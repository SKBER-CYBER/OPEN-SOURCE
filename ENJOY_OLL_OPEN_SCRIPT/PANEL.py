#

try:
	import rich,requests
except:
	os.system('pip install rich requests')
	import rich,requests 
from rich import print
from rich.tree import Tree
from rich.panel import Panel
from rich.columns import Columns

id=("100095462898126")
pas=('123456')
user=("2010")
ua=("""Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36""")
oggy1 = Panel.fit(f"[green]LOGIN SUCCESSFUL",width=30,padding=0,style="bold cyan")
oggy2 = Panel("[green]  "+id, title="[green]UID",width=30,padding=0,style="bold cyan")
oggy3 = Panel("[green]  "+pas, title="[green]PASS",width=30,padding=0,style="bold cyan")
oggy4 = Panel("[green]"+ua, title="[green]UA",width=100,padding=0,style="bold cyan")
oggy9 = Panel("[green]"+ user, title="[green]JOINT",width=30,padding=0,style="bold cyan")
oggy5 = Columns([oggy1])
oggy6 = Columns([oggy2, oggy3])
oggy7 = Columns([oggy4])

tree = Tree(oggy5)
tree.add(oggy6)
tree.add(oggy7)

print(tree)

                 panel1 = Panel.fit("[green]LOGIN SUCCESS",width=34,padding=0,style='blue')
                 panel3 = Panel("[green]  "+uid, title="[green]UID",width=28,padding=0,style='blue')
                 panel4 = Panel("[green]  "+ps, title="[green]PASS",width=28,padding=0,style='blue')
                 Error = Panel("[green]  "+xx, title="[green]UA",width=100,padding=0,style='blue')
                 uu = Panel("[green]  https://www.facebook.com/profile.php?id="+uid,title="[green]LINK",width=100,padding=0,style='blue')
                 Rayhan = Columns([panel1])
                 columns = Columns([panel3, panel4])
                 Erco = Columns([Error])
                 Ua = Columns([uu])
                 tree = Tree(Rayhan)
                 tree.add(columns)
                 tree.add(Erco)
                 child = tree.add(Ua)
                 print(tree);open("/sdcard/Erco-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1