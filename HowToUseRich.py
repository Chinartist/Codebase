from rich import print
from rich.progress import Progress,track, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn,SpinnerColumn ,RenderableColumn,MofNCompleteColumn
import time
from tqdm import tqdm
with open('/home/zhouxiaoyu/anaconda3/envs/spann3r/lib/python3.9/site-packages/sitecustomize.py', 'w') as f:
    f.write('from rich.traceback import install\n')
    f.write('install(show_locals=False)\n')
progress= Progress(TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TaskProgressColumn(),
    TimeRemainingColumn(),
    MofNCompleteColumn(),
    SpinnerColumn(),
    RenderableColumn(),) 
progress.start()
epoch_tqdm = progress.add_task(description="epoch progress", total=10)
batch_tqdm = progress.add_task(description="batch progress", total=100)
progress.reset(epoch_tqdm)
for ep in range(10):
    progress.reset(batch_tqdm)
    for batch in range(100):
        # print("ep: {} batch: {}".format(ep, batch))
        progress.advance(batch_tqdm, advance=1)
        time.sleep(0.01)
        # assert 1==2
    progress.advance(epoch_tqdm, advance=1)
    